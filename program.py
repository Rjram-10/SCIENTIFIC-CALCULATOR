import math
i=0
while i!=5:
    print('''               >>> Selct option for operation <<<


1.Elememtry Operation(Addition,Subtraction,Multiplication,Division,Mod)
2.Power and Square root operatrion
3.Trigonometric operation
4.Conversion(Degree -> Radian & Radian -> Degree)
5.Exit''')

    try:
        i=int(input('Enter  your choice :- '))
    except:
        pass
    if i==1:
        j=0
        while j!=7:
            j=0
            
            print('''>>> Select one option <<<
1.Addition
2.Subtrraction
3.Multiplication
4.Division
5.Mod
6.Main menu
7.Exit''')
            try:
                j=int(input("Enter your choice :- "))
            except:
                pass
            if j==1 or j==2:
                if j==1:
                    print('User allowed to enter only addition signs , starting with positive number eg.(42+254+52+12)' )
                    a=input().split('+')
                    l=0
                    for m in range(len(a)):
                        a[m]=int(a[m])
                        l+=a[m]
                    print('Addition :-',l)
                else:
                    print('User allowed to enter only substraction signs , starting with positive number eg.(42-8-25)')
                    a=input().split('-')
                    l=0
                    for m in range(len(a)):
                        if m>0:
                            a[m]=int(a[m])
                            l-=a[m]
                        else:
                            l=int(a[0])
                    print('Subtraction :- ',l)
            elif j==3 or j==4 or j==5:
                k=int(input('Enter first number :- '))
                l=int(input('Enter second number :- '))
                if j==3:
                    print("Multiplication :- ",k*l)
                elif j==4:
                    print('Division :- ',k/l)
                else:
                    print('Mod :- ',k%l)
            elif j==6:
                break
            elif j==7:
                exit()
                
            else:
                print('Invalid')
                continue
    elif i==2:
        j=0
        while j!=4:
            j=0
            print('''>>> Select one option <<<
    1.Power
    2.Square root
    3.Main menu
    4.Exit''')
            try:
                j=int(input('Select one choice :- '))
            except:
                pass
            if j==1:
                k=int(input('Enter base number :- '))
                l=int(input('Enter power number :- '))
                print("Power",math.pow(k,l))
            elif j==2:
                k=int(input("Enter number :- "))
                print('Square root',math.sqrt(k))
            elif j==3:
                break
            elif j==4:
                exit()
            else:
                print('Invalid')
                continue
    elif i==3 :
        j=0
        while j!=5:
            j=0
            print('''>>> Select one option(Trigonometric Function) <<<
    1.Sine function
    2.Cosine function
    3.Tangent Function
    4.Main menu
    5.Exit''')
            try:
                j=int(input('Enter your choice :- '))
            except:
                pass
            if j==1 or j==2 or j==3:
                k=float(input('Enter your value :- '))
                if j==1:
                    print('Sine value',math.sin(math.radians(k)))
                elif j==2:
                    print('Cosine value',math.cos(math.radians(k)))
                elif j==3:
                    print('Tangent value',math.tan(math.radians(k)))
            elif j==4:
                break
            elif j==5:
                exit()
            else:
                print('Invalid')
                continue
    elif i==4:
        j=0
        while j!=4:
            j=0
            print('''>>> Select one choice <<<
    1.Degree -> Radian
    2.Radian -> Degree
    3.Main menu
    4.Exit''')
            try:
                j=int(input('Enter your choice :- '))
            except:
                pass
            if j==1 or j==2:
                k=int(input('Enter your value '))
            
                if j==1:
                    print(math.radians(k))
                elif j==2:
                    print(math.degrees(k))
            elif j==3:
                break
            elif j==4:
                exit()
            else:
                print("Invalid")
                continue
    elif i==5:
        break
    else:
        print('Invalid')
        continue

