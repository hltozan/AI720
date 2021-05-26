even_numbers = list(range(0, 11, 2))

odd_numbers = list(range(1, 12, 2))

merged_list = list()


for i in range(len(even_numbers)):

  merged_list.append(even_numbers[i] * 2)

  merged_list.append(odd_numbers[i] * 2)


for i in merged_list:

  print(type(i))