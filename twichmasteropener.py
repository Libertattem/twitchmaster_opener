import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from threading import Thread
import random
import pandas as pd
import math
import datetime



ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
#Открываетсья "Промо"-----------------------------------------------------
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

driver.get('https://stream-booster.ru/dashboard/watch');

driver.execute_script("window.open('https://twitchmaster.ru/')")
driver.switch_to.window(driver.window_handles[-1])

findclass = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".ajax-popup")))
findclass.click()

driver.execute_script("window.open('https://www.twitch.tv')")
driver.switch_to.window(driver.window_handles[-1])

findclass = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".ScCoreButtonLabel-sc-lh1yxp-0")))
findclass.click()

print('Пройдите авторизацию на предложенных сайтах!')
print('Важно! Не закрывайте открытые вкладки, и не открывайте новые.')
print('После авторизации, введите команду: "start"')
start=input()
if start=='start':
    
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://twitchmaster.ru/static/profile');
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://stream-booster.ru/dashboard/watch');

    while True:
        now = datetime.datetime.now()
        if now.minute<55:
            
            continuebutton=False
            driver.switch_to.window(driver.window_handles[1])
            driver.refresh()
            #Открваеться промо страница и ее твич-----------------------------------------------------
            actions = ActionChains(driver)
            findclass = WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".left [href]")))
            actions.key_down(Keys.CONTROL).click(findclass).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            url = driver.current_url
            print('Промо страница: %s' % url)
            
            #Открываеться "Поднаятие"-----------------------------------------------------
            driver.switch_to.window(driver.window_handles[1])
            actions = ActionChains(driver)
            findclass = WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.LINK_TEXT, "Поднятие")))
            actions.key_down(Keys.CONTROL).click(findclass).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            
            #Открываеться первые поднятое видео-----------------------------------------------------
            actions = ActionChains(driver)
            findclass = WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".status [href]")))
            actions.key_down(Keys.CONTROL).click(findclass).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            url = driver.current_url
            print('Первое поднятое видео: %s' % url)
            
            while continuebutton==False and now.minute<54:
                driver.switch_to.window(driver.window_handles[0])
                driver.refresh()

                try:
                    findclass = WebDriverWait(driver, 3,ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".g-recaptcha.cool-button.youtube-button")))
                    findclass.click()
                    continuebutton=True
                except TimeoutException:
                    print('Ошибка: TimeoutException')
                    continuebutton=False
                except ElementNotInteractableException:
                    print('Ошибка: ElementNotInteractableException')
                    continuebutton=False
                except StaleElementReferenceException:
                    print('Ошибка: StaleElementReferenceException')
                    continuebutton=False
                else:
                    continuebutton=True              
                print('Кнопка продолжить просмотр: %s' % continuebutton)

                timesleep=120
                if now.minute*60+now.second+timesleep<55*60:
                    print('Жду появления кнопки(секунд): %s' % timesleep)
                    time.sleep(timesleep)
                else:
                    timesleep=54*60-now.minute*60-now.second+1
                    print('Конец часа! Ожидание перезапуска (секунд): %s' % timesleep)
                    time.sleep(timesleep)
                now = datetime.datetime.now()
            else:                
                now = datetime.datetime.now()
                timesleepview = (55 - now.minute)
                timesleep = (55 - now.minute)*60
                print ('Время сна (минут) : %s' % timesleepview)
                time.sleep(timesleep)

            
            print('Конец часа. Закрытие временных вкладок!')
            for x in range(5):
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
        else:
            time.sleep(60)

                

