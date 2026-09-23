import utils
from score import update_score, calculate_rating

score = 100
secret_number = utils.generate_secret_number()
while True:
    is_correct = utils.check_user_guess(secret_number)

    if is_correct:
        final_rating = calculate_rating(score)
        print(f"final Score: {score}")
        print(f"Rating: {final_rating}")
        break
    else:
        score = update_score(score, False)
        print(f"Current Score is: {score}")

