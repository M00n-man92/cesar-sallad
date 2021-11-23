from encript import cesar_encript
from encript import cesar_decrypt
yes=True
while yes:
    answer=input("input de for decode or en for encrypt or anything else to stop the code ").lower()
    if answer=="en":
        letter=input("please enter the lettert u wanna cypher   ").lower()
        shift=int(input("please enter the the number of shift u wanna associate with it   "))
        cesar_encript(msg=letter,shift=shift)
        another_answer=input("input de for decode or en for encrypt or anything else to stop the code ").lower()
        if another_answer=="de":
            letter=input("please enter the lettert u wanna decypher   ").lower()
            shift=int(input("please enter the the number of shift u wanna associate with it   "))
            cesar_decrypt(msg=letter,shift=shift)
        elif another_answer=="en":
            letter=input("please enter the lettert u wanna cypher   ").lower()
            shift=int(input("please enter the the number of shift u wanna associate with it   "))
            cesar_encript(msg=letter,shift=shift)
        else:
            print("thankin you for choosing us")
    elif answer=="de":
        letter=input("please enter the lettert u wanna decypher   ").lower()
        shift=int(input("please enter the the number of shift u wanna associate with it   "))
        cesar_decrypt(msg=letter,shift=shift)
        another_answer=input("input de for decode or en for encrypt or anything else to stop the code ").lower()
        if another_answer=="de":
            letter=input("please enter the lettert u wanna decypher   ").lower()
            shift=int(input("please enter the the number of shift u wanna associate with it   "))
            cesar_decrypt(msg=letter,shift=shift)
        elif another_answer=="en":
            letter=input("please enter the lettert u wanna cypher   ").lower()
            shift=int(input("please enter the the number of shift u wanna associate with it   "))
            cesar_encript(msg=letter,shift=shift)
        else:
            print("thankin you for choosing us")    
    else:
        print("thankin you for choosing us")
    
    no=input("do you wanna go agian? press yes or no if you want to quit ")
    if no=="no":
        yes=False            



 



