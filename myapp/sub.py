import csv

def save_csv_file(x_list, y_list):
  data = []

  for sublist1, sublist2 in zip(x_list, y_list):
    data.append([sublist1] + sublist2.tolist())

  header = ["step"]
  for n in range(len(y_list[0])):
    header.append("x_{}".format(n))

  with open('data_set.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csv_writer.writerows(data)
