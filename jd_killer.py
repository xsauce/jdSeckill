import os
import time
from datetime import datetime
from time import sleep
from selenium.webdriver import Chrome


def login(driver):
    driver.get("https://passport.jd.com/uc/login")
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
    driver.find_element_by_id("loginname").send_keys("13671549515")
    driver.find_element_by_id("nloginpwd").send_keys("Xsauce@0!2%")
    driver.find_element_by_id("loginsubmit").click()
    sleep(6)
    print('login success')


def buy(driver, url, buy_time=0.0):
    if time.time() < buy_time:
        return False
    driver.get(url)
    ele = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[14]/a[1]')
    # ele = driver.find_element_by_id("btn-reservation")
    print(ele.text)
    if 'btn-disable' not in ele.get_attribute("class"):
        print("buy enable")
        ele.click()
        return True
    else:
        return False


def main():
    with Chrome() as driver:
        login(driver)
        while True:
            if buy(driver, "https://item.jd.com/100011385146.html", buy_time=time.mktime(datetime.strptime("2020-02-16 20:00:00", "%Y-%m-%d %H:%M:%S").timetuple())):
                os.system('say "Buy Quickly, Buy Quickly"')
                break
            # if buy_hk(driver, "https://item.jd.com/100011385146.html"):
            #     break

        sleep(100)


if __name__ == '__main__':
    main()
