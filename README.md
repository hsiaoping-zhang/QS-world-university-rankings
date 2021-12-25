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

## Code
一頁一頁地把資料抓下來，直到 Selenium 無法再找到 `next` 按鈕可以繼續。

`get_indicator_scores`(string) : 獲取某一頁面的學校和成績資料
> element(class) filter : `.td-wrap-in`

```python
items = soup.select(".td-wrap-in")
school, scores = [], [[] for i in range(7)]
# ...
item =[]
for index in range(len(items)):
    # there are 8 indicators
    if(index % 8 == 0):
        item.append(items[index].contents[0].contents[0])
    else:
        try:
            test = float(items[index].contents[0])
            item.append(test)
        except:
            item.append("NULL")  # NULL score

    if(index % 8 == 7):  # append row to list
        school.append(item[0])
        if(len(item) != 8):  # abnormal data
            print(item)
        for i in range(len(scores)):
            scores[i].append(item[i+1])
        item =[]
        continue
```

`get_rank`(string) : 抓當頁面的所有 rank 數字  
> element(class) filter : `._univ-rank.show-this-in-mobile-indi`

`write_df_csv`(list, list, list) : 把目前抓到的先寫進 csv
