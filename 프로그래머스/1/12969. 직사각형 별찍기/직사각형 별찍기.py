a, b = map(int, input().strip().split(' '))

for x in range(b) :
    stars = ''
    for y in range(a) :
        stars += '*'
    print(stars)