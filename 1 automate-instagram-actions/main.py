import time
import numpy as np

from script_following import evaluate_0
from script_unfollowing import evaluate_1

from selenium import webdriver
import chromedriver_binary

from _contain.authenticate import access
from configurate import alternate

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup

import time
import numpy as np
import chromedriver_binary

from selenium import webdriver
from _contain.authenticate import access
from configurate import alternate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def settings():
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-infobars')
    
    # option.add_argument('--headless')
    # option.add_argument('--remote-debugging-port=9222')

    # chrome_prefs = {}
    # option.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}
    # chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    
    driver = webdriver.Chrome(options = option)
    driver.set_window_size(750,525)
    return driver


def initialize(browser):
    implicit_wait = WebDriverWait(browser, 5)

    class Expressive:

        username = ''
        password = 0

        def __init__(self, variesProfile, variesKey):
            self.username = variesProfile
            self.password = variesKey

        def user_choice(self):
            
            soup = BeautifulSoup(browser.page_source, features="html.parser")
            identity = soup.find_all('input')

            access = {
                'instagram' : []
            }

            time.sleep(1)

            for element in identity:
                access['instagram'].append(element['id'])

            authenticate_profile = "'"+ access['instagram'][0] +"'"
            authenticate_gate = "'"+ access['instagram'][1] +"'"

            profile_path = (f'//*[@id={authenticate_profile}]')
            gate_path = (f'//*[@id={authenticate_gate}]')

            send_identity = implicit_wait.until(
                EC.presence_of_element_located((
                    By.XPATH, profile_path)))

            pass_auth = implicit_wait.until(
                EC.presence_of_element_located((
                    By.XPATH, gate_path)))

            send_identity.send_keys(self.username)
            time.sleep(1)
            print('authenticate-user')
            
            pass_auth.send_keys(self.password) 
            time.sleep(1)
            print('authenticate-password')
            
            return True
            
    def retract_profile():
        try:
            time.sleep(2)
            convert = alternate['retract']['notification'][1]
            implicit_wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, convert)
                )
            ).click()
            
        except:
            time.sleep(2)
            convert = alternate['retract']['notification'][0]
            implicit_wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, convert)
                )
            ).click()
            

        convert = alternate['retract']['user_entry'][0]
        implicit_wait.until(
            EC.presence_of_element_located((
                By.XPATH, convert)
            )
        ).click()

        convert = alternate['retract']['user_list'][0]
        implicit_wait.until(
            EC.presence_of_element_located((
                By.XPATH, convert)
            )
        ).click()

        return True
        
    character_profile = input('[0]profile-0 or [1]profile-1 or [2]profile-2 or [3]profile-3 : ')
    
    def inclined(character_profile):
        convert = access[character_profile]
        if Expressive(convert[0], convert[1]).user_choice():

            try:
                for eval_btn in alternate['prime_authenticate']:
                    try:
                        profile = browser.find_element_by_xpath(eval_btn)

                        time.sleep(1)
                        profile.click()
                        break

                    except:
                        pass  

                implicit_wait.until(EC.presence_of_element_located((By.XPATH, alternate['profile_wait'][0])))
                print(f'profile load: complete')

                if retract_profile():
                    print('initialize engine: load')

                else:
                    print('retract_profile condition undefined')
                    pass

            except:
                print('authenticate undefined')
                pass
    try:     
        inclined(int(character_profile))
        
    except:
        print('userprofile conditional error')
        browser.quit()

def connect(browser):
    base_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    connection_attempts = 0

    while connection_attempts <3:
        try:
            browser.get(base_url)
            
            WebDriverWait(browser,5).until(
                EC.presence_of_element_located((By.XPATH,alternate['instagram_logo'][0]))
            )
            return True

        except:
            connection_attempts += 1
            time.sleep(1)
            print(f'error connecting to {base_url}.')
            print(f'attempt #{connection_attempts}.')
            
    return False

def process(browser):
    if connect(browser):

        condition = 0
        initialize(browser)
        
        while condition == '0' or '1' or '2':
            condition = input('[0] following | [1] unfollowing :: return: ')

            if condition == '0' or '1':
                session_defined = 25
                session_start = 1
                session_end = 6

                for session in range(session_defined):
                    print('')
                    print(f'----- {session} :: {session_start} - {session_end} -----')
                    
                    if int(condition) == 0:
                        evaluate_0(session, session_start, session_end, browser)

                    elif int(condition) == 1:
                        evaluate_1(session_start, session_end, browser)

                    else:
                        pass

                    session_start = session_end
                    session_end = session_end + 5

                browser.refresh()
        else:
            print(f'END SESSION: condition {condition}')
                    
    else:
        print('initialize(browser) undefined')


if __name__ == '__main__':
    browser = settings()
    
    process(browser)
    reengage = input('REENGAGE BROWSER: (y/return) ')
    
    if reengage == 'y':
        browser = settings
        process(browser)

    else:
        browser.quit()
        print('DRIVER DISENGAGED')