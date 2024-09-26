# Créé par thfruchart, le 16/09/2024 en Python 3.7

n = int(input('Entrer un entier : '))

print('étape1')
i = 1
while i <= n :
    print('*' * i)
    i = i + 1


print('étape2')
i = n
while i > 0 :
    print('*' * i)
    i = i-1


print('étape3')
print('*' * n)
i = n-2
while i > 0 :
    print('*' + ' ' * (n-2) + '*')
    i = i-1
print('*' * n)


print('étape4')
i = n-1
while i >= 0 :
    print(' ' * i + '*')
    i = i-1

print('étape5')
i = n-1
k = 0
while i >= 0 :
    print(' ' * i + '*' + 2*k*' ' + '*')
    i = i-1
    k = k+1

print('étape6')
k = n
while k > 0 :
    i = 0
    while i < k :
        print(k*'*')
        i = i+1
    k = k-1
