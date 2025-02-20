import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def key_values():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()
    print("it is working fine")

def test_nms_dashboard(key_values):
    driver=key_values
    driver.get("https://wavelabs.nms.pmn-dev.wavelabs.in/")
    driver.maximize_window()

    # Bypass security warnings
    driver.find_element(By.XPATH, "//button[@id='details-button']").click()
    driver.find_element(By.XPATH, "//a[text()='Proceed to wavelabs.nms.pmn-dev.wavelabs.in (unsafe)']").click()

    # Login
    driver.find_element(By.NAME, "email").send_keys("wl@wavelabs.ai")
    driver.find_element(By.NAME, "password").send_keys("password1234")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    # Wait for and interact with the Network button
    wait = WebDriverWait(driver, 15)
    network = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Network: masternet']")))
    network.click()
    print("Network button clicked")

    # Select Network
    network_select_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='vm-gw']")))
    network_select_button.click()
    print("Network is selected")

    # Click Dashboard button
    dashboard_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".jss58.jss59")))
    dashboard_button.click()
    print("Dashboard button clicked")

    # Open Subscribers tab
    subsciber_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/nms/vm-gw/subscribers']")))
    subsciber_tab.click()
    print("Subscriber tab clicked")

    print(driver.title)
    print(driver.current_url)
    time.sleep(4)

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "tbody tr:nth-child(2) td:nth-child(7) div:nth-child(1) button:nth-child(1) svg"))).click()
    time.sleep(4)
    remove = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Remove']")))
    remove.click()
    time.sleep(4)
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Confirm']")))
    confirm_button.click()

    time.sleep(4)
    # driver.quit()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Manage Subscribers']"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Subscribers']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Upload CSV']"))).click()

    file_path = r"C:\Latest_Pytest_FrameWork\TestData\subscribers_1738058399343.csv"  # Correct path to the file
    print("Upload CSV")

    # Locate the file input element and upload the file
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(file_path)
    print("File uploaded successfully")

    time.sleep(5)

    save_and_add_file = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save and Add Subscribers']")))
    save_and_add_file.click()

    time.sleep(5)

    driver.get_screenshot_as_file(r"C:\\Latest_Pytest_FrameWork\\Screenshot\\nms1.png")
    print("subscriber is successfully added ")



    # os.system(r'"C:\Users\Devarapu Ganesh\Downloads\MobaXterm_Portable_v23.2 (1)\MobaXterm_Personal_23.2.exe"')

    time.sleep(7)

