# Data for each character
char_1_name = "Jadhav"
char_1_health = 100

char_2_name = "Likitha"
char_2_health = 90

# function to take player health
def take_damage(health, amount):
    new_health = health - amount
    return new_health

char_1_health = take_damage(char_1_health, 20)
print(f"{char_1_name} has {char_1_health} HP/Points left.")

char_2_health = take_damage(char_2_health, 20)
print(f"{char_2_name} has {char_2_health} HP/Points left.")