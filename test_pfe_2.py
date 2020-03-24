import re

def test_pfe_2(research):
    matches = '[A-Z]+[a-z]+$'
    if re.search(matches, research):
        return "Found"
    else:
        return "Not Found"

#TEST
print(test_pfe_2("Alcindor"))
print(test_pfe_2("Lourdvic"))
print(test_pfe_2("Kaissens-Data"))
print(test_pfe_2("test"))
print(test_pfe_2("DaTaScience"))