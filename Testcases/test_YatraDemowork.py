from selenium.webdriver.common.by import By
import time

import pytest

@pytest.mark.usefixtures("input_values")
class TestYatraDemo():
    @pytest.mark.parametrize("email,mobile_number,password,title,first_name,Last_name", [("saivenkatesh@gamil.com","9030831377","A868850@s","Mr.","sai venkatesh","Addala")])

    def test_ParameYatraDemo(self,email,mobile_number,password,title,first_name,Last_name):

        self.driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "login-input").send_keys(email)
        self.driver.find_element(By.ID, "login-continue-btn").click()
        Mobile_number=self.driver.find_element(By.ID, "signup-mobile-number")
        Mobile_number.send_keys(mobile_number)
        Create_password=self.driver.find_element(By.ID,"signup-password")
        Create_password.send_keys(password)
        Title_Name=self.driver.find_element(By.ID, "signup-user-designation")
        Title_Name.send_keys(title)
        First_Name=self.driver.find_element(By.ID, "signup-user-first-name")
        First_Name.send_keys(first_name)
        Last=self.driver.find_element(By.ID,"signup-user-last-name")
        Last.send_keys(Last_name)
        self.driver.find_element(By.XPATH, "//label[@for='specialPromoNotif']").click()
        self.driver.find_element(By.XPATH,"//label[@for='whatsAppNotif']").click()
        Create_Account=self.driver.find_element(By.ID, "signup-form-continue-btn")
        Create_Account.click()
        time.sleep(5)
        self.driver.get_screenshot_as_file(r"C:\\Latest_Pytest_FrameWork\\Screenshot\\YATRA1.png")
        time.sleep(2)
        print(self.driver.current_url)
        print(self.driver.title)




