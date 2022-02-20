
# add
# multiply
# subtract
# divide
# pow


def add(x, y):
    return x + y

def mulitply(x, y):
    return x*y

def subtract(x,y):
    return x-y

def divide(x, y):
    return x/y

def pow(x, y):
    return x**y

print('Please Select Your operation : ')
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Pow")

print("--------------------")
while True:

    operation= input('Enter Choise (1/2/3/4/5) :')

    if operation in ('1', '2', '3', '4', '5'):
        input1= float(input('Please enter x  ..... :'))
        input2= float(input('Please enter y  ..... :'))

        
        if operation=='1':
            print(f'{input1} + {input2} ==> ',add(input1,input2))
        
        elif operation=='2':
            print(f'{input1} * {input2} ==> ',mulitply(input1,input2))
        
        elif operation=='3':
            print(f'{input1} - {input2} ==> ',subtract(input1,input2))
        
        elif operation=='4':
            print(f'{input1} / {input2} ==> ',divide(input1,input2))

        elif operation=='5':
            print(f'{input1} ^ {input2} ==> ',pow(input1,input2))
        
        next_calculation=input('Do you want to continue calculation (Yes / No).... ?')

        if next_calculation in ('no', 'No'):
            print('have a good time ...')
            break
    
    else:
        print('Choise is not valid try again please ...')
        
