# Python Command-Line Calculator

A robust command-line calculator application built in Python.  
This project demonstrates best practices in software development, including a **REPL interface**, **Object-Oriented Programming (OOP)**, **input validation**, comprehensive testing with **pytest**, and a **CI/CD pipeline** using GitHub Actions.

---

## ✨ Features

- **REPL Interface**: A Read-Eval-Print Loop for continuous user interaction.  
- **Object-Oriented**: Core logic is encapsulated within an `Operations` class.  
- **Arithmetic Operations**: Supports Addition, Subtraction, Multiplication, and Division.  
- **Input Validation**: Gracefully handles non-numeric inputs and invalid operation choices.  
- **Error Handling**: Specifically handles division-by-zero errors.  
- **Well-Tested**: Achieves 100% test coverage with unit and parameterized tests.  
- **CI Integrated**: Uses GitHub Actions to automatically run tests and verify coverage on every push.  

---

## 📂 Project Structure

```bash
.
├── .github/
│ └── workflows/
│ └── tests.yml # GitHub Actions workflow configuration
├── app/
│ ├── init.py
│ ├── calculator/
│ │ └── init.py # Main application logic (REPL)
│ └── operations/
│ └── init.py # Core arithmetic functions (Operations class)
├── tests/
│ ├── init.py
│ ├── conftest.py
│ ├── test_calculator.py
│ └── test_operations.py
├── .coveragerc # Coverage tool configuration
├── .gitignore
├── LICENSE # MIT License file
├── main.py # Main entry point for the application
├── pytest.ini # Pytest configuration file
└── requirements.txt # Project dependencies
```

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- **Python 3.8+**: Make sure Python is installed and accessible from your command line.  
  👉 [Download Python](https://www.python.org/downloads/)  

- **Git**: You'll need Git to clone the repository.  
  👉 [Download Git](https://git-scm.com/downloads)  

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```
### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.
```bash
# Create the virtual environment (e.g., named 'venv')
python3 -m venv venv
```

Activate it:

- macOS/Linux/WSL:
```bash
source venv/bin/activate
```

- Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```

When active, you will see (venv) at the beginning of your terminal prompt.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---
## ▶️ How to Run the Application

With your virtual environment active, run the application from the project’s root directory:
```bash
python main.py
```

The application will start, and you can follow the on-screen prompts to perform calculations.

---
## ✅ Running Tests

This project uses pytest and pytest-cov for testing, with configurations managed in pytest.ini and .coveragerc.
The Continuous Integration pipeline requires 100% test coverage to pass.

- Run All Tests
```bash
pytest
```

- Run Tests with Coverage Check
```bash
pytest --cov=app --cov-fail-under=100
```
---

## 📄 License

This project is licensed under the MIT License.