# fixtures can be used to make the test case executable first. Like launching a browser etc
# class name should always start with Camel Case
# if you ever create a class , then method must have 'self' argument
# the fixture defined in conftest will get executed before each method . if given at class leve;
# But if you want to run the fixture only once , then go to conftest file and add scope == class
# class name should always start with keyword Test , otherwise pytest will not run
# method name should have start with test
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjectModel.gmcPage import checkout
from pageObjectModel.homePage import homePage

from utilities.baseclass import baseclass



class Teste2e(baseclass):
    def test_openbrowser(self, forms):
        log = self.getlogger()
        log.info("print info logs")
        homepage = homePage(self.driver)  # sending driver argument to constructor
        homepage.access_homepage()  # here we can access homepage methods by using homepage object
        checkout_page = checkout(self.driver)
        checkout_page.device_checkout().click()
        log.info("ckicked the item ")
        checkout_page.inputName().send_keys(forms["name"])
        log.info("entered name ")
        checkout_page.inputEmail().send_keys(forms["email"])
        checkout_page.inputpassword().send_keys("1234")
        gender_dropdown = Select(checkout_page.genderselect())
        gender_dropdown.select_by_visible_text(forms["gender"])

    @pytest.fixture(params=[{"name": "ashu", "email": "test@gmail.com", "gender": "male"}])
    def forms(self, request):
        return request.param
