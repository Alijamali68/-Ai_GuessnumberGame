import random
avalbaze=1
akharbaze=99
Ai_guessed_number=random.randint(avalbaze,akharbaze)
print(Ai_guessed_number)
javab=input('b=bozirgtare  k=kochick tare d=doroste ')
while(javab!='d'):
	if javab=='b' :
		avalbaze=Ai_guessed_number
	elif javab=='k' :
		akharbaze=Ai_guessed_number
	else:
		break	
	Ai_guessed_number=random.randint(avalbaze,akharbaze)
	print(Ai_guessed_number)
	javab=input('b=bozirgtare  k=kochicktare d=doroste : ')		
