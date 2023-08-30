В папке "Test" в файле "tests" приведены следующие автотесты. Для запуска автотестов достаточно нажать на зеленый треугольник слева от названия теста или запустить весь файл tests на выполнение, командная строка для этого не требуется.


test_auth_page_elements - Проверка наличия элементов на странице и их названий

test_enter_firstname_correct - Проверка ввода корректного имени

test_enter_lastname_correct - Проверка ввода корректной фамилии

test_enter_firstname_incorrect - Проверка ввода некорректного имени

test_enter_lastname_incorrect - Проверка ввода некорректной фамилии

test_dropdown - Тестирование работы выпадающего списка регионов

test_enter_address_correct_number - Тестирует поле "email или телефон" с корректным номером телефона

test_enter_address_incorrect_number - Проверка ввода некорректного номера телефона

test_enter_address_correct_email - Проверка ввода корректного email

test_enter_address_incorrect_email - Проверка ввода некорректного email

test_enter_password - Проверка ввода корректного пароля и подтверждения пароля

test_enter_password_incorrect - Проверка ввода некорректного пароля

test_enter_password_confirm_incorrect - Проверка ввода некорректного подтверждения пароля

test_enter_difference_password - Проверка реакции системы на введенные корректные, но разные, пароль и подтверждение пароля

test_press_submit_with_empty_fields - Проверка реакции системы на нажатие кнопки "Зарегистрироваться" при незаполненных полях

def test_button_swap_address - Проверка на то, что при нажатии на кнопку "Изменить телефон" / "Изменить email" все введенные данные на странице регистрации сохранятся

test_incorrect_confirm_code - Проверка обработки системой некорректно введенного кода проверки