data = []
count = 0
with open('test.txt', 'r') as f:
	for line in f:   #for loop >一行行讀數據檔
		data.append(line)
		count += 1
		if count % 5 == 0:  #求餘數
			print(len(data))
		

print(data[1])
