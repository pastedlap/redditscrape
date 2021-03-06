from selenium import webdriver
import time,codecs,re
import glob
import os

exe_path=r"/usr/local/bin/chromedriver"

def parseComment(comment,fw):
    txt=comment.text.replace('\n', ' ').strip()
    if len(txt)==0:return
    M_del=re.search('level (\d+) Comment deleted (\d+) (.+?) ago',txt)
    if M_del is not None: return
    M_del=re.search('Continue this thread',txt)
    if M_del is not None: return
    M=re.search('level (\d+) (.+?) (.+?) points? .+?ago (.+) ',txt)
    level,user,points,text=M.group(1),M.group(2),M.group(3),M.group(4).strip().replace('\t',' ')
    if re.search('\(\d+$',text):text=''    
    fw.write('\t'.join([level,user,points,text])+'\n')
    
def expandComment(driver):
    num_elems=len(driver.find_elements_by_css_selector('p.s1tyd4zp-1'))
    for i in range(num_elems):
        try:
            elem=driver.find_element_by_css_selector('p.s1tyd4zp-1')
            driver.execute_script("arguments[0].click();", elem)
            time.sleep(1)
        except:
            print('load fail')

def get_comments(fl_name):
#driver = webdriver.Chrome('chromedriver.exe')
    coin=re.search('./data/links/(.+?)_threadLinks.txt',fl_name).group(1)
    if os.stat(r'./data/comments/'+ coin +'_comments.txt').st_size > 44533: return
    driver=webdriver.Chrome(executable_path=exe_path)
    fw=codecs.open(r'./data/comments/'+ coin +'_comments.txt','w',encoding='utf8')
    with open(fl_name) as f:links=f.readlines()
    for link in links:
        link=link.strip()
        driver.get(link)
        first=driver.find_elements_by_css_selector('div.s1knm1ot-9')[0].text
        first=re.sub('[\t\n]',' ',first)
        
        prevLen=driver.page_source
        
        consecutive_failures=0
        
        while consecutive_failures<3:
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            currLen=driver.page_source
            if currLen==prevLen:
                consecutive_failures+=1
            else:
                consecutive_failures=0
                prevLen=currLen
        
        fw.write('@@@THREAD@@@\t'+link+'\t'+first+'\n')
        expandComment(driver)
        comments=driver.find_elements_by_css_selector('div.s136il31-0')
        for comment in comments:
            try:
                parseComment(comment,fw)
            except:
                
                print('failed comment: %s' % (comment.text.replace('\n', ' ').strip()))
        
        fw.write('\n\n')
    fw.close()
    driver.quit()
def get_fl_names():
    fl_names=glob.glob("./data/links/*.txt")
#    fl_names=['./data/links/TRON_threadLinks.txt']
    for fl_name in fl_names:
        try:
            get_comments(fl_name)
        except:
            print(fl_name)
    
if __name__ == "__main__":
    get_fl_names()