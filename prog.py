def spin_words(sentence):
    temp = sentence.split(' ')
    temp = [i[::-1] for i in temp]
    return temp
    
    

print(spin_words('ot'))