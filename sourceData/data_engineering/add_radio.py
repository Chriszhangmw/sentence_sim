from fuzzywuzzy import fuzz
import re
import pandas as pd

def removeOral(string):
    startslist = ['有谁知道','大家知道','你知道','谁知道','谁了解','有谁了解','大家了解','你了解']
    endslist = ['吗']
    s,e = False,False
    for st in startslist:
        if string.startswith(st):
            s = True
            break
    for end in endslist:
        if string.endswith(end):
            e = True
            break
    if s and e:
        tmp = re.findall(st + '(.*)' + end,string)[0]
        if len(tmp)==0:
            return 'None'
        else:
            return tmp
    return string
def main():
    df = pd.read_csv('./train_eda.csv')

    df['text_a'] = df['text_a'].apply(removeOral)
    df['text_b'] = df['text_b'].apply(removeOral)
    df['ratio'] = df.apply(lambda x: fuzz.ratio(x.text_a, x.text_b), axis=1)  # 编辑距离
    df.to_csv('./train_eda_ratio.csv',index = None)


    test = pd.read_csv('./cuted_testB.csv')

    test['text_a'] = test['text_a'].apply(removeOral)
    test['text_b'] = test['text_b'].apply(removeOral)
    test['ratio'] = test.apply(lambda x: fuzz.ratio(x.text_a, x.text_b), axis=1)  # 编辑距离
    test.to_csv('./test_eda_ratio.csv',index = None)


if __name__ == "__main__":
    a = "成都哪里的牛肉火锅最好吃呢"
    b = "成都哪里的牛肉火锅最好吃"
    print(fuzz.ratio(a,b))