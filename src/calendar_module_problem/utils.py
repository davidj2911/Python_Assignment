from datetime import datetime
def cal_module(date_input):
    date_obj = datetime.strptime(date_input,"%d %m %Y")
    day = date_obj.weekday()
    days_of_the_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return days_of_the_week[day]
