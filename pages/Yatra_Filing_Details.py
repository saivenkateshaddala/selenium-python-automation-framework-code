
import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

class FilingPersonalDetails():

    def __init__(self,input_values):

        driver=input_values

        #click Book Tour Button
        Book_tour = driver.find_element(By.XPATH, "//div[1]//div[3]//div[1]//div[2]//a[2]//span[1]")
        Book_tour.click()

        #Filling Personsl Details here
    def Namefalling(self,Parru,input_values):
        driver=input_values
        Name = driver.find_element(By.NAME, "name")
        Name.send_keys(Parru)
    def EmailDetail(self,Email_text,input_values):
        driver=input_values
        Email = driver.find_element(By.NAME, "email")
        Email.send_keys(Email_text)
    def NumberNumeric(self,Phone_number,input_values):
        driver=input_values
        Number = driver.find_element(By.NAME, "number")
        Number.send_keys(Phone_number)
        Train_name = driver.find_element(By.NAME, "train_names")
        dd = Select(Train_name)
        dd.select_by_index(3)
        Tour = driver.find_element(By.NAME, "train_types")
        dd = Select(Tour)
        dd.select_by_value("Indian Sojourn")
        Book_Now = driver.find_element(By.ID, "booknow-btn")
        Book_Now.click()