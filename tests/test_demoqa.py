import os

import allure
from selene import browser, have


def test_dynamic_steps():
    with allure.step("Открываем страницу формы"):
        browser.open('/automation-practice-form')

    with allure.step("Заполняем Имя, фамилию, email, номер телефона"):
        browser.element('#firstName').type('Piter')
        browser.element('#lastName').type('Parker')
        browser.element('#userEmail').type('spaidermane@gmail.com')
        browser.element('#userNumber').type('1234567890')

    with allure.step("Выбираем пол"):
        browser.all('.custom-control-label').element_by(
            have.exact_text('Male')).click()

    with allure.step("Скролим страницу"):
        browser.execute_script("window.scrollBy(0, 500);")

    with allure.step("Выбираем дату рождения"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('May')
        browser.element('.react-datepicker__year-select').type('1994')
        browser.element('.react-datepicker__day--025').click()

    with allure.step("Выбираем предмет"):
        browser.element('#subjectsInput').type('English').press_enter()

    with allure.step("Выбираем хобби"):
        browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    with allure.step("Загружаем картинку"):
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), 'pictures', 'testPicture.jpg')
            ))

    with allure.step("Заполняем адрес"):
        browser.element('#currentAddress').type('Street, 1')
        browser.element('#state').click().element('#react-select-3-option-1').click()
        browser.element('#city').click().element('#react-select-4-option-0').click()

    with allure.step("Отправляем форму"):
        browser.element('#submit').press_enter()

    with allure.step("Проверяем результат"):
        browser.element('.table').should(have.text('Piter Parker'))
        browser.element('.table').should(have.text('spaidermane@gmail.com'))
        browser.element('.table').should(have.text('1234567890'))
        browser.element('.table').should(have.text('Male'))
        browser.element('.table').should(have.text('25 May,1994'))
        browser.element('.table').should(have.text('English'))
        browser.element('.table').should(have.text('Music'))
        browser.element('.table').should(have.text('testPicture.jpg'))
        browser.element('.table').should(have.text('Street, 1'))
        browser.element('.table').should(have.text('Uttar Pradesh Agra'))


