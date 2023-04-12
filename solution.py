import pandas as pd
import numpy as np
from scipy.stats import shapiro, ttest_ind

chat_id = 1134491798 

def solution(X: np.ndarray, Y: np.ndarray, alpha: float) -> bool:

_, p1 = shapiro(X)
_, p2 = shapiro(Y)
if p1 < alpha or p2 < alpha:
return False 
_, p = fligner(X, Y)
if p < alpha:
    equal_var = False 
else:
    equal_var = True 
_, p_value = ttest_ind(X, Y, equal_var=equal_var)


if p_value < alpha:
    return True 
else:
    return False 
