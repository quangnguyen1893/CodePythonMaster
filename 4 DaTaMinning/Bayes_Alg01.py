import pandas as pd

data = pd.read_csv('data/tennis.csv', sep=r'\s*,\s*', header=0, encoding='ascii', engine='python')

outlook = data.groupby(['outlook', 'play']).size()
temp = data.groupby(['temp', 'play']).size()
humidity = data.groupby(['humidity', 'play']).size()
windy = data.groupby(['windy', 'play']).size()
play = data.play.value_counts()

# outlook
ol = pd.crosstab(data['outlook'], data['play'], margins=True)
ol.columns = ["no", "yes", "rowtotal"]
ol.index = ["overcast", "rainy", "sunny", "coltotal"]
ol = ol / ol.loc["coltotal"]
# temp
tm = pd.crosstab(data['temp'], data['play'], margins=True)
tm.columns = ["no", "yes", "rowtotal"]
tm.index = ["cool", "hot", "mild", "coltotal"]
tm = tm / tm.loc["coltotal"]
# humidity
hm = pd.crosstab(data['humidity'], data['play'], margins=True)
hm.columns = ["no", "yes", "rowtotal"]
hm.index = ["high", "normal", "coltotal"]
hm = hm / hm.loc["coltotal"]
# windy
wd = pd.crosstab(data['windy'], data['play'], margins=True)
wd.columns = ["no", "yes", "rowtotal"]
wd.index = ["False", "True", "coltotal"]
wd = wd / wd.loc["coltotal"]
# play
pl = pd.crosstab(data['play'], data['play'], margins=True)
pl.columns = ["no", "yes", "rowtotal"]
pl.index = ["no", "yes", "coltotal"]
pl = pl.div(pl["rowtotal"], axis=0)

total_y = play.loc['yes']
total_n = play.loc['no']
play_total = total_y + total_n

def find_prob(outlook_val, temp_val, humidity_val, windy_val, play_val):
    if outlook_val != '':
        p_outlook_play_yes = ol.loc[outlook_val]['yes']
        p_outlook_play_no = ol.loc[outlook_val]['no']
    else:
        p_outlook_play_yes = 1
        p_outlook_play_no = 1

    if temp_val != '':
        p_temp_play_yes = tm.loc[temp_val]['yes']
        p_temp_play_no = tm.loc[temp_val]['no']
    else:
        p_temp_play_yes = 1
        p_temp_play_no = 1

    if humidity_val != '':
        p_humidity_play_yes = hm.loc[humidity_val]['yes']
        p_humidity_play_no = hm.loc[humidity_val]['no']
    else:
        p_humidity_play_yes = 1
        p_humidity_play_no = 1

    if  windy_val != '':
        p_windy_play_yes = wd.loc[windy_val]['yes']
        p_windy_play_no = wd.loc[windy_val]['no']
    else:
        p_windy_play_yes = 1
        p_windy_play_no = 1

    if  play_val != '':
        p_play_yes = pl.loc['coltotal']['yes']
        p_play_no = pl.loc['coltotal']['no']
    else:
        p_play_yes = 1
        p_play_no = 1

    likelihood_yes = p_outlook_play_yes * p_temp_play_yes * p_humidity_play_yes * p_windy_play_yes * p_play_yes
    likelihood_no = p_outlook_play_no * p_temp_play_no * p_humidity_play_no * p_windy_play_no * p_play_no
    if play_val == 'yes':
        prob = likelihood_yes / (likelihood_yes + likelihood_no)
    else:
        prob = likelihood_no / (likelihood_yes + likelihood_no)
    return prob

def pred_play(outlook_val, temp_val, humidity_val, windy_val):
    prob_yes = find_prob(outlook_val, temp_val, humidity_val, windy_val, 'yes')
    prob_no = find_prob(outlook_val, temp_val, humidity_val, windy_val, 'no')
    print(outlook_val,temp_val,humidity_val,windy_val)
    print("Xac xuat Co the choi: ", prob_yes)
    print("Xac xuat Khong nen choi: ", prob_no)
    if prob_yes > prob_no:
        print("Play: Yes")
    else:
        print("Play: No")

# pred_play('overcast', 'cool', 'high', 'False')
# print('===================================')
# pred_play('rainy', 'cool', 'high', 'False')
# print('===================================')
# pred_play('sunny', 'hot', 'normal', 'False')
print('===================================')
# pred_play('', 'hot', 'normal', 'False')
pred_play('', 'cool', 'high', 'True')