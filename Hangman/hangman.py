import random
from string import ascii_lowercase
word_list = ['python', 'java', 'kotlin', 'javascript']


def get_word():
    word = random.choice(word_list)
    return word.lower()


def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    tries = 8
    print("H A N G M A N")
    print('Type "play" to play the game, "exit" to quit: >' + input())
    print("")
    print(word_completion)
    while not guessed and tries > 0:
        guess = input("Input a letter: ")
        if len(guess) == 1 and guess.isalpha() and guess in ascii_lowercase:

            if guess in guessed_letters:
                print("You've already guessed this letter")

            elif guess not in word:
                print("That letter doesn't appear in the word")
                tries -= 1
                guessed_letters.append(guess)
                if tries == 0:
                    print("You lost!")
            else:
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True

        elif len(guess) != 1:
            print("You should input a single letter")

        elif guess not in ascii_lowercase:
            print("Please enter a lowercase English letter")

        if tries > 0:
            print("")
            print(word_completion)

    if guessed:
        print("You guessed the word!")
        print("You survived!")


def main():
    word = get_word()
    play(word)
    while input('Type "play" to play the game, "exit" to quit: >') == "play":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
