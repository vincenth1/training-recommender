
LANG_LEVEL_MAP = {"A1": 1, "A2": 2, "B1": 3, "B2": 4, "C1": 5, "C2": 6}
EDU_LEVEL_MAP = {"none": 0, "highschool": 1, "Bachelor": 2, "Master": 3, "University Diploma": 2.5}

SCORING_FIELDS = [
    "language_level_bonus",
    "has_language_certificate",
    "education_level_bonus",
    "work_experience_years",
    "job_interest_match",
    "learning_mode_match",
    "childcare_compatibility",
    "location_priority_match",
    "disability_friendly_match",
    "has_computer_skills",
    "has_driving_license"
]

FIELD_WEIGHTS = {
    "language_level_bonus": 20,
    "has_language_certificate": 5,
    "education_level_bonus": 10,
    "work_experience_years": 15,
    "job_interest_match": 15,
    "learning_mode_match": 10,
    "childcare_compatibility": 5,
    "location_priority_match": 5,
    "disability_friendly_match": 5,
    "has_computer_skills": 5,
    "has_driving_license": 5
}

def compute_feature_value(user, course, field):
    if field == "language_level_bonus":
        user_level = LANG_LEVEL_MAP.get(user.get("german_level", "A1"), 0)
        required_level = LANG_LEVEL_MAP.get(course.get("min_language_level", "A1"), 0)
        return max(0, user_level - required_level)

    if field == "has_language_certificate":
        return 1 if user.get("has_language_certificate") else 0

    if field == "education_level_bonus":
        user_edu = EDU_LEVEL_MAP.get(user.get("education", "none"), 0)
        course_edu_list = course.get("education_required", [])
        if isinstance(course_edu_list, list) and course_edu_list:
            course_edu_levels = [EDU_LEVEL_MAP.get(e, 0) for e in course_edu_list]
            course_edu = min(course_edu_levels)
        else:
            course_edu = EDU_LEVEL_MAP.get(course_edu_list, 0)
        return max(0, user_edu - course_edu)

    if field == "work_experience_years":
        field_required = course.get("required_field", "").lower()
        return user.get("work_experience", {}).get(field_required, 0)

    if field == "job_interest_match":
        tags = [t.lower() for t in course.get("tags", [])]
        desired = user.get("desired_job", "").lower()
        interests = [i.strip().lower() for i in user.get("interest", "").split(",")]
        if desired in tags:
            return 1
        if any(i in tags for i in interests):
            return 0.5
        return 0

    if field == "learning_mode_match":
        return 1 if user.get("preferred_learning_mode") == course.get("delivery_mode") else 0

    if field == "childcare_compatibility":
        needs = user.get("has_childcare_needs", False)
        supports = course.get("supports_childcare", False)
        return 1 if needs and supports else 0

    if field == "location_priority_match":
        if user.get("location") in course.get("locations", []):
            return 1
        elif user.get("can_relocate"):
            return 0.5
        else:
            return 0

    if field == "disability_friendly_match":
        if not user.get("has_disability", False):
            return 1
        elif course.get("is_physical_friendly"):
            return 0.5
        return 0

    if field == "has_computer_skills":
        return 1 if user.get("computer_skills") else 0

    if field == "has_driving_license":
        return 1 if user.get("driving_license") else 0

    return 0

def compute_final_score(user, course):
    total = 0
    for field in SCORING_FIELDS:
        value = compute_feature_value(user, course, field)
        weight = FIELD_WEIGHTS.get(field, 0)
        total += value * weight
    return round(min(total, 100), 2)
