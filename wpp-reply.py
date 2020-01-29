from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    r'C:/Users/mathe/Documents/OneDrive/Documents/Python/wpp-auto-reply/chromedriver_win32/chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

target = 'Michael Vinicius'

string = "Salve família. Mandado pelo meu programa de python maluco."

x_arg = '//span[@title = "{}"]'.format(target)
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()


inp_xpath = driver.find_element_by_class_name('_13mgZ')
for i in range(1):
    inp_xpath.send_keys(string)
    # The classname of send button may vary.
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
