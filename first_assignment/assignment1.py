students =[
{"name":"Lara","age":23,"track":"AI","hours_studied":40,"scores":[85,90,78]},
{"name":"Omar","age":31,"track":"Data","hours_studied":12,"scores":[60,55,70]},
{"name":"Rim","age":27,"track":"AI","hours_studied":55,"scores":[95,88,92]},
{"name":"Karim","age":19,"track":"Web","hours_studied":8,"scores":[50,65,40]},
{"name":"Nour","age":25,"track":"AI","hours_studied":30,"scores":[75,80,85]},
{"name":"Sami","age":35,"track":"Data","hours_studied":48,"scores":[88,91,79]},]

#Part 1: Exploring the Data (accessing nested structures)

#print the name of the first student in the list
print(f"First student: {students[0]['name']}")

#print the name of the last student in the list
print(f"Last student: {students[-1]['name']}")

#print Rim's scores
print(f"Rim's scores: {students[2]['scores']}")

#Loop through all students and print one line per student: `Lara is 23 years old and studies AI`.
for student in students:
    print(f"{student['name']} is {student['age']} years old and studies {student['track']}.")

#Part 2: Filtering (the most common data operation)

#a loop that contains only students who study AI and prints how many are they
ai_students = [student for student in students if student['track'] == 'AI']
print(f"Number of students studying AI: {len(ai_students)}")
for student in ai_students:
    print(f"{student['name']} is studying AI.")

#same thing but with list comprehension
ai_students_count = len([student for student in students if student['track'] == 'AI'])
print(f"Number of students studying AI (using list comprehension): {ai_students_count}")

#build a list of students who have studied more than 30 hours and print their names
students_studied_more_than_30_hours = [student for student in students if student['hours_studied'] > 30]
print("Students who have studied more than 30 hours:")
for student in students_studied_more_than_30_hours:
    print(f"{student['name']}")

#Build a list of students who are older than 24 AND in the AI track. (Combining conditions is everyday work.)
combined_filter = [student for student in students if student['age'] > 24 and student['track'] == 'AI']
print("Students who are older than 24 and studying AI:")
for student in combined_filter:
    print(f"{student['name']}")

#Part 3: Aggregating (turning many records into one number)

#calculate the average age of all students and print it
average_age = sum(student['age'] for student in students) / len(students)
print(f"Average age of all students: {average_age}")

#calculate the total hours studied across the whole cohort and print it
total_hours_studied = sum(student['hours_studied'] for student in students)
print(f"Total hours studied across the whole cohort: {total_hours_studied}")

#find the student who studied the most hours and print their names
max_hours_studied = max(student['hours_studied'] for student in students)
top_student = [student for student in students if student['hours_studied'] == max_hours_studied]
print("Student who studied the most hours:")
for student in top_student:
    print(f"{student['name']}")

#For each student, their final grade is the average of their `scores`. Print each student's name and their final grade, rounded to 1 decimal.
for student in students:
    final_grade = round(sum(student['scores']) / len(student['scores']), 1)
    print(f"{student['name']}: {final_grade}")

#Part 4: Transforming (reshaping data into something new)

#Write a list comprehension that produces a new list of dictionaries, each with only two keys: `name` and `average_score`. This is exactly how you'd prepare data for a report or a model.
transformed_data = [{"name": student['name'], "average_score": round(sum(student['scores']) / len(student['scores']), 1)} for student in students]
print("Transformed data (name and average score):")
for student in transformed_data:
    print(f"{student['name']}: {student['average_score']}")

# Build a dictionary that maps each track to the number of students in it, like `{"AI": 3, "Data": 2, "Web": 1}`.
track_counts = {}
for student in students:
    track = student['track']
    track_counts[track] = track_counts.get(track, 0) + 1
print("Number of students in each track:")
for track, count in track_counts.items():
    print(f"{track}: {count}")

#Create a set of all the unique tracks in the dataset. Explain in a comment why a set is the right tool here instead of a list.
unique_tracks = {student['track'] for student in students}
print("Unique tracks in the dataset:")
for track in unique_tracks:
    print(f"{track}")

# A set is the right tool here because it automatically ensures that only unique values are stored, which is exactly what we want when identifying distinct tracks in the dataset.

#Part 5 : Reusable Functions

#Write a function `filter_by_track(students, track)` that returns all students in a given track. Test it with `"AI"` and `"Data"`.

def filter_by_track(students, track):
    return [student for student in students if student['track'] == track]

# Test the function
ai_students = filter_by_track(students, "AI")
data_students = filter_by_track(students, "Data")

print("Students in the AI track:")
for student in ai_students:
    print(f"{student['name']}")

print("Students in the Data track:")
for student in data_students:
    print(f"{student['name']}")

#Write a function `average_score(student)` that takes one student dictionary and returns their average score.
def average_score(student):
    return round(sum(student['scores']) / len(student['scores']), 1)

#Write a function `top_student(students)` that returns the name of the student with the highest average score. (Use the function from #16 inside it — functions calling functions.)
def top_student(students):
    top_student = max(students, key=average_score)
    return top_student['name']

#Write a function `summary(students)` that returns a dictionary with three keys: `total_students`, `average_age`, and `tracks` (the set of unique tracks). One function, full overview.
def summary(students):
    total_students = len(students)
    average_age = sum(student['age'] for student in students) / total_students
    tracks = {student['track'] for student in students}
    return {
        "total_students": total_students,
        "average_age": average_age,
        "tracks": tracks
    }

#Write a function `report(students, min_hours)` that:
#    - filters the students who studied at least `min_hours`,
#    - for each one calculates their average score,
#    - returns a list of dictionaries with `name` and `average_score`,
#    - sorted from highest score to lowest.

def report(students, min_hours):
    filtered_students = [student for student in students if student['hours_studied'] >= min_hours]
    report_data = [{"name": student['name'], "average_score": average_score(student)} for student in filtered_students]
    sorted_report = sorted(report_data, key=lambda x: x['average_score'], reverse=True)
    return sorted_report

#Test the report function
min_hours = 30
report_result = report(students, min_hours)
print(f"Report of students who studied at least {min_hours} hours:")
for student in report_result:
    print(f"{student['name']}: {student['average_score']}")

