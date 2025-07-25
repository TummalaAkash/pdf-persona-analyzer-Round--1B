# Adobe-India-Hackathon25  
## Challenge 1B – Persona-Based Document Analysis

This repository contains my solution for *Challenge 1B* of the Adobe India Hackathon 2025.

The goal was to simulate a document assistant that understands a user's role and task (persona) and automatically extracts the most relevant content from a set of PDF documents. The extracted sections are then ranked and summarized in a structured JSON output.

---

## ✅ What I Did

I used a combination of **PyMuPDF** for PDF parsing and **Sentence Transformers (MiniLM)** for semantic similarity ranking.

- Each page of every PDF is processed as a "chunk"
- Chunks are compared to the **persona + job-to-be-done** using a sentence embedding model
- The most relevant chunks are **ranked by importance**
- Short summaries are generated using sentence splitting
- Everything is packaged inside a **Docker image**, running offline and CPU-only

---

## 📂 Input Format

All files go in the `/input/` directory:

- `persona.json`  
```json
{
  "persona": "Digital Strategy Consultant",
  "job_to_be_done": "Evaluate government and education digital transformation plans"
}
```

## 🧾 Output Format

The output is saved to /output/output.json with this structure:

```json
{
  "metadata": {
    "documents": [...],
    "persona": "...",
    "job_to_be_done": "...",
    "timestamp": "..."
  },
  "sections": [
    {
      "document": "E0H1CM114.pdf",
      "page": 3,
      "section_title": "Digital Library Strategy",
      "importance_rank": 1
    }
  ],
  "subsections": [
    {
      "document": "E0H1CM114.pdf",
      "page": 3,
      "refined_text": "The Ontario Digital Library plans to connect citizens to digital resources...",
      "importance_rank": 1
    }
  ]
}

```
## 🐳 How to Run It (Using Docker)

### 🔧 Build the Docker Image

```bash
docker build --platform linux/amd64 -t persona_analyzer:1b .
```

## ▶️ Run the Container
```bash
docker run --rm \
  -v ${PWD}/input:/app/input \
  -v ${PWD}/output:/app/output \
  --network none \
  persona_analyzer:1b
```

On Windows PowerShell, use ${PWD}. On Git Bash or Linux, use $PWD.

## 📁 Project Structure

```bash
.
├── app/
│   ├── main.py                  # Main application script
│   └── requirements.txt         # Python dependencies
│
├── Collection 1/
│   ├── PDFs/                    # Folder containing PDFs for Collection 1
│   ├── challenge1b_output.json  # Output of challenge 1B for this collection
│   └── persona.json             # Persona details used for relevance ranking
│
├── Collection 2/
│   ├── PDFs/                    # Folder containing PDFs for Collection 2
│   └── challenge1b_output.json  # Output of challenge 1B for this collection
│
├── Collection 3/
│   ├── PDFs/                    # Folder containing PDFs for Collection 3
│   └── challenge1b_output.json  # Output of challenge 1B for this collection
│
├── screenshots/
│   ├── image1.png               # Screenshot 1
│   ├── image2.png               # Screenshot 2
│   └── image3.png               # Screenshot 3
│
└── Dockerfile                   # Docker configuration to containerize the app
```

## 📦 Dependencies

- Python 3.x

- PyMuPDF (fitz)

- Sentence Transformers (all-MiniLM-L6-v2)

- NLTK (for sentence splitting)

- Docker (for containerized execution)

## 🔧Install Dependencies Locally (for testing)

```bash
pip install -r requirements.txt

```
