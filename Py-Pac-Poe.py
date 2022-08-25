# As a player (AAP), I want to see a welcome 
# message at the start:

print(''' 
----------------------
Let's play Py-Pac-Poe!
----------------------
''')

# define global variables
a1 = '   '
b1 = '   '
c1 = '   '
a2 = '   '
b2 = '   '
c2 = '   '
a3 = '   '
b3 = '   '
c3 = '   '

#AAP, before being prompted for a move,
#  I want to see the board printed out in the console, 
# so that I know what moves have been made:

def disp_board():
    print(f'''
         A   B   C

    1)  {a1}|{b1}|{c1}   
        -----------
    2)  {a2}|{b2}|{c2}  
        -----------
    3)  {a3}|{b3}|{c3} 
    
    ''')

disp_board()