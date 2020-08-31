from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\shantanu\\Desktop\\pic\\corona pandemic\\corona.ico",
        timeout=30
    )
def geturl(url):
    r=requests.get(url)
    return r.text
if __name__=="__main__":
    while True:
        #notifyme("swetant","jai rajputana")
        myhtmldata=geturl("https://covidindia.org/")
        soup = BeautifulSoup(myhtmldata, 'html.parser')
        #print(soup.prettify())
        a=[]
        for td in soup.find_all('tbody')[0].find_all('td'):
            a.append(td.get_text())
        datalist=[]
        for i in range(0,len(a),4):
            datalist.append(a[i:i+4])
        print("--- India Covid updates Statewise-2020---")
        states=input("Enter Your State name: ")
        #states=['Bihar','West Bengal']
        #print(datalist)
        for item in datalist:
            if item[0] in states:
                ntitle="Covid updates-2020"
                ntext=f"State : {item[0]}\nNo. of Cases : {item[1]}\nRecoveries : {item[2]}\nDeaths : {item[3]}"
                notifyme(ntitle,ntext)
                time.sleep(2)
        time.sleep(3600)


















