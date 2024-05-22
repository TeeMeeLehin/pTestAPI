from typing import List
from api.models import *


# function to compute dll
def compute_dll(score_ids: List[int]):
    score = 0
    for score_id in score_ids:
        option = DLLOption.objects.get(id=score_id)
        val = option.option_value
        score += val / 4

    if score >= 4:
        return "Your Digital Literacy Level - Advanced"
    elif score < 2.5:
        return "Your Digital Literacy Level - Beginner"
    else:
        return "Your Digital Literacy Level - Intermediate"


# function to compute personality
def compute_perse(p_options: List[int]):
    res = []
    for x in p_options:
        option = PersonalityOption.objects.get(id=x)
        option_res = option.option_res
        res.append(option_res)
    return res


# function to compute interests
def compute_interest(i_options: List[int]):
    res = []
    for x in i_options:
        interest = Interest.objects.get(id=x)
        res.append(interest.name)
    return res


def web_dll(score):
    if score >= 4:
        return "Advanced", "You're practically a digital guru! You navigate the web with the grace of a seasoned sailor. But even the best captains can learn new tricks. Our advanced courses will push your digital boundaries and keep you at the forefront of the ever-evolving online world. Time to become a legendary digital master!"
    elif score < 2.5:
        return "Beginner", "You're taking your first steps into the exciting world of the internet! Think of yourself as a digital explorer, learning the ropes and navigating uncharted territories (websites). Don't worry if things seem overwhelming at first. We have beginner-friendly courses to help you confidently conquer the online jungle and avoid any digital pitfalls."
    else:
        return "Intermediate", "You're no longer a digital newbie, but maybe not quite a web whiz. You can browse the web like a pro, but some online tools might still leave you scratching your head. That's okay! We have intermediate courses to boost your skills and turn you into a confident online citizen. Get ready to unleash your inner digital ninja!"

def web_perse(p_options: List[str]):
    res = []
    for x in p_options:
        option = PersonalityOption.objects.get(option_tag=x)
        option_res = option.option_res
        res.append(option_res)
    return res
