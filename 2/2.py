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

def get_games_from_lines(lines):
    lines = [re.sub('Game ', '', line) for line in lines]
    numbered_lines = [line.split(':') for line in lines]
    games = {}
    for line in numbered_lines:
        games[line[0]] = (re.sub('\n', '', line[1]))
    return games

def get_tallies_from_games(games):
    return [(key, tally_game(game)) for (key, game) in zip(games.keys(), games.values())]
 
def get_min_tally_from_tallies(tallies):
    mins = [0, 0, 0]
    for tally in tallies[1]:
        mins[0] = max(mins[0], tally['red'])
        mins[1] = max(mins[1], tally['green'])
        mins[2] = max(mins[2], tally['blue'])
    return (tallies[0], {'red': mins[0], 'green': mins[1], 'blue': mins[2]})

#  Part 1 
with open('2-input.txt', 'r') as f:
    games = get_games_from_lines(f.readlines())
    tallies = get_tallies_from_games(games)
    ids = [int(id) for (id, tally) in tallies if all([is_possible(t) for t in tally])]
    print(f'PART 1: {sum(ids)}')

#  Part 2
with open('2-input.txt', 'r') as f:
    games = get_games_from_lines(f.readlines())
    tallies = get_tallies_from_games(games)
    min_tallies = [get_min_tally_from_tallies(t) for t in tallies]
    powers = [t['red'] * t['green'] * t['blue'] for (id, t) in min_tallies]
    print(powers)
    print(f'PART 2: {sum(powers)}')
