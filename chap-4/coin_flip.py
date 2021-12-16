import random
numberOfStreaks = 0
count=0
def get_list():
    flip_list = []
    for i in range(100):
      flip_list.append(random.randint(0, 1))
    return flip_list

def streak_counter(flip_list,numberOfStreaks):
    internal_streak_count = 0
    for j in range(len(flip_list)-1):
        if flip_list[j] == flip_list[j+1]:
            internal_streak_count += 1
        else:
            if internal_streak_count == 6:
                numberOfStreaks+=1
            internal_streak_count=0
    return numberOfStreaks
for experimentNumber in range(10000):
    count += streak_counter(get_list(),numberOfStreaks)
numberOfStreaks = count 
print('Chance of streak: %s%%' % (numberOfStreaks / 100))