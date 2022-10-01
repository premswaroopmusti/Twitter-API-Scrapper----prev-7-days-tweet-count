import tweepy
import pandas as pd
import functools
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
import time

def pichle_saath_din(df):
    df.drop(df.iloc[:, 2:], inplace=True, axis=1)
    key = []
    for i in df['UNDERLYING']:
        key.append(i)


    def remove(key):
        s = []
        for i in key:
            # print(i.strip()+"gg")
            s.append(i.strip())
        return s

    a = remove(df['UNDERLYING'])
    b = remove(df['SYMBOL    '])

    c = a + b

    w = c[:100]
    x = c[100:200]
    y = c[200:300]
    z = c[300:]

    API_KEY = " lucRPh8PJNSphYSDtxNhKQi38"
    API_SECRET = "z6DWl5uZQyb4cltb15ZCco7i8PK1vpk9NeXuxEWIUuc1t6IbZU"
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANpCgQEAAAAAzebDWfE991mdqyGttAnI1pEsinI%3Dhn5ZiUkv7YlTOdeHGsnXYIbaEPA2vixX5LbhLIANAJOwshyJg9"
    ACCESS_TOKEN = "1562370412218298369-mOIEIVEBcT0pHdqxPxkWuZFMNkzU1J"
    ACCESS_TOKEN_SECRET = "rbz052p6Owe8SmQ1aXVqVX8mILKFIjWptBNGjsqYmEZps"

    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)
    w_7_days = []
    for i in w:
            i = i.replace("&", "")
            i = i.replace("and", "")
            i = i.replace("AND", "")

            from datetime import datetime, timedelta
            import pytz, dateutil.parser
            time = datetime.now()
            dt = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S.%f')
            f = dt - timedelta(hours = 167)
            utctime = dateutil.parser.parse(str(f))
            start_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))
            d = dt - timedelta(seconds=10)
            utctime = dateutil.parser.parse(str(d))
            end_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))

            counts = client.get_recent_tweets_count(query=i, start_time=start_time, end_time=end_time)
            final_count = 0
            for count in counts.data:
                    final_count += count["tweet_count"]

            a = (f'{i} : {final_count}')
            w_7_days.append(a)

    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)
    x_7_days = []
    for i in x:
            i = i.replace("&", "")
            i = i.replace("and", "")
            i = i.replace("AND", "")

            from datetime import datetime, timedelta
            import pytz, dateutil.parser
            time = datetime.now()
            dt = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S.%f')
            f = dt - timedelta(hours = 167)
            utctime = dateutil.parser.parse(str(f))
            start_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))
            d = dt - timedelta(seconds=10)
            utctime = dateutil.parser.parse(str(d))
            end_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))

            counts = client.get_recent_tweets_count(query=i, start_time=start_time, end_time=end_time)
            final_count = 0
            for count in counts.data:
                    final_count += count["tweet_count"]

            a = (f'{i} : {final_count}')
            x_7_days.append(a)

    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)
    y_7_days = []
    import time
    time.sleep(300)
    for i in y:
            i = i.replace("&", "")
            i = i.replace("and", "")
            i = i.replace("AND", "")

            from datetime import datetime, timedelta
            import pytz, dateutil.parser
            time = datetime.now()
            dt = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S.%f')
            f = dt - timedelta(hours=167)
            utctime = dateutil.parser.parse(str(f))
            start_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))
            d = dt - timedelta(seconds=10)
            utctime = dateutil.parser.parse(str(d))
            end_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))

            counts = client.get_recent_tweets_count(query=i, start_time=start_time, end_time=end_time)
            final_count = 0
            for count in counts.data:
                    final_count += count["tweet_count"]

            a = (f'{i} : {final_count}')
            y_7_days.append(a)

    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)
    z_7_days = []
    for i in z:
            i = i.replace("&", "")
            i = i.replace("and", "")
            i = i.replace("AND", "")

            from datetime import datetime, timedelta
            import pytz, dateutil.parser
            time = datetime.now()
            dt = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S.%f')
            f = dt - timedelta(hours=167)
            utctime = dateutil.parser.parse(str(f))
            start_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))
            d = dt - timedelta(seconds=10)
            utctime = dateutil.parser.parse(str(d))
            end_time = utctime.astimezone(pytz.timezone("Asia/Calcutta"))

            counts = client.get_recent_tweets_count(query=i, start_time=start_time, end_time=end_time)
            final_count = 0
            for count in counts.data:
                    final_count += count["tweet_count"]


            a = (f'{i} : {final_count}')
            z_7_days.append(a)


    final_7_days_count = w_7_days + x_7_days + y_7_days + z_7_days
    final_7_days_count_df = pd.DataFrame(final_7_days_count)

    keywithcount_a = []
    for i in final_7_days_count_df[0]:
        keywithcount_a.append(i.split(' : '))

    for i in keywithcount_a:
        i.append(int(i[1]))

    keywithcount_a = pd.DataFrame(keywithcount_a)
    keywithcount_a.set_axis(['Keywords', 'Count', 'rohit'], axis='columns', inplace=True)
    keywithcount_a.drop(['Count'], axis=1, inplace=True)

    count = keywithcount_a['rohit']
    key = keywithcount_a['Keywords']

    key1 = key[0:200].values
    key2 = key[200:].values

    count1 = count[0:200].values
    count2 = count[200:].values

    keywords = []
    realcount = []
    realkeyword = []
    for i in range(200):
        keys = []
        keys.append(key[i])
        keys.append(key[200 + i])
        keywords.append(keys)
        realcount.append(count[i] + count[200 + i])

    for i in keywords:
        realkeyword.append(','.join(i))

    antha_real = pd.DataFrame(list(zip(realkeyword, realcount)),
                              columns=['realkeyword', 'realcount'])

    antha_real.sort_values(by=['realcount'], inplace=True, ascending=False)
    chaabi = antha_real['realkeyword'].head(50)
    ginti = antha_real['realcount'].head(50)
    pellisupulu = {'keyword': chaabi, 'count': ginti}
    pellisupulu = pd.DataFrame(pellisupulu)
    return pellisupulu
