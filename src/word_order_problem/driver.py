from src.word_order_problem.utils import *
result = (word_order(5, ['hi', 'hello', 'hi', 'welcome', 'thankyou']))
print("Number of distinct words =" ,result[0])
print("Number of occurances for those distinct words is :", result[1])