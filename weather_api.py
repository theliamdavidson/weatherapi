from bs4 import BeautifulSoup
import requests
import datetime
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 
def weather():
    res = requests.get(
        f'https://www.google.com/search?q={"Redlands+weather"}&oq={"Redlands+weather"}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(info)
    print(weather+"°f")
    return([info, weather+"°f"])
 
def send_over_spi(package):
    print(package)
    

if __name__ == "__main__":
    t = datetime.datetime.today()
    future = datetime.datetime(t.year,t.month,t.day,6,45)
    if t.hour >= 7:
        future += datetime.timedelta(days=1)
        print((future-t).total_seconds())
        
    time.sleep((future-t).total_seconds())
    send_over_spi(weather())
