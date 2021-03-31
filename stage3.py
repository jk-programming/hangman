# Write your code here

from random import choice

lang_list = ['python', 'java', 'kotlin', 'javascript']

rand_word = choice(lang_list)

print('H A N G M A N')
print('Guess the word: ')
word = input()

if word == rand_word:
    print('You survived!')
else:
    print('You lost!')
