# FastAPI CRUD Operations with MongoDB

This project is a simple FastAPI application that performs CRUD (Create, Read, Update, Delete) operations using MongoDB.

---

## 🚀 Features
- Create new tasks
- Read all active tasks
- Update existing tasks
- Soft delete tasks using `is_deleted` flag
- REST API built using FastAPI
- MongoDB integration using PyMongo

---

## 🛠️ Technologies Used
- Python
- FastAPI
- MongoDB
- PyMongo
- Uvicorn

---

## 📂 Project Structure
curd_operation/
│
├── main.py
├── configrations.py
├── database/
│ ├── models.py
│ ├── schemas.py
│
├── README.md
├── .gitignore

yaml
Copy code

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
2️⃣ Activate Virtual Environment
Windows (VS Code Terminal)

bash
Copy code
venv\Scripts\Activate
3️⃣ Install Dependencies
bash
Copy code
pip install fastapi uvicorn pymongo dnspython
4️⃣ Start the Server
bash
Copy code
uvicorn main:app --reload --port 5000
🌐 API Documentation
Open in browser:

arduino
Copy code
http://127.0.0.1:5000/docs
📌 API Endpoints
Method	Endpoint	Description
GET	/	Get all tasks
POST	/	Create a task
PUT	/{task_id}	Update a task
DELETE	/{task_id}	Soft delete a task

🧠 Explanation
This application uses FastAPI for building REST APIs and MongoDB as the database. Instead of deleting records permanently, soft delete is implemented using an is_deleted flag.
