import re

def flatten(l):
    return [item for sublist in l for item in sublist]

def tally_game(game): 
    count = {'red': 0, 'green': 0, 'blue': 0}     
    steps = [step[1:].split(' ') for step in game]
    for step in steps:
        count[step[1]] += int(step[0])
    return count

def game_is_possible(tally): 
    return tally['red'] <= 12 and tally['green'] <= 13 and tally['blue'] <= 14

#  Part 1 
with open('2-input.txt', 'r') as f:
    lines = [re.sub('Game ', '', line) for line in f.readlines()]
    numbered_lines = [line.split(':') for line in lines]
    games = {} 
    for line in numbered_lines:
        games[line[0]] = (re.sub('\n', '', ','.join(line[1].split(';'))).split(','))
    tallies = [(key, tally_game(game)) for (key, game) in zip(games.keys(), games.values())]
    ids = [int(tally[0]) for tally in tallies if not game_is_possible(tally[1])]
    print(ids)
    for line in [(tally, game_is_possible(tally[1])) for tally in tallies]:
        print(line)
    print(f'PART 1: {sum(ids)}')
