from gtts import gTTS
import os
import random


text ='Global warming is the long-term rise in the average temperature of the Earth climate system'

language = 'en'

yup = 'Gay double faggot fucker 97 plus three'

first_list = ['douche', 'faggot', 'slut', 'cock bag']
second_list = ['gazelle', 'dumpster', 'cock bag']
third_list = ['97', '12', '69. . .  haha', '32', '912']

# third = '69haha'


first = random.choice(first_list)
second = random.choice(second_list)
third = random.choice(third_list)

the_string = f'{first} {second} {third}'

speech = gTTS(text = the_string, lang=language, slow=False)

speech.save('u8.mp3')

os.system('start u8.mp3')
