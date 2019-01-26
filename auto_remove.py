from time import sleep

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

c = ConfigParser()
c.read(".env")
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


def connections(con_filter: str):
    driver.get(con_filter)
    total_number = int(driver.find_element_by_class_name("search-results__total").text.split()[1])
    if total_number >= 1:
        try:
            result = driver.find_element_by_class_name("search-result__info")
            remove_con(result.find_element_by_tag_name('a').get_attribute('href'))
            sleep(1)
            connections(con_filter)
        except:
            connections(con_filter)
    else:
        return


def remove_con(url: str):
    driver.get(url)
    driver.find_element_by_css_selector('button[aria-label="More actions"]').click()
    driver.find_element_by_class_name('pv-s-profile-actions--disconnect').click()
    driver.find_element_by_class_name('pv-s-profile-actions--unfollow').click()


if __name__ == '__main__':
    login("https://www.linkedin.com")
    search_url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22in%3A0%22%5D&facetNetwork" \
                 "=%5B%22F%22%5D&origin=FACETED_SEARCH"
    connections(search_url)
