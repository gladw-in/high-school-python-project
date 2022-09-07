#By Gladwin Paul
import turtle
def schlogo(col,val):
    s = turtle.Turtle()
    screen = turtle.Screen()
    s.speed(150)
    s.width(2)
    for i in range(5):
        s.color(col)
        s.right(100)
        s.forward(122)
        s.right(80)
        s.forward(122)
        s.right(80)
        s.forward(122)
        s.right(100)
        s.forward(170)
    s.backward(90)
    s.left(90)
    for i in range(34):
        s.left(3)
        s.forward(1)
    s.forward(80)
    s.left(168)
    s.forward(102)
    s.left(90)
    for i in range(35):
        s.right(3)
        s.forward(1)
    s.forward(70)
    s.right(85)
    s.forward(123)
    s.right(80)
    s.forward(71)
    s.right(90)
    s.forward(2)
    s.color(val)
    s.forward(118)
    s.right(90)
    s.forward(85)
    s.backward(177)
    s.left(90)
    s.forward(1)
    s.right(90)
    s.forward(92)
    s.right(90)
    s.forward(120)
    s.color(col)
    s.forward(2)
    s.left(180)
    s.forward(1)
    s.right(90)
    s.forward(41)
    s.left(80)
    s.forward(2)
    s.right(360)
    s.forward(1)
    s.color(val)
    s.forward(120)
    s.left(100)
    s.forward(20)
    s.left(90)
    s.forward(119)
    s.color(col)
    s.forward(2)
    s.color(val)
    s.forward(10)
    s.right(90)
    s.color(col)
    s.forward(100)
    s.left(90)
    s.left(63)
    for i in range(52):
        s.left(1)
        s.forward(2)
    s.right(0)
    s.forward(1)
    s.left(155)
    s.forward(47)
    s.right(90)
    s.forward(18)
    s.right(42)
    for i in range(27):
        s.left(3)
        s.forward(3)
    s.left(98)
    for i in range(28):
        s.left(3)
        s.forward(3)
    s.left(49)
    s.color(col)
    s.color(val)
    s.forward(40)
    s.left(80)
    s.forward(106)
    s.left(100)
    s.color(col)
    s.forward(120)
    s.backward(40)
    s.color(val)
    s.backward(30)
    s.forward(11)
    s.left(90)
    s.forward(16)
    s.color(col)
    s.left(90)
    s.forward(56)
    s.backward(112)
    s.forward(40)
    s.color(val)
    s.forward(26)
    s.right(90)
    s.forward(16)
    s.left(90)
    s.forward(8)
    s.color(col)
    s.forward(36)
    s.color(val)
    s.right(101)
    s.forward(16)
    s.right(79)
    s.color(col)
    s.forward(31)
    s.backward(31)
    s.left(79)
    s.color(val)
    s.forward(16)
    s.right(79)
    s.color(col)
    s.forward(23)
    s.backward(23)
    s.left(79)
    s.color(val)
    s.forward(16)
    s.right(79)
    s.color(col)
    s.forward(24)
    s.backward(24)
    s.left(79)
    s.color(val)
    s.forward(16)
    s.right(79)
    s.color(col)
    s.forward(24)
    s.backward(24)
    s.color(val)
    s.left(79)
    s.forward(11)
    s.right(79)
    s.forward(37)
    s.color(col)
    s.forward(2)
    s.color(val)
    s.forward(47)
    s.right(79)
    s.forward(16)
    s.color(col)
    s.right(101)
    s.forward(37)
    s.backward(37)
    s.left(101)
    s.color(val)
    s.forward(16)
    s.right(101)
    s.color(col)
    s.forward(30)
    s.backward(30)
    s.left(101)
    s.color(val)
    s.forward(16)
    s.right(101)
    s.color(col)
    s.forward(27)
    s.backward(27)
    s.left(101)
    s.color(val)
    s.forward(16)
    s.right(101)
    s.color(col)
    s.forward(24)
    s.backward(24)
    s.left(101)
    s.color(val)
    s.forward(14)
    s.right(101)
    s.color(col)
    s.forward(37)

def multi_star(col,layer):
    t=turtle.Turtle()
    screen=turtle.Screen()
    t.speed(layer)
    g = len(col)
    layer0= layer*8
    for i in range (layer0):
        t.color(col[i%g])
        t.forward(i*4)
        t.left(150)
        t.width(3)
        
def multi_sqr(colr,nocr):
    u=turtle.Turtle()
    screen=turtle.Screen()
    u.speed(nocr)
    for i in range(nocr):
        for colors in colr:
            u.color(colors)
            u.width(3)
            u.left(12)
            for i in range(4):
                u.forward(210)
                u.left(95)
                    
def multi_hexa(colr,nohexa):
    colors = colr
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(nohexa)
    r = len(colr)
    j = nohexa*6
    for x in range(j):
        t.color(colors[x%r])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)
        
def sun(col):
    t = turtle.Turtle()
    screen = turtle.Screen()
    a = 0
    b = 0
    t.color(col)
    t.width(2)
    t.speed(150)
    t.goto(0,180)
    while(True):
        t.forward(a)
        t.color(col)
        t.right(b)
        a+=3
        b+=1
        if b == 205:
            break

def blank(val):
    s = turtle.Turtle()
    screen = turtle.Screen()
    s.speed(10)
    s.color(val)
    s.width(12000)
    s.forward(1)

print("------------------------------------------------------------------------------")
print("A program to diaplay some color paterns using turtle module!")
print("------------------------------------------------------------------------------")
while True:
    print("Enter One to display multicolor stars")
    print("Enter Two to display a combination of multicolor Squares")
    print("Enter Three to diplay multicolor Hexagon")    
    print("Enter Four display the pictur of Sun")
    print("Enter Five diplay the Sindhi High School logo")
    print("Enter Six to exit this program now!")
    ch=input("Enter your choice: ")
    a=ch.lower()

    if a=="1" or a=="one":
        print("You have selected option",ch)
        col = []
        while True:
            try:
                num = input("How many colors you want? ")
                num = int(num)
                if num >=1 and num <=20:
                    num = int(num)
                    break
                elif num ==0:
                    print("------------------------------------------------------------------------------")
                    print("Try again!")
                    print("------------------------------------------------------------------------------")
                else:
                    print("------------------------------------------------------------------------------")
                    print("The no of colors are limted to 20")
                    print("------------------------------------------------------------------------------")
            except ValueError:
                print("------------------------------------------------------------------------------")
                print("Invalid integer! Please try again ...")
                print("------------------------------------------------------------------------------")
        print("Valid input!")
        print("Enter the",num,"Colors correctly!")
        for i in range(0, num):
            add = input()
            c = add.lower()
            col.append(c)
        print("The colors you enttered are ",col)
        val = input("Enter the background color ")
        while True:
            try:
                layer = input("Enter the Number of Stars you need of each color [less than 25] ")
                layer = int(layer)
                if layer >=0 and layer <=25:
                    layer = int(layer)
                    break
                else:
                    print("Enter a number less than or egual 25")
            except ValueError:
                print("------------------------------------------------------------------------------")
                print("Invalid integer! Please try again ...")
                print("------------------------------------------------------------------------------")

        print("Valid input!")
        blank(val)
        multi_star(col,layer)
               
    elif a=="2" or a =="two":
        print("You have selected option",ch)
        colr = []
        while True:
            try:
                num = input("How many colors you want? ")
                num = int(num)
                if num >=1 and num <=20:
                    num = int(num)
                    break
                elif num ==0:
                    print("------------------------------------------------------------------------------")
                    print("Try again!")
                    print("------------------------------------------------------------------------------")
                else:
                    print("------------------------------------------------------------------------------")
                    print("The no of colors are limted to 20")
                    print("------------------------------------------------------------------------------")
            except ValueError:
                print("------------------------------------------------------------------------------")
                print("Invalid integer! Please try again ...")
                print("------------------------------------------------------------------------------")
        print("Valid input!")
        print("Enter the",num,"Colors correctly!")
        for i in range(0, num):
            add = input()
            c = add.lower()
            colr.append(c)
        print("The colors are ",colr)
        val = input("Enter the Background Color ")
        while True:
            try:
                nocr = input("Enter the Number of Squares you need of each color [less than 25] ")
                nocr = int(nocr)
                if nocr >=0 and nocr <=25:
                    break
                else:
                    print("Enter a number less than or egual 25")
            except ValueError:
                print("------------------------------------------------------------------------------")
                print("Invalid integer! Please try again ...")
                print("------------------------------------------------------------------------------")
        print("Valid input!")
        blank(val)
        multi_sqr(colr,nocr)
    
    elif a=="3" or a =="three":
        print("You have selected option",ch)
        colr = []
        while True:
            try:
                num = input("How many colors you want? ")
                num = int(num)
                if num >=1 and num <=20:
                    num = int(num)
                    break
                elif num ==0:
                    print("------------------------------------------------------------------------------")
                    print("Try again!")
                    print("------------------------------------------------------------------------------")
                else:
                    print("------------------------------------------------------------------------------")
                    print("The no of colors are limted to 20")
                    print("------------------------------------------------------------------------------")
            except ValueError:
                print("------------------------------------------------------------------------------")
                print("Invalid integer! Please try again ...")
                print("------------------------------------------------------------------------------")
        print("Valid input!")
        print("Enter the",num,"Colors correctly!")
        for i in range(0, num):
            add = input()
            c = add.lower()
            colr.append(c)
        print("The colors are ",colr)
        val = input("Enter the Background Color ")
        while True:
            try:
                nohexa = input("Enter the Number of Hexagons you need of each color [less than 25] ")
                nohexa = int(nohexa)
                if nohexa >=0 and nohexa <=25:
                    break
                else:
                    print("------------------------------------------------------------------------------")
                    print("Invalid integer! Please try again ...")
                    print("------------------------------------------------------------------------------")
            except ValueError:
                print("------------------------------------------------------------------------------")
                print("Invalid integer! Please try again ...")
                print("------------------------------------------------------------------------------")
        print("Valid input!")
        blank(val)
        multi_hexa(colr,nohexa)

    elif a=="4" or a =="four":
        print("You have selected option",ch)
        col = input("Enter the Color ")
        val = input("Enter the Background Color ")
        blank(val)
        sun(col)
        
    elif a=="5" or a =="five":
        print("You have selected option",ch)
        col = input("Enter the Color ")
        val = input("Enter the Background Color ")
        blank(val)
        schlogo(col,val)
        
    elif a=="6" or a =="six" or a =="exit" or a =="quit":
        break
    elif a =="0" or a =="zero":
        print("------------------------------------------------------------------------------")
        print("Try again!")
        print("------------------------------------------------------------------------------")
        
    else:
        print("------------------------------------------------------------------------------")
        print("Wrong Choice.... try again!")
        print("------------------------------------------------------------------------------")
