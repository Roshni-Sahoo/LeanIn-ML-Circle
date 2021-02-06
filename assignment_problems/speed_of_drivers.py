#Check Speed
speed=int(input())
if(speed<70):
	print("Ok")
else:
	a=(speed-70)
	demerit=int(a/5)
	if(demerit>12):
		print("License suspended")
	else:
		print("Points:",demerit)