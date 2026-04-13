# 🩹 Self-Healing CI/CD Pipeline

> **Winner of the Wakanda Data & Captain Code Awards** (Hopefully!) 🏆

A fully autonomous DevOps agent that detects CI/CD failures, performs Root Cause Analysis (RCA) using **Google Gemini 2.0 Flash**, and automatically generates code fixes validated by **CodeRabbit**.

---

## 🏗 Architecture

```
GitHub Push → CI Fails → Webhook → Kestra Flow 01 (RCA via Gemini)
  → Flow 02 (AI Code Fix) → Flow 03 (Create PR) → Flow 04 (Validate & Merge)
```

1. **Failure Detection:** GitHub Actions triggers a webhook upon pipeline failure.
2. **Orchestration:** **Kestra** receives the signal and starts the recovery flow.
3. **Analysis:** **Gemini 2.0** analyzes the logs + source code to identify the root cause.
4. **Repair:** The agent creates a fix, pushes a new branch, and opens a PR.
5. **Validation:** **CodeRabbit** reviews the fix for quality assurance.

---

## 📂 Project Structure

```
self-healing-demo-main/
├── src/                        # Application source code (e.g., calc.py)
├── tests/                      # Pytest suites designed to catch regressions
├── kestra/flows/               # Orchestration logic (YAML definitions)
│   ├── 01-failure-intake-rca.yaml    # Receives CI failure, runs Gemini RCA
│   ├── 02-cline-code-fixer.yaml      # AI generates the code fix
│   ├── 03-automated-pr-creator.yaml  # Pushes fix branch & opens PR
│   └── 04-auto-merge-validator.yaml  # Validates & auto-merges
├── .github/workflows/          # CI pipeline configuration
│   └── ci.yml                  # GitHub Actions workflow
├── Dockerfile                  # Custom Kestra image with AI plugin
├── docker-compose.yml          # Docker Compose for Kestra
├── requirements.txt            # Python dependencies
├── .env.example                # Template for environment variables
└── README.md
```

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| **Kestra** | Workflow orchestration |
| **Google Gemini 2.0 Flash** | AI-powered root cause analysis & code fixing |
| **GitHub Actions** | CI pipeline |
| **CodeRabbit** | Automated code review & quality assurance |
| **Docker** | Containerized execution |
| **ngrok** | Expose local Kestra to GitHub webhooks |

---

## ⚙️ Prerequisites

| Tool | Purpose | Install |
|---|---|---|
| **Docker & Docker Compose** | Runs Kestra orchestrator | [docker.com](https://docs.docker.com/get-docker/) |
| **Python 3.11+** | Local testing | `brew install python@3.11` |
| **Git** | Version control | Pre-installed on macOS |
| **ngrok** | Expose local Kestra to GitHub webhooks | `brew install ngrok` |

---

## 🚀 Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/self-healing-demo.git
cd self-healing-demo
```

### 2. Create Your `.env` File

```bash
cp .env.example .env
```

Edit `.env` and fill in your real keys:

| Variable | Where to Get It |
|---|---|
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/apikey) |
| `GITHUB_TOKEN` | [GitHub Settings → Tokens](https://github.com/settings/tokens) — needs **Contents (R/W)**, **Pull Requests (R/W)**, **Metadata (Read)** permissions |

### 3. Start Kestra via Docker Compose

```bash
docker compose up --build
```

This will:
- Build a custom Kestra image with the AI plugin installed
- Start Kestra on **http://localhost:8080**
- Mount your Kestra flows from `kestra/flows/`

### 4. Import the Kestra Flows

Once Kestra is running:

1. Open **http://localhost:8080** in your browser
2. Go to **Flows** → **Import**
3. Import all 4 YAML files from `kestra/flows/`

### 5. Expose Kestra with ngrok

```bash
ngrok http 8080
```

Copy the `https://xxxx.ngrok.io` URL — you'll need it for GitHub secrets.

### 6. Configure GitHub Repository Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions**, and add:

| Secret Name | Value |
|---|---|
| `GEMINI_API_KEY` | Your Gemini API key |
| `SELF_HEALING_GITHUB_TOKEN` | Your GitHub PAT |
| `KESTRA_WEBHOOK_URL` | `https://<your-ngrok-url>/api/v1/executions/webhook/company.self-healing/failure-intake-rca/ci-failure-webhook` |

### 7. (Optional) Local Python Testing

```bash
pip install -r requirements.txt
pytest tests/
```

---

## 🧪 Running the Demo

### Step 1: Introduce a Bug

Modify `src/calc.py` to break logic (e.g., change `+` to `-` in the `add` function):

```python
def add(a, b):
    return a - b  # 💥 Bug introduced!
```

### Step 2: Push to Main

```bash
git commit -am "Oops, broken code"
git push origin main
```

### Step 3: Watch the Magic

1. Go to the **Actions** tab → Watch the CI pipeline fail
2. **Kestra UI** (http://localhost:8080) → Watch the 4-flow chain execute automatically
3. Go to **Pull Requests** → See the AI agent open a fix PR automatically!

---

## 📜 License

MIT