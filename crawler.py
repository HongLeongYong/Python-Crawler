from selenium import webdriver  #從library中引入webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://www.tcb-bank.com.tw/company-banking/deposit-exchange/common-services/foreign-exchange-rates")
time.sleep(1)
element = driver.find_element( by = By.ID , value = "select_spot_time")

drp = Select(element)
drp.select_by_visible_text('日間收盤')
print(len(drp.options))

all_options = drp.options
for option in all_options:
    print(option.text)
button = driver.find_element(by= By.LINK_TEXT , value = "開始查詢").click()
time.sleep(1)
time.sleep(10)
