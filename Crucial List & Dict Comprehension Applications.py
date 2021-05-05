import pandas as pd
import numpy as np
import seaborn as sns


def load_car_data():
    data = sns.load_dataset("car_crashes")
    return data


def load_tips_data():
    dataset = sns.load_dataset("tips")
    return dataset


df = load_car_data()
df.head()

# Out[2]:
#    total  speeding  alcohol  ...  ins_premium  ins_losses  abbrev
# 0   18.8     7.332    5.640  ...       784.55      145.08      AL
# 1   18.1     7.421    4.525  ...      1053.48      133.93      AK
# 2   18.6     6.510    5.208  ...       899.47      110.35      AZ
# 3   22.4     4.032    5.824  ...       827.34      142.39      AR
# 4   12.0     4.200    3.360  ...       878.41      165.63      CA
# [5 rows x 8 columns]


""" ## CHALLENGE: aimed at creating a dictionary as follows: (car crashes data set in seaborn library)"""

# before:
# {'total_bill': ['mean', 'min', 'max', 'sum'],
#  'tip': ['mean', 'min', 'max', 'sum'],
#  'size': ['mean', 'min', 'max', 'sum']}

# after:
# {'TOTAL': ['total_mean', 'total_min', 'total_max', 'total_var'],
#  'SPEEDING': ['speeding_mean', 'speeding_min', 'speeding_max', 'speeding_var'],
#  'ALCOHOL': ['alcohol_mean', 'alcohol_min', 'alcohol_max', 'alcohol_var']
#   ....          ....           ....             ....         ....

num_cols = [col for col in df.columns if df[col].dtype != "O"]
agg_list = ["mean", "min", "max", "sum"]
new_dict1 = {col: agg_list for col in num_cols}

# Out[9]:
# {'total': ['mean', 'min', 'max', 'sum'],
#  'speeding': ['mean', 'min', 'max', 'sum'],
#  'alcohol': ['mean', 'min', 'max', 'sum'],
#  'not_distracted': ['mean', 'min', 'max', 'sum'],
#  'no_previous': ['mean', 'min', 'max', 'sum'],
#  'ins_premium': ['mean', 'min', 'max', 'sum'],
#  'ins_losses': ['mean', 'min', 'max', 'sum']}


new_dict = {col.upper(): [str(col) + "_" + c for c in agg_list] for col in num_cols}

#  {'TOTAL': ['total_mean', 'total_min', 'total_max', 'total_sum'],
#  'SPEEDING': ['speeding_mean', 'speeding_min', 'speeding_max', 'speeding_sum'],
#  'ALCOHOL': ['alcohol_mean', 'alcohol_min', 'alcohol_max', 'alcohol_sum'],
#  'NOT_DISTRACTED': ['not_distracted_mean', 'not_distracted_min', 'not_distracted_max', 'not_distracted_sum'],
#  'NO_PREVIOUS': ['no_previous_mean', 'no_previous_min', 'no_previous_max', 'no_previous_sum'],
#  'INS_PREMIUM': ['ins_premium_mean', 'ins_premium_min', 'ins_premium_max', 'ins_premium_sum'],
#  'INS_LOSSES': ['ins_losses_mean', 'ins_losses_min', 'ins_losses_max', 'ins_losses_sum']}


# Alternative way:

d = {}

for col in num_cols:
    d[col.upper()] = [str(col) + "_" + i for i in agg_list]

# =====================================================================================
# =====================================================================================

""" ## CHALLENGE: aimed at creating a dictionary as follows: (car crashes data set in seaborn library)

Let's assign the first element of particular columns in the dataset as "key" and the others as "value" in the dictionary.
"""
###############################################
# Creating a dictionary as follows:
###############################################
# before
#    total  speeding  alcohol  not_distracted  no_previous
# 0   18.8     7.332    5.640          18.048       15.040
# 1   18.1     7.421    4.525          16.290       17.014
# 2   18.6     6.510    5.208          15.624       17.856
# 3   22.4     4.032    5.824          21.056       21.280
# 4   12.0     4.200    3.360          10.920       10.680


# after:
# {18.8: [7, 5, 18, 15],
#  18.1: [7, 4, 16, 17],
#  18.6: [6, 5, 15, 17],
#  22.4: [4, 5, 21, 21],
#  12.0: [4, 3, 10, 10]}


num_cols = [col for col in df.columns if df[col].dtype != "O"]
df["total"].head()
df[num_cols].head()
new_dict_comp = df[num_cols].iloc[0:5, 0:5]

{new_dict_comp.values[i, :][0]: [int(s) for s in new_dict_comp.values[i, :][1:]] for i in range(len(new_dict_comp))}

# Out[20]:
# {18.8: [7, 5, 18, 15],
#  18.1: [7, 4, 16, 17],
#  18.6: [6, 5, 15, 17],
#  22.4: [4, 5, 21, 21],
#  12.0: [4, 3, 10, 10]}


# =====================================================================================
# =====================================================================================

""" ## CHALLENGE: aimed at creating a dictionary as follows: (car crashes data set in seaborn library)"""

# Output
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}


df = load_car_data()

num_cols = [col for col in df.columns if df[col].dtype != "O"]
agg_list = ['mean', 'min', 'max', 'var']
dic = {}

for col in num_cols:
    dic[col] = agg_list

# with Dict comprehension

dic_comp = {col: agg_list for col in num_cols}

# Let's utilize this dictionary by diffracting into "abbrev" categorical variable.

df.groupby("abbrev").agg(dic_comp)

# Out[56]:
#        total                 speeding  ... ins_premium ins_losses
#         mean   min   max var     mean  ...         var       mean     min     max var
# abbrev                                 ...
# AK      18.1  18.1  18.1 NaN    7.421  ...         NaN     133.93  133.93  133.93 NaN
# AL      18.8  18.8  18.8 NaN    7.332  ...         NaN     145.08  145.08  145.08 NaN
# AR      22.4  22.4  22.4 NaN    4.032  ...         NaN     142.39  142.39  142.39 NaN
# ...     ....  ...   ...  ..     ....   ...         ...      ...     ....    ....  ...


# another example? let's see the similar application on "tips" dataset in seaborn library

df = load_tips_data()
df.head()

num_cols = [col for col in df.columns if df[col].dtype in ["int64", "float64"]]
num_cols

agg_list  # ['mean', 'min', 'max', 'var']

dic_comp1 = {col: agg_list for col in num_cols}

df.groupby("time").agg(dic_comp1)

# Out[66]:
#        total_bill                          ...      size
#              mean   min    max        var  ...      mean min max       var
# time                                       ...
# Lunch   17.168676  7.51  43.11  59.503973  ...  2.411765   1   6  1.081651
# Dinner  20.797159  3.07  50.81  83.576697  ...  2.630682   1   6  0.828539
# [2 rows x 12 columns]
# =====================================================================================

""" ## EXAMPLE: LIST COMPREHENSIONS"""

###############################################
# Changing the variable names of a data set
###############################################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']


df.columns = [col.upper() for col in df.columns]

# Alternative way:
df = load_car_data()

a = []
for i in df.columns:
    a.append(i.upper())
df.columns = a
# =====================================================================================

""" ## EXAMPLE: LIST COMPREHENSIONS"""

###############################################
# Create a list comprehension that is written "FLAG" at the beginning of variables that contain
# the word "INS" in their name  and NO FLAG to the others.
###############################################

# before:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

df = load_car_data()
df.columns
# Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#        'ins_premium', 'ins_losses', 'abbrev'], dtype='object')


df.columns = ["FLAG_" + col.upper() if "ins" in col else "NO_FLAG_" + col.upper() for col in df.columns]

# Alternative way:
df = load_car_data()

b = []
for col in df.columns:
    if "ins" in col:
        b.append("FLAG_" + col.upper())
    else:
        b.append("NO_FLAG_" + col.upper())

df.columns = b

# =====================================================================================

""" ## EXAMPLE: LIST COMPREHENSIONS"""
###############################################
# Create a list comprehension that is written "CAT" at the beginning of categorical variable names
###############################################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL',
#  'SPEEDING',
#  'ALCOHOL',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM',
#  'INS_LOSSES',
#  'CAT_ABBREV']

df = load_car_data()

df.columns = ["CAT_" + col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]

# Alternative way:
df = load_car_data()

c = []
for col in df.columns:
    if df[col].dtype == "O":
        c.append("CAT_" + col.upper())
    else:
        c.append(col.upper())

df.columns = c

# =====================================================================================
""" ## EXAMPLE: DICT COMPREHENSIONS"""

# Assigning randomly generated numbers(n) to the "key" part of the dict, and (n * (n+1) / 2) of them to "value" part of
# the dictionary

nums = np.random.randint(0, 30, 10)
nums.sort()

{n: int((n * (n + 1)) / 2) for n in nums}

# Outcome:  {3: 6, 6: 21, 8: 36, 9: 45, 12: 78, 18: 171, 19: 190, 21: 231, 23: 276, 27: 378}


# example:
dictionary = {'rmse': 12, 'mse': 144, 'mae': 53}

{k.upper(): v ** 2 for k, v in dictionary.items()}
# {'RMSE': 144, 'MSE': 20736, 'MAE': 2809}
