# 🧠 GenAI Content Generator

An **end-to-end Generative AI platform** for automated content creation using open-source **1.3B parameter LLMs**, built with **FastAPI**, **React**, and **SQLite**. This project enables context-aware text generation, user authentication, and real-time interaction—all using **free and open-source technologies**.

---

## 🚀 Features

* 🤖 **Generative AI Model** – Powered by Hugging Face 1.3B parameter model for creative and factual content generation.
* ⚙️ **FastAPI Backend** – Modular API for prompt processing, authentication, and database operations.
* 💾 **SQLite Database** – Lightweight, file-based data persistence.
* 🔐 **JWT Authentication** – Secure user login and token-based access control.
* ⚡ **React Frontend** – Clean, responsive interface with real-time content generation.
* 🚀 **Optimized for CPU** – Efficient inference pipelines and caching for smooth performance.

---

## 🏗️ Project Structure

```
GENAI-CONTENT-GEN
├── backend
│   ├── __pycache__/
│   ├── app/
│   ├── data.sqlite
│   ├── migration/
│   ├── .env
│   ├── requirements.txt
│   ├── run.py
│   └── wsgi.py
│
├── frontend
│   ├── dist/
│   ├── dist/
│   ├── src/
│   ├── .env
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set environment variables

Create a `.env` file in the `backend` folder:

```bash
JWT_SECRET=your_secret_key
MODEL_NAME=EleutherAI/gpt-neo-1.3B
DATABASE_URL=sqlite:///data.sqlite
CORS_ORIGINS=*
```

### 4️⃣ Run the FastAPI server

```bash
python run.py
```

Backend will start at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 💻 Frontend Setup (React + Vite)

### 1️⃣ Navigate to frontend directory

```bash
cd frontend
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Start the development server

```bash
npm run dev
```

Frontend will run at **[http://localhost:5173](http://localhost:5173)** (by default).

---

## 🔗 API Endpoints

| Endpoint             | Method | Description                      |
| -------------------- | ------ | -------------------------------- |
| `/api/auth/register` | POST   | Register a new user              |
| `/api/auth/login`    | POST   | Authenticate user and return JWT |
| `/api/generate`      | POST   | Generate content from prompt     |
| `/api/history`       | GET    | Retrieve user generation history |

---

## 🔒 Security Best Practices

* Environment variables stored securely in `.env` files
* JWT-based authentication for API endpoints
* Input sanitization to prevent prompt injection or SQL injection

---

## 🧩 Tech Stack

| Layer        | Technology                       |
| ------------ | -------------------------------- |
| **Frontend** | React, Vite, HTML, CSS           |
| **Backend**  | FastAPI, Python                  |
| **Database** | SQLite                           |
| **Model**    | Hugging Face Transformers (1.3B) |
| **Auth**     | JWT                              |

---

## 🧠 How It Works

1. User logs in or registers securely.
2. User inputs a text prompt via the React frontend.
3. FastAPI backend processes the prompt and passes it to the 1.3B model.
4. Model returns generated text, stored in the SQLite database.
5. Result displayed instantly on the frontend.

---

## 🛡️ License

This project is licensed under the **MIT License** – free for personal and commercial use.

---

## 👨‍💻 Author

**Harsh Tikone**
M.S. in Engineering Science (AI) – SUNY Buffalo
⭐ 5-Star Python Developer | AI Engineer
