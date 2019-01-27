from time import sleep

from configparser import ConfigParser
from os.path import dirname
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

c = ConfigParser()
c.read(dirname(__file__) + "/.env")
email = c.get("SECRETS", "email")
passwd = c.get("SECRETS", "password")
opt = Options()
opt.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/71.0.3578.98 Safari/537.36")  # Changing user agent
driver = webdriver.Chrome(options=opt)


def login(url: str):
    driver.get(url)
    login_email_input = driver.find_element_by_id("login-email")
    login_password_input = driver.find_element_by_id("login-password")
    login_submit_btn = driver.find_element_by_id("login-submit")
    login_email_input.send_keys(email)
    login_password_input.send_keys(passwd)
    login_submit_btn.click()


def connections(con_filter: str, invitations_sent=0):
    driver.get(con_filter)
    if invitations_sent < 50:
        current_view = 760
        driver.execute_script("window.scrollBy(0,250);")
        container = driver.find_element_by_class_name('blended-srp-results-js')
        buttons = container.find_elements_by_class_name('search-result__actions--primary')
        for button in buttons:
            if button.get_attribute('disabled'):
                continue
            driver.execute_script("window.scrollBy(0,500);")
            button.click()
            sleep(2)
            driver.find_element_by_class_name('button-primary-large').click()
            invitations_sent += 1
            sleep(1)
        driver.find_element_by_class_name('next').click()
        connections(con_filter, invitations_sent)


if __name__ == '__main__':
    login("https://www.linkedin.com")
    search_url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22eg%3A0%22%2C%22ae%3A0%22%5D" \
                 "&facetNetwork=%5B%22S%22%5D&origin=FACETED_SEARCH"
    connections(search_url)
    pass
