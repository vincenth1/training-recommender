DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  title TEXT,
  locations TEXT[],
  education_required TEXT[],
  is_online BOOLEAN,
  min_language_level TEXT,
  required_field TEXT,
  tags TEXT[],
  delivery_mode TEXT,
  supports_childcare BOOLEAN,
  is_physical_friendly BOOLEAN
);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 1 in Hospitality', '{Hamburg}', '{Master}', false, 'A2', 'hospitality', '{service,hotel}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 2 in Hospitality', '{Leipzig,Hamburg}', '{Bachelor,Master}', false, 'C1', 'hospitality', '{service,hotel}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 3 in It', '{Munich,Leipzig}', '{Bachelor}', true, 'A2', 'IT', '{programming,web}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 4 in Healthcare', '{Munich,Dresden,Hamburg}', '{none}', true, 'B2', 'healthcare', '{elderly,care}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 5 in Logistics', '{Hamburg,Dresden}', '{Bachelor,Master}', false, 'A1', 'logistics', '{forklift,inventory}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 6 in Construction', '{Berlin,Munich,Leipzig}', '{Bachelor}', true, 'C1', 'construction', '{carpentry,bricklaying}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 7 in Logistics', '{Hamburg}', '{highschool}', true, 'A2', 'logistics', '{warehouse,inventory}', 'hybrid', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 8 in It', '{Dresden,Leipzig}', '{none,highschool}', true, 'B2', 'IT', '{python,web}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 9 in Healthcare', '{Leipzig,Dresden,Berlin}', '{none,highschool}', false, 'C2', 'healthcare', '{care,nursing}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 10 in Hospitality', '{Berlin,Leipzig}', '{Master}', true, 'B1', 'hospitality', '{hotel,service}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 11 in Healthcare', '{Berlin,Hamburg}', '{highschool}', false, 'C2', 'healthcare', '{elderly,nursing}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 12 in Construction', '{Munich,Leipzig,Hamburg}', '{none}', true, 'A2', 'construction', '{bricklaying,tools}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 13 in It', '{Munich,Dresden,Berlin}', '{Bachelor}', false, 'C1', 'IT', '{programming,python}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 14 in Construction', '{Dresden,Berlin}', '{highschool}', false, 'B1', 'construction', '{bricklaying,carpentry}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 15 in Healthcare', '{Berlin,Munich}', '{Master}', false, 'C2', 'healthcare', '{care,nursing}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 16 in Hospitality', '{Leipzig}', '{Bachelor,Master}', true, 'A2', 'hospitality', '{kitchen,service}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 17 in Logistics', '{Leipzig,Hamburg,Munich}', '{Bachelor,Master}', true, 'B2', 'logistics', '{forklift,warehouse}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 18 in It', '{Berlin,Dresden,Munich}', '{none,highschool}', true, 'B2', 'IT', '{python,web}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 19 in It', '{Leipzig,Hamburg}', '{Master}', true, 'A2', 'IT', '{programming,web}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 20 in It', '{Dresden}', '{Bachelor}', false, 'A1', 'IT', '{web,programming}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 21 in Construction', '{Hamburg}', '{Bachelor,Master}', false, 'A2', 'construction', '{carpentry,tools}', 'online', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 22 in Construction', '{Leipzig,Dresden,Berlin}', '{Master}', true, 'C1', 'construction', '{tools,carpentry}', 'offline', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 23 in Logistics', '{Hamburg}', '{Bachelor,Master}', false, 'C2', 'logistics', '{warehouse,forklift}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 24 in Logistics', '{Munich,Hamburg,Leipzig}', '{Bachelor,Master}', true, 'C2', 'logistics', '{warehouse,inventory}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 25 in Healthcare', '{Berlin,Hamburg,Leipzig}', '{highschool}', true, 'C2', 'healthcare', '{care,nursing}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 26 in It', '{Leipzig,Munich,Hamburg}', '{Master}', true, 'C1', 'IT', '{python,programming}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 27 in Logistics', '{Munich,Hamburg}', '{highschool}', true, 'A2', 'logistics', '{inventory,forklift}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 28 in Construction', '{Berlin,Munich}', '{highschool}', true, 'C1', 'construction', '{tools,carpentry}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 29 in Construction', '{Berlin,Hamburg}', '{Bachelor}', false, 'A2', 'construction', '{bricklaying,carpentry}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 30 in Hospitality', '{Leipzig,Munich}', '{Bachelor,Master}', true, 'C1', 'hospitality', '{service,hotel}', 'hybrid', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 31 in Logistics', '{Munich,Hamburg,Dresden}', '{none}', true, 'C2', 'logistics', '{forklift,inventory}', 'offline', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 32 in Hospitality', '{Munich}', '{none,highschool}', true, 'C2', 'hospitality', '{service,kitchen}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 33 in Healthcare', '{Leipzig,Berlin}', '{none}', true, 'B2', 'healthcare', '{elderly,nursing}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 34 in Hospitality', '{Berlin,Leipzig}', '{none,highschool}', true, 'B2', 'hospitality', '{service,kitchen}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 35 in Healthcare', '{Berlin,Hamburg,Leipzig}', '{highschool}', true, 'A2', 'healthcare', '{care,elderly}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 36 in Construction', '{Leipzig}', '{Bachelor,Master}', true, 'C1', 'construction', '{carpentry,tools}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 37 in It', '{Leipzig}', '{Bachelor,Master}', false, 'B2', 'IT', '{programming,web}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 38 in It', '{Hamburg}', '{none,highschool}', true, 'B2', 'IT', '{web,python}', 'offline', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 39 in It', '{Hamburg,Munich,Berlin}', '{highschool}', false, 'B2', 'IT', '{programming,web}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 40 in It', '{Munich,Hamburg,Berlin}', '{Bachelor}', false, 'B1', 'IT', '{web,python}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 41 in Hospitality', '{Berlin,Leipzig,Dresden}', '{Bachelor}', false, 'B2', 'hospitality', '{service,kitchen}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 42 in Hospitality', '{Munich,Dresden,Leipzig}', '{Bachelor,Master}', true, 'C1', 'hospitality', '{hotel,service}', 'hybrid', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 43 in Healthcare', '{Munich}', '{highschool}', false, 'B2', 'healthcare', '{elderly,nursing}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 44 in Construction', '{Hamburg,Dresden}', '{Master}', false, 'B2', 'construction', '{bricklaying,tools}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 45 in It', '{Leipzig,Munich}', '{highschool}', false, 'C1', 'IT', '{programming,python}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 46 in It', '{Berlin,Munich,Hamburg}', '{highschool}', false, 'A1', 'IT', '{python,web}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 47 in Construction', '{Munich,Hamburg}', '{highschool}', false, 'A2', 'construction', '{bricklaying,carpentry}', 'offline', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 48 in Healthcare', '{Berlin}', '{Bachelor}', true, 'C1', 'healthcare', '{elderly,care}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 49 in It', '{Berlin,Munich,Hamburg}', '{Master}', true, 'B2', 'IT', '{web,python}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 50 in Logistics', '{Berlin,Leipzig}', '{Bachelor}', true, 'B1', 'logistics', '{inventory,forklift}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 51 in It', '{Berlin}', '{none,highschool}', true, 'A2', 'IT', '{web,python}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 52 in It', '{Hamburg}', '{none}', true, 'A2', 'IT', '{web,programming}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 53 in Hospitality', '{Hamburg,Leipzig,Munich}', '{none,highschool}', false, 'A1', 'hospitality', '{service,kitchen}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 54 in Construction', '{Berlin,Dresden}', '{none}', true, 'A1', 'construction', '{bricklaying,carpentry}', 'online', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 55 in Construction', '{Dresden}', '{Bachelor}', true, 'C1', 'construction', '{carpentry,tools}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 56 in It', '{Leipzig}', '{Bachelor,Master}', true, 'A2', 'IT', '{programming,web}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 57 in Healthcare', '{Munich,Leipzig,Hamburg}', '{Bachelor}', true, 'A2', 'healthcare', '{care,nursing}', 'hybrid', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 58 in It', '{Berlin,Munich}', '{none,highschool}', false, 'C2', 'IT', '{web,python}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 59 in It', '{Hamburg}', '{none,highschool}', true, 'C2', 'IT', '{python,programming}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 60 in Logistics', '{Munich}', '{highschool}', true, 'C2', 'logistics', '{warehouse,inventory}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 61 in Logistics', '{Hamburg,Leipzig,Berlin}', '{Master}', true, 'B2', 'logistics', '{inventory,warehouse}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 62 in Healthcare', '{Munich,Dresden}', '{none}', true, 'B1', 'healthcare', '{nursing,elderly}', 'online', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 63 in Construction', '{Berlin,Munich,Dresden}', '{Bachelor}', false, 'A1', 'construction', '{bricklaying,carpentry}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 64 in Construction', '{Munich}', '{Bachelor,Master}', false, 'B1', 'construction', '{bricklaying,carpentry}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 65 in Healthcare', '{Leipzig}', '{highschool}', false, 'A2', 'healthcare', '{care,elderly}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 66 in Healthcare', '{Munich}', '{highschool}', true, 'A1', 'healthcare', '{care,elderly}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 67 in It', '{Dresden}', '{none}', true, 'B2', 'IT', '{web,python}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 68 in It', '{Berlin,Hamburg}', '{none,highschool}', false, 'B1', 'IT', '{web,programming}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 69 in Construction', '{Hamburg}', '{Bachelor}', true, 'A1', 'construction', '{bricklaying,carpentry}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 70 in Logistics', '{Dresden}', '{none}', true, 'C1', 'logistics', '{forklift,inventory}', 'offline', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 71 in Logistics', '{Leipzig}', '{Master}', true, 'C1', 'logistics', '{warehouse,forklift}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 72 in Construction', '{Dresden}', '{Bachelor,Master}', false, 'C2', 'construction', '{bricklaying,carpentry}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 73 in Logistics', '{Munich}', '{highschool}', true, 'A2', 'logistics', '{warehouse,forklift}', 'online', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 74 in Logistics', '{Leipzig}', '{Bachelor,Master}', true, 'C1', 'logistics', '{warehouse,forklift}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 75 in Construction', '{Hamburg,Leipzig}', '{highschool}', false, 'A1', 'construction', '{tools,carpentry}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 76 in It', '{Munich,Dresden}', '{Master}', false, 'C2', 'IT', '{python,web}', 'offline', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 77 in Hospitality', '{Hamburg,Berlin}', '{none,highschool}', true, 'B2', 'hospitality', '{hotel,service}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 78 in Hospitality', '{Leipzig,Berlin,Dresden}', '{none}', false, 'C2', 'hospitality', '{service,kitchen}', 'offline', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 79 in It', '{Munich}', '{Master}', true, 'A1', 'IT', '{programming,web}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 80 in Logistics', '{Leipzig,Hamburg}', '{Bachelor,Master}', false, 'A1', 'logistics', '{inventory,forklift}', 'online', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 81 in Construction', '{Dresden,Hamburg,Munich}', '{highschool}', false, 'A1', 'construction', '{carpentry,tools}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 82 in Construction', '{Hamburg,Leipzig,Dresden}', '{Bachelor,Master}', true, 'A1', 'construction', '{tools,carpentry}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 83 in Construction', '{Munich,Berlin}', '{Bachelor,Master}', true, 'B2', 'construction', '{carpentry,tools}', 'hybrid', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 84 in Hospitality', '{Munich,Dresden,Berlin}', '{Bachelor}', false, 'B1', 'hospitality', '{hotel,service}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 85 in It', '{Leipzig,Munich,Hamburg}', '{Bachelor}', false, 'C1', 'IT', '{programming,web}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 86 in It', '{Munich}', '{Bachelor,Master}', true, 'C1', 'IT', '{web,python}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 87 in Hospitality', '{Munich,Leipzig,Berlin}', '{none,highschool}', false, 'A1', 'hospitality', '{hotel,service}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 88 in Logistics', '{Berlin,Munich,Hamburg}', '{Master}', false, 'B2', 'logistics', '{warehouse,forklift}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 89 in Healthcare', '{Hamburg,Leipzig,Berlin}', '{highschool}', false, 'C2', 'healthcare', '{elderly,nursing}', 'hybrid', true, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 90 in Construction', '{Dresden,Berlin}', '{Bachelor}', false, 'C1', 'construction', '{carpentry,bricklaying}', 'hybrid', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 91 in Healthcare', '{Berlin,Hamburg,Munich}', '{Bachelor}', true, 'B2', 'healthcare', '{nursing,elderly}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 92 in It', '{Munich,Leipzig}', '{none,highschool}', true, 'C2', 'IT', '{python,programming}', 'offline', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 93 in It', '{Hamburg,Dresden,Leipzig}', '{highschool}', false, 'C1', 'IT', '{programming,web}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 94 in Construction', '{Hamburg,Berlin}', '{none,highschool}', true, 'A1', 'construction', '{carpentry,bricklaying}', 'online', false, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 95 in It', '{Munich,Dresden}', '{Master}', false, 'A1', 'IT', '{programming,python}', 'hybrid', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 96 in Healthcare', '{Berlin}', '{Bachelor}', false, 'A1', 'healthcare', '{nursing,elderly}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 97 in It', '{Berlin}', '{Master}', true, 'B1', 'IT', '{web,python}', 'online', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 98 in Construction', '{Berlin,Dresden,Leipzig}', '{Bachelor,Master}', false, 'B1', 'construction', '{tools,bricklaying}', 'offline', false, false);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 99 in Construction', '{Berlin,Munich}', '{highschool}', false, 'B1', 'construction', '{tools,bricklaying}', 'hybrid', true, true);
INSERT INTO courses (title, locations, education_required, is_online, min_language_level, required_field, tags, delivery_mode, supports_childcare, is_physical_friendly) VALUES ('Course 100 in It', '{Munich,Dresden,Hamburg}', '{none}', true, 'C1', 'IT', '{web,programming}', 'offline', false, true);

-- Berufsspezifische Skills
CREATE TABLE job_skills (
  job_type TEXT,
  skill TEXT
);

-- Regionale Nachfrage
CREATE TABLE regional_demand (
  region TEXT,
  job_type TEXT,
  demand_index INTEGER
);

-- Bildungsträger
CREATE TABLE training_providers (
  provider_id SERIAL PRIMARY KEY,
  name TEXT,
  location TEXT,
  contact TEXT
);

-- Bildungsmaßnahmen
CREATE TABLE training_courses (
  course_id SERIAL PRIMARY KEY,
  provider_id INTEGER REFERENCES training_providers(provider_id),
  job_type TEXT,
  title TEXT,
  delivery_mode TEXT,
  min_language_level TEXT,
  education_required TEXT[],
  supports_childcare BOOLEAN,
  is_physical_friendly BOOLEAN,
  locations TEXT[]
);

-- Unternehmen mit Jobangeboten
CREATE TABLE employer_opportunities (
  employer_id SERIAL PRIMARY KEY,
  name TEXT,
  job_type TEXT,
  region TEXT,
  start_date DATE,
  notes TEXT
);

-- Teilnehmer-Statusverfolgung
CREATE TABLE participant_progress (
  user_id INTEGER,
  course_id INTEGER,
  certificate_issued BOOLEAN,
  expected_completion DATE,
  job_matched BOOLEAN
);