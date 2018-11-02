import random
from collections import Counter
DIE = [1, 2, 3, 4, 5, 6]
history = []
while True:
    num = random.randint(1, 6) + random.randint(1, 6)
    history.append(num)
    print num
    i = raw_input()
    if i == 'end':
        print Counter(history)
        exit()

    
    






