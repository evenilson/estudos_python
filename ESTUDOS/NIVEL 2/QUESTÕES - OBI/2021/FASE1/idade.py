idade1 = input()
idade2 = input()
idade3 = input()

if(((idade1 >= idade2) and (idade1 <= idade3)) or ((idade1 <= idade2) and (idade1 >= idade3))): print(idade1) 
elif(((idade2 >= idade1) and (idade2 <= idade3)) or ((idade2 <= idade1) and (idade2 >= idade3))): print(idade2)
else: print(idade3)