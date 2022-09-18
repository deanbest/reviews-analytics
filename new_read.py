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


#先讀資料 > 裝清單 > 篩條件
new = []
#一筆筆叫出來, 每筆叫出來都叫d
for d in data:
	if len(d) > 5:
		new.append(d)
print('一共有', len(new), '筆歌詞長度大於5')
print(new[7])
