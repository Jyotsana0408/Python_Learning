student = {
    "stu1" :{
        "name" : "raj",
        "age" : 17,
        "marks" : 98
    },
    "stu2" :{
        "name" : "neha",
        "age" : 17,
        "marks" : 99
    }
}

print(student["stu1"]["name"])

for student_id, details in student.items():
    print(f"{student_id} : {details["name"]}, {details["age"]}, {details["marks"]}")