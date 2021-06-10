import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import formats

from csv_to_pandas import csv_to_pandas


plotting_dir = './plotting'

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

def violins_chromatic_v_diatonic(partition, data,x,y,name=""):
    n_groups = len(data.groupby(partition))
    fig, axes = plt.subplots(ncols=n_groups, sharex=True, sharey=True)
    fig.suptitle(name, fontsize=16)

    for ax, (n,grp) in zip(axes, data.groupby(partition)):
        # sns.violinplot(x=x, y=y, data=grp, ax=ax, palette=['green','purple'], inner="stick")
        # sns.violinplot(x=x, y=y, data=grp, ax=ax, inner="box")

        sns.barplot(x=x, y=y, data=grp, ax=ax, palette=['#A64669', '#9688F2'])
        # sns.stripplot(x=x, y=y, data=grp, palette=['black'], ax=ax)

        # sns.pointplot(x=x, y=y, hue="subject", data=grp,
        #               palette=["black"], ax=ax)
        ax.set_title(n)
    for ax in axes:
        try:
            ax.get_legend().remove()
        except:
            1+1
    # plt.ylim(0.35, 0.9)
    # plt.ylim(800, 2750)
    plt.savefig('plots/' + name + ".svg")
    plt.show()

def bars_contour_v_pitch(partition, data,x,y,name=""):
    n_groups = len(data.groupby(partition))
    fig, axes = plt.subplots(ncols=n_groups, sharex=True, sharey=True,figsize=[3,8])
    fig.suptitle(name, fontsize=16)
    for ax, (n,grp) in zip(axes, data.groupby(partition)):
        # print(grp.head())
        sns.barplot(x=x, y=y, data=grp,ax=ax)
        sns.stripplot(x=x, y=y, data=grp,palette=['black'],ax=ax)
        # change_width(ax, .35)

        ax.set_title(n)
    for i,ax in enumerate(axes):
        try:
            if(i>0): ax.set_ylabel('')
            ax.set_xlabel('')
            ax.set(xticklabels=[''])
            ax.get_legend().remove()
        except:
            1+1
    plt.show()




format_general = formats.general()

#8 notes
data_8 = csv_to_pandas(plotting_dir + "/8-note.csv",format_general)
data_8.head()
data_8["bias"] = data_8['bias'].astype('float')
data_8["pc_decoy_at_condition"] = data_8['pc_decoy_at_condition'].astype('float')
data_8["rt"] = data_8['rt'].astype('float')
data_8["rt_type"] = data_8['rt_type'].astype('float')
data_8["shifted-swapped"] = data_8['shifted-swapped'].astype('float')

# violins_chromatic_v_diatonic('type',data_8,x='manipulation',y='bias',name="8-notes-bias")
# violins_chromatic_v_diatonic('type',data_8,x='manipulation',y='pc_decoy_at_condition',name="8-notes-decoy")
# violins_chromatic_v_diatonic('type',data_8, x='manipulation',y='rt',name='RT_8-notes')
# violins_chromatic_v_diatonic('type',data_8, x='type',y='rt_type',name='RT_8-notes_ALL')
# violins_chromatic_v_diatonic('type',data_8, x='type',y='shifted-swapped',name='8-notes')

#8 notes - excluding trials that didn't violate chromatic
data_8_exc = csv_to_pandas(plotting_dir + "/8-note _violated_chromatic.csv",format_general)
data_8_exc.head()
data_8_exc["bias"] = data_8_exc['bias'].astype('float')
data_8_exc["pc_decoy_at_condition"] = data_8_exc['pc_decoy_at_condition'].astype('float')
data_8_exc["rt"] = data_8_exc['rt'].astype('float')
data_8_exc["rt_type"] = data_8_exc['rt_type'].astype('float')
data_8_exc["shifted-swapped"] = data_8_exc['shifted-swapped'].astype('float')



# violins_chromatic_v_diatonic('type',data_8_exc,x='manipulation',y='bias',name="8-notes-bias")
# violins_chromatic_v_diatonic('type',data_8_exc,x='manipulation',y='pc_decoy_at_condition',name="8-notes-decoy")
# violins_chromatic_v_diatonic('type',data_8_exc, x='manipulation',y='rt',name='RT_8-notes')
# violins_chromatic_v_diatonic('type',data_8_exc, x='type',y='rt_type',name='RT_8-notes_ALL')
# violins_chromatic_v_diatonic('type',data_8_exc, x='type',y='shifted-swapped',name='8-notes')

#12 notes
data_12 = csv_to_pandas(plotting_dir + "/12-note.csv",format_general)
data_12["bias"] = data_12['bias'].astype('float')
data_12["pc_decoy_at_condition"] = data_12['pc_decoy_at_condition'].astype('float')
data_12["rt"] = data_12['rt'].astype('float')
data_12["rt_type"] = data_12['rt_type'].astype('float')
data_12["shifted-swapped"] = data_12['shifted-swapped'].astype('float')


# violins_chromatic_v_diatonic('type',data_12,x='manipulation',y='bias',name="12-notes-bias")
# violins_chromatic_v_diatonic('type',data_12,x='manipulation',y='pc_decoy_at_condition',name="12-notes-decoy")
# violins_chromatic_v_diatonic('type',data_12, x='manipulation',y='rt',name='RT_12-notes')
# violins_chromatic_v_diatonic('type',data_12, x='type',y='rt_type',name='RT_12-notes_ALL')
# violins_chromatic_v_diatonic('type',data_12, x='type',y='shifted-swapped',name='12-notes')


#12 notes - excluding trials that didn't violate chromatic
data_12_exc = csv_to_pandas(plotting_dir + "/12-note_violated_chromatic.csv",format_general)
data_12_exc.head()
data_12_exc["bias"] = data_12_exc['bias'].astype('float')
data_12_exc["pc_decoy_at_condition"] = data_12_exc['pc_decoy_at_condition'].astype('float')
data_12_exc["rt"] = data_12_exc['rt'].astype('float')
data_12_exc["rt_type"] = data_12_exc['rt_type'].astype('float')
data_12_exc["shifted-swapped"] = data_12_exc['shifted-swapped'].astype('float')



# violins_chromatic_v_diatonic('type',data_12_exc,x='manipulation',y='bias',name="12-notes-bias")
# violins_chromatic_v_diatonic('type',data_12_exc,x='manipulation',y='pc_decoy_at_condition',name="12-notes-decoy")
# violins_chromatic_v_diatonic('type',data_12_exc, x='manipulation',y='rt',name='RT_12-notes')
# violins_chromatic_v_diatonic('type',data_12_exc, x='type',y='rt_type',name='RT_12-notes_ALL')
# violins_chromatic_v_diatonic('type',data_12_exc, x='type',y='shifted-swapped',name='12-notes')



#16 notes
data_16 = csv_to_pandas(plotting_dir + "/16-note.csv",format_general)
data_16["bias"] = data_16['bias'].astype('float')
data_16["pc_decoy_at_condition"] = data_16['pc_decoy_at_condition'].astype('float')
data_16["rt"] = data_16['rt'].astype('float')
data_16["rt_type"] = data_16['rt_type'].astype('float')
data_16["shifted-swapped"] = data_16['shifted-swapped'].astype('float')

# violins_chromatic_v_diatonic('type',data_16,x='manipulation',y='bias',name="16-notes-bias")
# violins_chromatic_v_diatonic('type',data_16,x='manipulation',y='pc_decoy_at_condition',name="16-notes-decoy")
# violins_chromatic_v_diatonic('type',data_16, x='manipulation',y='rt',name='RT_16-notes')
# violins_chromatic_v_diatonic('type',data_16, x='type',y='rt_type',name='RT_16-notes_ALL')
# violins_chromatic_v_diatonic('type',data_16, x='type',y='shifted-swapped',name='16-notes')



#16 notes - excluding trials that didn't violate chromatic
data_16_exc = csv_to_pandas(plotting_dir + "/16-note_violated_chromatic.csv",format_general)
data_16_exc.head()
data_16_exc["bias"] = data_16_exc['bias'].astype('float')
data_16_exc["pc_decoy_at_condition"] = data_16_exc['pc_decoy_at_condition'].astype('float')
data_16_exc["rt"] = data_16_exc['rt'].astype('float')
data_16_exc["rt_type"] = data_16_exc['rt_type'].astype('float')
data_16_exc["shifted-swapped"] = data_16_exc['shifted-swapped'].astype('float')



# violins_chromatic_v_diatonic('type',data_16_exc,x='manipulation',y='bias',name="16-notes-bias")
# violins_chromatic_v_diatonic('type',data_16_exc,x='manipulation',y='pc_decoy_at_condition',name="16-notes-decoy")
# violins_chromatic_v_diatonic('type',data_16_exc, x='manipulation',y='rt',name='RT_16-notes')
# violins_chromatic_v_diatonic('type',data_16_exc, x='type',y='rt_type',name='RT_16-notes_ALL')
# violins_chromatic_v_diatonic('type',data_16_exc, x='type',y='shifted-swapped',name='16-notes')


#12 note decoys
data_12d = csv_to_pandas(plotting_dir + "/12-note-decoys.csv",format_general)
data_12d["pc_decoy_at_condition"] = data_12d['pc_decoy_at_condition'].astype('float')
data_12d["decoy_rt_type"] = data_12d['decoy_rt_type'].astype('float')
data_12d["decoy_rt_at_condition"] = data_12d['decoy_rt_at_condition'].astype('float')

# violins_chromatic_v_diatonic('type',data_12d,x='manipulation',y='pc_decoy_at_condition',name="12-notes-decoy-only")
# violins_chromatic_v_diatonic('type',data_12d, x='type',y='decoy_rt_type',name='12Decoy_RT_Type')
# violins_chromatic_v_diatonic('type',data_12d, x='manipulation',y='decoy_rt_at_condition',name='12Decoy_RT_at_Cond')



#16 note decoys
data_16d = csv_to_pandas(plotting_dir + "/16-note-decoys.csv",format_general)
data_16d["pc_decoy_at_condition"] = data_16d['pc_decoy_at_condition'].astype('float')
data_16d["decoy_rt_type"] = data_16d['decoy_rt_type'].astype('float')
data_16d["decoy_rt_at_condition"] = data_16d['decoy_rt_at_condition'].astype('float')

# violins_chromatic_v_diatonic('type',data_16d,x='manipulation',y='pc_decoy_at_condition',name="16-notes-decoy-only")
# violins_chromatic_v_diatonic('type',data_16d, x='type',y='decoy_rt_type',name='16Decoy_RT_Type')
# violins_chromatic_v_diatonic('type',data_16d, x='manipulation',y='decoy_rt_at_condition',name='16Decoy_RT_at_Cond')



#12 notes below chance
data_12b = csv_to_pandas(plotting_dir + "/12-note-BC.csv",format_general)
data_12b["bias"] = data_12b['bias'].astype('float')
data_12b["pc_decoy_at_condition"] = data_12b['pc_decoy_at_condition'].astype('float')
data_12b["rt"] = data_12b['rt'].astype('float')
data_12b["rt_type"] = data_12b['rt_type'].astype('float')
data_12b["shifted-swapped"] = data_12b['shifted-swapped'].astype('float')

# violins_chromatic_v_diatonic('type',data_12b,x='manipulation',y='bias',name="B12-notes-bias")
# violins_chromatic_v_diatonic('type',data_12b,x='manipulation',y='pc_decoy_at_condition',name="B12-notes-decoy")
# violins_chromatic_v_diatonic('type',data_12b, x='manipulation',y='rt',name='BRT_12-notes')
# violins_chromatic_v_diatonic('type',data_12b, x='type',y='rt_type',name='BRT_12-notes_ALL')
# violins_chromatic_v_diatonic('type',data_12b, x='type',y='shifted-swapped',name='B12-notes')

#16 notes below chance
data_16b = csv_to_pandas(plotting_dir + "/16-note-BC.csv",format_general)
data_16b["bias"] = data_16b['bias'].astype('float')
data_16b["pc_decoy_at_condition"] = data_16b['pc_decoy_at_condition'].astype('float')
data_16b["rt"] = data_16b['rt'].astype('float')
data_16b["rt_type"] = data_16b['rt_type'].astype('float')
data_16b["shifted-swapped"] = data_16b['shifted-swapped'].astype('float')

# violins_chromatic_v_diatonic('type',data_16b,x='manipulation',y='bias',name="B16-notes-bias")
# violins_chromatic_v_diatonic('type',data_16b,x='manipulation',y='pc_decoy_at_condition',name="B16-notes-decoy")
# violins_chromatic_v_diatonic('type',data_16b, x='manipulation',y='rt',name='BRT_16-notes')
# violins_chromatic_v_diatonic('type',data_16b, x='type',y='rt_type',name='BRT_16-notes_ALL')
# violins_chromatic_v_diatonic('type',data_16b, x='type',y='shifted-swapped',name='B16-notes')


# format_66 = []
#
# for i in range(66):
#     obj = {
#         'static': {
#             'set':i,
#         },
#         'dynamic':{
#             'value':str(i),
#         }
#     }
#     format_66.append(obj)

format_66 = formats.sixty_six()


score_matrix = csv_to_pandas(plotting_dir + "/score-matrix.csv",format_66)
# score_matrix = csv_to_pandas(plotting_dir + "/likert-Q1-score.csv",format_66)
# score_matrix = csv_to_pandas(plotting_dir + "/likert-Q2-score.csv",format_66)
# score_matrix = csv_to_pandas(plotting_dir + "/likert-Q3-score.csv",format_66)

nan_value = float("NaN")
score_matrix.replace("", nan_value, inplace=True)
score_matrix.dropna(inplace=True)
score_matrix["value"] = score_matrix["value"].astype('float')
plt.figure(figsize=(10,5))

# sns.violinplot(x="set", y="value", data=score_matrix)
ax = sns.barplot(x="set", y="value", data=score_matrix, palette=['green', 'purple'])
ax = sns.barplot(x="set", y="value", data=score_matrix)
# sns.stripplot(x="set", y="value", data=score_matrix, palette=['black'], ax=ax)
# plt.ylim(2.5,3.65)
plt.savefig("plots/66-scores.svg")
plt.show()


# score_matrix = csv_to_pandas("./score-matrix.csv",format_66)
# score_matrix = csv_to_pandas("./RT-matrix.csv",format_66)
# score_matrix = score_matrix.loc[score_matrix['set'].isin(['3','65'])]
# score_matrix = score_matrix.loc[score_matrix['set'].isin(['11','30'])]
# score_matrix = score_matrix.loc[score_matrix['set'].isin(['5','43'])]


# nan_value = float("NaN")
# score_matrix.replace("", nan_value, inplace=True)
# score_matrix.dropna(inplace=True)
#
# score_matrix["value"] = score_matrix["value"].astype('float')
# plt.figure(figsize=(10,5))
# # # ax = sns.violinplot(x="set", y="value", data=score_matrix)
# # # sns.violinplot(x="set", y="value", data=score_matrix, ax=ax, inner="box")
# # ax = sns.barplot(x="set", y="value", data=score_matrix, palette=['green', 'purple'])
# ax = sns.regplot(x="set", y="value", data=score_matrix,
#                  x_estimator=np.mean)
# # sns.stripplot(x="set", y="value", data=score_matrix, palette=['black'], ax=ax)
#
# plt.savefig("test.svg")
# plt.show()

format_sem = [
    {
        'static': {
            'type':'score',
        },
        'dynamic':{
            'value':'Score SEM',
        }
    },
{
        'static': {
            'type':'pos',
        },
        'dynamic':{
            'value':'Pos SEM'
        }
    },
]

# sem_matrix = csv_to_pandas(plotting_dir + "/SEM.csv",format_sem)
# nan_value = float("NaN")
# sem_matrix.replace("", nan_value, inplace=True)
# sem_matrix.dropna(inplace=True)
# sem_matrix["value"] = sem_matrix["value"].astype('float')
# # plt.figure(figsize=(100,5))
# # sns.violinplot(x="set", y="value", data=score_matrix)
# ax = sns.barplot(x="type", y="value", data=sem_matrix, palette=sns.color_palette("hls", 2))
# # sns.stripplot(x="type", y="value", data=sem_matrix, palette=['black'], ax=ax)
# plt.ylim(0.3, 0.4)
#
# plt.show()

# DvND = pd.read_csv(plotting_dir + '/DvND_Score.csv')
# ax = sns.barplot(x="Type", y="Score", data=DvND, palette=sns.color_palette("Blues_r"))
# plt.savefig("plots/diatonic_v_ND.svg")
# plt.show()
#
#
# DvND = pd.read_csv(plotting_dir + '/ScoreByP5.csv')
# ax = sns.barplot(x="Type", y="Score", data=DvND, palette=sns.color_palette("rocket"))
# # sns.stripplot(x="Type", y="Score", data=DvND, palette=['black'], ax=ax)
# plt.savefig("plots/score_by_P5.svg")
# plt.show()


# DScoreByP5 = pd.read_csv(plotting_dir + '/DScoreByP5.csv')
# ax = sns.barplot(x="Type", y="Score", data=DScoreByP5, palette=sns.color_palette("rocket"))
# sns.stripplot(x="Type", y="Score", data=DScoreByP5, palette=['black'], ax=ax)
# ax.set_title("Diatonic")
# plt.show()
#
# NDScoreByP5 = pd.read_csv(plotting_dir + '/NDScoreByP5.csv')
# ax = sns.barplot(x="Type", y="Score", data=NDScoreByP5, palette=sns.color_palette("rocket"))
# sns.stripplot(x="Type", y="Score", data=NDScoreByP5, palette=['black'], ax=ax)
# ax.set_title("NDiatonic")
# plt.show()


format_expertise = formats.expertise()

# expertise_long = csv_to_pandas(plotting_dir + "/similarity_results_with_qualtrics_12-16notes.csv",format_expertise)
#
# expertise_long["value"] = expertise_long['value'].astype('float')
# levels = ['0-1','2-5','6+']
# mapping = {level: i for i, level in enumerate(levels)}
# key = expertise_long['expertise'].map(mapping)
# expertise_long = expertise_long.iloc[key.argsort()]
#
# sns.catplot(x='expertise', y='value', hue='manipulation', data=expertise_long, kind='bar')
# # sns.catplot(x='expertise', y='shifted-swapped', hue='type', data=expertise_long, kind='strip', palette=['black'])
# plt.savefig("plots/score_by_expertise.svg")
# plt.show()


# expertise_short = csv_to_pandas(plotting_dir + "/similarity_results_with_qualtrics _8notes.csv",format_expertise)
# expertise_short["shifted-swapped"] = expertise_short['shifted-swapped'].astype('float')
# sns.catplot(x='expertise', y='shifted-swapped', hue='type', data=expertise_short, kind='bar')
# # sns.catplot(x='expertise', y='shifted-swapped', hue='type', data=expertise_long, kind='strip', palette=['black'])
#
# plt.show()

# format_musicality = formats.musicality()
#
# musicality_long = csv_to_pandas(plotting_dir + "/similarity_results_with_qualtrics_12-16notes.csv",format_musicality)
# musicality_long["shifted-swapped"] = musicality_long['shifted-swapped'].astype('float')
# sns.catplot(x='musicality', y='shifted-swapped', hue='type', data=musicality_long, kind='bar')
# # sns.catplot(x='expertise', y='shifted-swapped', hue='type', data=expertise_long, kind='strip', palette=['black'])
#
# plt.show()

# format_decoys = formats.decoys()
# expertise_decoys_66 = csv_to_pandas(plotting_dir + "/66_results_with_qualtrics.csv",format_decoys)
# expertise_decoys_66["decoy_pc"] = expertise_decoys_66['decoy_pc'].astype('float')
# levels = ['low','medium','high']
# mapping = {level: i for i, level in enumerate(levels)}
# key = expertise_decoys_66['expertise'].map(mapping)
# expertise_decoys_66 = expertise_decoys_66.iloc[key.argsort()]
# ax = sns.barplot(x='expertise', y='decoy_pc', data=expertise_decoys_66)
# # sns.stripplot(ax=ax, x='expertise', y='decoy_pc', data=expertise_decoys_66, palette=['black'])
# plt.savefig("plots/decoy_score_by_expertise.svg")
# plt.show()



# Load the dataset
# scores = pd.read_csv(plotting_dir + '/score-pair-values.csv')
#
# # Make the PairGrid
# g = sns.PairGrid(scores.sort_values("Score", ascending=False),
#                  x_vars=scores.columns[1], y_vars=["Set"],
#                  height=10, aspect=.8
#                  )
#
# # Draw a dot plot using the stripplot function
# g.map(sns.stripplot, size=10, orient="h", linewidth=1, edgecolor="w")
#
# # # Use the same x axis limits on all columns and add better labels
# g.set(xlabel="Score", ylabel="Set", xlim=(0.4,0))
#
# # # Use semantically meaningful titles for the columns
# titles = ["Bias"]
#
# for ax, title in zip(g.axes.flat, titles):
#
#     # Set a different title for each axes
#     ax.set(title=title)
#
#     # Make the grid horizontal instead of vertical
#     ax.xaxis.grid(False)
#     ax.yaxis.grid(True)
#
# sns.despine(left=True, bottom=True)
# plt.savefig("plots/66-distribution.svg")
# plt.show()
