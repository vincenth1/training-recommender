import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template
from db.db_reader import fetch_courses
from scoring.rule_score_function import compute_final_score

app = Flask(__name__)

# --- Dummy Data ---
# This simulates the output of your course_ranker.py
DUMMY_COURSES = [
    {"id": 80, "title": "Logistics Expert", "field": "Logistics", "score": 85.0},
    {"id": 5, "title": "Warehouse Logistics", "field": "Logistics", "score": 80.0},
    {"id": 94, "title": "Construction Basics", "field": "Construction", "score": 77.5},
    {"id": 70, "title": "Forklift Operator", "field": "Logistics", "score": 77.5},
    {"id": 53, "title": "Hotel Management Intro", "field": "Hospitality", "score": 67.5},
]

# This simulates a database of training providers for Stage 2
DUMMY_PROVIDERS = {
    80: [
        {"name": "ZAV Institute", "capacity": 15, "schedule": "Mon-Fri, 9-5", "cost": "€500", "funding": "BAMF eligible"},
        {"name": "Logistics Academy", "capacity": 20, "schedule": "Weekends", "cost": "€700", "funding": "None"},
    ],
    5: [
        {"name": "Adult Education Center", "capacity": 10, "schedule": "Evenings", "cost": "€350", "funding": "BAMF eligible"},
    ],
    94: [
        {"name": "Build-It Academy", "capacity": 25, "schedule": "Full-time", "cost": "€1200", "funding": "BAMF eligible"},
        {"name": "Construction Skills Center", "capacity": 18, "schedule": "Part-time", "cost": "€800", "funding": "None"},
    ],
    70: [
        {"name": "Safe-Lift School", "capacity": 12, "schedule": "3-day course", "cost": "€450", "funding": "BAMF eligible"},
    ],
    53: [
        {"name": "Hotelier Institute", "capacity": 30, "schedule": "Mon-Wed, 6-9pm", "cost": "€650", "funding": "BAMF eligible"},
        {"name": "Gastro-Profi School", "capacity": 15, "schedule": "Weekends", "cost": "€900", "funding": "None"},
    ]
}

# This simulates a database of jobs for Stage 3
DUMMY_JOBS = {
    "Logistics": [
        {"title": "Warehouse Associate", "company": "Global Trade Inc.", "status": "Open"},
        {"title": "Logistics Coordinator", "company": "Speedy Deliveries", "status": "Open"},
    ],
    "Construction": [
        {"title": "Construction Worker", "company": "Urban Developers", "status": "Open"},
        {"title": "Site Assistant", "company": "BuildFast Corp.", "status": "Urgent"},
    ],
    "Hospitality": [
        {"title": "Hotel Receptionist", "company": "Grand Palace Hotel", "status": "Open"},
        {"title": "Restaurant Staff", "company": "The Golden Spoon", "status": "Open"},
    ]
}

# Mock data - In a real application, this would come from a database
COURSES = [
    {'id': 80, 'title': 'Logistics Expert', 'field': 'Logistics', 'score': 92, 'duration': '6 Months', 'enrolled': 125, 'skills': ['Inventory Management', 'Warehousing', 'Procurement', 'Global Logistics'], 'next_intake': '2024-09-01'},
    {'id': 5, 'title': 'Warehouse Logistics', 'field': 'Logistics', 'score': 88, 'duration': '8 Months', 'enrolled': 88, 'skills': ['Project Planning', 'Risk Management', 'Building Codes', 'Cost Estimation'], 'next_intake': '2024-10-15'},
    {'id': 94, 'title': 'Construction Basics', 'field': 'Construction', 'score': 85, 'duration': '4 Months', 'enrolled': 210, 'skills': ['Customer Service', 'Event Management', 'Hotel Operations', 'Marketing'], 'next_intake': '2024-08-20'},
    {'id': 70, 'title': 'Forklift Operator', 'field': 'Logistics', 'score': 82, 'duration': '5 Months', 'enrolled': 76, 'skills': ['TIG Welding', 'MIG Welding', 'Blueprint Reading', 'Safety Protocols'], 'next_intake': '2024-09-10'},
    {'id': 53, 'title': 'Hotel Management Intro', 'field': 'Hospitality', 'score': 79, 'duration': '3 Months', 'enrolled': 150, 'skills': ['Customs Law', 'Intl. Shipping', 'Documentation', 'Trade Agreements'], 'next_intake': '2024-11-01'},
]

PROVIDERS = {
    80: [
        {"name": "ZAV Institute", "capacity": 15, "schedule": "Mon-Fri, 9-5", "cost": "€500", "funding": "BAMF eligible"},
        {"name": "Logistics Academy", "capacity": 20, "schedule": "Weekends", "cost": "€700", "funding": "None"},
    ],
    5: [
        {"name": "Adult Education Center", "capacity": 10, "schedule": "Evenings", "cost": "€350", "funding": "BAMF eligible"},
    ],
    94: [
        {"name": "Build-It Academy", "capacity": 25, "schedule": "Full-time", "cost": "€1200", "funding": "BAMF eligible"},
        {"name": "Construction Skills Center", "capacity": 18, "schedule": "Part-time", "cost": "€800", "funding": "None"},
    ],
    70: [
        {"name": "Safe-Lift School", "capacity": 12, "schedule": "3-day course", "cost": "€450", "funding": "BAMF eligible"},
    ],
    53: [
        {"name": "Hotelier Institute", "capacity": 30, "schedule": "Mon-Wed, 6-9pm", "cost": "€650", "funding": "BAMF eligible"},
        {"name": "Gastro-Profi School", "capacity": 15, "schedule": "Weekends", "cost": "€900", "funding": "None"},
    ]
}

# Example user profile (replace with real user data as needed)
USER_PROFILE = {
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

# --- Routes ---

@app.route('/')
def dashboard():
    """Main dashboard showing the overall process."""
    return render_template('dashboard.html')

@app.route('/recommendations')
def recommendations():
    """Displays the top 10 course recommendations with real scoring."""
    courses = fetch_courses()
    ranked_courses = []
    for course in courses:
        score = compute_final_score(USER_PROFILE, course)
        course_copy = course.copy()
        course_copy['score'] = score
        ranked_courses.append(course_copy)
    ranked_courses.sort(key=lambda x: x['score'], reverse=True)
    top_courses = ranked_courses[:10]
    # Ensure every course has a 'skills' key for the template
    for course in top_courses:
        if 'skills' not in course:
            course['skills'] = course.get('tags', [])
    return render_template('recommendations.html', courses=top_courses)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    """
    Shows details for a selected course, including provider info (Stage 2)
    and related jobs (Stage 3).
    """
    course = next((c for c in COURSES if c['id'] == course_id), None)
    if not course:
        return "Course not found", 404
    providers = DUMMY_PROVIDERS.get(course_id, [])
    if not providers:
        providers = [{
            "name": "Generic Training Center",
            "capacity": 20,
            "schedule": "Flexible",
            "cost": "€500",
            "funding": "Available"
        }]
    jobs = DUMMY_JOBS.get(course['field'], [])
    if not jobs:
        jobs = [
            {"title": "General Associate", "company": "AnyCorp", "status": "Open", "location": "Remote", "type": "Full-time"},
            {"title": "Entry Level Position", "company": "Startup Hub", "status": "Open", "location": "On-site", "type": "Part-time"},
        ]
    return render_template('course_detail.html', course=course, providers=providers, jobs=jobs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)