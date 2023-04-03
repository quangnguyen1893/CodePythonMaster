import pandas as pd

data = pd.read_csv('data/tennis.csv', sep=r'\s*,\s*', header=0, encoding='ascii', engine='python')

outlook = data.groupby(['outlook', 'play']).size()
temp = data.groupby(['temp', 'play']).size()
humidity = data.groupby(['humidity', 'play']).size()
windy = data.groupby(['windy', 'play']).size()
play = data.play.value_counts()

# # outlook
# ol = pd.crosstab(data['outlook'], data['play'], margins=True)
# ol.columns = ["no", "yes", "rowtotal"]
# ol.index = ["overcast", "rainy", "sunny", "coltotal"]
# ol = ol / ol.loc["coltotal"]
# # temp
# tm = pd.crosstab(data['temp'], data['play'], margins=True)
# tm.columns = ["no", "yes", "rowtotal"]
# tm.index = ["cool", "hot", "mild", "coltotal"]
# tm = tm / tm.loc["coltotal"]
# # humidity
# hm = pd.crosstab(data['humidity'], data['play'], margins=True)
# hm.columns = ["no", "yes", "rowtotal"]
# hm.index = ["high", "normal", "coltotal"]
# hm = hm / hm.loc["coltotal"]
# # windy
# wd = pd.crosstab(data['windy'], data['play'], margins=True)
# wd.columns = ["no", "yes", "rowtotal"]
# wd.index = ["False", "True", "coltotal"]
# wd = wd / wd.loc["coltotal"]
# # play
# pl = pd.crosstab(data['play'], data['play'], margins=True)
# pl.columns = ["no", "yes", "rowtotal"]
# pl.index = ["no", "yes", "coltotal"]
# pl = pl.div(pl["rowtotal"], axis=0)
# print(ol)
# print(tm)
# print(hm)
# print(wd)
# print(pl)
# print(ct.iloc[1,1])
# print(play.loc['yes'])

total_y = play.loc['yes']
total_n = play.loc['no']

play_total = total_y + total_n

# pred_play     ('sunny',   'mild',     'normal',    False,     'no')
def find_prob(outlook_val, temp_val, humidity_val, windy_val, play_val):
    p_outlook_play = outlook[outlook_val][play_val] / play.loc[play_val]
    p_temp_play = temp[temp_val][play_val] / play.loc[play_val]
    p_humidity_play = humidity[humidity_val][play_val] / play.loc[play_val]
    p_windy_play = windy[windy_val][play_val] / play.loc[play_val]
    p_play = play.loc[play_val] / play_total
    prob = p_outlook_play * p_temp_play * p_humidity_play * p_windy_play * p_play
    return prob


def pred_play(outlook_val, temp_val, humidity_val, windy_val):
    prob_yes = find_prob(outlook_val, temp_val, humidity_val, windy_val, 'yes')
    prob_no = find_prob(outlook_val, temp_val, humidity_val, windy_val, 'no')
    print("Xac xuat Co the choi: ", prob_yes)
    print("Xac xuat Khong nen choi: ", prob_no)
    if prob_yes > prob_no:
        print("Co the choi")
    else:
        print("Khong nen choi: ")

pred_play('sunny', 'mild', 'normal', False)
# pred_play('overcast', 'mild', 'normal', False)
