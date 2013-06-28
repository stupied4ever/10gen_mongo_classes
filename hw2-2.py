import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

grades = connection.students.grades
homeworks = grades.find({'type': 'homework'})
sorted_grades = homeworks.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

itens_to_remove = []

student_id = -1
for grade in sorted_grades:
    if student_id != grade['student_id']:
        itens_to_remove.append(grade['_id'])
    student_id = grade['student_id']

for grade in itens_to_remove:
    grades.remove({'_id': grade})

