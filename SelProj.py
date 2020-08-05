from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\akaverma\Downloads\Drivers\chromedriver.exe")

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = '"AishPS"'
string = "Hey!"
x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_2FVVk _2UL8j"]/div[@class="_3FRCZ copyable-text selectable-text"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(3):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)