#Show Odd and Even
limit=int(input())
for i in range(0,limit+1):
	if(i%2==0):
		print(i,"EVEN")
	else:
		print(i,"ODD")