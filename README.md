# Palindrome test with Pytest

This repository contains a **palindrome.py** file containing a function that checks if the string given as input is a palindrome. 

The file **palindrome_test.py** contains tests using the **pytest** library to validate the **is_palindrome()** function.

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

Next you have to install all required packages.


## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which is **pytest**, and optionally you can also install **pytest-watch**. You can use the command below.

```bash
pip install pytest pytest-watch
```

## Launch

To run a given program, you can use the IDE or the system console by typing the example command:

```bash
python palindrome.py
```

To run tests for the function used in the main program, you can use the terminal command given below:

```bash
pytest palindrome_test.py
```

You can also use the **pytest-watch** tool to start all tests by typing the following command in the terminal:

```bash
ptw
```

This will run all the tests, and they will also run whenever you make any changes to the file and then save them.
