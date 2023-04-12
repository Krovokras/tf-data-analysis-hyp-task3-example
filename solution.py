import scipy.stats as stats
import numpy as np
chat_id = 1134491798 
def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    _, p_value = stats.ks_2samp(x, y)
    return p_value < alpha
