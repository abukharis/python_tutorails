ISBN =input( 'enter isbn:')
sum1=0
sum2=0
for i in range(1,13,2): 
  sum1= sum1+3*int(ISBN[i])
for i in range(0,12,2):
    sum2=sum2+int(ISBN[i])

THRITEEN =10-(sum1+sum2)%10
print(THRITEEN)