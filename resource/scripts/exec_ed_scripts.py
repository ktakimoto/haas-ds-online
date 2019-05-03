import math
import numpy as np
import pandas as pd

# utility function for histograms notebook
def round_down_nearest_10(i):
    """Given an integer i, round i down to the nearest multiple of 10."""
    return math.floor(i/10) * 10


# utility function for notebook 2 
def conversion_rate(array):
    """Given an array with values whether or not a user converted,
    return the proportion of users that converted."""
    yesses = (array == 'yes').sum()
    total = len(array)
    return yesses / total

def rename_rocketfuel(rf_tbl):
    """Given RF_TBL, a Table of the Rocket Fuel case data,
    renames columns and values for easier parsability and 
    write to csv."""
    ads_rlbl = rf_tbl.relabeled(['test', 'tot_impr', 'mode_impr_day', 'mode_impr_hour'], 
                     ['test group', 'total ads', 'most ads day', 'most ads hour'])
    def rename_grp(x):
        if x == 0:
            return "control"
        else:
            return "experiment"

    def rename_day(x):
        days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 
               6:'Saturday', 7:'Sunday'}
        return '{0}: {1}'.format(x, days[x])

    def rename_conv(x):
        if x == 0:
            return 'no'
        else:
            return 'yes'

    ads_rlbl.append_column('test group', ads_rlbl.apply(rename_grp, "test group"))
    ads_rlbl.append_column('most ads day', ads_rlbl.apply(rename_day, "most ads day"))
    ads_rlbl.append_column('converted', ads_rlbl.apply(rename_conv, "converted"))

    ads_rlbl.to_csv("data/rocketfuel_data_renamed.csv")


#utility function for notebook 4 section 2a
def format_X(table):
    """Given a Table of explanatory variables, one-hot encodes
    variables if they are categorical and returns a dataframe with 
    all the given explanatory variables."""
    data = table.to_df()
    categorical = ("month", "day of week", "season")
    X = pd.DataFrame({"intercept":np.ones(table.num_rows, dtype='int')})
    for var in table.labels:
        if var in categorical:
            dummies = pd.get_dummies(data[var])
            formatted = dummies.drop(dummies.columns[-1], axis=1)
        else:
            formatted = data.loc[:, [var]]
        X = X.join(formatted)
      
    return X

def rmse(actual, predicted):
    """Return the root mean squared error of the predictions.
    PREDICTED: n-length array with predicted values
    ACTUAL: n-length array with actual values."""
    return np.sqrt(np.mean((actual - predicted)**2))