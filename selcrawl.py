#/usr/bin/env python
from selenium import webdriver
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

from pyvirtualdisplay import Display  
display = Display(visible=0, size=(800, 600))  
display.start()  

browser  = webdriver.Firefox()

sys.argv =[None, 'https://www.youtube.com/watch?v=WFR3lOm_xhE']
#https://www.youtube.com/all_comments?v=WFR3lOm_xhE
link = sys.argv[1].replace('watch', 'all_comments')

browser.get(link)
time.sleep(10)
print(browser.title)

print(browser.page_source)
browser.close()
display.stop()
