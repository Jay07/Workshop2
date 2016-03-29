choice=input("""1.	Show the even numbers from x to y
2.	Show the odd numbers from x to y
3.	Show the squares from x to y
4.	Exit the program
""")
while choice!=4:
    if choice=='1':
        x=int(input('Enter x:'))
        y=int(input('Enter y:'))
        for num in range(x,y+1):
            if num%2 ==0:
                print(num)
    elif choice=='2':
        x=int(input('Enter x:'))
        y=int(input('Enter y:'))
        for num in range(x,y+1):
            if num%2!=0:
                print(num)
    elif choice=='3':
        x=int(input('Enter x:'))
        y=int(input('Enter y:'))
        for num in range(x,y+1):
            print(num**2)
    elif choice=='4':
        quit()
    choice=input("""1.	Show the even numbers from x to y
2.	Show the odd numbers from x to y
3.	Show the squares from x to y
4.	Exit the program
""")