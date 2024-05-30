from collections import namedtuple

def avg_namedTuple(students_data):
    N = int(students_data[0])
    columns = students_data[1].split()
    Student = namedtuple('Student', columns)
    total_marks = sum(int(Student(*x.split()).MARKS) for x in students_data[2:])
    avg = format (total_marks / N, '.2f')
    return avg