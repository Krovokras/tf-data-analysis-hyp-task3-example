from scipy import stats
from typing import List
import pandas as pd
import numpy as np

chat_id = 1134491798 

def solution(X: List[float], Y: List[float], alpha: float = 0.07) -> bool:
    t_stat, p_value = stats.ttest_ind(Y, X, equal_var=False)
    return p_value / 2 < alpha and t_stat > 0
X = [500, 500, 500]
Y = [500, 500, 525]
