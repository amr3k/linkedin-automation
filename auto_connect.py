from time import sleep

import pyautogui
import webbrowser

pyautogui.PAUSE = 0.5

x = 870
y = 320

send_invitation_x = 900
send_invitation_y = 580
step = 123

difference_between_pages = 50

next_btn_x = 890
next_btn_y = 542
search_url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22eg%3A0%22%2C%22us%3A0%22%2C%22ae" \
             "%3A0%22%2C%22sa%3A0%22%5D&facetNetwork=%5B%22S%22%5D&origin=FACETED_SEARCH"
webbrowser.open_new(search_url)

for page in range(4):  # Uncomment these lines to make it do the job
    sleep(3)
    for i in range(5):
        pyautogui.moveTo(x, y + (step * i), 1)
        # pyautogui.click()
        # pyautogui.moveTo(send_invitation_x, send_invitation_y, 1)
        # pyautogui.click()
    pyautogui.press("pgup")
    pyautogui.press("pgdn")
    for i in range(5):
        pyautogui.moveTo(x, y - difference_between_pages + (step * i), 1)
        # pyautogui.click()
        # pyautogui.moveTo(send_invitation_x, send_invitation_y, 1)
        # pyautogui.click()
    pyautogui.press("pgdn")
    pyautogui.moveTo(next_btn_x, next_btn_y, 1)
    pyautogui.click()
