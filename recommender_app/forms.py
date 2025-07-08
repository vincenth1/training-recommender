from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FieldList, FormField, RadioField, BooleanField, IntegerField, EmailField, TelField
from wtforms.validators import DataRequired, Optional, Email

# Repeating section for children
class ChildForm(FlaskForm):
    age = SelectField('child_age', choices=[(str(i), str(i)) for i in range(1, 19)], validators=[DataRequired()])
    childcare_needed = RadioField('childcare_needed', choices=[('yes', 'Ja'), ('no', 'Nein')], validators=[DataRequired()])
    class Meta:
        csrf = False

# Repeating section for foreign languages
class ForeignLanguageForm(FlaskForm):
    language = SelectField('foreign_language', choices=[('ukrainian', 'Ukrainisch'), ('german', 'Deutsch'), ('polish', 'Polnisch'), ('turkish', 'Türkisch'), ('arabic', 'Arabisch'), ('afghan', 'Afghanisch'), ('russian', 'Russisch'), ('kurdish', 'Kurdisch'), ('somali', 'Somali')], validators=[DataRequired()])
    level = SelectField('language_level', choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], validators=[DataRequired()])
    certificate = RadioField('language_certificate', choices=[('yes', 'Ja'), ('no', 'Nein')], validators=[DataRequired()])
    class Meta:
        csrf = False

# Repeating section for school diplomas
class SchoolDiplomaForm(FlaskForm):
    diploma = SelectField('school_diploma', choices=[('none', 'Kein Abschluss'), ('hauptschule', 'Hauptschulabschluss (Germany)'), ('realschule', 'Realschulabschluss (Germany)'), ('abitur', 'Abitur (Germany)'), ('ua_9', 'Ukrainischer Schulabschluss (9. Klasse)'), ('ua_11', 'Ukrainischer Schulabschluss (11. Klasse)'), ('ua_junior', 'Dyplom Molodshoho Spetsialista')], validators=[DataRequired()])
    date = DateField('school_diploma_date', validators=[Optional()])
    country = SelectField('school_diploma_country', choices=[('de', 'Deutschland'), ('ua', 'Ukraine'), ('pl', 'Polen'), ('tr', 'Türkei'), ('other', 'Andere')], validators=[DataRequired()])
    class Meta:
        csrf = False

# Repeating section for university degrees
class UniversityDegreeForm(FlaskForm):
    degree = SelectField('university_degree', choices=[('none', 'Kein Abschluss'), ('bachelor', 'Bachelor'), ('master', 'Master'), ('diplom', 'Diplom'), ('phd', 'PhD (Doktor)')], validators=[DataRequired()])
    field = SelectField('university_field', choices=[('none', 'Kein Studium'), ('engineering', 'Ingenieurwissenschaften'), ('it', 'Informatik/IT'), ('medicine', 'Medizin/Gesundheit'), ('business', 'Wirtschaft'), ('humanities', 'Geisteswissenschaften'), ('science', 'Naturwissenschaften'), ('teaching', 'Lehramt'), ('art', 'Kunst/Design'), ('other', 'Andere')], validators=[DataRequired()])
    date_from = DateField('university_from', validators=[Optional()])
    date_to = DateField('university_to', validators=[Optional()])
    country = SelectField('university_country', choices=[('de', 'Deutschland'), ('ua', 'Ukraine'), ('pl', 'Polen'), ('tr', 'Türkei'), ('other', 'Andere')], validators=[DataRequired()])
    class Meta:
        csrf = False

# Repeating section for work experience
class WorkExperienceForm(FlaskForm):
    industry = SelectField('work_industry', choices=[('health', 'Gesundheit'), ('tech', 'Technik'), ('education', 'Bildung'), ('gastronomy', 'Gastronomie'), ('retail', 'Einzelhandel'), ('construction', 'Bauwesen'), ('other', 'Andere'), ('none', 'Keine')], validators=[DataRequired()])
    date_from = DateField('work_from', validators=[Optional()])
    date_to = DateField('work_to', validators=[Optional()])
    class Meta:
        csrf = False

# Repeating section for driver's license
class DriversLicenseForm(FlaskForm):
    license_class = SelectField('license_class', choices=[('AM', 'AM (A1)'), ('A1', 'A1'), ('A2', 'A2 (A)'), ('B', 'B'), ('BE', 'BE'), ('C1', 'C1'), ('C', 'C'), ('D', 'D')], validators=[Optional()])
    date = DateField('license_date', validators=[Optional()])
    class Meta:
        csrf = False

class UserIntakeForm(FlaskForm):
    # 1. Personal Information
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    date_of_birth = DateField('date_of_birth', validators=[DataRequired()])
    gender = SelectField('gender', choices=[('male', 'Männlich'), ('female', 'Weiblich'), ('diverse', 'Divers')], validators=[DataRequired()])
    nationality = SelectField('nationality', choices=[('ukrainian', 'Ukrainisch'), ('german', 'Deutsch'), ('polish', 'Polnisch'), ('turkish', 'Türkisch'), ('arabic', 'Arabisch'), ('afghan', 'Afghanisch'), ('russian', 'Russisch'), ('kurdish', 'Kurdisch'), ('somali', 'Somali')], validators=[DataRequired()])
    since_in_germany = DateField('since_in_germany', validators=[DataRequired()])
    residence_permit = SelectField('residence_permit', choices=[('aufenthaltserlaubnis', 'Aufenthaltserlaubnis'), ('blaue_karte', 'Blaue Karte EU'), ('niederlassung', 'Niederlassungserlaubnis'), ('daueraufenthalt', 'Daueraufenthalt-EU'), ('visum', 'Visum'), ('studierende', 'Aufenthaltserlaubnis für Studierende'), ('asyl', 'Asylberechtigung'), ('duldung', 'Duldung')], validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    postal_city = StringField('postal_city', validators=[DataRequired()])
    phone = TelField('phone', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])

    # 2. Children & Childcare
    children = FieldList(FormField(ChildForm), min_entries=0, max_entries=10)

    # 3. Health Restrictions (matrix handled in template)
    # 4. Language & Education
    mother_tongue = SelectField('mother_tongue', choices=[('ukrainian', 'Ukrainisch'), ('german', 'Deutsch'), ('polish', 'Polnisch'), ('turkish', 'Türkisch'), ('arabic', 'Arabisch'), ('afghan', 'Afghanisch'), ('russian', 'Russisch'), ('kurdish', 'Kurdisch'), ('somali', 'Somali')], validators=[DataRequired()])
    foreign_languages = FieldList(FormField(ForeignLanguageForm), min_entries=0, max_entries=5)
    school_diplomas = FieldList(FormField(SchoolDiplomaForm), min_entries=0, max_entries=5)
    university_degrees = FieldList(FormField(UniversityDegreeForm), min_entries=0, max_entries=5)

    # 5. Work Experience
    work_experience = FieldList(FormField(WorkExperienceForm), min_entries=0, max_entries=5)
    drivers_licenses = FieldList(FormField(DriversLicenseForm), min_entries=0, max_entries=5)
    desired_profession = SelectField('desired_profession', choices=[('nurse', 'Pflegekraft'), ('it', 'IT-Spezialist'), ('teacher', 'Lehrer'), ('craftsman', 'Handwerker'), ('sales', 'Verkäufer'), ('engineer', 'Ingenieur'), ('chef', 'Koch'), ('other', 'Andere'), ('none', 'Keine Präferenz')], validators=[Optional()])
    desired_working_hours = SelectField('desired_working_hours', choices=[('full', 'Vollzeit'), ('part', 'Teilzeit')], validators=[Optional()])
    willing_to_relocate = RadioField('willing_to_relocate', choices=[('yes', 'Ja'), ('no', 'Nein')], validators=[DataRequired()])

    # 6. Support Needs & Learning Preferences (matrix handled in template)
    # Leistungsbezug, preferred learning, interests, other qualifications handled in template
    submit = SubmitField('submit') 