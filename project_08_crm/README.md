# User Manager

This is a simple Python project I created to manage users with their contact information: first name, last name, address, and phone number. Basically, it works like a small address book, similar to what you find in many CRMs (Customer Relationship Management).

## Description

I designed this project to help me learn the basics of a professional Python project.

With this project, I practice:
- Organizing code and files
- Creating a virtual environment
- Using `pip` to manage packages
- Documenting my code
- Adding logging

The program itself is simple, so I can focus on how a real Python project is structured, including tests, logging, and documentation.

Later, I will also use this project to practice:
- Object-oriented programming
- Unit testing
- Building command-line programs with Typer
- Creating web APIs with Django

---

## Requirements

- Python 3.13
- Install dependencies from `requirements.txt`

---

## How to Run It

1. **Accède au dossier du projet** :
   ```bash
   cd project_08_crm
   ```

2. **Crée et active un environnement virtuel** (recommandé) :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows : `venv\Scripts\activate`
   ```

3. **Installe les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Lance le programme** :
   ```bash
   python3 src/user_generator/main.py
   ```