from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import choice
from phoneData import area_code, numbers

##--------------------------------------------##
# browser.minimize_window()
# option.binary_location = brave_path
# option.add_argument("--start-maximized") 

driver = "C:\\Users\\Stef\\.cache\\selenium\\chromedriver\\win32\\109.0.5414.74\\chromedriver.exe"
driver_path = "C:\\Users\\Stef\\.cache\\selenium\\chromedriver\\win32\\109.0.5414.74\\chromedriver.exe"
# brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

Options = webdriver.ChromeOptions()
# option.add_argument("--headless") 

Options.add_experimental_option("detach", True)
Options.add_argument("--incognito")

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=Options)


browser.get("https://www.homedepot.com/")

##--------------------------------------------##
enterCatchall = "userName1234" #fill this out before running script

usrEmail = f'{enterCatchall}@gmail.com'
userPass = 'Password1234'
sleep(1)

print ("Opened Home Depot...")
sleep(.25)

def phoneNumberGen():
    randomFill = ""
    areaCode = choice(area_code)
    randomFill = areaCode
    for number in range(1, 8):
        randomFill += choice(numbers)
    return randomFill

def navigateWebsite():
    myAccount = browser.find_element(By.ID, 'headerMyAccount').click()
    print ("Done...")
    sleep(.25)

    createAnAccount = browser.find_element(By.ID, 'SPSORegister').click()
    print ("Done...")
    sleep(.25)

def enterInformation():
    personalAccount = browser.find_element(By.CLASS_NAME, 'bttn__content').click()
    print ("Done...")
    sleep(.25)

    hdEmail = browser.find_element(By.ID, 'email')
    hdEmail.send_keys(usrEmail)
    print ("Email entered...")
    sleep(.25)

    hdPassword = browser.find_element(By.ID, 'password-input-field')
    hdPassword.send_keys(userPass)
    print ("Password entered...")
    sleep(.25)

    zipCode = browser.find_element(By.ID, 'zipCode')
    zipCode.send_keys('77014')
    print ("Zipcode entered...")
    sleep(.25)

    phoneNumber = browser.find_element(By.ID, 'phone')
    phoneNumber.send_keys(phoneNumberGen())
    print ("Phone number entered...")
    sleep(.25)

    WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@title='reCAPTCHA']")))
    sleep(2) 
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))).click()
    print('Checked captcha box')
    sleep(5)

    browser.maximize_window()

navigateWebsite()
enterInformation()
##--------------------------------------------##
# FUTURE
# https://2captcha.com/?from=3019071
# import catcha solver library + pay for service