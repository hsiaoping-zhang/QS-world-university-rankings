
import time
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# user defined function in function.py
from function import get_indicator_scores
from function import get_rank
from function import write_df_csv


indicators = ["Overall Score", "International Students Ratio", "International Faculty Ratio", 
            "Faculty Student Ratio", "Citations per Faculty", "Academic Reputation", "Employer Reputation"]

# target file: write header line
file = open("QS-2022-ranking.csv", 'w')
file.write("Rank,University,")
for index in range(len(indicators)):
    file.write(indicators[index] + ",")
file.write("\n")
file.close()
print("finish csv init")

# webdriver setting
option = Options()
option.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', options=option)

# # # target website address # # #
url = "https://www.topuniversities.com/university-rankings/world-university-rankings/2022"
chrome.get(url)
time.sleep(2)

# click ranking indicator tag
chrome.find_element_by_link_text("Rankings indicators", ).send_keys(Keys.ENTER)
time.sleep(3)

print("current page:", 1)
soup = BeautifulSoup(chrome.page_source, 'html.parser')
school, scores = get_indicator_scores(soup)
ranks = get_rank(soup)
result = write_df_csv(ranks, school, scores)
if(result == False):
    print("END with ERROR")

current_page = 2
while(True):
    print("current page:", current_page)
    try:
        chrome.find_element_by_class_name("next").send_keys(Keys.ENTER)  # click next page
    except:
        break
    
    time.sleep(3)
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    
    school, scores = get_indicator_scores(soup)
    ranks = get_rank(soup)

    # write to csv
    result = write_df_csv(ranks, school, scores)
    if(result == False):
        break
    current_page += 1

chrome.close()
print("- finish -")