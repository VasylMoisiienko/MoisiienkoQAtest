import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту керування браузером
    driver = webdriver.Chrome(
        service=Service(r"C:\Users\38067\MoisiienkoQAtest" +
                        r"\chromedriver.exe")
    )
    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача
    login_elem = driver.find_element("id", "login_field")

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("vasylmoisiienko@mistakinemail.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element("id", "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_elem = driver.find_element("name", "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()
