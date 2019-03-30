# artemis

## Requirements/Steps:
1. pip2 install selenium
2. Make sure Google Chrome Web Browser is installed
3. git clone https://github.com/r3cursive123/artemis.git
4. cd artemis
5. chmod +x chromedriver
6. Good to go


## Purpose: 
Read a local file with ip:port listing and take screenshots - saves to local directory

## Description:
Reads from a text file named 'ips.txt' that includes ip:port - one per entry per line. Loops through each line and based on port number will assign http:// or https:// before making the request to the website. Uses selenium and chrome webdriver to make a .png screenshot of the webpage and saves it to the local directory.
