import numpy
from matplotlib import pyplot as plt
import pandas as pd

player_1_amount = []
player_1_heads = []
player_1_tails = []

player_2_amount = []
player_2_heads = []
player_2_tails = []

player_3_amount = []
player_3_heads = []
player_3_tails = []

player_4_amount = []
player_4_heads = []
player_4_tails = []

player_5_amount = []
player_5_heads = []
player_5_tails = []

player_one = 1000
player_two = 1000
player_three = 1000
player_four = 1000
player_five = 1000
turns = 1

p1_heads = 0
p1_tails = 0
p2_heads = 0
p2_tails = 0
p3_heads = 0
p3_tails = 0
p4_heads = 0
p4_tails = 0
p5_heads = 0
p5_tails = 0

turns_list = []

def Player_one_turn():
    global player_one
    global p1_heads
    global p1_tails
    global player_two
    global player_three
    global player_four
    global player_five
    global turns

    turns = turns + 1
    samples = numpy.random.randint(2, size=1)

    for s in samples:
        if s == 1:
            p1_heads += 1
            player_one += 4
            player_two -= 1
            player_three -= 1
            player_four -= 1
            player_five -= 1
            print(f"Player 1 rolls Heads\n")

            player_1_heads.append(p1_heads)
        else:
            p1_tails += 1
            player_one -= 4
            player_two += 1
            player_three += 1
            player_four += 1
            player_five += 1
            print(f"Player 1 rolls Tails\n")

            player_1_tails.append(p1_tails)

    print(f'Player 1 has {player_one}')
    print(f'Player 2 has {player_two}')
    print(f'Player 3 has {player_three}')
    print(f'Player 4 has {player_four}')
    print(f'Player 5 has {player_five}')

    player_1_amount.append(player_one)
    player_2_amount.append(player_two)
    player_3_amount.append(player_three)
    player_4_amount.append(player_four)
    player_5_amount.append(player_five)


def Player_two_turn():
    global player_one
    global player_two
    global p2_heads
    global p2_tails
    global player_three
    global player_four
    global player_five
    global turns

    turns = turns + 1
    samples = numpy.random.randint(2, size=1)

    for s in samples:
        if s == 1:
            p2_heads += 1
            player_two += 4
            player_three -= 1
            player_four -= 1
            player_five -= 1
            player_one -= 1

            print(f"Player 2 rolls Heads\n")
            player_2_heads.append(p2_heads)
        else:
            p2_tails += 1
            player_two -= 4
            player_three += 1
            player_four += 1
            player_five += 1
            player_one += 1
            print(f"Player 2 rolls Tails\n")

            player_2_tails.append(p2_tails)
    print(f'Player 1 has {player_one}')
    print(f'Player 2 has {player_two}')
    print(f'Player 3 has {player_three}')
    print(f'Player 4 has {player_four}')
    print(f'Player 5 has {player_five}')

    player_1_amount.append(player_one)
    player_2_amount.append(player_two)
    player_3_amount.append(player_three)
    player_4_amount.append(player_four)
    player_5_amount.append(player_five)


def Player_three_turn():
    global player_one
    global player_two
    global player_three
    global p3_heads
    global p3_tails
    global player_four
    global player_five
    global turns

    turns = turns + 1
    samples = numpy.random.randint(2, size=1)
    for s in samples:
        if s == 1:
            p3_heads += 1
            player_three += 4
            player_two -= 1
            player_four -= 1
            player_five -= 1
            player_one -= 1
            print(f"Player 3 rolls Heads\n")

            player_3_heads.append(p3_heads)
        else:
            p3_tails += 1
            player_three -= 4
            player_two += 1
            player_four += 1
            player_five += 1
            player_one += 1
            print(f"Player 3 rolls Tails\n")

            player_3_tails.append(p3_tails)

    print(f'Player 1 has {player_one}')
    print(f'Player 2 has {player_two}')
    print(f'Player 3 has {player_three}')
    print(f'Player 4 has {player_four}')
    print(f'Player 5 has {player_five}')

    player_1_amount.append(player_one)
    player_2_amount.append(player_two)
    player_3_amount.append(player_three)
    player_4_amount.append(player_four)
    player_5_amount.append(player_five)


def Player_four_turn():
    global player_one
    global player_two
    global player_three
    global player_four
    global p4_heads
    global p4_tails
    global player_five
    global turns

    turns = turns + 1
    samples = numpy.random.randint(2, size=1)
    for s in samples:
        if s == 1:
            p4_heads += 1
            player_four += 4
            player_five -= 1
            player_two -= 1
            player_three -= 1
            player_one -= 1
            print(f"Player 4 rolls Heads\n")

            player_4_heads.append(p4_heads)
        else:
            p4_tails += 1
            player_four -= 4
            player_five += 1
            player_two += 1
            player_three += 1
            player_one += 1
            print(f"Player 4 rolls Tails\n")

            player_4_tails.append(p4_tails)

    print(f'Player 1 has {player_one}')
    print(f'Player 2 has {player_two}')
    print(f'Player 3 has {player_three}')
    print(f'Player 4 has {player_four}')
    print(f'Player 5 has {player_five}')

    player_1_amount.append(player_one)
    player_2_amount.append(player_two)
    player_3_amount.append(player_three)
    player_4_amount.append(player_four)
    player_5_amount.append(player_five)


def Player_five_turn():
    global player_one
    global player_two
    global player_three
    global player_four
    global player_five
    global p5_heads
    global p5_tails
    global turns

    turns = turns + 1
    samples = numpy.random.randint(2, size=1)
    for s in samples:
        if s == 1:
            p5_heads += 1
            player_five += 4
            player_four -= 1
            player_two -= 1
            player_three -= 1
            player_one -= 1
            print(f"Player 5 rolls Heads\n")

            player_5_heads.append(p5_heads)

        else:
            p5_tails += 1
            player_five -= 4
            player_four += 1
            player_two += 1
            player_three += 1
            player_one += 1
            print(f"Player 5 rolls Tails\n")

            player_5_tails.append(p5_tails)

    print(f'Player 1 has {player_one}')
    print(f'Player 2 has {player_two}')
    print(f'Player 3 has {player_three}')
    print(f'Player 4 has {player_four}')
    print(f'Player 5 has {player_five}')

    player_1_amount.append(player_one)
    player_2_amount.append(player_two)
    player_3_amount.append(player_three)
    player_4_amount.append(player_four)
    player_5_amount.append(player_five)

while player_one != 0 and player_two != 0 and player_three != 0 and player_four != 0 and player_five !=0:
#while player_one + player_two > 1 or player_one + player_three > 1 or player_two + player_three > 1 or player_four + player_two > 1 or player_four + player_one > 1:
    Player_one_turn()
    print(f'Turn {turns}\n')
    turns_list.append(turns)

    Player_two_turn()
    print(f'Turn {turns}\n')
    turns_list.append(turns)

    Player_three_turn()
    print(f'Turn {turns}\n')
    turns_list.append(turns)

    Player_four_turn()
    print(f'Turn {turns}\n')
    turns_list.append(turns)

    Player_five_turn()
    print(f'Turn {turns}\n')
    turns_list.append(turns)

df2 = pd.DataFrame()
df2['Player_1_amount'] = pd.Series(player_1_amount)
df2['Player_1_heads'] = pd.Series(player_1_heads)
df2['Player_1_tails'] = pd.Series(player_1_tails)

df2['Player_2_amount'] = pd.Series(player_2_amount)
df2['Player_2_heads'] = pd.Series(player_2_heads)
df2['Player_2_tails'] = pd.Series(player_2_tails)

df2['Player_3_amount'] = pd.Series(player_3_amount)
df2['Player_3_heads'] = pd.Series(player_3_heads)
df2['Player_3_tails'] = pd.Series(player_3_tails)

df2['Player_4_amount'] = pd.Series(player_4_amount)
df2['Player_4_heads'] = pd.Series(player_4_heads)
df2['Player_4_tails'] = pd.Series(player_4_tails)

df2['Player_5_amount'] = pd.Series(player_5_amount)
df2['Player_5_heads'] = pd.Series(player_5_heads)
df2['Player_5_tails'] = pd.Series(player_5_tails)

df2['Turns'] = pd.Series(turns_list)
print(df2["Turns"])
ax = plt.gca()



df2.plot(kind='line', x="Turns", y="Player_1_amount", color='red', ax=ax)
plt.title("Coin Flip Game")
plt.xlabel("Number of turns")
plt.ylabel("$ held by player")
df2.plot(kind='line', x='Turns', y="Player_2_amount", color='blue', ax=ax)
df2.plot(kind='line', x='Turns', y="Player_3_amount", color='black', ax=ax)
df2.plot(kind='line', x='Turns', y="Player_4_amount", color='yellow', ax=ax)
df2.plot(kind='line', x='Turns', y="Player_5_amount", color='green', ax=ax)

plt.show()










