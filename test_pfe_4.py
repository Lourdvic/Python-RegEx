import re

def test_pfe_4(research):
    matches = "\Bz\B"
    if re.search(matches, research):
        return 'Match'
    else:
        return 'No Match'

#TEST
print(test_pfe_4("azertyuiop"))
print(test_pfe_4("I love dataz"))
print(test_pfe_4("Data is future"))
print(test_pfe_4("Je zozote, tu zozote"))
print(test_pfe_4("Pourquoi quand on veut vizer on ferme un œil ?"))
print(test_pfe_4('Car si on fermait les deux on verrait plus rien !'))