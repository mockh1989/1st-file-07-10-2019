import random

def get_numeric_input(lower, upper):
    user_input = "X"
    while not user_input.isdigit() or int(user_input) < lower or int(user_input) > upper:
        user_input = input('Please enter a number ({}-{}): '.format(lower, upper))
    return int(user_input)

def check_answer(guess_num, ans, lower, upper):
    if guess_num > ans:
        return lower, guess_num - 1
    elif guess_num < ans:
        return guess_num + 1, upper
    else:
        return None, None

# set range
lower = 1
upper = 99
max_trial = 5
# set answer
ans = random.randint(lower, upper)
for i in range(max_trial):
    # ask user to input
    guess_num = get_numeric_input(lower, upper)
    # check answer 
    lower, upper = check_answer(guess_num, ans, lower, upper)
    # check status
    if lower is None:
        print("You win!")
        break
print('Game over')