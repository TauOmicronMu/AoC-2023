import re

def flatten(l):
    return [item for sublist in l for item in sublist]

def tally_game(game): 
    return [tally_run(run) for run in game.split(';')]

def tally_run(run): 
    count = {'red': 0, 'green': 0, 'blue': 0}     
    for step in run.split(','):
        amt, colour = step[1:].split(' ')
        count[colour] += int(amt)
    return count

def is_possible(tally): 
    return tally['red'] <= 12 and tally['green'] <= 13 and tally['blue'] <= 14

#  Part 1 
with open('2-input.txt', 'r') as f:
    lines = [re.sub('Game ', '', line) for line in f.readlines()]
    numbered_lines = [line.split(':') for line in lines]
    games = {} 
    for line in numbered_lines:
        games[line[0]] = (re.sub('\n', '', line[1]))
    tallies = [(key, tally_game(game)) for (key, game) in zip(games.keys(), games.values())]
    ids = [int(id) for (id, tally) in tallies if all([is_possible(t) for t in tally])]
    print(f'PART 1: {sum(ids)}')
