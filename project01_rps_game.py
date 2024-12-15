import random
def game(comp,you):
    if comp == 'r':
        if you == 's':
            return "you loose"
        elif you == 'p':
            return "you win"
        else:
            return "tie"
    elif comp == 's':
        if you == 'r':
            return "you win"
        elif you == 'p':
            return "you loose"
        else:
            return "tie"
    elif comp == 'p':
        if you == 's':
            return "you win"
        elif you == 'r':
            return "you loose"
        else:
            return "tie"

print("comp turn: rock(r),paper(p),or scissor(s)?")
rand_no = random.randint(1,3)
if rand_no == 1:
    comp = 'r'
elif rand_no == 2:
    comp = 's'
elif rand_no == 3:
    comp = 'p'
you = input("your turn: rock(r),paper(p),or scissor(s)?") 
print(f"comp choose {comp}")
print(game(comp,you))