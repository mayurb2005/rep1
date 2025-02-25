
import numpy as np
week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = 1
big_spending = week_spendings[0]
index = np.argmax(week_spendings)
days = {1:'mon', 2'tue', 3:'wed', 4:'thus', 5'fri', 6:'sat', 7:'sun'}
print(big_spending, days[index])

'''
for i in range(len(week_spendings)):
	if week_spendings[i] > big_spending:
		big_spending = week_spendings[i]
		index = i
'''
expenses = np.array([20, 60, 5, 80, 45, 90])
modified_expenses = np.where(expenses < 50, 0, expenses)
print(modified_expenses)
random_data = np.random.rand(3, 4) 