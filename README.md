## 🟦 `Challenge_1b/Collection 1/README.md`

```markdown
# Challenge 1B – Persona-Based Document Analysis

This is my submission for Challenge 1B of the Adobe Hackathon.  
Here, the task was to simulate a smart assistant that understands the user's intent (persona + task) and extracts the most relevant information from several PDFs.

---

## 🧠 What I Built

The system:
- Reads a `persona.json` describing who the user is and what they want to do
- Analyzes all the PDFs in the input folder
- Ranks the most relevant pages or sections using a transformer model
- Generates short summaries of those key sections
- Saves everything in a structured `output.json`

---

## 🛠 Tools I Used

- `PyMuPDF` for PDF parsing
- `sentence-transformers (MiniLM)` to match the user’s intent with PDF content
- `nltk` for basic text summarization
- Docker to make sure everything runs offline and reproducibly

---

## 📁 Input Format

Put the following in the `input/` folder:
- One `persona.json` file
- 3–10 PDF files

```json
{
  "persona": "Digital Strategy Consultant",
  "job_to_be_done": "Evaluate government and education digital transformation plans"
}
```

## 📁 Project Structure
```bash
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

## 🐳 How to Run 
 
```bash
docker build --platform linux/amd64 -t persona_analyzer:1b .
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none persona_analyzer:1b
```


This round was really interesting because we had to think about the user's intent and match it with dense PDF content using embeddings.
It was a good balance of NLP, PDF parsing, and logic structuring — and a fun challenge overall.
