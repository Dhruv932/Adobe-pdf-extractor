# Adobe India Hackathon 2025 – Round 1B Submission

## 🔍 Problem Statement
Given a set of PDFs and a defined persona + job-to-be-done, extract the most relevant sections that match the user's intent.

---

## 🧠 Approach

We use a **hybrid semantic retrieval system**:
1. **Heading + Section Extraction**:
   - Uses layout and font cues to extract headings (`H1` to `H3`).
   - Pulls section content between two headings.
2. **Embedding**:
   - Uses `intfloat/e5-small-v2` for semantic search.
3. **Ranking**:
   - Combines semantic similarity + light keyword-based scoring for improved relevance.
4. **Output**:
   - Conforms to Adobe’s required JSON format with `metadata`, `extracted_sections`, and `subsection_analysis`.

---

## 🛠 How to Build & Run

### 🔨 Build

```bash
docker build --platform linux/amd64 -t round1b-solution:latest .
