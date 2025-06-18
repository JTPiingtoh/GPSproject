import pandas as pd

adjusted_values_dict = {}

measures = ['HSR/min', 'Dis/min', 'SD/min', 'Accels + Decels /min', 'PlayerLoad']
for measure in measures:
    adjusted_values_dict[measure] = {}


dispermin_team_mean_data = {
    'Team': ['1st', 'U17', 'U18', 'U23'],
    'Mean': [107.066, 109.717, 112.354, 107.278],
    'Std. Error': [1.802, 2.230, 2.152, 1.500],
    'df': [41.909, 43.856, 41.455, 42.439],
    '95% CI Lower Bound': [103.429, 105.223, 108.008, 104.250],
    '95% CI Upper Bound': [110.704, 114.211, 116.699, 110.305]
}

dispermin_team_mean_df = pd.DataFrame(dispermin_team_mean_data)
adjusted_values_dict["Dis/min"]["team"] = dispermin_team_mean_df

dispermin_position_mean_data = {
    'Position': ['CB', 'CM', 'FB', 'FWD'],
    'Mean': [102.225, 114.389, 111.063, 108.738],
    'Std. Error': [1.719, 1.428, 2.574, 1.589],
    'df': [46.075, 49.304, 41.476, 51.077],
    '95% CI Lower Bound': [98.765, 111.519, 105.865, 105.547],
    '95% CI Upper Bound': [105.685, 117.259, 116.260, 111.929]
}

dispermin_position_mean_df = pd.DataFrame(dispermin_position_mean_data)
adjusted_values_dict["Dis/min"]["position"] = dispermin_position_mean_df



dispermin_team_position_mean_data = {
    'Team': ['1st', '1st', '1st', '1st',
             'U17', 'U17', 'U17', 'U17',
             'U18', 'U18', 'U18', 'U18',
             'U23', 'U23', 'U23', 'U23'],
    'Position': ['CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD'],
    'Mean': [100.759, 118.548, 104.376, 104.582,
             99.919, 116.822, 114.843, 107.284,
             105.077, 116.298, 115.064, 112.975,
             103.144, 105.886, 109.969, 110.111],
    'Std. Error': [3.118, 2.740, 3.451, 3.179,
                   3.975, 3.181, 6.616, 3.137,
                   3.162, 2.976, 6.535, 3.545,
                   3.430, 2.482, 2.767, 2.813],
    'df': [47.088, 54.164, 61.754, 48.216,
           47.172, 50.669, 40.258, 50.112,
           46.940, 41.173, 38.300, 50.175,
           43.212, 55.374, 43.974, 58.202],
    '95% CI Lower Bound': [94.488, 113.055, 97.477, 98.191,
                           91.922, 110.434, 101.474, 100.983,
                           98.716, 110.289, 101.837, 105.857,
                           96.229, 100.912, 104.393, 104.481],
    '95% CI Upper Bound': [107.031, 124.042, 111.274, 110.972,
                           107.916, 123.209, 128.212, 113.584,
                           111.438, 122.308, 128.290, 120.094,
                           110.060, 110.860, 115.544, 115.741]
}

dispermin_team_position_mean_df = pd.DataFrame(dispermin_team_position_mean_data).set_index(["Position", "Team"])
adjusted_values_dict["Dis/min"]["team_position"] = dispermin_team_position_mean_df


hsr_team_mean_data = {
    'Team': ['1st', 'U17', 'U18', 'U23'],
    'Mean': [5.863, 5.845, 5.860, 6.063],
    'Std. Error': [0.369, 0.457, 0.440, 0.307],
    'df': [39.592, 42.196, 39.254, 40.103],
    '95% CI Lower Bound': [5.118, 4.923, 4.970, 5.442],
    '95% CI Upper Bound': [6.609, 6.768, 6.750, 6.684]
}

hsr_team_mean_df = pd.DataFrame(hsr_team_mean_data)
adjusted_values_dict["HSR/min"]["team"] = hsr_team_mean_df

hsr_position_mean_data = {
    'Position': ['CB', 'CM', 'FB', 'FWD'],
    'Mean': [4.059, 5.362, 6.786, 7.424],
    'Std. Error': [0.353, 0.294, 0.526, 0.328],
    'df': [44.095, 47.339, 39.316, 48.916],
    '95% CI Lower Bound': [3.347, 4.770, 5.721, 6.764],
    '95% CI Upper Bound': [4.772, 5.954, 7.850, 8.084]
}

hsr_position_mean_df = pd.DataFrame(hsr_position_mean_data)
adjusted_values_dict["HSR/min"]["position"] = hsr_position_mean_df


hsr_team_position_mean_data = {
    'Team': ['1st', '1st', '1st', '1st',
             'U17', 'U17', 'U17', 'U17',
             'U18', 'U18', 'U18', 'U18',
             'U23', 'U23', 'U23', 'U23'],
    'Position': ['CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD'],
    'Mean': [4.327, 6.537, 5.709, 6.879,
             3.262, 5.601, 7.211, 7.307,
             4.457, 4.814, 7.095, 7.072,
             4.191, 4.496, 7.128, 8.437],
    'Std. Error': [0.641, 0.567, 0.718, 0.655,
                   0.818, 0.657, 1.351, 0.647,
                   0.650, 0.608, 1.331, 0.732,
                   0.703, 0.514, 0.567, 0.583],
    'df': [45.146, 53.066, 59.281, 46.002,
           46.173, 49.214, 38.186, 49.346,
           44.209, 39.223, 35.931, 48.850,
           40.624, 51.176, 42.320, 52.524],
    '95% CI Lower Bound': [3.035, 5.399, 4.272, 5.560,
                           1.615, 4.281, 4.476, 6.006,
                           3.147, 3.584, 4.396, 5.601,
                           2.771, 3.464, 5.983, 7.267],
    '95% CI Upper Bound': [5.619, 7.676, 7.146, 8.198,
                           4.909, 6.921, 9.945, 8.608,
                           5.768, 6.045, 9.795, 8.542,
                           5.610, 5.527, 8.273, 9.607]
}

hsr_team_position_mean_df = pd.DataFrame(hsr_team_position_mean_data).set_index(["Position", "Team"])
adjusted_values_dict["HSR/min"]["team_position"] = hsr_team_position_mean_df

sprintdistance_team_mean_data = {
    'Team': ['1st', 'U17', 'U18', 'U23'],
    'Mean': [1.914, 1.097, 1.405, 1.533],
    'Std. Error': [0.169, 0.212, 0.202, 0.141],
    'df': [40.058, 45.882, 40.487, 40.891],
    '95% CI Lower Bound': [1.573, 0.671, 0.997, 1.248],
    '95% CI Upper Bound': [2.256, 1.523, 1.812, 1.817]
}

sprintdistance_team_mean_df = pd.DataFrame(sprintdistance_team_mean_data)
adjusted_values_dict["SD/min"]["team"] = sprintdistance_team_mean_df

sprintdistance_position_mean_data = {
    'Position': ['CB', 'CM', 'FB', 'FWD'],
    'Mean': [0.731, 0.878, 1.866, 2.474],
    'Std. Error': [0.164, 0.138, 0.241, 0.154],
    'df': [46.411, 50.234, 40.619, 51.586],
    '95% CI Lower Bound': [0.401, 0.602, 1.378, 2.165],
    '95% CI Upper Bound': [1.061, 1.155, 2.353, 2.783]
}

sprintdistance_position_mean_df = pd.DataFrame(sprintdistance_position_mean_data)
adjusted_values_dict["SD/min"]["position"] = sprintdistance_position_mean_df

sprintdistance_team_position_mean_data = {
    'Team': ['1st', '1st', '1st', '1st',
             'U17', 'U17', 'U17', 'U17',
             'U18', 'U18', 'U18', 'U18',
             'U23', 'U23', 'U23', 'U23'],
    'Position': ['CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD'],
    'Mean': [1.055, 1.517, 2.087, 2.999,
             0.333, 0.481, 1.212, 2.361,
             0.830, 0.643, 1.976, 2.171,
             0.706, 0.872, 2.188, 2.364],
    'Std. Error': [0.299, 0.269, 0.343, 0.305,
                   0.383, 0.309, 0.617, 0.306,
                   0.301, 0.279, 0.603, 0.344,
                   0.323, 0.241, 0.263, 0.274],
    'df': [47.292, 58.908, 59.039, 46.517,
           53.039, 53.618, 39.946, 57.151,
           43.487, 41.545, 36.269, 54.339,
           40.462, 48.680, 45.921, 47.942],
    '95% CI Lower Bound': [0.454, 0.978, 1.401, 2.385,
                           -0.436, -0.138, -0.036, 1.749,
                           0.223, 0.079, 0.753, 1.481,
                           0.055, 0.388, 1.659, 1.814],
    '95% CI Upper Bound': [1.655, 2.056, 2.773, 3.613,
                           1.102, 1.101, 2.460, 2.973,
                           1.437, 1.206, 3.198, 2.861,
                           1.358, 1.357, 2.717, 2.915]
}

sprintdistance_team_position_mean_df = pd.DataFrame(sprintdistance_team_position_mean_data).set_index(["Position", "Team"])
adjusted_values_dict["SD/min"]["team_position"] = sprintdistance_team_position_mean_df

accelsdeccels_team_data = {
    'Team': ['1st', 'U17', 'U18', 'U23'],
    'Mean': [1.943, 2.174, 1.947, 2.050],
    'Std. Error': [0.116, 0.143, 0.139, 0.096],
    'df': [45.484, 45.915, 44.922, 45.991],
    '95% CI Lower Bound': [1.709, 1.886, 1.667, 1.856],
    '95% CI Upper Bound': [2.177, 2.462, 2.227, 2.244]
}

accelsdeccels_team_df = pd.DataFrame(accelsdeccels_team_data)
adjusted_values_dict["Accels + Decels /min"]["team"] = accelsdeccels_team_df

accelsdeccels_position_data = {
    'Position': ['CB', 'CM', 'FB', 'FWD'],
    'Mean': [1.651, 2.033, 2.188, 2.242],
    'Std. Error': [0.109, 0.090, 0.166, 0.099],
    'df': [48.063, 50.940, 44.829, 53.312],
    '95% CI Lower Bound': [1.431, 1.852, 1.853, 2.043],
    '95% CI Upper Bound': [1.871, 2.213, 2.523, 2.442]
}

accelsdeccels_position_df = pd.DataFrame(accelsdeccels_position_data)
adjusted_values_dict["Accels + Decels /min"]["position"] = accelsdeccels_position_df

accelsdeccels_team_position_data = {
    'Team': ['1st', '1st', '1st', '1st',
             'U17', 'U17', 'U17', 'U17',
             'U18', 'U18', 'U18', 'U18',
             'U23', 'U23', 'U23', 'U23'],
    'Position': ['CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD',
                 'CB', 'CM', 'FB', 'FWD'],
    'Mean': [1.698, 2.200, 1.777, 2.097,
             1.653, 2.386, 2.691, 1.965,
             1.722, 1.741, 2.128, 2.196,
             1.531, 1.804, 2.153, 2.711],
    'Std. Error': [0.198, 0.171, 0.211, 0.201,
                   0.253, 0.200, 0.429, 0.198,
                   0.200, 0.193, 0.427, 0.223,
                   0.220, 0.152, 0.177, 0.170],
    'df': [48.635, 52.723, 60.020, 50.548,
           47.483, 50.662, 43.813, 49.312,
           49.881, 44.319, 42.768, 50.265,
           46.933, 62.558, 45.962, 72.329],
    '95% CI Lower Bound': [1.301, 1.857, 1.356, 1.694,
                           1.145, 1.984, 1.826, 1.567,
                           1.320, 1.353, 1.268, 1.748,
                           1.089, 1.500, 1.796, 2.372],
    '95% CI Upper Bound': [2.096, 2.543, 2.199, 2.500,
                           2.162, 2.787, 3.556, 2.363,
                           2.124, 2.129, 2.989, 2.645,
                           1.973, 2.108, 2.511, 3.050]
}

accelsdeccels_team_position_df = pd.DataFrame(accelsdeccels_team_position_data).set_index(["Position", "Team"])
adjusted_values_dict["Accels + Decels /min"]["team_position"] = accelsdeccels_team_position_df

playerload_team_data = {
    'Team': ['1st', 'U17', 'U18', 'U23'],
    'Mean': [458.137, 442.324, 472.515, 431.082],
    'Std. Error': [3.515, 5.067, 4.344, 2.894],
    'df': [90.881, 346.583, 205.736, 149.401],
    '95% CI Lower Bound': [451.155, 432.358, 463.949, 425.363],
    '95% CI Upper Bound': [465.119, 452.290, 481.080, 436.800]
}

playerload_team_df = pd.DataFrame(playerload_team_data)
adjusted_values_dict["PlayerLoad"]["team"] = playerload_team_df

playerload_position_data = {
    "Position": ["CB", "CM", "FB", "FWD"],
    "Mean": [409.217, 479.663, 486.069, 429.107],
    "Std. Error": [3.498, 2.990, 4.604, 3.507],
    "df": [407.769, 340.886, 526.888, 423.549],
    "95% CI Lower Bound": [402.341, 473.781, 477.024, 422.214],
    "95% CI Upper Bound": [416.093, 485.545, 495.114, 436.001]
}

playerload_position_df = pd.DataFrame(playerload_position_data)
adjusted_values_dict["PlayerLoad"]["position"] = playerload_position_df

playerload_team_position_data = {
    "Team": ["1st", "1st", "1st", "1st",
             "U17", "U17", "U17", "U17",
             "U18", "U18", "U18", "U18",
             "U23", "U23", "U23", "U23"],
    "Position": ["CB", "CM", "FB", "FWD",
                 "CB", "CM", "FB", "FWD",
                 "CB", "CM", "FB", "FWD",
                 "CB", "CM", "FB", "FWD"],
    "Mean": [391.522, 521.282, 485.339, 434.405,
             396.609, 464.843, 479.397, 428.447,
             427.322, 479.068, 521.355, 462.313,
             421.416, 453.460, 458.186, 391.264],
    "Std. Error": [5.743, 6.119, 6.017, 5.684,
                   9.928, 6.674, 12.330, 7.963,
                   5.060, 6.012, 10.552, 8.476,
                   5.580, 4.101, 5.726, 4.802],
    "df": [403.025, 423.404, 420.338, 398.840,
           529.674, 543.667, 542.171, 534.019,
           405.331, 448.432, 546.690, 516.924,
           521.239, 376.398, 519.903, 469.530],
    "95% CI Lower Bound": [380.232, 509.255, 473.511, 423.230,
                           377.105, 451.733, 455.176, 412.804,
                           417.375, 467.252, 500.628, 445.662,
                           410.453, 445.396, 446.937, 381.828],
    "95% CI Upper Bound": [402.812, 533.309, 497.166, 445.580,
                           416.113, 477.953, 503.618, 444.090,
                           437.270, 490.884, 542.083, 478.964,
                           432.379, 461.524, 469.436, 400.701]
}

playerload_team_position_df = pd.DataFrame(playerload_team_position_data).set_index(["Position", "Team"])
adjusted_values_dict["PlayerLoad"]["team_position"] = playerload_team_position_df

print(adjusted_values_dict)