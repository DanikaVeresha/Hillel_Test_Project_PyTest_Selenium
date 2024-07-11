# Hillel_Test_Project_PyTest_Selenium

## To start working with a project on the Windows operating system, you need to:

1. Copy the HTTPS address of the repository
2. Open a terminal in PyCharm IDE
3. Run the following command in terminal
> clone git https://github.com/DanikaVeresha/Hillel_Test_Project_PyTest_Selenium.git
4. Create a virtual environment. Command to create a virtual environment
> py -m venv <virtual_environment_name>
5. Activate your virtual environment using the command in the terminal
> <virtual_environment_name>\Scripts\activate
5. Install the following dependencies by running the command in terminal
> pip install pytest, selenium
6. Go to the project root directory
7. Run the setup.py file with the command
> pip install -e .
8. From the root directory, go to the __"Tests"__ directory
9. Open the Python file __“test_login_page.py”__
10. Run the file for execution by clicking the __“Run”__ button.

## If you want to run the project from the PyCharm IDE terminal, run the following commands in the terminal:

1. Open a terminal in PyCharm IDE
2. Create a virtual environment. Command to create a virtual environment
> py -m venv <virtual_environment_name>
3. Activate the virtual environment using the following command
> <virtual_environment_name>\Scripts\activate
4. Enter the command
> pytest
5. or -> 
> >py -m pytest [test_login_page.py]

### P.S. This project was developed on:
OS -> Windows 3.11;
Python version -> 3.12;
pip version -> 24.1.1;
pytest version -> 8.2.2;
selenium version -> 4.22.0;
Win32 platform;
