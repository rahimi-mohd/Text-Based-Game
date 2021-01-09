from random import randint
import time
from art import *

def fullEnemyEnergy():
    return randint(enemy['energy_min'], enemy['energy_max'])

def run(player, enemy):
    print(f"{player['name']} try to run, {enemy['name']} try to avoid that by using Energy.")
    time.sleep(2)
    if player['energy'] > fullEnemyEnergy():
        return "Run succesfully"

    else:
        print("You don't have enough energy!")
        time.sleep(2)
        return fight_action(player, enemy)

def fight_action(player, enemy):

    game_on = True
    game_result = []

    def playerAttackVisual():
        print(f'''{player["icon"]}  **======================================> ⚡⚡⚡{enemy["icon"]}⚡⚡⚡''')
        time.sleep(2)
        return "Turn end."


    def enemyAttackVisual():
        print(f'''⚡⚡⚡{player["icon"]}⚡⚡⚡  <======================================**  {enemy["icon"]}''')
        time.sleep(2)
        return "Turn end."

    def fullMonsterAttack():
        return randint(enemy['attack_min'], enemy['attack_max'])

    while game_on:
        #counter = 0 #use for formerly choice 3

        new_round = True
        while new_round:

            #counter += 1 #use for formerly choice 3
            player_won = False
            enemy_won = False

            time.sleep(2)
            print("Please select action")
            time.sleep(1)
            print('1) Attack')
            print('2) Heal')
            #print('3) Show Result')
            print('3) Run')
            pchoice = input()

            if pchoice == '1':
                print(f"{player['name']} turn.")
                time.sleep(2)
                print(f"{player['name']} attack {enemy['name']}!.")
                time.sleep(2)
                print(playerAttackVisual())
                enemy['life'] -= player['attack']
                if enemy['life'] <= 0:
                    player_won = True
                else:
                    print(f"{enemy['name']} turn.")
                    time.sleep(2)
                    print(f"{enemy['name']} attack back.")
                    time.sleep(2)
                    print(enemyAttackVisual())
                    player['life'] -= fullMonsterAttack()
                    if player['life'] <= 0:
                        enemy_won = True

            elif pchoice == '2':
                player['life'] += player['heal']
                print(f"{player['name']} turn, {player['name']} want to heal.")
                print(f"You heal your hp : {player['heal']} point. Turn end.")
                time.sleep(2)
                print(f"{enemy['name']} turn, {enemy['name']} attack you !")
                time.sleep(2)
                player['life'] -= fullMonsterAttack()

            elif pchoice == '3':
                print(run(player, enemy))

            #elif pchoice == '3':
                #for i in game_result:
                    #print(i)

            else:
                print('Invalid input')

            if player_won == False and enemy_won == False:
                print(f"{player['name']} life is: {player['life']}")
                print(f"{enemy['name']} life is: {enemy['life']}")

            elif player_won:
                print("Player won")
                round_result = {'name': player['name'], 'life': player['life'],}
                game_result.append(round_result)
                # print(replay_game())
                new_round = False


            elif enemy_won:
                print("Enemy won")
                round_result = {'name': player['name'], 'life': player['life']}
                game_result.append(round_result)
                # print(replay_game())
                new_round = False

#player stat
player = {'icon' : '🤖','name': '', 'attack': 10, 'life': 100, 'heal': 7, 'energy': 10}
enemy = {'icon' : '👻', 'name': '', 'attack_min': 7, 'attack_max': 10, 'life': 100, 'energy_min': 7, 'energy_max': 20}

tprint("RPG  text  game !!")

player['name'] = input("Please insert your name or press 'enter' to use default name: \n").title()
if player['name'] == '':
    player['name'] = "Krept"

enemy['name'] = input("Please insert enemy name or press 'enter' to use default name: \n").title()
if enemy['name'] == '':
    enemy['name'] = "Gorzon"

#print(f"Player name is {player['name']}, enemy name is : {enemy['name']}") #check for player name

while True:
    c1 = input("You saw an enemy, 'fight' or 'run': \n")
    if c1 == 'fight':
        print(fight_action(player, enemy))
        break
    elif c1 == 'run':
        print(run(player, enemy))
        break
    else:
        print("Invalid input.")
