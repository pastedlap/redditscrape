from selenium import webdriver
import time

num_scrolls=10

url='https://www.reddit.com/r/btc/'

#open the browser and visit the url
#driver = webdriver.Chrome('chromedriver.exe')
driver=webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
driver.get(url)

done=set()
fw=open('threadLinks.txt','w')
for i in range(num_scrolls):

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    threads=driver.find_elements_by_css_selector('[data-click-id="comments"]')

    for thread in threads:
        link=thread.get_attribute('href')
        if link in done:continue
        done.add(link)
        fw.write(link+'\n')
    

fw.close()