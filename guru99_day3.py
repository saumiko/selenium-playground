import csv
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()


def get_user_pass_cases():
    cases = []
    with open('user_pass.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                case = {
                    'username': row[0],
                    'password': row[1],
                    'case': bool(int(row[2]))
                }
                cases.append(case)
                line_count += 1
    return cases


def nav_to_site():
    global driver
    driver.get('http://www.demo.guru99.com/V4/')


def login(user_id, pass_id):
    global driver
    username = driver.find_element_by_name('uid')
    password = driver.find_element_by_name('password')
    login_btn = driver.find_element_by_name('btnLogin')
    username.send_keys(user_id)
    password.send_keys(pass_id)
    login_btn.click()
    try:
        current_page = driver.current_url
        if current_page.endswith('manager/Managerhomepage.php'):
            return True
        else:
            alert = driver.switch_to.alert
            alert.accept()
            return False
    except selenium.common.exceptions.UnexpectedAlertPresentException:
        alert = driver.switch_to.alert
        alert.accept()
        return False


if __name__ == '__main__':
    for case in get_user_pass_cases():
        nav_to_site()
        if case['case'] == login(case['username'], case['password']):
            print(case, 'PASS')
        else:
            print(case, 'FAIL')
    driver.quit()