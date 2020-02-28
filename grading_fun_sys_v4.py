
name= input('please enter studen name:')
homework=float(input('please enter homewrok mark:'))
assigment =float(input('please enter assigment mark:'))
final=float(input('please enter final mark :'))




def grade():
   

    ICTscore = ((homework/25+assigment/50+final/100)/3)*100
    
    if ICTscore>=70:
       grade='A'
    elif ICTscore >=60:
        grade='B'
    elif ICTscore == 50:
        grade='C'
    elif  ICTscore >= 40:
        grade='D'
    else:
         grade='F'
    return  grade

print(name, grade())

    
