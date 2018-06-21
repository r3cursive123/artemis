from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Requirements:
1. pip2 install selenium
2. download chrome driver and place in same directory as this script
    https://chromedriver.storage.googleapis.com/index.html?path=2.40/
    
Purpose: read a local file with ip:port listing and take screenshots - saves to local directory

"""
# Initialize chrome driver
chrome_driver = './chromedriver'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

# Loop through ip file and visit pages
with open('ips.txt','r') as f1:
    lines = f1.readlines()
    for i, line in enumerate(lines):
        port = line.strip().split(':'[0])
        port = port[1]
        if port == '443':
            line = 'https://' + line
            print line
        elif port == '80':
            line = 'http://' + line
            print line
        elif port == '808':
            line = 'http://' + line
            print line
        else:
            print ("""The following page could not be visited: %s\n(The port may not be added to this script yet)""") % (line)
        try:
            driver.get(line)
            out_file = (line.strip().replace(':','%3A').replace('/','%2F') + '.png')
            driver.get_screenshot_as_file(str(out_file))
        except:
            pass