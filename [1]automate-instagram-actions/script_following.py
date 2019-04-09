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

from configurate import Profile, Interact, alternate, alternate_ratio


def retract(browser):
    browser.execute_script('window.history.go(-1)')
    time.sleep(1)  

def following(browser, session):
    time.sleep(1)
    for convert_opn in alternate['following']:
        try:
            eval_follow = browser.find_element_by_xpath(convert_opn).text.strip()
            if 'follow' in eval_follow.lower():
                browser.find_element_by_xpath(convert_opn).click()
                time.sleep(2)
                return True

        except:
            pass
        
def valve(browser, session, element, profile):
    
    implicit_wait = WebDriverWait(browser, 15)
    convert = alternate['pulse'][0]
    navigate = implicit_wait.until(EC.presence_of_element_located((By.XPATH, convert)))
    browser.execute_script("arguments[0].scrollIntoView(true);", navigate)

    
    def cascade(browser, element):
        soup  = BeautifulSoup(browser.page_source, features="html.parser")
        spriteHeart = soup.find_all('span')

        for specify in [str(item.get('class')) for item in spriteHeart]:
            if 'glyphsSpriteHeart__filled__24__red_5' in specify:
                print(f'defined {element} :|:: pulse:heartfelt')
                return True     
        else:
            return False

    def comment(browser, navigate, element, session, profile):
        
        if element == 1 and profile%3 == 0: 
            navigate.click()

            browser.find_element_by_xpath(alternate['comment']['prime'][0]).click() 

            randint = np.random.randint(11)
            event = alternate['comment']['exchange'][randint]

            for value in range(len(alternate['comment']['path'])):
                convert = alternate['comment']['path'][value]
                try:
                    eval_comm = browser.find_element_by_xpath(convert)

                    if 'webelement' in str(eval_comm):

                        actions = ActionChains(browser)
                        actions.click(eval_comm)
                        actions.send_keys(event)

                        actions.send_keys(Keys.RETURN)
                        actions.perform()
                        print(f'-- defined {element} :|:: pulse:comment')
                        return True
                except:
                    pass 

        elif element == 1 or element == 2:
            navigate.click()
            print(f'-- defined {element} :|:: pulse')
            return True

    if cascade(browser, element):
        time.sleep(1)
        return False
    
    elif comment(browser, navigate, element, session, profile):
        time.sleep(1)
        return True
    
    
def interact(element, session, browser, profile):
    
    number = np.random.randint(1,4, size=1)[0]
    expression = Interact(element, number).define_interact()
    
    for eval_interact in expression['interact']:
        try:
            eval_domain = browser.find_element_by_xpath(eval_interact)
            browser.execute_script("arguments[0].scrollIntoView(true);", eval_domain)
            eval_domain.click() 
            
            if valve(browser, session, element, profile):
                time.sleep(2)
                retract(browser)
                break
                
            else:
                time.sleep(2)
                retract(browser)
                break
            
        except:
            pass


def internal_gates(browser, profile):
    
    def degree_n0():
        for convert_opn in alternate['following']:
            try:
                eval_following = browser.find_element_by_xpath(convert_opn).text.strip()
                if 'following' in eval_following.lower():
                    print('-- eval_n0  :following profile')
                    return True

            except:
                pass 
        else:
            print('-- eval_n0 :initiate')
            return False
            

    def degree_n1():
        for value in range(len(alternate['degree_n1'])):
            convert = str(alternate['degree_n1'][value])
            try:
                text_n1 = browser.find_element_by_xpath(convert).text.strip()
                if text_n1:
                    print(f'-- eval_n1 :private/else')
                    return True   

            except:
                pass
        else:
            print(f'-- eval_n1 :initiate')
            return False
            
            
            
    if degree_n0() or degree_n1():
        return False
    
    else:
        return True
            
        
def external_gates(browser, profile):
    
    def degree_n3():

        contain = [] 

        def defined_ratio(express):

            if ',' in str(express):

                localized_comma = int(express.replace(',',''))
                contain.append(localized_comma)

            elif 'k' or '.' in express:

                localized_period = express.replace('.','').replace('k','00')
                contain.append(localized_period)

            elif 'm' or '.' in express:

                localized_mil = express.replace('.','').replace('m','00000')
                contain.append(localized_mil)

        def alleviate(convert):
            try:
                for element in range(len(convert)):
                    refined = convert[element]
                    express = browser.find_element_by_xpath(refined).text.strip()
                    return express

            except:
                pass

        for element in range(len([alternate_ratio[item] for item in alternate_ratio])):
            convert = [alternate_ratio[item] for item in alternate_ratio][element]

            if alleviate(convert):
                defined_ratio(alleviate(convert))

        try:
            ratio = [int(ratio) for ratio in contain]

            post = ratio[0]
            followers = ratio[1]
            following = ratio[2]

            ratio = round(followers/following,2)

        except:
            post = 0
            
            followers = 0
            following = 0

            ratio = 0
            
        if post >= 25 and followers <= 100000 and following >= 125:
            if 0.1 <= ratio <= 100:
                print(f'-- eval_n3 :initiate :: post {post} ratio {ratio} followers {followers} following {following}')
                return True
            else:
                print(f'-- eval_n3 :ratio unmet :: ratio {ratio} followers {followers} following {following}')
        else:
            print(f'-- eval_n3 :aggregate :: post {post} followers {followers} following {following}')

    def degree_n4():
        
        def eval_language(convert):
            
            eval_des = browser.find_element_by_xpath(convert).text.strip()
            eval_language = detect(eval_des)

            print(f'-- eval_n4 :{eval_language}')
            
            if 'en' in eval_language:
                return True

        convert_n0 = alternate['degree_n4'][0]
        convert_n1 = alternate['degree_n4'][1]
        
        try:           
            eval_path = browser.find_element_by_xpath(convert_n0)
            browser.execute_script("arguments[0].scrollIntoView(true);",eval_path)

            if eval_language(convert_n0):
                return True

        except:
            try:           
                eval_path = browser.find_element_by_xpath(convert_n1)
                browser.execute_script("arguments[0].scrollIntoView(true);",eval_path)
                
                if eval_language(convert_n1):
                    return True
                
            except:
                print(f'-- eval_n4 :no-container')
            
    if degree_n3() and degree_n4():
        return True
    
    else:
        return False
    

def engine_(session, profile, browser):
    
    expression = Profile(profile).define_profile()
    for user_id in expression['profile']:

        try:
            eval_engine = browser.find_element_by_xpath(user_id)
            browser.execute_script("arguments[0].scrollIntoView(true);",eval_engine)
            username_collections = eval_engine.text.strip()
            set_time = time.strftime('%X %x %Z')

            print('')
            print(f'profile : {profile} : {set_time} ::: {username_collections}')
            eval_engine.click()

            eval_gate()
            break

        except:
            pass
    try:
        implicit_wait = WebDriverWait(browser, 15)
        implicit_wait.until(EC.presence_of_element_located((By.XPATH, alternate['internal_gates'][0])))

    except:
        print('-- internal gates not found')
        pass
    
    if internal_gates(browser, profile):
        if external_gates(browser, profile):

            [interact(element, session, browser, profile) for element in range(1,3)]

            browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            if following(browser, session):
                print(f'-- following profile {profile} ')
                return True  
        else:
            print('-- external gate initate-closed')
            return False
    else:
        print('-- internal gate initiate-closed')
        return False
    
def evaluate_0(session, session_start, session_end, browser):
    
    for profile in range(session_start, session_end):
        if engine_(session, profile, browser):
            time.sleep(1)
            retract(browser)

        else:
            time.sleep(1)
            retract(browser) 
    
    print('')
    print(f'----- {session} :: {session_start} - {session_end} ----- ')
    print('')

