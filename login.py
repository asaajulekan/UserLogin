
def userName():
    welcm = input("Hi there! press the enter key to login:<>:")
    if welcm == True:
        pass
    name = 0
    while name != 4:
        username = input('Enter your username::>> ')
        conv = username.lower()
        if conv == 'nathaniel':
            print('\n')
            break
        elif conv != 'nathaniel':
            print('Incorrect username')
            print('int: nath')
            name += 1
        if name == 3:
            print('<<Seems you forget your username')
            print("Try again")
    attempt = 0
    flag = 0
    while attempt != 3:
        password = input('Enter your password::>> ')
        get = password.lower()
        if get == 'admin':
            flag = 1
            print('\n')
            break
        elif password != 'admin':
            print('Incorrect password')
            attempt = attempt + 1
        if attempt == 3:
            print('You have reached the maximum attempt')
            print('Try again in 15sec')
    if flag == 1:
        print(f'>>welcome {username} do not forget to log out\n')

userName()
def logout():
    spam = input("Type 'exit' to logout")
    if spam == "exit":
        print('\n')
        print(">>Don't forget to check in later" )


logout ()








