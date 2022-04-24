import pandas as pd
import os
from pandas.api.types import CategoricalDtype

'''
讀取和寫入當次遊戲的紀錄並排序
'''

scoreList = []
timeList = []
#排序分數(由253~0)及時間(由00:00~99:59)
def order():
    for i in range (253,-1,-1):
        scoreList.append(i)
    for minute in range (0,100):
        for second in range (0,60):
            strMinute = str(minute)
            strSecond = str(second)
            if minute < 10:
                strMinute = "0" + strMinute
            if second < 10:
                strSecond = "0" + strSecond
            timeList.append(strMinute + ":" + strSecond)
order()
scoreSort = CategoricalDtype(scoreList,ordered=True)
timeSort = CategoricalDtype(timeList,ordered=True)
rank = {
    "score" : [],
    "time" : []
}
df = pd.DataFrame(rank)
if (os.path.isfile("record.csv")==False):
    print("no file")
    rankInit = {
        "score": [0, 0, 0, 0, 0, 0],
        "time": ["00:00", "00:00", "00:00", "00:00", "00:00", "00:00"]
    }
    initDf = pd.DataFrame(rankInit)
    initDf.to_csv("record.csv",index=False)
#自訂義排序方式:分數 -> 時間
def sort():
    global df
    df["score"] = df["score"].astype(scoreSort)
    df["time"] = df["time"].astype(timeSort)
    df = df.sort_values(["score", "time"])
#將此次紀錄寫入record.csv並排序
def doRecord():
    global df
    old = pd.read_csv("record.csv")
    df = pd.concat([df,old])
    sort()
    df.to_csv("record.csv",index=False)
