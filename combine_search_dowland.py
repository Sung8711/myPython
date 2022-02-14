import requests
from bs4 import BeautifulSoup
import os
import time
import subprocess


mp3_path = "D:\\mp3place\\"
m4a_path = "D:\\m4aplace\\"

def search_DB(searchWord):
    m4a_file = m4a_path + searchWord + '.m4a'
    if os.path.isfile(m4a_file):
        print("Exist m4a file")
        return
    mp3_file = mp3_path + searchWord + '.mp3'
    if os.path.isfile(mp3_file):
        print("Exist mp3 file")
        print("Converting")
        convert_m4a(searchWord)
        print("Convert end")
        return
    print("No exist")
    print("Prepare to dowland")
    dowland_mp3(searchWord)
    print("Converting")
    convert_m4a(searchWord)
    print("Convert end")
        


def dowland_mp3(searchWord):
    url = "https://www.oxfordlearnersdictionaries.com/definition/american_english/"+s
    
    search_pro = {'q':str(searchWord)}

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    res = requests.get(url, headers=headers, params = search_pro,timeout=1000000)

    soup = BeautifulSoup(res.text,'html.parser')

    exs = soup.find('span',class_ = "pron-g")

    link = str(exs.find('div')['data-src-mp3']) # 拿連結
    
    name = str(searchWord) #檔案命名

    time.sleep(1)

    print("Start to dowland")

    a = requests.get(link,headers = headers)

    with open(mp3_path+'{}.mp3'.format(searchWord), 'wb') as ff:
        ff.write(a.content)

    time.sleep(1)
    
    print("Dowland end")


def convert_m4a(searchWord):
    str = 'ffmpeg -i "{}" -ab 320k "{}" -y'
    str_cmd = str.format(mp3_path + searchWord + '.mp3', m4a_path + searchWord + '.m4a')
    
    pp = subprocess.Popen(str_cmd, shell=True, stdout=subprocess.PIPE)

    for line in iter(pp.stdout.readline, b''):
        print(line.strip().decode('gbk'))


if __name__ == "__main__":
    word = input("請輸入要搜尋的單字:")
    search_DB(word)
