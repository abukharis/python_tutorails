bio=float(input('please enter bio mark:'))
chem=float(input('please enter chem mark:'))
phy=float(input('please enter phy mark :'))
score = float((bio+chem+phy)/3)
if bio<40:
    print('fail')
elif chem <40:
    print('fail')
elif phy<40:
    print('fail')
elif score >=70:
    print('1st')
elif score >=60:
    print ('2.1')
elif score >= 50:
    print('2.2')
    
elif score >= 40:
    print('pass')
else:
    print('fail')
