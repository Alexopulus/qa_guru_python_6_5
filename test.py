from selene import browser, have, be
import pytest
import os

@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1068

def test_form_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')

#заполнение формы
    browser.element('[id="firstName"]').should(be.blank).type('Алексей')
    browser.element('[id="lastName"]').should(be.blank).type('Погодин')
    browser.element('[id="userEmail"]').should(be.blank).type('test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('89040527687')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1989"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__day--024').click()
    browser.element('[id="subjectsInput"]').should(be.blank).type('Test')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('images/ios_large_1550063059_image.jpg'))
    browser.element('[id="currentAddress"]').should(be.blank).type('улица Нижегородская, 125')
    browser.element('[id="state"]').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    browser.element('[id="submit"]').click()


#проверяем форму
    browser.element('.table-responsive').should(have.text('Алексей Погодин'))
    browser.element('.table-responsive').should(have.text('test@test.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('24 December,1989'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('ios_large_1550063059_image.jpg'))
    browser.element('.table-responsive').should(have.text('улица Нижегородская, 125'))
    browser.element('.table-responsive').should(have.text('NCR Delhi'))

    browser.element('[id="closeLargeModal"]').click()
