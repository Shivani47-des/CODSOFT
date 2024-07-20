import random 
def password_generator():
    password = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
    
    passwrd_len = int(input("ENTER THE LENGTH OF PASSWORD : "))

    passwd = " "
    for a in range(passwrd_len):
        passwd = passwd+random.choice(password)


    print("YOUR GENERATED PASSWORD IS : ", passwd)

password_generator()