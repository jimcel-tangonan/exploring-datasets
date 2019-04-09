import time
import numpy as np

from selenium import webdriver
import chromedriver_binary

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
from langdetect import detect

from configurate import Profile, Interact, alternate

def cascade(browser):
    try:
        implicit_wait = WebDriverWait(browser, 5)
        
        convert = alternate['pulse'][0]
        navigate = implicit_wait.until(EC.presence_of_element_located((By.XPATH, convert)))
        browser.execute_script("arguments[0].scrollIntoView(true);", navigate)
        return True

    except:
        return False
    
def retract(browser):
    time.sleep(2)
    browser.execute_script('window.history.go(-1)')

def interact(element, profile, browser):
    number = np.random.randint(1,4, size=1)[0]
    expression = Interact(element, number).define_interact()
    
    for eval_interact in expression['interact']:
        try:
            eval_domain = browser.find_element_by_xpath(eval_interact)
            browser.execute_script("arguments[0].scrollIntoView(true);", eval_domain)

            time.sleep(1)
            eval_domain.click() 
            time.sleep(2)
            if cascade(browser):
                print(f':|:: pulse')

                retract(browser)
                return True
                
            else:
                return False
    
        except:
            pass
        
def movement(browser):
    time.sleep(2)
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)
    return True
      
def unfollowing(browser):
    for convert_opn in alternate['following']:
        try:
            eval_follow = browser.find_element_by_xpath(convert_opn).text.strip()
            if 'follow' in eval_follow.lower():
                browser.find_element_by_xpath(convert_opn).click()
                break
        except:
            pass 

    time.sleep(1)
    for confirm in alternate['unfollowing']:
        try:
            browser.find_element_by_xpath(confirm).click()
            time.sleep(2)
            return True

        except:
            pass        
    
def defined_engine(profile, browser):
    implicit_wait = WebDriverWait(browser, 15)
    
    eval_post = implicit_wait.until(EC.presence_of_element_located((By.XPATH, alternate['internal_gates'][0])))
    browser.execute_script("arguments[0].scrollIntoView(true);",eval_post)

    time.sleep(1)
    if [interact(element, profile, browser) for element in range(1,8)]:
        if movement(browser):
            unfollowing(browser)
            return True

    else:
        print(f':|:: pulse undefined')
        return True
        
def evaluate_1(session_start, session_end, browser):
    for profile in range(session_start, session_end):
        
        expression = Profile(profile).define_profile()
        
        for user_id in expression['profile']:
            try:
                eval_engine = browser.find_element_by_xpath(user_id)

                browser.execute_script("arguments[0].scrollIntoView(true);",eval_engine)
                time.sleep(2)

                username_collections = eval_engine.text.strip()
                set_time = time.strftime('%X %x %Z')

                print(f'execute profile {profile} : {set_time} ::: {username_collections}')

                eval_engine.click()
                if defined_engine(profile, browser):

                    retract(browser)
                    print('session done')
                    break

                else:
                    if movement(browser):
                       
                        unfollowing(browser)

                        retract(browser)
                        print('container found undefined')
                        break
 
            except:
                pass
            
        print(f'DEFINED: {profile}')