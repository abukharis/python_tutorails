

def SEE1(word,phrase):
    count=0
    word=word.strip()
    xx=phrase.split()
    n=len(xx)
    for i in range (n):  
        if xx[i]==word:

            count=count+1
        else:
            continue

return count


