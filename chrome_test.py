from selenium import webdriver
from pyvirtualdisplay import Display
display = Display(visible=0,size=(800,600))
display.start()

service_log_path = 'chromedriver.log'
service_args = ['--verbose', '--no-sandbox']
driver = webdriver.Chrome('/usr/bin/chromedriver', service_args=service_args,
service_log_path=service_log_path)
driver.get('http://www.google.com/xhtml')
driver.quit()
display.stop()  