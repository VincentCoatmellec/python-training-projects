# User Manager

This is a simple Python project I created to manage users with their contact information: first name, last name, address, and phone number. It works like a small address book stored locally using TinyDB.

## Description

I designed this project to practice object-oriented programming in Python with a real use case.

With this project, I practice:
- Organizing code with a `dataclass`
- Using `@property` for computed and database-related attributes
- Validating data with custom methods
- Using TinyDB as a lightweight local database
- Generating fake data with Faker for testing

The program lets you create, save, retrieve, and delete users from a local JSON database.

---

## Features

- Create a `User` with first name, last name, phone number, and address
- Validate names (no digits or special characters) and phone numbers
- Save users to a local TinyDB database
- Retrieve all users from the database
- Check if a user already exists in the database
- Delete a user from the database
- Generate fake users with `seed.py` for testing

---

## Requirements

- Python 3.13
- Install dependencies from `requirements.txt`

---

## How to Run It

1. **Navigate to the project directory**:
```bash
   cd project_10_crm_v2
```

2. **Create and activate a virtual environment** (recommended):
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

3. **Install dependencies**:
```bash
   pip install -r requirements.txt
```

4. **Seed the database with fake users**:
```bash
   python3 src/seed.py
```
---