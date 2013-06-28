import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

grades = connection.students.grades
bigger_grades = grades.find({'score': {'$gte': 65}})

# lowest exam score above 65
lowest = bigger_grades.sort('score', pymongo.ASCENDING).limit(1)[0]

print(lowest['student_id'])
