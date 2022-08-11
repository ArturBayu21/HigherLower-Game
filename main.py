import art
import game_data
import random
import os


def show_update_score(score):
    print(f"Your score is {score}")


# this below can be shorted by using random.choice
def get_comparison():
    '''return data of the object comparison such as name, followers, follower count, and country'''
    random_num = random.randint(0, len(game_data.data)-1)
    comparison = game_data.data[random_num]
    return comparison


score = 0
game_continue = True
while game_continue == True:
    print(art.logo)
    # when user get no score
    if score == 0:
        # get compare A
        compare_a = get_comparison()
    else:
        show_update_score(score)
    # when user already scores
    print(
        f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    print(art.vs)
    # get compare B
    compare_b = get_comparison()
    # checking wheather A is equal to B, if so, get a new B
    while compare_a == compare_b:
        compare_b = get_comparison()
    print(
        f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}")
    # getting the comparison's winner
    if compare_a['follower_count'] > compare_b['follower_count']:
        comparison_winner = compare_a
    else:
        comparison_winner = compare_b
    # user guessing
    user_input = input("Who has more followers? type 'A' or 'B' : ").lower()
    # transforming the user input
    correct_input = True
    if user_input == 'a':
        user_guess = compare_a
    elif user_input == 'b':
        user_guess = compare_b
    else:
        print("Input is not valid")
        correct_input = False
        game_continue = False
    # checking the user input correct or not
    if correct_input:
        if user_guess == comparison_winner:
            score += 1
            compare_a = compare_b
            os.system('cls')
        else:
            os.system('cls')
            print(art.logo)
            print(f"Sorry, that's wrong, finnal score: {score}")
            game_continue = False
