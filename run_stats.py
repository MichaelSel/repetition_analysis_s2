import pandas as pd
import formats
import stat_funcs as music_stat


reps = 10000

plotting_dir = './plotting'

scores = pd.read_csv(plotting_dir + "/16-note.csv")

print(scores.head())

print(scores['c_shifted-swapped'])
print(scores['d_shifted-swapped'])
print(scores['rt_diatonic_shifted'])
print(scores['rt_diatonic_swapped'])

#BIAS
# obs_stat, prob = music_stat.perm_bias_paired(scores['%_diatonic_shifted'],scores['%_diatonic_swapped'])
# obs_stat, prob = music_stat.perm_bias_paired(scores['%_chromatic_shifted'],scores['%_chromatic_swapped'])
# obs_stat, prob = music_stat.perm_t_test_paired(scores['c_shifted-swapped'],scores['d_shifted-swapped'])

#RT
scores_rt_d = scores.dropna(subset = ['rt_diatonic_shifted'])
scores_rt_d = scores_rt_d.dropna(subset = ['rt_diatonic_swapped'])
obs_stat, prob = music_stat.perm_bias_paired(scores_rt_d['rt_diatonic_shifted'],scores_rt_d['rt_diatonic_swapped'])

# scores_rt_c = scores.dropna(subset = ['rt_chromatic_shifted'])
# scores_rt_c = scores_rt_c.dropna(subset = ['rt_chromatic_swapped'])
# obs_stat, prob = music_stat.perm_bias_paired(scores_rt_c['rt_chromatic_shifted'],scores_rt_c['rt_chromatic_swapped'])
# obs_stat, prob = music_stat.perm_bias_paired(scores['rt_chromatic'],scores['rt_diatonic'])





