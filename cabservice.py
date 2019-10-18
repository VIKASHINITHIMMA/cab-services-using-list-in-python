a1=""
a2=""
a3=""
a4=""
import datetime
def bill(name,d,charges):
	global a1
	global a2
	global a3
	global a4
	a1=greet(name)
	a2=dis_tra(d)
	a3=date()
	a4=charge(charges)
def greet(name):
	print('Hello Mr/Ms.'+name+'Greetings from cab services')
	return name
def dis_tra(d):
	print('You have travelled',str(d),'kms')
	return d
def date():
	a=datetime.datetime.now()
	print('Date:',a)
	return a
def charge(charges):
	
	print('You have been charged Rs',charges )
	return charges
def mini(d):
	return 10*d
def micro(d):
	return 20*d
def suv(d):
	return 30*d
def sedan(d):
	return 40*d
reg_cus=['aaa','bbb','ccc']
cus=raw_input('Enter your name:')
if cus not in reg_cus:
	print('not a registered customer.\nWould u like to register?If yes press y else n')
	ch=raw_input()
	if ch=='y':
		reg_cus.append(cus)
		print('Successfully registered.Welcome to cab services!')
	else:
		exit()
dis=float(raw_input("Enter the distance in kilometers:"))	
if dis<1:
	print('Services not available for distance less than 1km')
	exit()
else:
	print("mini-Rs10pkm/nmicro-Rs20pkm/suv-Rs30pkm/sedan-Rs40pkm")	
	car_ch=raw_input('What type of car would u like to have?')
	if(car_ch=='mini'):
		charges=mini(dis)
	elif(car_ch=='micro'):
		charges=micro(dis)
	elif(car_ch=='suv'):
		charges=suv(dis)
	elif(car_ch=='sedan'):
		charges=sedan(dis)
	else:
		print('invalid choice')
		exit()

	bill(cus,dis,charges)
fp=open("log.txt","w")
fp.write(a1)
fp.write("\n")
fp.write(str(a2))
fp.write("\n")
fp.write(str(a3))
fp.write("\n")
fp.write(str(a4))
fp.write("\n")
fp.close()

