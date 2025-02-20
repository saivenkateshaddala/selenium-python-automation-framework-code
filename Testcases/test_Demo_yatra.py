import pytest

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import  Select

from webdriver_manager.chrome import ChromeDriverManager

from pages.Yatra_Filing_Details import FilingPersonalDetails

class TestPagesClass():


    def test_pagedemo(self,input_values):
        driver=input_values
        url="https://www.yatra.com/"
        driver.get(url)
        driver.maximize_window()
        trains_luxs=driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/luxury-trains']//div[@class='MuiBox-root css-tbbkkf']")
        trains_luxs.click()

        ip=FilingPersonalDetails(driver)
        ip.Namefalling("sai venkatesh",driver)
        ip.EmailDetail("saivenkateshaddala77@gmail.com",driver)
        ip.NumberNumeric("9030831377",driver)


        #driver.get_screenshot_as_file(r"C:\\Latest_Pytest_FrameWork\\Screenshot\\Optpage.png")
        time.sleep(4)
        driver.get_screenshot_as_file(r"C:\\Latest_Pytest_FrameWork\\Screenshot\\Optpage1.png")

