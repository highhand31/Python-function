# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:23:10 2018

@author: Johnny
"""
from selenium import webdriver

'''
驅動程式來源
1.Firefox
https://github.com/mozilla/geckodriver/releases

2.Chrome
http://chromedriver.chromium.org/downloads
'''

'''Chrome的開啟方式

driverPath="D:\Python\webdriver\chromedriver.exe"

browser=webdriver.Chrome(executable_path=driverPath)

print(type(browser))

'''
def lottoResults(lotto_kind,num):
    
    if lotto_kind == "威力彩":
        
        driverPath="D:\Python\webdriver\geckodriver.exe"

        browser=webdriver.Firefox(executable_path=driverPath)
        
        #威力彩各期獎號
        url='http://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'
        
        browser.get(url) 
        
        #網路爬蟲要的關鍵詞
        select_name="SuperLotto638Control_history1_dlQuery_DrawTerm_"
        
        date_name="SuperLotto638Control_history1_dlQuery_Date_"
                
        eDate_name="SuperLotto638Control_history1_dlQuery_EDate_"
        
        sellAmount_name="SuperLotto638Control_history1_dlQuery_SellAmount_"
        
        total_name="SuperLotto638Control_history1_dlQuery_Total_"
        
        winner_name="SuperLotto638Control_history1_dlQuery_SL638_CategA3_"
        
        #第m期第n個數字 lottNum_Black_name+'n'+'_'+'m'
        lottNum_Black_name='SuperLotto638Control_history1_dlQuery_SNo'
        
        try:
           for i in range(num):
               
               lottDrawTerm=browser.find_element_by_id(select_name+str(i))
               
               lottoDate=browser.find_element_by_id(date_name+str(i))
               
               lottoEDate=browser.find_element_by_id(eDate_name+str(i))
               
               lottoSellAmount=browser.find_element_by_id(sellAmount_name+str(i))
               
               lottoTotal=browser.find_element_by_id(total_name+str(i))
               
               lottoWinner_1=browser.find_element_by_id(winner_name+str(i))
               
               print("=====================================")
               
               print(browser.title)
               
               #print(len(lottDrawTerm.text))
               
               print('第%s期號碼'%lottDrawTerm.text)
               
               print('開獎日期',lottoDate.text)
               
               print("兌獎期限",lottoEDate.text)
               
               print("銷售金額",lottoSellAmount.text)
                    
               print("獎金總額",lottoTotal.text)
               
               print("頭獎得獎人數",lottoWinner_1.text)
               
               print('第一區號碼為')
               
               for j in range(1,8):
                              
                   lottNum_Black=browser.find_element_by_id(lottNum_Black_name+str(j)+'_'+str(i))
                   
                   if j ==7:
                       print('第二區號碼為')
                   
                   print("開獎號碼",lottNum_Black.text)  
               
           browser.quit()#quit除了會關閉瀏覽器之後，也會釋放 client/server的連線
           
        except:
            print("沒有找到相符的元素，表示已經顯示完全部的開獎號碼")
        
    else:
        print("抱歉，沒有你要的樂透種類")


if __name__ == "__main__":
    
    lottoResults('威力彩',10)






