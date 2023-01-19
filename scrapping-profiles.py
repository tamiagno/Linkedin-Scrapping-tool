# -*- coding: utf-8 -*-


import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
from IPython.display import display, HTML

"""download do csv com links"""

path = 'YOURFILE.csv'             
employeeslink = []                   

with open(path, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: 
        for item in row:        
            employeeslink.append(item) 

"""criando o dataframe"""

dict = {"Link":[],
        "Nome":[],
        "Trabalho":[],
        "Localizacao":[],
        "Experiencia": [],
        "Competencias": [],
        "Certificados": []
       }
  
df = pd.DataFrame(dict)
  
  




"""
logando 
"""

opts=Options()

driver = webdriver.Chrome(executable_path=r'C:\\Users\\Default\\Desktop\\chromedriver.exe')

def validate_field(field):
    
    if field:
        pass
    else:
        field="No Results"
    return field

driver.get('https://www.linkedin.com')

username=driver.find_element(By.ID,'session_key')

username.send_keys('YOUR-EMAIL')

sleep(0.5)

password=driver.find_element(By.ID,'session_password')

password.send_keys('YOUR-PASSWORD')

sleep(0.5)

sign_in_button= driver.find_element(By.XPATH,'//*[@type="submit"]')

sign_in_button.click()
sleep(15)





profile1={}

""" pessoal """

def pessoal(profile):
    link = f'https://www.linkedin.com/in/{profile}/'
    driver.get(link)
    sleep(5)
    SCROLL_PAUSE_TIME = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(3):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    name_div = soup.find('div', {'class': 'ph5'})

    profile1["Nome"] = name_div.find('h1').get_text().strip()
    #print(name)

    profile1["Trabalho"] = name_div.find(
        'div', {"class": "text-body-medium break-words"}).get_text().strip()
    #print(work)

    profile1["Localizacao"] = name_div.find(
        'span', {"class": "text-body-small inline t-black--light break-words"}).get_text().strip()
        #print(location)

    return 


"""experiência"""

def experiencia(profile):
    link_ex = f'https://www.linkedin.com/in/{profile}/details/experience/'
    driver.get(link_ex)
    sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    exp_div = soup.find('section', {'class': "artdeco-card ember-view pb3"})
    text = []
    try:
        exp_section = exp_div.find_all("ul")
        x = exp_section[0].find_all(
            'li', {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        for i in range(len(x)):
            try:
                y = ((x[i].find('span', {'aria-hidden': "true"}).get_text().strip()),
                     (x[i].find('span', {'class': "t-14 t-normal"}).find('span',
                                                                         {'aria-hidden': "true"}).get_text().strip()),
                     (x[i].find('span', {'class': "t-14 t-normal t-black--light"}).find('span', {'aria-hidden': "true"}).get_text().strip()))
                text.append(y)
            except:
                    try:
                        y = ((x[i].find('span', {'aria-hidden': "true"}).get_text().strip()),
                             (x[i].find('span', {'class': "t-14 t-normal"}).find('span', {'aria-hidden': "true"}).get_text().strip()))
                        text.append(y)
                    except:
                            try:
                                y = ((x[i].find('span', {'aria-hidden': "true"}).get_text().strip()),
                                     (x[i].find('span', {'class': "t-14 t-normal t-black--light"}).find('span', {'aria-hidden': "true"}).get_text().strip()))
                                text.append(y)
                            except:
                                    y = (
                                        (x[i].find('span', {'aria-hidden': "true"}).get_text().strip()))
                                    text.append(y)

    except:
        text = "NA"
        text

    profile1["Experiencia"] = text
    return

"""certificados"""

def certificados(profile):
    link_cert = f'https://www.linkedin.com/in/{profile}/details/certifications/'
    driver.get(link_cert)
    sleep(5)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cert_div = soup.find('section', {'class': "artdeco-card ember-view pb3"})
    text1 = []
    try:
        cert_section = cert_div.find_all("ul")
        x1 = cert_section[0].find_all(
            'li', {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        for i in range(len(x1)):
            try:
                y1 = ((x1[i].find('span', {'aria-hidden': "true"}).get_text().strip()),
                      (x1[i].find('span', {'class': "t-14 t-normal"}).find(
                          'span', {'aria-hidden': "true"}).get_text().strip()),
                      (x1[i].find('span', {'class': "t-14 t-normal t-black--light"}).find('span', {'aria-hidden': "true"}).get_text().strip()))
                text1.append(y1)
            except:
                try:
                    y1 = ((x1[i].find('span', {'aria-hidden': "true"}).get_text().strip()),
                          (x1[i].find('span', {'class': "t-14 t-normal"}).find('span', {'aria-hidden': "true"}).get_text().strip()))
                    text1.append(y1)
                except:
                    try:
                        y1 = ((x1[i].find('span', {'aria-hidden': "true"}).get_text().strip()),
                              (x1[i].find('span', {'class': "t-14 t-normal t-black--light"}).find('span', {'aria-hidden': "true"}).get_text().strip()))
                        text1.append(y1)
                    except:
                        y1 = (
                            (x1[i].find('span', {'aria-hidden': "true"}).get_text().strip()))
                        text1.append(y1)
    except:
        text1 = "NA"

    profile1["Certificados"] = text1
    return

"""Competências"""

def competencias(profile):
    link_skills = f'https://www.linkedin.com/in/{profile}/details/skills/'
    driver.get(link_skills)
    sleep(5)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cert_div = soup.find('section', {'class': "artdeco-card ember-view pb3"})
    text2 = []
    try:
        cert_section = cert_div.find_all("ul")
        x2 = cert_section[0].find_all(
            'li', {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        for i in range(len(x2)):
            y2 = ((x2[i].find('span', {'aria-hidden': "true"}).get_text().strip()))
            text2.append(y2)
    except:
        text2.append("NA")
    text2
    profile1["Competencias"] = text2
    return

p=0
t=len(employeeslink)-1
while p <= t:
    profile1["Link"] = employeeslink[p]
    pessoal(employeeslink[p])
    experiencia(employeeslink[p])
    certificados(employeeslink[p])
    competencias(employeeslink[p])
    df = df.append(profile1, ignore_index = True)
    df.to_csv('dataemployeesdata.csv')
    p=p+1

display(df)
