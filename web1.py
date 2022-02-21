# first real project!!!
# goes to microcenter website, checks stock of GPUs, stores the dataframe in an excel file, and pushes the related notifications to my phone

from pushsafer import init, Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import openpyxl

path = 'C:\\bin\\chromedriver.exe'
driver = webdriver.Chrome(path)
url1 = 'https://www.microcenter.com/category/4294966937/video-cards'
driver.get(url1)


def getem():
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((
            By.CLASS_NAME,
            'detail_wrapper')))
    except Exception as e:
        print(e)
        print("error")
        driver.quit()

# list to be saved as a dataframe - df1
pageInfo = []
cards = driver.find_elements(By.CLASS_NAME, 'detail_wrapper')

for card in cards:
    # print(card.text)
    element = card.find_element_by_css_selector('a')
    link = element.get_attribute('href')
    brand = element.get_attribute('data-brand')
    name = element.get_attribute('data-name')
    price = element.get_attribute('data-price')
    stock = card.find_element_by_class_name('stock').text
    checkDate = time.ctime()
    pageInfo.append({
        'brand' : brand,
        'name' : name,
        'price' : price,
        'stock' : stock,
        'time' : checkDate,
    })

# plugs list into dataframe and searches for 'names' containing 3080
# 1 = GPU dataframe
time.sleep(2)
df1 = pd.DataFrame(pageInfo)
gpu6 = df1.name.str.contains('3090')
gpu1 = df1.name.str.contains('3080')
gpu2 = df1.name.str.contains('3070')
gpu3 = df1.name.str.contains('3060')
gpu4 = df1.name.str.contains('5700')
gpu5 = df1.name.str.contains('5600')
gpu7 = df1.name.str.contains('6900')
gpu8 = df1.name.str.contains('6800')
# gpu9 = df1.name.str.contains('6700')
GPUset1 = df1[gpu1]
GPUset2 = df1[gpu2]
GPUset3 = df1[gpu3]
GPUset4 = df1[gpu4]
GPUset5 = df1[gpu5]
GPUset6 = df1[gpu6]
GPUset7 = df1[gpu7]
GPUset8 = df1[gpu8]
# GPUset9 = df1[gpu9]


def printCards():
    print(" ")
    print("The time is: ", time.ctime())
    print(" ")
    if not GPUset1.empty:
        print("ATTENTION")
        print("ATTENTION")
        print("ATTENTION")
        print("ATTENTION")
        print("The following 3080s are in stock:")
        print(GPUset1)
        print(" ")
    else:
        print("There are no 3080s in stock.")
        print(" ")
    if not GPUset2.empty:
        print("The following 3070s are in stock:")
        print(GPUset2)
        print(" ")
    else:
        print("There are no 3070s in stock.")
        print(" ")
    if not GPUset3.empty:
        print("The following 3060s are in stock:")
        print(GPUset3)
        print(" ")
    else:
        print("There are no 3060s in stock.")
        print(" ")
    if not GPUset4.empty:
        print("The following 5700s are in stock:")
        print(GPUset4)
        print(" ")
    else:
        print("There are no 5700s in stock.")
        print(" ")
    if not GPUset5.empty:
        print("The following 5600s are in stock:")
        print(GPUset5)
        print(" ")
    else:
        print("There are no 5600s in stock.")
        print(" ")

    if not GPUset7.empty:
        print("The following 6900s are in stock:")
        print(GPUset7)
        print(" ")
    else:
        print("There are no 6900s in stock")
        print(" ")


    if not GPUset8.empty:
        print("The following 6800s are in stock:")
        print(GPUset8)
        print(" ")
    else:
        print("There are no 6800s in stock")
        print(" ")

    # if not GPUset9.empty:
    #     print("The following 6600s are in stock:")
    #     print(GPUset9)
    #     print(" ")
    # else:
    #     print("There are no 3090s in stock")

    if not GPUset6.empty:
        print("The following 3090s are in stock:")
        print(GPUset6)
        print(" ")
    else:
        print("There are no 3090s in stock")
    print(" ")
    print("The time is: ", time.ctime())
    print(" ")

def excellent():
    filename = "c:\\Users\\dkrol\\Desktop\\CODING\\videocards.xlsx"
    # df1.to_excel(filename)
    with pd.ExcelWriter(filename,
        mode='a') as writer:
        df1.to_excel(writer, sheet_name='1')

def alertMeGPU():
    init("pwPCHclouvKPB2llqtEV")
    if not GPUset1.empty and not GPUset2.empty and not GPUset3.empty:
        Client("").send_message("They're all here!", "3080/3070/3060", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("all 3 30 series cards in stock")
        print("3080/3070/3060 push notification")
    elif not GPUset1.empty and not GPUset2.empty:
        Client("").send_message("2/3", "3080/3070", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("no 3060s")
        print("3080/3070 push notification")
    elif not GPUset1.empty and not GPUset3.empty:
        Client("").send_message("2/3", "3080/3060", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("no 3070s")
        print("3080/3060 push notification")
    elif not GPUset2.empty and not GPUset3.empty:
        print("no 3080s")
        print("3070/3060 push notification")
    elif not GPUset1.empty:
        Client("").send_message("Bingo", "3080", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("only 3080s")
        print("3080 push notification")
    elif not GPUset2.empty:
        # Client("").send_message("Meh", "3070", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("only 3070s")
        print("3070 push notification")
    elif not GPUset3.empty:
        # Client("").send_message("Aww", "3060", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("only 3060s")
        print("3060 push notification")
    else:
        # Client("").send_message(":(", "Better luck next time", "a", "1", "4", "2", "", "Open Microcenter", "0", "2", "60", "600", "1", "", "", "")
        print("There are no 30 series cards in stock")

printCards()
excellent()
# alertMeGPU()

driver.quit()

# fileName = 'videocards' + ' ' + str(time.time()) + ' ' + '.csv'
# df1.to_csv(fileName)

# url2 = 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002'
# driver.get(url2)
#
# bbcards = driver.find_elements(By.CLASS_NAME, 'sku-item')
#
# for bbcard in bbcards:
#     # print(bbcard.text)
#     price = driver.find_element_by_class_name('priceView-hero-price').text
#     # print(price)
#     name = driver.find_element_by_class_name('sku-title').text
# print(price)
# print(name)
