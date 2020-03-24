import re

#date with the "/"
slash = "Question posée le 12/12/2012 : Pourquoi les Martiens ne renversent-ils jamais de café sur la table ? | " \
           "Réponse : Parce qu'ils ont des soucoupes ! "

dates = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", slash)

for s in dates:
    print(s)

#ful date with the month in letter
full_date = "Question asked the 14 May 2015: Quel est la date de la fête des fumeurs ? | Réponse : Le 1 Juin 1850"

fd = re.findall(r"[\d]{1,2} [JFMASOND]\w* [\d]{4}", full_date)

for f in fd:
    print(f)

crop_date = "Un jour, le 01 JAN 0000 : Dieu dit à Casto de ramer | Et depuis, Castorama"

cd = re.findall(r"[\d]{1,2}\s (?:JAN|FEB|FEV|MAR|AVR|APR|MAI|MAY|JUN|JUL|AUG|AOU|SEP|OCT|NOV|DEC)\s [\d]{4}", crop_date)

for c in cd:
    print(c)


#date with the dash
dash = "Vous connaissez l'histoire de l'armoire datant du 25-07-18 " \
           "Elle n'est pas commode... "

dash_date = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2}", dash)

for d in dash_date:
    print(d)
