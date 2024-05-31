def percentage_cal(stu_marks, name):
    total = sum(stu_marks[name])
    #n = len(stu_marks[name])
    n = len(stu_marks)
    avg = format(total/n, '.2f')
    return avg
