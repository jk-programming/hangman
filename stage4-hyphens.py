# Write your code here

from random import choice

lang_list = ['python', 'java', 'kotlin', 'javascript']

rand_word = choice(lang_list)

rand_word_len = len(rand_word)

num_of_hyphens = rand_word_len - 3

print('H A N G M A N')
print('Guess the word ' + rand_word[:3] + '-' * num_of_hyphens + ': ')
word = input()

if word == rand_word:
    print('You survived!')
else:
    print('You lost!')
