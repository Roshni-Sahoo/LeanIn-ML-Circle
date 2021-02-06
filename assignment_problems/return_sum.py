#Sum of numbers
limit=int(input())
ans=0
for i in range(0,limit+1):
	if(i%3==0):
		ans+=i
	elif(i%5==0):
		ans+=i

print(ans)