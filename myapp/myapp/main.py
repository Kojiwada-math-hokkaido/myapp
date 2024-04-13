import numpy as np
import math

# 写像を定義
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

# 時系列を生成
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

# 時系列の差を生成
def product_dif_list(y_list):
	num_coupled = len(y_list[0])
	dif_list = []
	for n1 in range(len(y_list)):
		sub_list = y_list[n1]
		sub_dif_list = []
		for n2 in range(num_coupled):
			for n3 in range(n2 + 1, num_coupled):
				sub_dif_list.append(abs(sub_list[n2] - sub_list[n3]))
		dif_list.append(sub_dif_list)
	return dif_list

# 確率分布のラベルを生成
def product_label(y_min, y_max, num_label):
	y_length = (y_max - y_min) / num_label
	x_list = []
	for n1 in range(num_label):
		y_min += y_length
		x_list.append(round(y_min, 4))
	return x_list

# n進展開
def Dec_to_N(num, base):
	if num >= base:
			yield from Dec_to_N(num // base, base)
	yield num % base

# 状態空間を判別
def state_replace(state_matrix, convert_list):
	for i in range(len(state_matrix)):
		for j in range(len(state_matrix[i])):
			state_matrix[i][j] = convert_list[state_matrix[i][j]]
	return state_matrix

# 全体の状態ラベルの行列を作成
def product_whole_label_list(label_list, num_coupled):
	num_label = len(label_list) # number of state
	whole = list(range(num_label ** num_coupled))
	state_matrix = [list(Dec_to_N(n, num_label)) for n in whole]
	for n1 in range(len(state_matrix)):
			while len(state_matrix[n1]) < num_coupled:
					state_matrix[n1].insert(0, 0)
	whole_label_list = state_replace(state_matrix, label_list)
	return whole_label_list

# 状態を判定
def label_func(dif_label, dif_list):
	z_list = np.array(dif_list).copy()
	for n1 in range(len(dif_list)):
		for n2 in range(len(dif_list[0])):
			for n3 in range(len(dif_label)):
				if dif_list[n1][n2] <= dif_label[len(dif_label) - n3 - 1]:
					z_list[n1][n2] = dif_label[len(dif_label) - n3 - 1]
					z_list[n1][n2] = len(dif_label) - n3 - 1
	return z_list

# 逆N進展開
def N_to_Dec(digits, base):
	result = 0
	power = 0
	for digit in reversed(digits):
		result += digit * (base ** power)
		power += 1
	return int(result)

# 全体の確率行列を生成
def product_whole_prob_matrix(dif_list, dif_label):
	couple = len(dif_list[0])
	z_list = label_func(dif_label, dif_list)
	dif_list = [N_to_Dec(z_list[n], len(dif_label)) for n in range(len(z_list))]
	whole_dist = [0 for n in range(len(dif_label) ** couple)]
	for n in dif_list:
		whole_dist[n] += 1
	whole_dist = [x / sum(whole_dist) for x in whole_dist]
	return whole_dist

# エントロピーを計算
def cal_entropy(whole_dist):
	entorpy = 0
	for n in range(len(whole_dist)):
		if whole_dist[n] > 0:
			entorpy -= whole_dist[n] * np.log(whole_dist[n])
	return entorpy

# 部分の確率分布を生成
def product_sub_prob_matrix(dif_list, dif_label):
	sub_dist = []
	z_list = label_func(dif_label, dif_list)
	for n1 in range(len(dif_list[0])):
		distribution = [0 for _ in range(len(dif_label))]
		for n2 in range(len(dif_list)):
			distribution[int(z_list[n2][n1])] += 1
		distribution = [x / sum(distribution) for x in distribution]
		sub_dist.append(distribution)
	return sub_dist

# クラスター数の判定
def count_num_cluster(y_list):
	num_cluster = 0
	cluster_list = [y_list[0]]
	for n in range(1, len(y_list)):
		check = 0
		for cluster in cluster_list:
			if abs(cluster - y_list[n]) > 0.00001:
				check += 1
			if check == len(cluster_list):
				cluster_list.append(y_list[n])
	num_cluster = len(cluster_list)
	return num_cluster

# 階層的クラスター化を確認
def hierarchical(y_list, accuracy, base):
	accuracy_list = [n for n in range(accuracy + 1)]
	hierar_list = []
	for x in accuracy_list:
		hie_list = []
		for y in y_list:
			hie_list.append(num_round(y * base**x) / base**x)
		hierar_list.append(hie_list)
	return hierar_list, accuracy_list

def num_round(num):
	if num < 0:
		num = -math.floor(-num)
	else:
		num = math.floor(num)
	return num
