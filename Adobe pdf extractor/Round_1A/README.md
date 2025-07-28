# 🧠 Adobe Hackathon 2025 — Round 1A
## 📑 Unsupervised Document Outline Extraction

This project extracts structured outlines (Title, H1, H2, H3) from unstructured PDFs using layout parsing and unsupervised learning.

---

### 🛠 Technologies
- Python
- PDFMiner
- Scikit-learn
- Docker

---

### 📂 Folder Structure

Round_1A/
├── layout_parser.py
├── main.py
├── train.py
├── model/gbt_model.pkl
├── input/.pdf
├── output/.json
├── data/labeled_features.jsonl
├── Dockerfile


### 🚀 Run Instructions

#### Docker:
```bash
docker build -t adobe-round1a .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output adobe-round1a

Local:bash
pip install -r requirements.txt
python main.py

💡 Output Format
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Section", "page": 1 },
    { "level": "H2", "text": "Subsection", "page": 2 }
  ]
}
