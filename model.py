def recommend_career(skills):
    skills = [s.strip().lower() for s in skills]

    data_skills = {"python", "sql", "excel", "statistics"}
    web_skills = {"html", "css", "javascript"}

    score_data = len(set(skills) & data_skills)
    score_web = len(set(skills) & web_skills)

    if score_data > score_web:
        return "Data Analyst"
    elif score_web > score_data:
        return "Web Developer"
    else:
        return "Software Engineer"
