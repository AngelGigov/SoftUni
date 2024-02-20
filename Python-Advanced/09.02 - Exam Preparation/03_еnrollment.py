def gather_credits(credits_needed, *course_info):
    total_credits = credits_needed
    enrolled_credits = 0
    courses = []

    for course in course_info:
        course_name, course_credits = course

        if enrolled_credits + course_credits <= credits_needed:
            courses.append(course_name)
            enrolled_credits += course_credits

    if enrolled_credits == credits_needed:
        sorted_courses = sorted(courses)
        return f"Enrollment finished! Maximum credits: {enrolled_credits}.\nCourses: {', '.join(sorted_courses)}"
    else:
        credits_shortage = credits_needed - enrolled_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."




print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
