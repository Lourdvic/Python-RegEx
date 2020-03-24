import re

research = "Comment, dit-on ;soutien-gorge\n en créole\t ? S-a_k@a&né&né"

splited = re.split(';| , | \* |\n |\t |-|_|&|@', research)
print(splited)
