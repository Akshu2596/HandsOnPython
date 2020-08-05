from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text = '******'
no_of_message = 1
mobile_no_list = [919412647618, 918290101806, 917060356919]


def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:

        socket.create_connection(("www.google.com", 80))
        print("Connected to server - host reachable")
        return True
    except:
        is_connected()


driver = webdriver.Chrome(executable_path=r"C:\Users\akaverma\Downloads\Drivers\chromedriver.exe")
driver.get("http://web.whatsapp.com")
print("Connected!")
sleep(10)


def send_whatsapp_msg(phone_no, text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to.alert()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
        txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invalid phone no :" + str(phone_no))


for mobile_no in mobile_no_list:
    try:
        send_whatsapp_msg(mobile_no, message_text)

    except Exception as e:
        sleep(10)
        is_connected()
