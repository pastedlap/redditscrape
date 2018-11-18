from selenium import webdriver
import time
exe_path=r"/usr/local/bin/chromedriver"

def get_url():
    """
    get top 50 market cap coins url in reddit
    """
    urllst=[]
    prefix='https://www.reddit.com/r/'
    with open('coinlist.txt') as f:coinlst=f.readlines()
    coin_exclude=['Zcash', 'BitcoinGold','0x', 'Populous', 'Status']
    coinlst = [x for x in coinlst if x not in coin_exclude]
    for coin in coinlst:
        urllst.append(prefix + coin.split(':')[0].replace(" ", "") + '/')

    return urllst


#open the browser and visit the url
#driver = webdriver.Chrome('chromedriver.exe')
def url_test():
    urllst=get_url()
    driver=webdriver.Chrome(executable_path=exe_path)
    for url in urllst:
        driver.get(url)

def get_threadlinks(urllst):
    num_scrolls=10
    for url in urllst:
        coin=url.split('/')[-2]
        driver=webdriver.Chrome(executable_path=exe_path)
        driver.get(url)
        
        done=set()
        fw=open(r'./data/links/' + coin + '_threadLinks.txt','w')
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
        driver.quit()
if __name__ == "__main__":
    urllst=get_url()
    get_threadlinks(urllst)