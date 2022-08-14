from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
import random
import string
import os
import subprocess
import sys

os.system(f'{sys.executable} -m pip install -r requirements.txt')
clear = lambda: os.system('cls')
clear()

UserAgent = UserAgent()
agente = UserAgent.random

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--headless")
options.add_argument(f'user-agent={agente}')
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
actions = ActionChains(driver)
username = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(10))
last_username = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(16))
final_password = password

clear()

def abre_web2():
    
    global driver
    url = "https://tempmail.dev/es/Gmail"
    clear()
    new_handle = driver.current_window_handle ,driver.execute_script("window.open('');") # open new tab
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    clear()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'current-mail')))

    for correo in driver.find_elements(By.ID, 'current-mail'):
        if driver.find_element(By.ID,'current-mail').text == "Loading":
            time.sleep(1)
        else:
            break
    gmailtor = driver.find_element(By.ID,'current-mail').text
    driver.switch_to.window(driver.window_handles[0])
    clear()
    return gmailtor

def rellena_formulario():
    while True:
        clear()
        driver.get("https://mega.nz/register")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="register-firstname-registerpage2"]')))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="register-firstname-registerpage2"]').send_keys(username)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="register-lastname-registerpage2"]').send_keys(last_username)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="register-email-registerpage2"]').send_keys(abre_web2())
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="register-password-registerpage2"]').send_keys(final_password)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="register-password-registerpage3"]').send_keys(final_password)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="register_form"]/div[8]/div[1]/input').click()
        driver.find_element(By.XPATH, '//*[@id="register-check-registerpage2"]').click()
        driver.find_element(By.XPATH, '//*[@id="register_form"]/button').click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'reg-resend-email-txt')))
        succes = driver.find_element(By.CLASS_NAME, 'reg-resend-email-txt').text
        if succes is not "":
            return False
        else:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            driver.delete_all_cookies()
            

def confirmar_registro():
    clear()
    driver.switch_to.window(driver.window_handles[1])
    for refresh in range(0,20):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inbox-dataList"]/a/div/div[1]/div[1]')))
            driver.find_element(By.XPATH, '//*[@id="inbox-dataList"]/a/div/div[1]/div[1]').click()
            break
        except:
            driver.refresh()
    
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="bottom-button"]').click()
    driver.switch_to.window(driver.window_handles[2])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-password2"]')))
    driver.find_element(By.XPATH, '//*[@id="login-password2"]').send_keys(final_password)
    driver.find_element(By.XPATH, '//*[@id="login_form"]/button').click()
    time.sleep(1)
    clear()
    return True

def guarda_usuario():
    clear()
    with open('usuarios.txt', 'a') as f:
        f.write('USERNAME: '+username + '\n')
        f.write('PASSWORD: '+final_password + '\n')
        f.write('EMAIL: '+abre_web2() + '\n')
        f.write('HORA DE REGISTRO: '+time.strftime("%H:%M:%S") + '\n')
        f.write('\n')
        f.write('****************************** DEV: ANDSSES ***************************' + '\n')
        f.write('\n')
        f.close()

for a in True, False:
    if rellena_formulario() == False:
        break

clear()

if confirmar_registro() == True:
    guarda_usuario()
    print('Usuario registrado con exito' + '\n')
    print('Dev: @Andsses')
    time.sleep(3)
    driver.quit()
else:
    driver.quit()



