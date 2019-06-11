import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
print("imported succesfully")
df = pd.read_csv('VIF_data.csv')
print(df)
from statsmodels.tools.tools import add_constant
df_corr = df.corr()
print(df_corr)
print(pd.DataFrame(np.linalg.inv(df.corr().values), index = df_corr.index, columns=df_corr.columns))
print(df.corr().values)
print(np.linalg.inv(df.corr().values))

VIF : Variance Inflation Factor
If you have two variables that are highly correlated, your best course of action is to just remove one of them.
Multicollinearity was measured by variance inflation factors (VIF) and tolerance
Multicollinearity occurs when two or more predictors in the model are correlated and provide redundant information about the response
variance inflation factor (VIF) is the reciprocal of the tolerance.
Tolerance ranges from 0 to 1



