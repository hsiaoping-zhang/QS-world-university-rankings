# QS-world-university-rankings
[ ranking crawler ] 2022 QS World University Rankings 

## Introduction
- language : `python`
- package : `pip install`
    - BeautifulSoup
    - Selenium
    - requests
    - pandas
- output : `.csv` files 
- website : [QS World University Rankings 2022 ](https://www.topuniversities.com/university-rankings/world-university-rankings/2022)
- \* reqiured : 需要先將 [webdriver (chrome) ](https://sites.google.com/a/chromium.org/chromedriver/downloads) 載下來並放在執行資料夾

## Code
一頁一頁地把資料抓下來，直到 Selenium 無法再找到 `next` 按鈕可以繼續。

在 `code/` 資料夾底下執行 `python main.py` 即可產生 `QS-2022-ranking.csv`

### Function
`get_indicator_scores`(string) : 獲取某一頁面的學校和成績資料
> element(class) filter : `.td-wrap-in`

```python
items = soup.select(".td-wrap-in")
school, scores = [], [[] for i in range(7)]
# ...

item = []  # container for [school, score, score, ...]
for index in range(len(items)):
    # there are 7 indicators
    if(index % 8 == 0):
        item.append(items[index].contents[0].contents[0])
    else:
        try:
            test = float(items[index].contents[0])
            item.append(test)
        except:
            item.append("NULL")  # NULL score

    if(index % 8 == 7):  # append row to list
        school.append(item[0])  # the first element
        if(len(item) != 8):  # abnormal data
            print(item)
        
        for i in range(len(scores)):  # other scores
            scores[i].append(item[i+1])
        item =[]
        continue
```

`get_rank`(string) : 抓當頁面的所有 rank 數字  
> element(class) filter : `._univ-rank.show-this-in-mobile-indi`

`write_df_csv`(list, list, list) : 把目前抓到的先寫進 csv
