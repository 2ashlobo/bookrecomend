![Screenshot 2025-07-06 174226](https://github.com/user-attachments/assets/1a5a34dc-c9bb-45fe-b56a-d7ae8ec3910d)
![Screenshot 2025-07-06 174256](https://github.com/user-attachments/assets/3757763b-6d28-41b5-ac5d-9e304ace95a4)
![Screenshot 2025-07-06 174328](https://github.com/user-attachments/assets/d8fb1129-4c10-4142-af71-be08fa4a68ba)
![Screenshot 2025-07-06 174344](https://github.com/user-attachments/assets/a02728f8-cf3b-423d-a37b-4bdc67fcd1cb)
# 📚 BookRecomend

A Django-based Book Management and Recommendation Web App.

## 🔧 Tech Stack

- 🐍 Python 3
- 🌐 Django Web Framework
- 🗃️ SQLite (default) or PostgreSQL
- 🎨 HTML/CSS (Bootstrap)
- 🔐 Django Authentication

## 🚀 Features

- User registration and login
- Add, edit, delete, and view books
- Book ratings and genres
- Search by title and genre
- Responsive UI

## ▶️ Run Locally

```bash
git clone https://github.com/2ashlobo/bookrecomend.git
cd bookrecomend
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
