student={"name":"Khushi",
         "age":20,
         "University":"SIT"}

print(type(student))
print(student)
student["branch"]="CSE"
print(student)
print(student.keys())
for i in student.keys():
    print(i,student[i])