mport pandas as pd
import numpy as np
from scipy.stats import shapiro, ttest_ind


chat_id = 1134491798 

def solution(X: np.ndarray, Y: np.ndarray, alpha: float) -> bool:
    
p1 = shapiro(X)
p2 = shapiro(Y)
if p1 < alpha or p2 < alpha:
return False 
p = fligner(X, Y)
if p < alpha:
equal_var = False 
else:
equal_var = True 


p_value = ttest_ind(X, Y, equal_var=equal_var)


if p_value < alpha:
return True # Отклоняем нулевую гипотезу о равенстве средних значений
else:
return False # Не отклоняем нулевую гипотезу о равенстве средних значений
