if 3 > 2:
    print('it works!')
if 5>2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey awesome')
volume = 57
if volume < 20:
    print("its kinda quiet")
elif 20 <= volume < 40:
    print("it's nice for background music")
elif 40 <= volume < 60:
    print ("perfect, I can hear all the details")
elif 60 <= volume < 80:
    print ("nice for parties")
elif 80 <= volume < 100:
    print ("a bit loud")
else:
    print ("my ears!")
if volume < 20 or volume > 80:
    volume = 50
    print ("well done")
def hi():
    print ('hello beautiful')
    print ('hows it hanging?')
hi()
def hi(name):
    if name == 'Ola':
        print ('Hi Ola')
    elif name == 'Sonja':
        print ('Hi Sonja')
    else: print('hi love')
hi('Bettina')

def hi(name):
    print ('hi ' + name + '!')
hi('Bettina')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Bettina']
for name in girls:
    hi(name)
    print('next girl')

for i in range (1, 6):
    print(i)
