import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    print("it is working ")


class TestDemoGoogle():
    @pytest.mark.parametrize("searching", [("www.pytest documentation"),("pytest framework"), ("selenium python")])

    def test_DemoGoogle(self,driver,searching):

        driver.get("https://www.google.com/")
        driver.maximize_window()
        Search=driver.find_element(By.NAME, "q")
        Search.send_keys(searching)
        time.sleep(1)

    @pytest.mark.parametrize("email,password", [("saivenkateshaddala77@gmail.com","A868850@s"),("saivenkatesh.addala@veltris.com","A868850@"),("addalasaicse2019@gmail.com","sai@123")])

    def test_DemoYatra(self,driver,email,password, ):


        driver.get("https://www.tutorialspoint.com/market/login.jsp")
        driver.maximize_window()
        e=driver.find_element(By.ID, "login_email")
        e.send_keys(email)
        p=driver.find_element(By.ID, "login_password")
        p.send_keys(password)
        print(f"It is passes {password} here")
        time.sleep(2)


