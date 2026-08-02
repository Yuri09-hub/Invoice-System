# 📄 Invoice Management System

An invoice management application built with **Python**, **SQLAlchemy**, and **SQLite** that allows users to manage customers and invoices through a simple command-line interface.

This project was developed to practice database modeling, CRUD operations, object-relational mapping (ORM), and relationships between database entities.

---

## 🚀 Features

* User management

  * Create users
  * List all users
  * Prevent duplicate email registration

* Invoice management

  * Create invoices
  * Associate invoices with users
  * View invoice history
  * Automatic invoice creation date

* Database

  * SQLite database
  * SQLAlchemy ORM
  * One-to-many relationship between users and invoices

---

## 🛠️ Technologies Used

* SQLAlchemy
* SQLite
* Datetime

---

## 📂 Project Structure

```text
Invoice-System/
│
├── database.py
├── models.py
├── function.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Database Design

### User

| Field      | Type    |
| ---------- | ------- |
| id         | Integer |
| name       | String  |
| email      | String  |
| created_at | Date    |
| status     | Boolean |

### Invoice

| Field      | Type        |
| ---------- | ----------- |
| id         | Integer     |
| user_id    | Foreign Key |
| created_at | Date        |
| price      | Float       |

Relationship:

```text
User (1)
   │
   ├─────────────── (N)
                 Invoice
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Yuri09-hub/Invoice-System.git
cd Invoice-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the application:

```bash
python main.py
```

---

## 📸 Example Output

### User List

```text
=========================================================================
                              USER LIST
=========================================================================

ID      NAME                    EMAIL                          STATUS
-------------------------------------------------------------------------
1       Yuri Rodrigues          yuri@email.com                Active
2       John Smith              john@email.com                Active

=========================================================================
```

### Invoice History

```text
=========================================================================
                           INVOICE HISTORY
=========================================================================

ID      CUSTOMER                DATE            TOTAL
-------------------------------------------------------------------------
1       Yuri Rodrigues          02/08/2026      40000 Kz
2       John Smith              03/08/2026      15000 Kz

=========================================================================
```

---

## 🎯 Learning Objectives

This project helped reinforce the following concepts:

* CRUD operations
  
* SQLAlchemy ORM
  
* SQLite database management
  
* One-to-many relationships

* Database queries

* Python functions and modularization

* Command-line application development

---

## 👨‍💻 Author

**Yuri Rodrigues**

GitHub: **https://github.com/Yuri09-hub**

