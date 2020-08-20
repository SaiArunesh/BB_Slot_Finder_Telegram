from selenium import webdriver
import chromedriver_autoinstaller
import sys
import time
import os

import telegram

bot = telegram.Bot(token = "INSERT_API_KEY_HERE")
chat_id = INSERT_CHAT_ID_HERE;

def get_bb_slot(url):
    chromedriver_autoinstaller.install() 
    
    driver = webdriver.Chrome()
    driver.get(url)
    print("Please login using OTP and then wait for a while.")
    time.sleep(60)


    while 1:
        driver.get(url)     
        time.sleep(2)
        print("Trying to find a slot!")
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()

            time.sleep(5) 
            try:
                driver.find_element_by_xpath("//button[@id = 'confirm']").click()
            except Exception:
                pass
            time.sleep(5)  
            src = driver.page_source
            #print(src)
            if "checkout" in driver.current_url and not "Unfortunately, we do not have" in src:
                time.sleep(15)
                src = driver.page_source
                if not "Unfortunately, we do not " in src:
                    for i in range(5):
                     
                        bot.sendMessage(chat_id = chat_id, text = "SLOTTTT!!!!!!")
                   
                     
        except Exception  as e:
            print("If this message pops up multiple times, please find the error and create a PR!")
            print (e)
            pass
        
        print("No Slots found. Will retry again.")
        
        #bot.sendMessage(chat_id = chat_id, text = "nope")

        time.sleep(50)

def main():
    get_bb_slot('https://www.bigbasket.com/basket/?ver=1')

if __name__ == '__main__':
    main()
