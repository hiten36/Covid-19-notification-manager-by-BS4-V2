import requests
from bs4 import BeautifulSoup
from plyer import notification

def noti(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="/home/hiten/PycharmProjects/covid-19 notification manager/covid19 notification/icon.png",
        timeout=6
    )
def request(url):
    p=requests.get(url)
    return p.text
if __name__ == '__main__':
    url=request('https://www.mygov.in/corona-data/covid19-statewise-status/')
    soup=BeautifulSoup(url,'html.parser')
    states_list=[]
    l=soup.find_all('div',class_='field')
    for i in l:
        states_list.append(i.find_all('div',class_='field-item'))
        # print(i)
        # print(i.find_all('div',class_='field-item'))
    # print(states_list[16:])
    states_list1=[]
    for i in states_list[16:-8]:
        states_list1.append(i[0].get_text())
    # print(states_list1)
    states_list2=[]
    for i in states_list1:
        if 'http' not in i:
            states_list2.append(i)
    # print(states_list2)
    states_to_show=['rajasthan','delhi','mumbai','bihar']
    for index,states in enumerate(states_list2):
        if states.lower() in states_to_show:
            ntitle=states_list2[index]
            nmessage=f'Total confirmed: {states_list2[index+1]}\nTotal cured: {states_list2[index+2]}\nTotal death: {states_list2[index+3]}'
            noti(ntitle,nmessage)