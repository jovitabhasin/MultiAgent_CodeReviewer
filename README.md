# Multi-Agent AI Code Reviewer

An intelligent **Multi-Agent Code Review System** built using **LangGraph**, **LangChain**, **Groq Llama 3.3**, and **Streamlit**.

The application analyzes source code using multiple specialized AI agents that collaborate to produce a comprehensive code review.

---

## Features

- Upload or paste source code
- Automatic programming language detection
- Bug Detection
- Time & Space Complexity Analysis
- Code Style Review
- Security Analysis
- Aggregated Professional Code Review
- Download review as Markdown

---

## Multi-Agent Architecture

The project follows the **Parallel + Aggregator** orchestration pattern.

```
                    User
                      │
                      ▼
              Supervisor Agent
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
  Bug Agent    Complexity Agent   Style Agent
                      │
                      ▼
              Security Agent
                      │
                      ▼
             Aggregator Agent
                      │
                      ▼
               Final Code Review
```

Each agent performs a specialized task independently before the Aggregator combines their outputs into a professional review.

---

## Agents

### Bug Detection Agent

Detects:

- Logical bugs
- Runtime errors
- Edge cases
- Incorrect conditions
- Invalid indexing
- Off-by-one errors

---

### Complexity Analysis Agent

Analyzes:

- Algorithm identification
- Time Complexity
- Space Complexity
- Performance bottlenecks
- Optimization opportunities

---

### Style Review Agent

Reviews:

- Naming conventions
- Readability
- Maintainability
- Code duplication
- Formatting

---

### Security Agent

Checks for:

- Unsafe memory access
- Integer overflow
- Buffer overflow
- Dangerous pointer usage
- Common security vulnerabilities

---

### Aggregator Agent

Combines all agent reports into a single structured review containing:

- Overall Score
- Executive Summary
- Bug Analysis
- Complexity Analysis
- Style Analysis
- Security Analysis
- Priority Fixes
- Final Verdict

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- Streamlit

---

## Project Structure

```
CodeReviewer/
│
├── agents/
│   ├── supervisor.py
│   ├── bug.py
│   ├── complexity.py
│   ├── style.py
│   ├── security.py
│   └── aggregator.py
│
├── prompts/
│   ├── bug.txt
│   ├── complexity.txt
│   ├── style.txt
│   └── security.txt
│
├── utils/
│   └── parser.py
│
├── llm.py
├── graph.py
├── state.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/CodeReviewer.git

cd CodeReviewer
```

Create a virtual environment

### Linux / macOS / WSL

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```text
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Project

```bash
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

---

## Example Workflow

1. Upload or paste source code.
2. The Supervisor Agent detects the programming language.
3. The review agents analyze the code in parallel.
4. The Aggregator Agent combines the results.
5. A final professional code review is generated.
6. The report can be downloaded as a Markdown file.
