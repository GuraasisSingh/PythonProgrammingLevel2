'''

Inner Join 
Show the names and ages of students enrolled in different courses.
SELECT table1.column1,table1.column2,table2.column1,....
FROM table1 
INNER JOIN table2
ON table1.matching_column = table2.matching_column;

Select Student_course.course_id, Student.name, Student.age from Student inner join student_course on student.roll_no=student_course.roll_no

'''