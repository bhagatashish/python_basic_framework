import pytest
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(request):  # request instace in by defaut
    print("before fixture")


'''everything written here will always
# get executed for all the files. The file is mandatory to have a name as "conftest"
# fixtures can be used to make the test case executable first. Like launching a browser etc
# data driven and parameterizartion can be done with return statements in tuple format
# when we define fixture to class only then it will run only once

'''


# go to path https://docs.pytest.org/en/6.2.x/example/simple.html to copy pytest_addoption() method
def pytest_addoption(
        parser):  # in built python method, carefully enter the correct name , otherwise python will start giving you internal errors

    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def openBrowser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\bhaga\\Downloads\\chromedriver_win32\\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.firefox(
            executable_path="C:\\Users\\bhaga\\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe")

    elif browser_name == "IE":
        driver = webdriver.ie(
            executable_path="C:\\Users\\bhaga\\Downloads\\IEDriverServer_x64_4.0.0\\IEDriverServer.exe")

    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver

