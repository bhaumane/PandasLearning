# PandasLearning
This repository contains all the information related to Python Pandas Learning.

---
## __name__ == "__main__"

In Python, if __name__ == "__main__": is a conditional statement used to determine whether a script is being run directly or being imported as a module into another script.

### How It Works
Every Python file has a built-in special variable called __name__. The Python interpreter sets this variable automatically before executing any code in the file:

- **Running Directly**: If you run the script itself (e.g., python script.py), Python assigns the string "__main__" to the __name__ variable.
- **Importing as a Module**: If you import the script into another file (e.g., import script), Python assigns the filename (without the .py extension) to the __name__ variable

```bash
def my_function():
    print("This function is reusable.")

def main():
    print("This runs only if executed directly.")
    my_function()

if __name__ == "__main__":
    main()

```

If you run this file directly, it will print both messages. If you import it into another file, only my_function will be available for use, and nothing will be printed automatically.

---

## pip freeze > requirements.txt

The **pip freeze > requirements.txt** is a command used in the context of Python programming to generate a file called requirements.txt. This file contains a list of all the installed packages in your Python environment, along with their corresponding versions.

The generated requirements.txt file is often used to share and manage dependencies in a Python project. When collaborating with others, it helps ensure that everyone is using the same package versions, which can prevent compatibility issues. To install the packages listed in a requirements.txt file, you can run the command **pip install -r requirements.txt**

---