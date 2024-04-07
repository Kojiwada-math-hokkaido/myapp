import numpy as np

def f(x, alpha):
	y = 1 - alpha*x*x
	return y

def coupled_f(x_list, alpha, e):
	total = 0
	y_list = []
	num = len(x_list)

	for n in range(num):
		total += f(x_list[n], alpha)
	for n in range(num):
		y_list.append((1 - e) * f(x_list[n], alpha) + (e / num) * total)
	return y_list

def series(alpha, e, initial, length, trans_period):
	num_coupled = len(initial)  # 結合数
	x_list = [n + trans_period for n in range(length)]
	y_list = []

	for n in range(num_coupled):
		y_list.append([initial[n]])
	length -= 1
	for n1 in range(length + trans_period):
		pre_y_list = []
		for n2 in range(len(initial)):
			pre_y_list.append(y_list[n2][n1])

		after_y_list = coupled_f(pre_y_list, alpha, e)
		for n2 in range(len(initial)):
			y_list[n2].append(after_y_list[n2])

	for n1 in range(num_coupled):
		y_list[n1] = y_list[n1][trans_period:]
	return x_list, np.transpose(y_list)
