from lib2to3.pytree import base
import time
from selenium.webdriver import chrome
from selenium.webdriver.common.by import by
from selenium.webdriver.support.select import select
from selenium .webdriver.chrome.services import service
from webdriver_manager.chrome import chromedrivemanager
dri = chrome(service=service(chromedrivemanager().install()) )
dri.get('http://www.manabadi.info/2022/AP-Intermediate-1st-year-regular-exam-results-May-2022.htm')
dri.maximize_window()
dri.implicity_wait(20)
num=2207111050
for i in range(0,150):
    path_f="/users/sohail.sd/pycharmprojects/pythonprojects/results/"
    dri.find_element(*(By.ID, 'htno')).clear()
    dri.find_element(*(By.ID, 'htno')).send_keys(str(num))
    dri.find_element(*(By.ID, 'btnsubmit')).click()
    file_nam = "{}{}.jpeg".format(path_f, num)
    print(file_nam)
    S = lambda X: dri.execute_script('return document.body.parentNode.scroll' + X)
    dri.set_window_size(S('Width'),
                        S('Height') + 300)  # May need manual adjustment
    dri.find_element_by_tag_name('body').screenshot(file_nam)
    num += 1

    time.sleep(3)