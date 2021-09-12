import random
dice_list = [1,2,3,4,5,6]
for i in range(len(dice_list)):
    print(random.choice(dice_list))

import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)

print(die1, die2)
print(die1 + die2)
if(die1 + die2) > 6:
    print("You won!!!")
else:
    print("You suck!!!")
