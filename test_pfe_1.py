import re

def test_pfe_1(research):
    matches = 'ab*'
    if re.search(matches, research):
        return 'There is a match'
    else:
        return 'There is no match'

#TEST
print(test_pfe_1("alcindor"))
print(test_pfe_1("lourdvic"))
print(test_pfe_1("kaissens-data"))
print(test_pfe_1("test"))
print(test_pfe_1("datascience"))