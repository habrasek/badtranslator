from bs4 import BeautifulSoup
import requests
import json
import csv

import time
import datetime
 
# Create class that acts as a countdown
def countdown(s):
 
    # Calculate the total number of seconds
    total_seconds = s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")
    
# s = input("Enter the time in seconds: ")
# countdown(int(s))

enter = input('Type in a word or sentence: ')

url_input = enter.replace(' ', '%20')

url =  f'https://translate.yandex.com/?lang=en-zh&text={url_input}'

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

browser.visit(url)

countdown(20)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

quotes = soup.find_all('span', class_='translation-word translation-chunk')

characters = str(quotes[0].text)

sentence = []

for x in characters:
#     url = f'https://translate.yandex.com/?lang=zh-en&text={x}'
    url = f'https://translate.google.com/?sl=zh-CN&tl=en&text={x}&op=translate'
    browser.visit(url)
    
    countdown(3)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.find_all('span', class_='Q4iAWc')
    
    characters = str(quotes[0].text)
    
#     print(characters)
    
    sentence.append(characters)
    
