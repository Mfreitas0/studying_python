"""
for / while
0 10
1 9
2 8
3 7
4 6
...
"""

a = 0
b= 10

while a < 10:
    a += 1
    
    
    while b > 0:
        b -= 1
        print(a, b)
        break

print('Fim!')
        