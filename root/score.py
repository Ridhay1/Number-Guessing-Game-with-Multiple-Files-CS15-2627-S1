def update_score(current_score, correct_guess):
    if correct_guess:
        return current_score

    new_score = current_score - 10

    if new_score < 0:
        return 0
    else:
        return new_score

def calculate_rating(score):
    if score >= 80:
        return "excellent"
    elif score >= 50:
        return "good i guess"
    else:
        return "Keep practicing( you need it)"

if __name__ == "__main__":

    test_score = 100
    print("initial score:", test_score)

    test_score = update_score(test_score, False)
    print("score after 1 wrong guess:", test_score)

    test_score = update_score(test_score, True)
    print("Score after correct guess:", test_score)

    print("Rating for 85:", calculate_rating(85))
    print("Rating for 60:", calculate_rating(60))
    print("Rating for 30:", calculate_rating(30))
