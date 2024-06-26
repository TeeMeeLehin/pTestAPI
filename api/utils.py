from typing import List
from api.models import *
import os
import pickle
from sklearn.metrics.pairwise import linear_kernel

MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'recommendation_model.pkl')

# load recommender model
def load_recommendation_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            recommendation_model = pickle.load(f)
        return recommendation_model
    else:
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# recommender function
def recommend_courses(query):
    recommendation_model = load_recommendation_model()
    df = recommendation_model['df']
    tfidf = recommendation_model['tfidf']
    tfidf_matrix = recommendation_model['tfidf_matrix']
    cosine_sim = recommendation_model['cosine_sim']

    tfidf_query = tfidf.transform([query])
    sim_scores = list(linear_kernel(tfidf_query, tfidf_matrix).flatten())
    course_indices = sorted(range(len(sim_scores)), key=lambda i: sim_scores[i], reverse=True)
    recommended_titles = df.iloc[course_indices][:10]['Title'].tolist()
    
    recommended_courses = Courses.objects.filter(title__in=recommended_titles)
    return recommended_courses

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
        return (
            "Advanced",
            "You're practically a digital guru! You navigate the web with the grace of a seasoned sailor. But even the best captains can learn new tricks. Our advanced courses will push your digital boundaries and keep you at the forefront of the ever-evolving online world. Time to become a legendary digital master!",
        )
    elif score < 2.5:
        return (
            "Beginner",
            "You're taking your first steps into the exciting world of the internet! Think of yourself as a digital explorer, learning the ropes and navigating uncharted territories (websites). Don't worry if things seem overwhelming at first. We have beginner-friendly courses to help you confidently conquer the online jungle and avoid any digital pitfalls.",
        )
    else:
        return (
            "Intermediate",
            "You're no longer a digital newbie, but maybe not quite a web whiz. You can browse the web like a pro, but some online tools might still leave you scratching your head. That's okay! We have intermediate courses to boost your skills and turn you into a confident online citizen. Get ready to unleash your inner digital ninja!",
        )


def web_perse(p_options: List[str]):
    res = []
    for x in p_options:
        option = PersonalityOption.objects.get(option_tag=x)
        option_res = option.option_res
        res.append(option_res)
    return res


def compute_ability(ability_ids):
    res = []
    for id in ability_ids:
        ability = Ability.objects.get(id=id)
        res.append(ability.ability_tag)
        res.append(ability.ability_text)
    return res


def compute_query(session):
    # personality = ", ".join(web_perse(session.get("ptest_responses", [])))
    dll = session.get("dll_level", [])[0]
    abilities = ", ".join(compute_ability(session.get("abilities", [])))
    wants = session.get("wants", "")
    wants = wants.replace(",", "")
    wants = wants.replace(".", "")
    wants = wants.replace("&", "")

    query = dll + " " + abilities + " " + wants

    query = query.replace(",", "")
    query = query.replace(".", "")
    return query
