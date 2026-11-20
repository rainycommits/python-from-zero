# Rain Runner: our hero's character card
name = "Rain"
hero_class = "Runner"
level = 1
hp = 100
max_hp = 100
power = 12
gold = 75
xp = 0

print("=" * 32)
print("   CHARACTER CARD")
print("=" * 32)
print("   Name  :", name)
print("   Class :", hero_class)
print("   Level :", level)
print("   HP    :", hp, "/", max_hp)
print("   Power :", power)
print("   Gold  :", gold)
print("=" * 32)

# a battle with a slime
hp -= 18
xp += 40
gold += 15
power += 2   # we learned something

print()
print("=" * 32)
print("   AFTER THE BATTLE")
print("=" * 32)
print("   Name  :", name)
print("   HP    :", hp, "/", max_hp)
print("   Power :", power)
print("   Gold  :", gold)
print("   XP    :", xp)
print("=" * 32)
