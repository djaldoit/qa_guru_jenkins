import allure
from selene import browser, have


def test_dynamic_steps():
    with allure.step("Открываем страницу формы"):
        browser.open('automation-practice-form')

    with allure.step("Заполняем Имя, фамилию, email, номер телефона"):
        browser.element('#firstName').type('Piter')
        browser.element('#lastName').type('Parker')
        browser.element('#userEmail').type('spaidermane@gmail.com')
        browser.element('#userNumber').type('1234567890')

    with allure.step("Выбираем пол"):
        browser.all('.custom-control-label').element_by(
            have.exact_text('Male')).click()

    with allure.step("Выбираем предмет"):
        browser.element('#subjectsInput').type('English').press_enter()

    with allure.step("Выбираем хобби"):
        browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    with allure.step("Отправляем форму"):
        browser.element('#submit').press_enter()

    with allure.step("Проверяем результат"):
        browser.element('.table').should(have.text('Piter Parker'))
        browser.element('.table').should(have.text('spaidermane@gmail.com'))
        browser.element('.table').should(have.text('1234567890'))
        browser.element('.table').should(have.text('Male'))
        browser.element('.table').should(have.text('English'))
        browser.element('.table').should(have.text('Music'))
