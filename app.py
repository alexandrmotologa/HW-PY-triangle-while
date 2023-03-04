def triangle(n):
    
    i = 1
    while i <= n:
        spaces = (' ' *2) * ((n-i) // 2)
        plus = '+ ' * i
        print(spaces + plus)
        i += 2

n = int(input("Introduceți mărimea triunghiului: "))
triangle(n)