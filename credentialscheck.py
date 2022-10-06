#Check Credentials  
Var_username_checks=str(input('Please enter the correct username: ')) #enter reference username
Var_Pass_checks= str(input('Please enter the correct password: '))         #enter reference password

Var_username=str(input('Please enter your username: '))
Var_Pass=str(input('Please enter your password: '))
if (Var_Pass_checks==Var_Pass and Var_username_checks==Var_username):
    print('Credentials Matched, Authentication Succesful')

else:
    print('Authentication failed. Please retry')
