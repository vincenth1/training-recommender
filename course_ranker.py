
from db.db_reader import fetch_courses
from scoring.rule_score_function import compute_final_score

user = {
    "german_level": "A2",
    "has_language_certificate": True,
    "education": "Master",
    "work_experience": {
        "IT": 1,
        "logistics": 2
    },
    "desired_job": "warehouse worker",
    "interest": "logistics, transport",
    "preferred_learning_mode": "online",
    "has_childcare_needs": True,
    "location": "Berlin",
    "can_relocate": False,
    "has_disability": True,
    "computer_skills": True,
    "driving_license": False
}

courses = fetch_courses()

ranked_courses = []
for course in courses:
    score = compute_final_score(user, course)
    ranked_courses.append((score, course["title"]))

ranked_courses.sort(reverse=True)

print("📋 Ranked Course Recommendations:")
for score, title in ranked_courses[:10]:
    print(f"{title} - {score}/100")
