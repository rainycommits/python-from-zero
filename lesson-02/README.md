# Lesson 02 · Variables

▶ Video: coming soon

**In this lesson:** you store values in variables and change them, and our hero from
lesson 1 gets a character card with health, power and gold.

## You learn

- variables: a name for a value (`name = "Rain"`)
- kinds of values: `int`, `float`, `str`, `bool`, and `type()` to check them
- changing values: `gold = gold + 50`, `+=`, `-=`
- clear names in snake_case (`hero_class`, `max_hp`)

## Where games use this

Every online game keeps each player's health, gold, level and XP in variables on the server.
When you open a chest or take a hit, one of those values changes, just like `gold += 15` here.

## Run it

```
python main.py
```

## Try it yourself

1. Add `mana = 30` to the card.
2. Cast a spell: `mana -= 10`, and show mana on the card after the battle.
3. Give your hero a different name and class.

Example answer: [`solution.py`](solution.py). Try first, peek later.

**Next lesson:** input & strings, the player names their own hero.
