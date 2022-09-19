from selenium.webdriver.common.by import By


class homePage:
    def __init__(self, driver): # created a constructor , so that we can access it from actuall test, here driver is an argument, it could be of any name
        self.driver = driver
    homepage_variable = (By.XPATH, "//*[contains(text(),'Shop')]")  # created a tuple

    input_name = (By.XPATH, "//*[@name='name']")
    input_email = (By.XPATH, "//*[@name='email']")
    input_password = (By.XPATH, "//*[@placeholder='Password']")
    checkbox = (By.XPATH, "//*[@type = 'checkbox']")

    def access_homepage(self):
        return self.driver.find_element(*homePage.homepage_variable).click()

    def input_name(self , name ):
        print(homePage.homepage_variable)
        return self.driver.find_element(*homePage.input_name).sendkeys(name)

    def input_email(self , email):
        print(homePage.homepage_variable)
        return self.driver.find_element(*homePage.input_email).sendkeys(email)

    def input_password(self , password):
        print(homePage.homepage_variable)
        return self.driver.find_element(*homePage.input_password).sendkeys(password)

    def checkbox(self):
        print(homePage.homepage_variable)
        return self.driver.find_element(*homePage.checkbox).click()








