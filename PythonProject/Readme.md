Follow these steps to set up and run your Selenium + Pytest automation framework


1.Install Dependencies
Since we are not using a virtual environment, install the required packages globally.

🔹 Install Required Python Packages

This will install:

selenium>=4.11.0
pytest==7.4.0
pytest-xdist==3.3.1
pytest-html==4.0.2
pytest-rerunfailures==12.0
webdriver-manager==4.0.1
pytest-selenium-auto==1.3.1

The command pip install -r requirements.txt will install all the dependencies listed in the requirements.txt file.
command :pip install -r requirements.txt
2. Run the Tests
Run All Tests:pytest tests/

3.Generate HTML Report:
pytest tests/ --html=reports/test_report.html --self-contained-html

--->this will generate a proper HTML report.
The report file can be found in the reports/test_report.html folder.

4.Run Specific Test File:
pytest tests/test_login.py

