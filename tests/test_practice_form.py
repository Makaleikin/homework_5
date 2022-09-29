import os.path

from selene import have, be
from selene.support.shared import browser

from test_data.user_data import date_of_birth

def test_filling_registration_form():
    #GIVEN
    browser.open('/automation-practice-form')

    #WHEN
    browser.element('#firstName').type('Artem')
    browser.element('#lastName').type('Mlynskii')
    browser.element('#userEmail').type('mlynskii@gmail.com')
    browser.element('[id="gender-radio-1"][value="Male"]').double_click()
    browser.element('#userNumber').type('89003050250')
    browser.element('#dateOfBirthInput').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_data/qapicture.png'))
    browser.element('#subjectsInput').type('Math').press_enter()
    pick_month_of_birth.click().type(date_of_birth[1]).press_enter()
    pick_year_of_birth.click().type(date_of_birth[2]).press_enter()
    pick_day_of_birth.click()
    pick_hobbies_sport.click()
    pick_state.type('NCR').press_enter()
    pick_city.type('Gurgaon').press_enter()
    browser.element('#submit').press_enter()

    #THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Artem Mlynskii'))
    browser.element('.table-responsive').should(have.text('mlynskii@gmail.com'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('8900305025'))
    browser.element('.table-responsive').should(have.text('13 October,1999'))
    browser.element('.table-responsive').should(have.text('Maths'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('qapicture.png'))
    browser.element('.table-responsive').should(have.text('NCR Gurgaon'))


pick_month_of_birth = browser.element('.react-datepicker__month-select')
pick_year_of_birth = browser.element('.react-datepicker__year-select')
pick_day_of_birth = browser.element(f'.react-datepicker__day--0{date_of_birth[0]}')
pick_hobbies_sport = browser.element('[for="hobbies-checkbox-1"][class="custom-control-label"]')
pick_state = browser.element('#react-select-3-input')
pick_city = browser.element('#react-select-4-input')