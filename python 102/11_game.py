import random

print("[ 🤖 Welcome to game Rock, Paper o Scissors 🙋] >>> Select Option <<<\n")
result = {
    "rock": {"scissors": 1, "paper": 0},
    "paper": {"scissors": 0, "rock": 1},
    "scissors": {"paper": 1, "rock": 0},
}


def choose_options():
    options = ("rock", "paper", "scissors")
    user_option = input(">>> rock, paper o scissors => ").lower()

    if not user_option in options:
        print("Erro Error Invalid Option")
        # continue
        return None, None

    computer_option = random.choice(options)

    print("User option => ", user_option)
    print("Computer option => ", computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Draw!\n")

    else:
        ganador = result[user_option][computer_option]
        if ganador:
            print("{} Kill  {}".format(user_option, computer_option))
            print("¡User Win!\n")
            user_wins += 1
        else:
            print("{} Kill  {}".format(computer_option, user_option))
            print("¡Computer Win!\n")
            computer_wins += 1

    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    print(
        f"""
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
            """
    )

    if user_wins == 3:
        print('"🎖️ The Winner is User "️')
        exit()

    if computer_wins == 3:
        print("🎖️ The Winner is Computer")
        exit()


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print("***" * 10)
        print("Round ", rounds)
        print("***" * 10)

        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins
        )
        check_winner(user_wins, computer_wins)


run_game()
