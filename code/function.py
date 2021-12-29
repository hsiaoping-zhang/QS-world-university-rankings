import pandas as pd

def get_indicator_scores(soup):
    items = soup.select(".td-wrap-in")
    school, scores = [], [[] for i in range(7)]

    if(len(items) % 8 != 0):
        return [], []

    item =[]
    for index in range(len(items)):
        
        if(index % 8 == 0):
            item.append(items[index].contents[0].contents[0])
        else:
            try:
                test = float(items[index].contents[0])
                item.append(items[index].contents[0])
            except:
                item.append("NULL")  # NULL score

        if(index % 8 == 7):
            # append row to list
            school.append(item[0])
            if(len(item) != 8):
                print(item)
            for i in range(len(scores)):
                scores[i].append(item[i+1])

            item =[]
            continue
    
    return school, scores
    
def get_rank(soup):
    rows = soup.select("._univ-rank.show-this-in-mobile-indi")
    ranks = []
    for row in rows:
        ranks.append(row.contents[0])
    return ranks


def write_df_csv(rank, school, scores):
    df = pd.DataFrame()

    if(len(rank) != len(school)):
        print("length error:", len(rank), len(school))
        return False

    df["Rank"] = rank
    df["University"] = school

    indicators = ["Overall Score", "International Students Ratio", "International Faculty Ratio", 
            "Faculty Student Ratio", "Citations per Faculty", "Academic Reputation", "Employer Reputation"]
    
    for index in range(len(indicators)):
        df[indicators[index]] = scores[index]
        
    df.to_csv("QS-2022-ranking.csv", mode='a', header=False, index=False, encoding="utf-8")
    return True