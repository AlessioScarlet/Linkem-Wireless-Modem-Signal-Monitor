# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:44:46 2021

@author: alessiosca
"""
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


novemin=0
while 0<1:
    
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\Users\\YOUR_PC_NAME\\Downloads\\geckodriver.exe")
    
    driver.set_window_position(-2000, 0)
    '''
    user="guest"
    pwd="linkem123"
    payload = {'user_name': 'guest',
              'user_passwd': 'linkem123'}
    ''' #540

    driver.get('https://192.168.1.1/login.asp')
    driver.find_element_by_id('user_name').send_keys('guest')
    driver.find_element_by_id('user_passwd').send_keys('linkem123')
    #time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[4]/div[1]/button').click()
    
    #pagina=driver.page_source
    #print(pagina)
    while novemin<540: #visto che ogni 10 minuti si disconnette, ho fatto in modo che ogni 9 minuti chiude e riapre il driver.
        time.sleep(5)
        novemin+=5
        try:
            segnale=driver.find_element_by_css_selector('.signal1')
            cont=1
        except:
            try:
                segnale=driver.find_element_by_css_selector('.signal2')
                cont=2
            except:
                try:
                    segnale=driver.find_element_by_css_selector('.signal3')
                    cont=3
                except:
                    try:
                        segnale=driver.find_element_by_css_selector('.signal4')
                        cont=4
                    except:
                        try:
                            segnale=driver.find_element_by_css_selector('.signal5')
                            cont=5
                        except:
                            cont=0
                            print('signal is dead')
        
        stringa=('Signal: '+ str(cont)+ '/5 ' + '--- '+ time.ctime() + '\n')
        with open('logs.txt', mode='a') as f:
            f.write(stringa)
        print('Segnale: ',cont,'/ 5')
    driver.close()
    novemin=0
#segnale2=driver.find_element_by_xpath('//*[@id="lte_signal"]')

#segnale.get_attribute('outerHTML')
#print(segnale.get_attribute('outerHTML'))
#print("HTML code of element: " + segnale.get_attribute('outerHTML'))


print('ok')
