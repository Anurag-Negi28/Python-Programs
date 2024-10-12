java_course={"john","jack","jill","joe"}
python_course={"jake","john","eric","jill"}
print(python_course)
print("STUDENTS WHO OPTED JAVA COURSES ONLY")
s=java_course.difference(python_course)
print(s)
print("STUDENTS WHO OPTED PYTHON COURSES ONLY")

print(python_course.difference(java_course))
print("STUDENTS WHO OPTED both JAVA AND PYTHON COURSE")
print(python_course.intersection(java_course))
print("STUDENTS WHO OPTED EITHER JAVA OR PYTHON COURSES BUT NOT BOTH")
print(python_course.union(java_course)-python_course.intersection(java_course))
print("STUDENTS WHO OPTED EITHER JAVA OR PYTHON COURSE")
print(python_course.union(java_course))
