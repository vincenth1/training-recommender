import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db.db_reader import fetch_courses
from scoring.rule_score_function import compute_final_score
from .forms import UserIntakeForm
import json

app = Flask(__name__)
app.secret_key = 'dev-secret-key'

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

# --- Mock Coach Data ---
COACHES = [
    {
        "id": 1,
        "name": "Anna Müller",
        "photo": "/static/coaches/anna.jpg",
        "city": "Berlin",
        "languages": ["German", "English"],
        "meeting_types": ["in-person", "online"],
        "slots": [
            {"datetime": "2024-07-15 10:00", "type": "in-person", "city": "Berlin"},
            {"datetime": "2024-07-16 14:00", "type": "online"},
            {"datetime": "2024-07-17 09:00", "type": "in-person", "city": "Potsdam"},
        ],
        "description": "Specializes in career orientation and job application strategies."
    },
    {
        "id": 2,
        "name": "Omar Al-Farouq",
        "photo": "/static/coaches/omar.jpg",
        "city": "Hamburg",
        "languages": ["German", "Arabic", "English"],
        "meeting_types": ["in-person", "online"],
        "slots": [
            {"datetime": "2024-07-15 11:00", "type": "in-person", "city": "Hamburg"},
            {"datetime": "2024-07-16 15:00", "type": "online"},
            {"datetime": "2024-07-18 13:00", "type": "in-person", "city": "Bremen"},
        ],
        "description": "Experienced in supporting international professionals and documentation for job centers."
    },
    {
        "id": 3,
        "name": "Svitlana Ivanenko",
        "photo": "/static/coaches/svitlana.jpg",
        "city": "Leipzig",
        "languages": ["German", "Ukrainian", "Russian"],
        "meeting_types": ["online"],
        "slots": [
            {"datetime": "2024-07-15 16:00", "type": "online"},
            {"datetime": "2024-07-17 10:00", "type": "online"},
        ],
        "description": "Focus on integration, language support, and next steps for newcomers."
    },
    {
        "id": 4,
        "name": "Jonas Becker",
        "photo": "/static/coaches/jonas.jpg",
        "city": "Munich",
        "languages": ["German", "English"],
        "meeting_types": ["in-person"],
        "slots": [
            {"datetime": "2024-07-16 09:00", "type": "in-person", "city": "Munich"},
            {"datetime": "2024-07-18 11:00", "type": "in-person", "city": "Augsburg"},
        ],
        "description": "Helps with planning, documentation, and job center applications."
    }
]

# --- Routes ---

@app.route('/')
def dashboard():
    """Main dashboard showing the overall process."""
    return render_template('dashboard.html')

def form_data_to_scoring_profile(form_data):
    profile = {}
    # German language level: from foreign_languages or mother_tongue
    profile['german_level'] = next((fl['level'] for fl in form_data.get('foreign_languages', []) if fl.get('language') == 'german'), 'A1')
    # German language certificate
    profile['has_language_certificate'] = any(fl.get('certificate') == 'yes' and fl.get('language') == 'german' for fl in form_data.get('foreign_languages', []))
    # Education: highest degree (university), fallback to school diploma
    uni_degrees = [ud['degree'] for ud in form_data.get('university_degrees', []) if ud.get('degree') and ud['degree'] != 'none']
    school_degrees = [sd['diploma'] for sd in form_data.get('school_diplomas', []) if sd.get('diploma') and sd['diploma'] != 'none']
    profile['education'] = uni_degrees[0] if uni_degrees else (school_degrees[0] if school_degrees else 'none')
    # Work experience: count by industry
    work_exp = {}
    for w in form_data.get('work_experience', []):
        field = w.get('industry')
        if field and field != 'none':
            work_exp[field] = work_exp.get(field, 0) + 1
    profile['work_experience'] = work_exp
    # Desired job
    profile['desired_job'] = form_data.get('desired_profession', '')
    # Interests
    interest = form_data.get('interest', [])
    if isinstance(interest, list):
        profile['interest'] = ', '.join(interest)
    else:
        profile['interest'] = interest
    # Preferred learning mode
    preferred_learning = form_data.get('preferred_learning', [])
    if isinstance(preferred_learning, list) and preferred_learning:
        profile['preferred_learning_mode'] = preferred_learning[0]
    else:
        profile['preferred_learning_mode'] = preferred_learning if preferred_learning else 'online'
    # Childcare needs
    profile['has_childcare_needs'] = any(child.get('childcare_needed') == 'yes' for child in form_data.get('children', []))
    # Location (use city part of postal_city, fallback to 'berlin')
    pc = form_data.get('postal_city', 'berlin')
    profile['location'] = pc.split()[-1].lower() if pc else 'berlin'
    # Can relocate
    profile['can_relocate'] = form_data.get('willing_to_relocate', 'no') == 'yes'
    # Disability (not in form, default False)
    profile['has_disability'] = False
    # Computer skills
    oq = form_data.get('other_qualifications', [])
    if isinstance(oq, str): oq = [oq]
    profile['computer_skills'] = 'it_basics' in oq
    # Driving license
    profile['driving_license'] = bool(form_data.get('drivers_licenses'))
    # Skills (collect from diplomas, degrees, work, etc. - here just a placeholder)
    profile['skills'] = []
    return profile

@app.route('/recommendations')
def recommendations():
    """Displays the top 4 course recommendations with real scoring."""
    user_profile = USER_PROFILE
    if 'user_profile' in session:
        form_data = session['user_profile']
        user_profile = form_data_to_scoring_profile(form_data)
        print('USING SUBMITTED USER PROFILE FOR SCORING:', user_profile)
        session.pop('user_profile')  # Clear after use
    courses = fetch_courses()
    ranked_courses = []
    for course in courses:
        score = compute_final_score(user_profile, course)
        course_copy = course.copy()
        course_copy['score'] = score
        ranked_courses.append(course_copy)
    ranked_courses.sort(key=lambda x: x['score'], reverse=True)
    top_courses = ranked_courses[:4]  # Only show top 4
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

@app.route('/book-coach')
def book_coach():
    """
    Show available coaches and allow the user to book a meeting.
    """
    user_city = None
    if 'user_profile' in session:
        form_data = session['user_profile']
        pc = form_data.get('postal_city', '')
        if pc:
            user_city = pc.split()[-1]
    return render_template('book_coach.html', coaches=COACHES, user_city=user_city)

@app.route('/user-form', methods=['GET', 'POST'])
def user_form():
    with open('recommender_app/form_translations.json', encoding='utf-8') as f:
        translations = json.load(f)
    form = UserIntakeForm()
    if form.validate_on_submit():
        # Fetch submitted data
        user_data = form.data
        print('USER FORM SUBMISSION:', user_data)  # For debugging
        session['user_profile'] = user_data
        return redirect(url_for('book_coach'))
    else:
        if form.is_submitted():
            print('FORM ERRORS:', form.errors)
    return render_template('user_form.html', form=form, translations=translations)

@app.route('/book-slot', methods=['POST'])
def book_slot():
    data = request.json
    coach_id = data.get('coach_id')
    slot_datetime = data.get('slot_datetime')
    # Here you would save the booking to a database or send an email, etc.
    # For now, just return a success message.
    return jsonify({
        "success": True,
        "message": "Your meeting has been booked!",
        "coach_id": coach_id,
        "slot_datetime": slot_datetime
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)