from selenium.webdriver.common.by import By


class BaseLocator:
    REGISTRATION = (By.ID, "kc-register")


class RegLocators:
    REG_FIRSTNAME = (By.NAME, "firstName")
    REG_LASTNAME = (By.NAME, "lastName")
    REG_ADDRESS = (By.ID, "address")
    REG_PASSWORD = (By.ID, "password")
    REG_PASSWORD_CONF = (By.ID, "password-confirm")
    REG_LABELS = (By.CLASS_NAME, "rt-input__placeholder")
    REG_BUTTON = (By.NAME, "register")
    REG_DROPDOWN = (By.XPATH, "//*[@class='rt-select rt-select--search register-form__dropdown']")
    REG_OPTIONS = (By.CLASS_NAME, 'rt-select__list-item')
    LABELS = (By.XPATH, "//span[@class='rt-input__mask-start']")
    EYES = (By.XPATH, "//*[@class='rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye rt-input__eye']")


class ErrorLocators:
    ERR_LABEL = (By.XPATH, "//*[@class='rt-input-container__meta rt-input-container__meta--error']")
    ERR_LABEL_CODE = (By.ID, 'form-error-message')


class ConfirmLocators:
    BACK_ADDRESS = (By.NAME, 'otp_back_phone')
    CONFIRM_CODE = (By.ID, 'rt-code-0')
