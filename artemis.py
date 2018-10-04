from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
"""
Requirements:
1. pip2 install selenium
2. download chrome driver and place in same directory as this script
    https://chromedriver.storage.googleapis.com/index.html?path=2.40/
    
Purpose: read a local file with ip:port listing and take screenshots - saves to local directory

"""
# Initialize chrome driver
chrome_driver = './chromedriver'
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--no-sandbox")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-errors")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True
capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capabilities, executable_path=chrome_driver)
proto = ""

# Loop through ip file and visit pages
with open('ips.txt','r') as f1:
    lines = f1.readlines()
    for i, line in enumerate(lines):
        port = line.strip().split(':'[0])
        port = port[1]
        if port == '443':
            proto = 'https://'
            line =  proto + line
        elif port == '80':
            proto = 'http://'
            line = proto + line
        elif port == '8080':
            proto = 'http://'
            line = proto + line
        elif port == '8443':
            proto = 'https://'
            line = proto + line
        try:
            driver.get(line)
            out_file = (line.strip().replace(':','%3A').replace('/','%2F') + '.png')
            driver.get_screenshot_as_file(str(out_file))
            print "Screenshot of " + line + " created successfully!"
        except Exception as e:
            print "We got a problem..."
            print (
                  """The following page could not be visited: %s\n(The port may not be added to this script yet)""") % (line)
            print e
