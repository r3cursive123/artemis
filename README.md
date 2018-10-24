# artemis

## Requirements:
1. pip2 install selenium
2. download chrome driver and place in same directory as this script
    https://chromedriver.storage.googleapis.com/index.html?path=2.40/
3. Make sure Google Chrome Web Browser is installed


## Purpose: 
Read a local file with ip:port listing and take screenshots - saves to local directory

## Description:
Reads from a text file named 'ips.txt' that includes ip:port - one per entry per line. Loops through each line and based on port number will assign http:// or https:// before making the request to the website. Uses selenium and chrome webdriver to make a .png screenshot of the webpage and saves it to the local directory.
