import random
computer = random.randint(0,100)
allcount = 0
MenWeiJia_num = 0
while True:
	
	MenWeiJia = int(input("请猜一个数字"))
	if computer > MenWeiJia:
		print("你猜的数字猜小了，请接着猜")
		allcount+=1
	elif computer < MenWeiJia:
		print("你猜的数字猜大了，请接着猜")
		allcount+=1
	elif computer == MenWeiJia:
		print("恭喜你猜中了，是否要继续此游戏？")
		allcount+=1
		print("猜了"+str(allcount)+"次才猜中。")
		mode = int(input("1:继续 2:退出"))
		if mode == 1:
			MenWeiJia_num+=1
			print("玩了"+str(MenWeiJia_num)+"次!")
			continue
			
		elif mode == 2:
			break

	
		



