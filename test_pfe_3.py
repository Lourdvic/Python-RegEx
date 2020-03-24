import re

def test_pfe_3(research):
    matches = 'a.*?b$'
    if re.search(matches, research):
        return "Match"
    else:
        return 'No Match'

#TEST
print(test_pfe_3("Alcindorb"))
print(test_pfe_3("alcindorb"))
print(test_pfe_3("Lourdvicb"))
print(test_pfe_3("Kaissens-Datab"))
print(test_pfe_3("testB"))
print(test_pfe_3("DaTaScienceb"))