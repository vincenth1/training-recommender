
import psycopg2

def fetch_courses():
    try:
        conn = psycopg2.connect(
            database="courses_db3",
            user="vincent",
            password="1",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT id, title, locations, education_required, is_online, min_language_level, delivery_mode, supports_childcare, required_field, tags, is_physical_friendly FROM courses")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        courses = []
        for row in rows:
            courses.append({
                "id": row[0],
                "title": row[1],
                "locations": row[2],
                "education_required": row[3],
                "is_online": row[4],
                "min_language_level": row[5],
                "delivery_mode": row[6],
                "supports_childcare": row[7],
                "required_field": row[8],
                "tags": row[9],
                "is_physical_friendly": row[10]
            })
        return courses

    except Exception as e:
        print("❌ SQL 查询失败:", e)
        return []
