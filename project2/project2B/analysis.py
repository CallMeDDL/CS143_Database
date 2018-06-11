# May first need:
# In your VM: sudo apt-get install libgeos-dev (brew install on Mac)
# pip3 install https://github.com/matplotlib/basemap/archive/v1.1.0.tar.gz

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np

from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from sklearn.metrics import roc_curve, auc


"""
IMPORTANT
This is EXAMPLE code.
There are a few things missing:
1) You may need to play with the colors in the US map.
2) This code assumes you are running in Jupyter Notebook or on your own system.
   If you are using the VM, you will instead need to play with writing the images
   to PNG files with decent margins and sizes.
3) The US map only has code for the Positive case. I leave the negative case to you.
4) Alaska and Hawaii got dropped off the map, but it's late, and I want you to have this
   code. So, if you can fix Hawaii and Alask, ExTrA CrEdIt. The source contains info
   about adding them back.
"""



# =========================== PLOT 1: SENTIMENT OVER TIME (TIME SERIES PLOT) ===========================
# Assumes a file called time_data.csv that has columns
# date, Positive, Negative. Use absolute path.


ts = pd.read_csv("./output/time_data.csv/part-00000-236df31d-a7c4-41c3-8571-fc4d4593d84e-c000.csv")

# Remove erroneous row.
ts = ts[ts['date'] != '2018-12-31']

plt.figure(figsize=(12, 5))
ts.date = pd.to_datetime(ts['date'], format='%Y-%m-%d')
ts.set_index(['date'],inplace=True)

ax = ts.plot(title="President Trump Sentiment on /r/politics Over Time", color=['green', 'red'], ylim=(0, 1.05))
ax.plot()
plt.savefig("./plots/part1.png")



# ================== PLOT 2 & 3: SENTIMENT BY STATE (POSITIVE AND NEGATIVE SEPARATELY) =================
# This assumes you have a CSV file called "state_data.csv" with the columns:
# state, Positive, Negative
# You should use the FULL PATH to the file, just in case.
# You also need to download the following files. Put them somewhere convenient:
# https://github.com/matplotlib/basemap/blob/master/examples/st99_d00.shp
# https://github.com/matplotlib/basemap/blob/master/examples/st99_d00.dbf
# https://github.com/matplotlib/basemap/blob/master/examples/st99_d00.shx
state_data = pd.read_csv("./output/state_data.csv/part-00000-fdc7c744-a27b-4762-870a-13fd9a572d44-c000.csv")


# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
            projection='lcc', lat_1=33, lat_2=45, lon_0=-95)
shp_info = m.readshapefile('./st99_d00','states', drawbounds=True)
pos_data = dict(zip(state_data.state, state_data.Positive))
neg_data = dict(zip(state_data.state, state_data.Negative))


# choose a color for each state based on sentiment.
pos_colors = {}
statenames = []
pos_cmap = plt.cm.Greens # use 'hot' colormap

vmin = 0
vmax = 1
for shapedict in m.states_info:
    statename = shapedict['NAME']
    # skip DC and Puerto Rico.
    if statename not in ['District of Columbia', 'Puerto Rico']:
        if statename in pos_data:
            pos = pos_data[statename]
            pos_colors[statename] = pos_cmap(np.sqrt((pos - vmin)/(vmax - vmin)))[:3]
        else:
            pos = 0.0
            pos_colors[statename] = pos_cmap(np.sqrt((pos - vmin)/(vmax - vmin)))[:3]
    statenames.append(statename)


# POSITIVE MAP
ax = plt.gca() # get current axes instance
for nshape, seg in enumerate(m.states):
    # skip Puerto Rico and DC
    if statenames[nshape] not in ['District of Columbia', 'Puerto Rico']:
        color = rgb2hex(pos_colors[statenames[nshape]]) 
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)
plt.title('Positive Trump Sentiment Across the US')
plt.savefig("./plots/part2_pos.png")


# choose a color for each state based on sentiment.
neg_colors = {}
statenames = []
neg_cmap = plt.cm.Reds # use 'hot' colormap

vmin = 0
vmax = 1
for shapedict in m.states_info:
    statename = shapedict['NAME']
    # skip DC and Puerto Rico.
    if statename not in ['District of Columbia', 'Puerto Rico']:
        if statename in neg_data:
            neg = neg_data[statename]
            neg_colors[statename] = neg_cmap(np.sqrt((neg - vmin)/(vmax - vmin)))[:3]
        else:
            neg = 0.0
            neg_colors[statename] = neg_cmap(np.sqrt((neg - vmin)/(vmax - vmin)))[:3]
    statenames.append(statename)


# NEGATIVE MAP
ax = plt.gca() # get current axes instance
for nshape, seg in enumerate(m.states):
    # skip Puerto Rico and DC
    if statenames[nshape] not in ['District of Columbia', 'Puerto Rico']:
        color = rgb2hex(neg_colors[statenames[nshape]]) 
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)
plt.title('Negtive Trump Sentiment Across the US')
plt.savefig("./plots/part2_neg.png")


# choose a color for each state based on sentiment.
diff_colors = {}
statenames = []
diff_cmap = plt.cm.Blues # use 'hot' colormap

vmin = 0
vmax = 1
for shapedict in m.states_info:
    statename = shapedict['NAME']
    # skip DC and Puerto Rico.
    if statename not in ['District of Columbia', 'Puerto Rico']:
        if statename in pos_data and statename in neg_data:
            diff = (pos_data[statename] - neg_data[statename] + 1.0) / 2.0
            diff_colors[statename] = diff_cmap(np.sqrt((diff - vmin)/(vmax - vmin)))[:3]
        else:
            diff = 0.0
            diff_colors[statename] = diff_cmap(np.sqrt((diff - vmin)/(vmax - vmin)))[:3]
    statenames.append(statename)


# NEGATIVE MAP
ax = plt.gca() # get current axes instance
for nshape, seg in enumerate(m.states):
    # skip Puerto Rico and DC
    if statenames[nshape] not in ['District of Columbia', 'Puerto Rico']:
        color = rgb2hex(diff_colors[statenames[nshape]]) 
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)
plt.title('Difference between Positive and Negtive Trump Sentiment Across the US')
plt.savefig("./plots/part3.png")
# SOURCE: https://stackoverflow.com/questions/39742305/how-to-use-basemap-python-to-plot-us-with-50-states
# (this misses Alaska and Hawaii. If you can get them to work, EXTRA CREDIT)



# ======================== PART 4 SHOULD BE DONE IN SPARK ==============================




# ========================= PLOT 5A: SENTIMENT BY STORY SCORE ==========================
# What is the purpose of this? It helps us determine if the story score
# should be a feature in the model. Remember that /r/politics is pretty
# biased.

# Assumes a CSV file called submission_score.csv with the following coluns
# submission_score, Positive, Negative

sub_pos = pd.read_csv("./output/sub_score_pos_pct.csv/part-00000-39aac039-e86a-4d98-b056-1fc540f1fc82-c000.csv")
sub_neg = pd.read_csv("./output/sub_score_neg_pct.csv/part-00000-2a5f6798-e1f7-4ee7-91a6-1d0ce4e2498f-c000.csv")
plt.figure(figsize=(12, 5))
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(sub_pos['sub_score'], sub_pos['pos_pct'], s=10, c='b', marker="s", label='Positive')
ax1.scatter(sub_neg['sub_score'], sub_neg['neg_pct'], s=10, c='r', marker="o", label='Negative')
plt.legend(loc='lower right');

plt.xlabel('President Trump Sentiment by Submission Score')
plt.ylabel("Percent Sentiment")
plt.savefig("./plots/part5_sub.png")



com_pos = pd.read_csv("./output/com_score_pos_pct.csv/part-00000-7f3dbec1-b6d6-4c6a-b7a1-1e9751d589f0-c000.csv")
com_neg = pd.read_csv("./output/com_score_neg_pct.csv/part-00000-5b1ba261-cb87-43eb-b5ba-ac83b2c4761b-c000.csv")
plt.figure(figsize=(12, 5))
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(com_pos['com_score'], com_pos['pos_pct'], s=10, c='b', marker="s", label='Positive')
ax1.scatter(com_neg['com_score'], com_neg['neg_pct'], s=10, c='r', marker="o", label='Negative')
plt.legend(loc='lower right');

plt.xlabel('President Trump Sentiment by Comment Score')
plt.ylabel("Percent Sentiment")
plt.savefig("./plots/part5_com.png")



# =============================== PART 7 ROC =====================================
ROC_pos = pd.read_csv("./output/posResult_ROC.csv/part-00000-f1d01163-357d-4e21-be50-b72107fb73df-c000.csv")
ROC_neg = pd.read_csv("./output/negResult_ROC.csv/part-00000-dad86fac-f92a-4436-b7d0-69e23c5d147d-c000.csv")

prob_pos = ROC_pos['probability']
label_pos = list()
prob_neg = ROC_neg['probability']
label_neg = list()

label = ROC_pos['label']
for i in range(len(label)):
	if label[i] != 1:
		label_pos.append(0)
	else:
		label_pos.append(1)
for i in range(len(label)):
	if label[i] != -1:
		label_neg.append(0)
	else:
		label_neg.append(1)

fpr_pos, tpr_pos, _ = roc_curve(label_pos, prob_pos)
fpr_neg, tpr_neg, _ = roc_curve(label_neg, prob_neg)

auc_pos = auc(fpr_pos, tpr_pos)
auc_neg = auc(fpr_neg, tpr_neg)


plt.figure(figsize=(12, 5))
lw = 2
plt.plot(fpr_pos, tpr_pos, color='deeppink', lw=lw, label='ROC curve for pos (area = %0.2f)' % auc_pos)
plt.plot(fpr_neg, tpr_neg, color='navy', lw=lw, label='ROC curve for neg (area = %0.2f)' % auc_neg)
plt.plot([0, 1], [0, 1], color='black', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.savefig("./plots/part7.png")