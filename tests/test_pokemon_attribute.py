
HEIGHT = 5
WEIGHT = 90
NAME = "squirtle"

def test_pokemon_attribute(pokemon_info):
  assert pokemon_info['name'] == NAME
  assert pokemon_info['height'] == HEIGHT
  assert pokemon_info['weight'] == WEIGHT
