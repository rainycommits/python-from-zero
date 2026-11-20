# Try it yourself: an example answer for lesson 02
# A new hero with mana, and a spell that uses it.
name = "Drizzle"
hero_class = "Mage"
level = 1
hp = 80
max_hp = 80
mana = 30
power = 9
gold = 40

print("=" * 32)
print("   CHARACTER CARD")
print("=" * 32)
print("   Name  :", name)
print("   Class :", hero_class)
print("   HP    :", hp, "/", max_hp)
print("   Mana  :", mana)
print("=" * 32)

# cast a spell
mana -= 10
print()
print("   Spell cast! Mana left:", mana)
