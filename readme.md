# Aura - Your Proactive Mental Fitness Companion
**SIH ID: 25092** | **Title:** Development of a Digital Mental Health and Psychological Support System for Students in Higher Education.

---

## ✨ Vision
Aura is not just another mental health app; it's a proactive, AI-powered companion designed to foster mental fitness as a daily habit for students. We're building a safe, intelligent, and deeply personalized sanctuary that anticipates needs before they become critical, bridging the gap between students and the support they deserve.

## 🚀 Core Features
- **🧠 Multi-Agent AI Companion:** An intelligent system powered by LangGraph that provides empathetic chat, resource recommendations, and guided wellness journeys.
- **🔐 Privacy-First by Design:** Featuring a zero-knowledge encrypted journal and fully anonymized data analytics.
- **📈 Proactive & Personalized Journeys:** Guided, gamified programs for specific challenges like exam stress or improving sleep.
- **📊 The "Campus Pulse":** An anonymized, real-time dashboard for university administrators to identify campus-wide mental health trends and allocate resources effectively.
- **🗣️ (Stretch Goal) Vocal Biomarkers & AR Sanctuaries:** Innovative features to provide deeper insight and connect wellness to the physical campus.

## 🛠️ Tech Stack
- **Frontend:** Next.js, React, Tailwind CSS, Shadcn/UI, Framer Motion
- **Backend:** FastAPI (Python)
- **AI/GenAI:** LangChain, LangGraph, LLMs (e.g., OpenAI/Gemini), Sentence-Transformers
- **Database:** PostgreSQL (Relational), Qdrant (Vector)
- **DevOps:** Docker, Docker Compose

---

## 🏁 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/) installed and running.
- Git installed.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd aura-sih-project
    ```

2.  **Configure Environment Variables:**
    - Create a `.env` file inside the `backend/` directory by copying the example:
      ```bash
      cp backend/.env.example backend/.env
      ```
    - Open `backend/.env` and fill in the required API keys and secrets (e.g., `OPENAI_API_KEY`, `SECRET_KEY`, etc.).

3.  **Build and Run the Services:**
    The entire application stack is orchestrated by Docker Compose.
    ```bash
    docker-compose up --build
    ```
    This command will build the backend container, download the database images, and start all services.

4.  **Accessing the Application:**
    - **Backend API & Docs:** `http://localhost:8000`
    - **Qdrant Dashboard:** `http://localhost:6333/dashboard`
    - **Frontend App:** `http://localhost:3000` (Once the frontend setup is complete)

---

## 🧑‍💻 Our Team

| Role | Developer | Responsibilities |
| :--- | :--- | :--- |
| 1️⃣ GenAI + Cybersecurity | **Dev 1** | LangGraph Agent Architecture, Security, Encryption |
| 2️⃣ AI + ML Engineer | **Dev 2** | RAG Pipeline, Vector DB Ingestion, Analytics |
| 3️⃣ Backend Engineer (API) | **Dev 3** | FastAPI Endpoints, Auth, Docker Environment |
| 4️⃣ Backend Engineer (DB) | **Dev 4** | PostgreSQL Schema, SQLModel, Data Anonymization |
| 5️⃣ Frontend Engineer | **Dev 5** | Next.js UI/UX, Component Design, API Integration |
| 6️⃣ Fullstack / QA / Support | **Dev 6** | Integration Testing, Bug Fixing, Dashboard Dev |