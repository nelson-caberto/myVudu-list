from splinter import Browser
from keys import email, password

import time

executable_path = {'executable_path':'chromedriver.exe'}
movies = []
with Browser('chrome', **executable_path, headless=True) as browser:
    browser.visit('https://www.vudu.com/content/MyLogin.html?type=sign_in')
    browser.fill('email',email)
    browser.fill('password',password)
    browser.find_by_text('Sign In')[1].click()
    time.sleep(3)
    browser.visit('https://www.vudu.com/content/movies/mymovies')
    time.sleep(3)
    count = int(browser.find_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]/div[1]/span[2]').text[2:-1])
    for x in range(29, count+29, 29):
        for movie in browser.find_by_xpath('//div[@class="contentPosterWrapper"]'):
            title = movie.find_by_tag('a')['href'].split('/')[-2].replace('-',' ')
            print(title)
            if title not in movies:
                movies.append(title)
        browser.visit(f'https://www.vudu.com/content/movies/mymovies?minVisible={x}')
    with open('movies.txt','w') as file:
        for title in movies:
            file.write(title+'\n')
    
