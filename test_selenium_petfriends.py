import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_my_pets():
    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    # Вводим email и пароль
    pytest.driver.find_element_by_id('email').send_keys('evgenagurkina@yandex.ru')
    pytest.driver.find_element_by_id('pass').send_keys('gurnetur')

    # Устанавливаем неявные ожидания
    pytest.driver.implicitly_wait(10)

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Настраиваем переменную явного ожидания
    wait = WebDriverWait(pytest.driver, 10)

    # Проверяем, что оказались на главной странице
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    # Открываем страницу Мои питомцы
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # Проверяем, что мы оказались на  странице Мои питомцы
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # Настраиваем переменную явного ожидания
    wait = WebDriverWait(pytest.driver, 10)

    # Ищем в таблице все строки с полными данными питомцев (имя, порода, возраст, "х")
    css_locator = 'tbody>tr'
    data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)

    # Ожидаем, что данные всех питомцев, найденных локатором css_locator = 'tbody>tr', отображены на странице
    for i in range(len(data_my_pets)):
        assert wait.until(EC.visibility_of(data_my_pets[i]))

    # Ищем в таблице все фотографии питомцев; ожидаем, что все загруженные фото, отображены на странице
        image_my_pets = pytest.driver.find_elements_by_css_selector('img[style="max-width: 100px; max-height: 100px;"]')
        for i in range(len(image_my_pets)):
            if image_my_pets[i].get_attribute('src') != '':
                assert wait.until(EC.visibility_of(image_my_pets[i]))

    # Ищем все имена питомцев; ожидаем увидеть их на странице
        name_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
        for i in range(len(name_my_pets)):
            assert wait.until(EC.visibility_of(name_my_pets[i]))

    # Ищем все породы питомцев; ожидаем увидеть их на странице
        type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
        for i in range(len(type_my_pets)):
            assert wait.until(EC.visibility_of(type_my_pets[i]))

    # Ищем все возраста питомцев; ожидаем увидеть их на странице
        type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')
        for i in range(len(type_my_pets)):
            assert wait.until(EC.visibility_of(type_my_pets[i]))

    # Ищем на странице Мои питомцы статистику пользователя; вычленяем из полученных данных количество питомцев пользователя
        all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
        statistics_pets = all_statistics[1].split(" ")
        all_my_pets = int(statistics_pets[-1])

      # Проверяем, что количество строк в таблице совпадает с общим количеством питомцев в статистике
        assert len(data_my_pets) == all_my_pets

      # Проверяем, что у всех питомцев есть имя
        for i in range(len(name_my_pets)):
            assert name_my_pets[i].text != ''

      # Проверяем, что у всех питомцев есть порода
        for i in range(len(type_my_pets)):
            assert type_my_pets[i].text != ''

      # Проверяем, что у всех питомцев разные имена
      # Устанавливаем явное ожидание
        element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

        list_name_my_pets = []
        for i in range(len(name_my_pets)):
            list_name_my_pets.append(name_my_pets[i].text)
        set_name_my_pets = set(list_name_my_pets)  #изменяем список на множество
        assert len(list_name_my_pets) == len(set_name_my_pets)  # сравниваем длину списка и множества

      # Проверяем, что в списке нет повторяющихся питомцев
      # Устанавливаем явное ожидание
        element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

        list_data_my_pets = []
        for i in range(len(data_my_pets)):
            list_data = data_my_pets[i].text.split("\n")  # отделяем символ "х"
            list_data_my_pets.append(list_data[0])  # выбираем элемент с данными питомца и добавляем его в список
            set_data_my_pets = set(list_data_my_pets)  # изменяем список на множество
        assert len(list_data_my_pets) == len(set_data_my_pets)  # сравниваем длину списка и множества


#python -m pytest -v --driver Chrome --driver-path C:/Users/Пользователь/PycharmProjects/pythonProject_25/chromedriver.exe  test_selenium_petfriends.py








