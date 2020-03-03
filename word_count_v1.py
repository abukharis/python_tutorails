    
word='hi'
phrase='hi hi word'
count=0
word=word.strip()
xx=phrase.split()
n=len(xx)
for i in range(n):  
    if i==word:

        count=count+1
    else:
        continue

print (count)
