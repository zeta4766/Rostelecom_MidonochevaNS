import time
import uuid

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException

from Pages.locators import ErrorLocators
from Pages.reg_page import RegPage
from functions import *


@pytest.fixture
def setup_teardown():
    # Фикстура, открывающая и закрывающая драйвер
    page = RegPage(driver=webdriver.Chrome())
    yield page
    page.driver.quit()


@pytest.fixture
def enter_correct_data(request, setup_teardown, phone):
    # Фикстура для заполнения полей корректными данными
    # Применяется для тестирования страницы с кодом подтверждения
    page = setup_teardown
    firstname, lastname = generator_valid_text_for_name(10, ''), generator_valid_text_for_name(10, '')
    page.enter_firstname(firstname)
    page.enter_lastname(lastname)
    page.dropdown_click()
    option = page.option_click()
    # Заполнить email или телефон
    if phone:
        address = correct_phone_number()
    else:
        address = correct_email()
    page.enter_address(address)
    text = correct_password()
    page.enter_password(text)
    page.enter_password_confirm(text)
    page.button_click()
    request.node.funcargs['params'] = [firstname.title(), lastname.title(), option, address.title(), text, text]


def test_auth_page_elements(setup_teardown):
    # Проверка наличия элементов на странице и их названий
    page = setup_teardown
    etalon = iter(['Имя', 'Фамилия', 'Регион', 'E-mail или мобильный телефон',
                   'Пароль', 'Подтверждение пароля', 'Продолжить'])
    elements = page.labels
    for element in elements:
        assert element.text == next(etalon)
    assert page.button.text == next(etalon)


@pytest.mark.parametrize("n, delimiter", return_data('enter_name'))
def test_enter_firstname_correct(n: int, delimiter: str, setup_teardown):
    # Тестирует поле "Имя" с корректными данными
    page = setup_teardown
    text = generator_valid_text_for_name(n, delimiter)
    page.enter_firstname(text)
    page.driver.execute_script("arguments[0].blur();", page.firstname)
    try:
        page.driver.implicitly_wait(2)
        page.driver.find_element(*ErrorLocators.ERR_LABEL)
        page.driver.save_screenshot(f"Screens/test_enter_firstname_correct/{text}.png")
        assert False
    except NoSuchElementException:
        assert True


@pytest.mark.parametrize("n, delimiter", return_data('enter_name'))
def test_enter_lastname_correct(n: int, delimiter: str, setup_teardown):
    # Тестирует поле "Фамилия" с корректными данными
    page = setup_teardown
    text = generator_valid_text_for_name(n, delimiter)
    page.enter_lastname(text)
    page.driver.execute_script("arguments[0].blur();", page.lastname)
    try:
        page.driver.implicitly_wait(2)
        page.driver.find_element(*ErrorLocators.ERR_LABEL)
        page.driver.save_screenshot(f"Screens/test_enter_lastname_correct/{text}.png")
        assert False
    except NoSuchElementException:
        assert True


@pytest.mark.parametrize("text", return_data('enter_name_un'))
def test_enter_firstname_incorrect(text: str, setup_teardown):
    # Тестирует поле "Имя" с некорректными данными
    page = setup_teardown
    page.enter_firstname(text)
    page.driver.execute_script("arguments[0].blur();", page.firstname)
    try:
        page.driver.implicitly_wait(2)
        page.driver.find_element(*ErrorLocators.ERR_LABEL)
        assert True
    except NoSuchElementException:
        page.driver.save_screenshot(f"Screens/test_enter_firstname_incorrect/{text}.png")
        assert True


@pytest.mark.parametrize("text", return_data('enter_name_un'))
def test_enter_lastname_incorrect(text: str, setup_teardown):
    # Тестирует поле "Фамилия" с некорректными данными
    page = setup_teardown
    page.enter_lastname(text)
    page.driver.execute_script("arguments[0].blur();", page.lastname)
    try:
        page.driver.implicitly_wait(2)
        page.driver.find_element(*ErrorLocators.ERR_LABEL)
        assert True
    except NoSuchElementException:
        page.driver.save_screenshot(f"Screens/test_enter_lastname_incorrect/{text}.png")
        assert True


def test_dropdown(setup_teardown):
    # Тестирование выпадающего списка регионов
    page = setup_teardown
    page.dropdown_click()
    label = page.option_click()
    assert label == page.return_region_name()


def test_enter_address_correct_number(setup_teardown):
    # Тестирует поле "email или телефон" с корректным телефоном
    page = setup_teardown
    result = []
    for _ in range(10):
        page.clear_address()
        text = correct_phone_number()
        page.enter_address(text)
        page.driver.execute_script("arguments[0].blur();", page.address)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            page.driver.save_screenshot(f"Screens/test_enter_address_correct/{text}.png")
            result.append((text, False))
        except NoSuchElementException:
            result.append((text, True))
    assert all(map(lambda x: x[1], result))


def test_enter_address_incorrect_number(setup_teardown):
    # Тестирует поле "email или телефон" с некорректным телефоном
    page = setup_teardown
    result = []
    for _ in range(10):
        page.clear_address()
        text = incorrect_phone_number()
        page.enter_address(text)
        page.driver.execute_script("arguments[0].blur();", page.address)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            result.append((text, True))
        except NoSuchElementException:
            page.driver.save_screenshot(f"Screens/test_enter_address_correct/{text}.png")
            result.append((text, False))
    assert all(map(lambda x: x[1], result))


def test_enter_address_correct_email(setup_teardown):
    # Тестирует поле "email или телефон" с корректным email
    page = setup_teardown
    result = []
    for _ in range(10):
        page.clear_address()
        text = correct_email()
        page.enter_address(text)
        page.driver.execute_script("arguments[0].blur();", page.address)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            page.driver.save_screenshot(f"Screens/test_enter_address_correct/{text}.png")
            result.append((text, False))
        except NoSuchElementException:
            result.append((text, True))
    assert all(map(lambda x: x[1], result))


def test_enter_address_incorrect_email(setup_teardown):
    # Тестирует поле "email или телефон" с некорректным email
    page = setup_teardown
    result = []
    for _ in range(10):
        page.clear_address()
        text = incorrect_email()
        page.enter_address(text)
        page.driver.execute_script("arguments[0].blur();", page.address)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            result.append((text, True))
        except NoSuchElementException:
            page.driver.save_screenshot(f"Screens/test_enter_address_correct/{text}.png")
            result.append((text, False))
    assert all(map(lambda x: x[1], result))


def test_enter_password(setup_teardown):
    # Тестирует поля "Пароль" и "Подтверждение пароля" с корректными данными
    page = setup_teardown
    result = []
    page.eye_password_click()
    page.eye_password_confirm_click()
    for _ in range(10):
        page.clear_password()
        page.clear_password_confirm()
        text = correct_password()
        page.enter_password(text)
        page.enter_password_confirm(text)
        page.driver.execute_script("arguments[0].blur();", page.password)
        page.driver.execute_script("arguments[0].blur();", page.password_confirm)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            page.driver.save_screenshot(f"Screens/test_enter_password/{text}.png")
            result.append((text, False))
        except NoSuchElementException:
            result.append((text, True))
    assert all(map(lambda x: x[1], result))


def test_enter_password_incorrect(setup_teardown):
    # Тестирует поле "Пароль" с некорректными данными
    page = setup_teardown
    result = []
    page.eye_password_click()
    for _ in range(10):
        page.clear_password()
        text = incorrect_password()
        page.enter_password(text)
        page.driver.execute_script("arguments[0].blur();", page.password)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            result.append((text, True))
        except NoSuchElementException:
            page.driver.save_screenshot(f"Screens/test_enter_password/{text}.png")
            result.append((text, False))
    assert all(map(lambda x: x[1], result))


def test_enter_password_confirm_incorrect(setup_teardown):
    # Тестирует поле "Подтверждение пароля" с некорректными данными
    page = setup_teardown
    result = []
    page.eye_password_confirm_click()
    for _ in range(10):
        page.clear_password_confirm()
        text = incorrect_password()
        page.enter_password_confirm(text)
        page.driver.execute_script("arguments[0].blur();", page.password_confirm)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            result.append((text, True))
        except NoSuchElementException:
            page.driver.save_screenshot(f"Screens/test_enter_password/{text}.png")
            result.append((text, False))
    assert all(map(lambda x: x[1], result))


def test_enter_difference_password(setup_teardown):
    # Тестирует поля "Пароль" и "Подтверждение пароля" с различными, но корректными, данными
    page = setup_teardown
    result = []
    page.eye_password_click()
    page.eye_password_confirm_click()
    for _ in range(10):
        page.clear_password()
        page.clear_password_confirm()
        text_pass = correct_password()
        text_pass_conf = correct_password()
        page.enter_password(text_pass)
        page.enter_password_confirm(text_pass_conf)
        page.driver.execute_script("arguments[0].blur();", page.password)
        page.driver.execute_script("arguments[0].blur();", page.password_confirm)
        try:
            page.driver.implicitly_wait(2)
            page.driver.find_element(*ErrorLocators.ERR_LABEL)
            result.append((text_pass, text_pass_conf, True))
        except NoSuchElementException:
            page.driver.save_screenshot(f"Screens/test_enter_password/{str(uuid.uuid4())}.png")
            result.append((text_pass, text_pass_conf, False))
    assert all(map(lambda x: x[2], result))


def test_press_submit_with_empty_fields(setup_teardown):
    page = setup_teardown
    page.button_click()
    try:
        page.driver.implicitly_wait(2)
        page.driver.find_element(*ErrorLocators.ERR_LABEL)
        assert True
    except NoSuchElementException:
        page.driver.save_screenshot(f"Screens/test_press_submit_with_empty_fields/{str(uuid.uuid4())}.png")
        assert False


@pytest.mark.usefixtures("enter_correct_data")
@pytest.mark.parametrize("phone", [False, True])
def test_button_swap_address(setup_teardown, params, phone):
    page = setup_teardown
    page.back_address_click()
    data = page.return_all_information()
    assert data == params


@pytest.mark.usefixtures("enter_correct_data")
@pytest.mark.parametrize("phone", [False])
def test_incorrect_confirm_code(setup_teardown, phone):
    page = setup_teardown
    page.enter_confirm_code(123456)
    try:
        page.driver.implicitly_wait(2)
        page.driver.find_element(*ErrorLocators.ERR_LABEL_CODE)
        assert True
    except NoSuchElementException:
        page.driver.save_screenshot(f"Screens/incorrect_confirm_code/{str(uuid.uuid4())}.png")
        assert False
    time.sleep(3)
