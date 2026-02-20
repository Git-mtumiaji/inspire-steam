# Name : Ronnie Muturi
# Date : 19/02/2026

# PROBLEM 1:When a character kicks another character, the opponent gets more damage than what the character deals. Once this problem is solved, the final health of the warrior after taking damage should be 120

class FighterCharacter:

    def __init__ (self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

    def report_status(self):
        print(f"\nCharacter Log: \n Role: {self.character_role} \n Health: {self.character_health} \n Damage: {self.character_damage} \n Speed: {self.character_speed}\n __ \n")

    def kick(self, opponent):

        character_damage = self.character_damage
        opponent.character_health = opponent.character_health - character_damage
        print(f"Game Log: {self.character_role} deals a damage of {character_damage} to the {opponent.character_role}.")

    def takle(self, opponent):

        character_speed = self.character_speed
        opponent.character_speed = opponent.character_speed - (character_speed/2)
        print(f"Game log: {self.character_role} used tackle which reduced his speed to {opponent.character_speed}")
        # implement this so that the opponent's charater_speed is reduced by the damager dealt by the fighter
        # For instance, if the ninja's speed is 120, a takle from the warrior should reduce their speed to 80
        # Remember to remove the pass below before running your trial
        



ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("Warrior", health=160, damage=80, speed=80)


ninja_character.report_status()
warrior_character.report_status()

ninja_character.run("Up")
ninja_character.kick(warrior_character)

ninja_character.report_status()
warrior_character.report_status()

warrior_character.takle(ninja_character)

ninja_character.report_status()
warrior_character.report_status()