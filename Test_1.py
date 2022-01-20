from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main_Test(value,cl,tag):
   # s=Service(ChromeDriverManager().install())
   # driver = webdriver.Chrome(service=s)
   driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
   driver.get("https://pentaschool.ru/")
   input_username = driver.find_element(By.XPATH,'//*[@id="form_are_questions"]/div[1]/div[1]/input')
   send_button = driver.find_element(By.XPATH,'//*[@id="form_are_questions"]/div[1]/div[4]/button')

   input_username.send_keys(value)
   send_button.click()
   error_alarm = driver.find_element(By.CLASS_NAME,cl)
   items = error_alarm.find_elements(By.TAG_NAME,tag)
   for item in items:
      if 'Поле Имя должно быть заполнено русскими буквами.' in item.text:
         return(False)
      elif 'ФИО должно быть не менее 2 букв'  in item.text:
         return(False)

   return(True)