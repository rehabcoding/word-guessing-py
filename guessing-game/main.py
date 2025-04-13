import random

word_bank = [
    'cat', 'run', 'car', 'dog', 'sun', 'pen', 'bed', 'mug', 'book', 'keys',
    'milk', 'door', 'shoe', 'soap', 'rain', 'walk', 'dish', 'fork', 'home', 'sink',
    'phone', 'apple', 'table', 'chair', 'spoon', 'brush', 'water', 'shirt', 'clock', 'towel',
    'light', 'jeans', 'movie', 'stairs', 'cereal', 'bottle', 'wallet', 'window', 'blanket', 'sweater',
    'charger', 'backpack', 'notebook', 'umbrella', 'calendar', 'sandwich', 'microwave', 'television',
    'refrigerator', 'toothpaste', 'dishwasher'
]

word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
        
        if '_' not in guessedWord:
            print('\nCongratulations!! You guessed the word: ' + word)
            break

    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)