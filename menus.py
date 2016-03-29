name=input('Enter name:')
choice=input("""
(H)ello
(G)oodbye
(Q)uit
""")

while choice !='Q':
    if choice == 'H':
        print('hello',name)
    elif choice=='G':
        print('goodbye',name)
    else:
        print('Error')
    choice=input("""(H)ello
(G)oodbye
(Q)uit
""")

if choice=='Q':
    exit()