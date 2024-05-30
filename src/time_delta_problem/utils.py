from datetime import datetime

def time_delta(t1,  t2):
    time_str = "%a %d %b %Y %H:%M:%S %z"
    obj1 = datetime.strptime(t1, time_str)
    obj2 = datetime.strptime(t2, time_str)

    timedelta = obj1 - obj2 if obj1 >= obj2 else obj2 - obj1

    return str(int(timedelta.total_seconds()))