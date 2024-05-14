from typing import List
from api.models import *


#function to compute dll
def compute_dll(score_ids: List[int]):
    score = 0
    for score_id in score_ids:
        option = DLLOption.objects.get(id = score_id)
        val = option.option_value
        score += val / 4
    
    if score >= 4:
        return 'Your Digital Literacy Level - Advanced'
    elif score < 2.5 :
        return 'Your Digital Literacy Level - Beginner'
    else:
        return 'Your Digital Literacy Level - Intermediate'

#function to compute personality
def compute_perse(p_options: List[int]):
    res = []
    for x in p_options:
        option = PersonalityOption.objects.get(id = x)
        option_res = option.option_res
        res.append(option_res)
    return res

#function to compute interests
def compute_interest(i_options: List[int]):
    res = []
    for x in i_options:
        interest = Interest.objects.get(id = x)
        res.append(interest.name)
    return res
