from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/Users/ethanikegami/desktop/Sports Quiz Revival/article-writer/chromedriver", options=chrome_options)
url = "https://quillbot.com/login/"
driver.get(url)
time.sleep(3)


driver.find_element_by_xpath('//*[@class="MuiInputBase-input MuiFilledInput-input MuiInputBase-inputMarginDense MuiFilledInput-inputMarginDense jss110"]').send_keys("nextlvlig@gmail.com")
driver.find_element_by_xpath('//*[@type="password"]').send_keys("bball123")
driver.find_element_by_xpath('//*[@class="MuiButtonBase-root MuiButton-root MuiButton-contained auth-btn MuiButton-containedPrimary MuiButton-fullWidth"]').click()
 

time.sleep(2)
driver.refresh()
    
time.sleep(2)

while True:
    try:
        driver.find_element_by_xpath('//*[@class="MuiSlider-thumb jss128 jss146 MuiSlider-thumbColorPrimary"]').click()
        elem = driver.find_elements_by_xpath('//*[@class="MuiSlider-mark jss132"]')
        elem[1].click()
        break
    except:
        continue
    
time.sleep(2)

driver.find_element_by_xpath('//*[@class="MuiButtonBase-root MuiTab-root jss88 MuiTab-textColorPrimary jss103 jss102"]').click()

time.sleep(2)

driver.refresh()

time.sleep(1)

refresh = 1

def single_para_spin(paragraph):
    '''
    Takes in a string paragraph and retuns a spun string paragraph through Quillbot.
    '''
    global refresh
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="inputText"]').send_keys(paragraph)
            break
        except:
            continue
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="MuiGrid-root"]').click()

    time.sleep(5)

    while True:
        try:
            result = driver.find_elements_by_xpath('//*[@class="article-sentence"]')
            lis = []
            for i in result:
                lis.append(i.text)
            break
        except:
            continue
    if refresh == 2:
        driver.refresh()
        time.sleep(2)
    refresh += 1
    return " ".join(lis)

def delete_input():
    '''
    Deletes text in Quillbot field.
    '''
    global refresh
    while True:
        if refresh == 3:
            refresh += 1
            print("Error 1")
            break
        try:
            print("Error 2")
            driver.find_element_by_xpath('//*[@d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM8 9h8v10H8V9zm7.5-5l-1-1h-5l-1 1H5v2h14V4h-3.5z"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@class="MuiTouchRipple-root"]').click()
            break
        except:
            print("Error 3")
            continue

print(single_para_spin("This is a string I want to be spun. Please make it very high quality."))
delete_input()
print(single_para_spin("This is another string that 1should and could be spun!1"))
delete_input()
print(single_para_spin("This is another string that 2should and could be spun!2"))
delete_input()
print(single_para_spin("This is another string that 3should and could be spun!3"))
delete_input()
print(single_para_spin("This is another string that 4should and could be spun!4"))
delete_input()
