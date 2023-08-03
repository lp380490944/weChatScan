"""
demo.py
The demo of WeReadScan.py
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
"""

import sys
sys.path.append('../WeReadScan')

from selenium.webdriver import Chrome, ChromeOptions

from WeReadScan import WeRead

# options
chrome_options = ChromeOptions()

# now you can choose headless or not
chrome_options.add_argument('--headless')  
 
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('log-level=3')

# launch Webdriver
print('Webdriver launching...')
driver = Chrome(options=chrome_options)
print('Webdriver launched.')

with WeRead(driver) as weread:
    weread.login() #? login for grab the whole book
    weread.scan2html('https://weread.qq.com/web/reader/a9532350813ab778bg015d69k16732dc0161679091c5aeb1')
