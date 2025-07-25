import os
import fitz
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

# Load multilingual, lightweight embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_persona(persona_path):
    with open(persona_path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_text_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        if text.strip():
            chunks.append({
                "document": os.path.basename(pdf_path),
                "page": page_num + 1,
                "text": text.strip()
            })
    return chunks

def rank_chunks(chunks, query, top_n=5):
    results = []
    query_embed = model.encode(query, convert_to_tensor=True)
    for chunk in chunks:
        chunk_embed = model.encode(chunk["text"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(query_embed, chunk_embed).item()
        chunk["score"] = score
        results.append(chunk)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]

def summarize_text(text, max_sentences=3):
    import nltk
    from nltk.tokenize import sent_tokenize
    nltk.download("punkt", quiet=True)
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences])

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    persona_data = load_persona(os.path.join(input_dir, "persona.json"))
    persona = persona_data["persona"]
    job = persona_data["job_to_be_done"]
    query = f"{persona} needs to {job}"

    all_chunks = []
    pdf_files = []
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_files.append(file)
            chunks = extract_text_chunks(os.path.join(input_dir, file))
            all_chunks.extend(chunks)

    top_chunks = rank_chunks(all_chunks, query)

    output = {
        "metadata": {
            "documents": pdf_files,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "sections": [],
        "subsections": []
    }

    for rank, chunk in enumerate(top_chunks, start=1):
        output["sections"].append({
            "document": chunk["document"],
            "page": chunk["page"],
            "section_title": chunk["text"][:80].split("\n")[0],
            "importance_rank": rank
        })
        output["subsections"].append({
            "document": chunk["document"],
            "page": chunk["page"],
            "refined_text": summarize_text(chunk["text"]),
            "importance_rank": rank
        })

    output_path = os.path.join(output_dir, "output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
