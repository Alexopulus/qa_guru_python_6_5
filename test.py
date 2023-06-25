from selene import browser, have, be
import pytest
def test_complete_todo():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('[id="new-todo"]').should(be.blank)

    browser.element('[id="new-todo"]').type('a').press_enter()
    browser.element('[id="new-todo"]').type('b').press_enter()
    browser.element('[id="new-todo"]').type('c').press_enter()
    browser.all('#todo-list>li').should(have.size(3))

@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768

def test_form_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')

#заполнение формы
    browser.element('[id="firstName"]').should(be.blank).type('Алексей')
    browser.element('[id="lastName"]').should(be.blank).type('Погодин')
    browser.element('[id="userEmail"]').should(be.blank).type('test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('89999999999')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__day--026').click()
    browser.element('[id="subjectsInput"]').should(be.blank).type('Test')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('ios_large_1550063059_image.jpg'))
    browser.element('[id="currentAddress"]').should(be.blank).type('улица Нижегородская, 125')
    browser.element('[id="state"]').click()
    browser.element('[id="state"]').set('NCR')
    browser.element('[id="state"]').set('Delhi')

    browser.element('[id="submit"]').click()


