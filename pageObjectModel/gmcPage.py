from selenium.webdriver.common.by import By


class checkout:
    def __init__(self, driver):
        self.driver = driver

    elements_locators = (By.XPATH, "//a[contains(text(),'Samsung Note 8')]")
    namefield_locator = (By.XPATH, ".//div/input[@name = 'name']")
    emailfield_locator = (By.XPATH, ".//div/input[@name = 'email']")
    passwordfield_locator = (By.XPATH, ".//*[@type= 'password']")
    genderfield_locator = (By.XPATH, ".//*[@id= 'exampleFormControlSelect1']")

    def device_checkout(self):
        return self.driver.find_element(*checkout.elements_locators)

    def inputName(self):
        return self.driver.find_element(*checkout.namefield_locator)

    def inputEmail(self):
        return self.driver.find_element(*checkout.emailfield_locator)

    def inputpassword(self):
        return self.driver.find_element(*checkout.passwordfield_locator)

    def genderselect(self):
        return self.driver.find_element(*checkout.genderfield_locator)



