data = []
count = 0
with open('test.txt', 'r') as f:
	for line in f:   #for loop >一行行讀數據檔
		data.append(line)
		count += 1
		if count % 5 == 0:  #求餘數
			print(len(data))
		

print('檔案讀完, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('平均每筆資料長度為', sum_len / len(data))

