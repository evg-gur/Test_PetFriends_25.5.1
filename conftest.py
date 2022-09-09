import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)

def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Пользователь/PycharmProjects/pythonProject_25/chromedriver.exe')
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


