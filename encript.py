list_of_alp=[]
list_of_alp.extend("abcdefghijklmnopqrstuvwxyz")
def cesar_encript(msg,shift):
    
    new_word=""
    count=0
    for i in range(0,len(msg)):
        for j in range(0,26):
            if msg[i]==list_of_alp[j]:
                placeholder=j+shift
            
                if placeholder>25:
                    crazy=placeholder-25
                    new_word+=list_of_alp[crazy-1]
                    
                else:
                    new_word+=list_of_alp[placeholder]
            elif msg[i]==" ":
                count+=1

                if count==26:
                    
                    new_word+=" "
                    count=0
    print(new_word)
def cesar_decrypt(msg,shift):
    another_word=""
    count=0
    for i in range(0,len(msg)):
        for j in range(0,26):
            if msg[i]==list_of_alp[j]:
                placeholder=j-shift
                
                if placeholder<0:
                    crazy=25+placeholder
                    another_word+=list_of_alp[crazy+1]
                    
                else:
                    another_word+=list_of_alp[placeholder]
            elif msg[i]==" ":
                count+=1

                if count==26:
                    
                    another_word+=" "
                    count=0
    print(another_word)
    