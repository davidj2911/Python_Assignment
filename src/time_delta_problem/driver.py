from src.time_delta_problem.utils import *
result1 = time_delta("Sun 10 May 2015 13:54:36 -0700","Sun 10 May 2015 13:54:36 -0000")
result2 = time_delta("Sat 02 May 2015 19:54:36 +0530","Fri 01 May 2015 13:54:36 -0000")
print("The first time difference is :", result1, "seconds",)
print("The second time difference is :", result2, "seconds",)