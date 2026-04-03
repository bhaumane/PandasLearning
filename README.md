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