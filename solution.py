import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 1134491798

def solution(x: np.array, y: np.array, alpha: float) -> bool:
   
    is_normal_x = np.all(np.abs((x - np.mean(x)) / np.std(x)) < 3)
    is_normal_y = np.all(np.abs((y - np.mean(y)) / np.std(y)) < 3)
    
   
    is_homogeneous = np.abs(np.var(x) - np.var(y)) < 0.1*np.mean(np.abs([np.var(x), np.var(y)]))
    
    
    if is_normal_x and is_normal_y and is_homogeneous:
        t_statistic, p_value = ttest_ind(x, y, equal_var=True)
        if p_value < alpha:
            return True
        else:
            return False
    else:
        return False
