import re

CARD_PATTERN = r'Card\s*(\d*):(.*)\|(.*)$'

def parse_card(card): 
    matches = re.findall(CARD_PATTERN, card)
    return matches[0]

def clean_card(vals):
    return [int(v) for v in vals.strip().split(" ") if v != '']

def num_winners(winning, candidates):
    return sum([1 for x in candidates if x in winning])

def get_points(num_winners):
    return 2 ** (num_winners - 1) if (num_winners > 0) else 0

def get_listed_cards(): 
    with open('4-input.txt', 'r') as f:
        cards = f.readlines() 
        parsed_cards = [parse_card(card) for card in cards]
        return [(card[0], clean_card(card[1]), clean_card(card[2])) for card in parsed_cards]
    
#  PART 1 
listed_cards = get_listed_cards()
cards_winners = [(card[0], num_winners(card[1], card[2])) for card in listed_cards]
points = [(get_points(card[1])) for card in cards_winners]    
print(f'PART ONE: {sum([p for p in points])}')

#  PART 2
#  Process the listed cards in order
num_to_process = {} 
total_processed = 0
for i in range(len(listed_cards)): 
    print(num_to_process)

    #  NB: i is also the number on the card. 
    
    #  Initialise our 'state' for this scratchcard
    num_to_process[i] = 1 if (i not in num_to_process.keys()) else (num_to_process[i] + 1)

    #  Process them all in order
    while (num_to_process[i]) > 0:
        #  Calculate the number of winners 
        winners = num_winners(listed_cards[i][1], listed_cards[i][2])
        
        #  Work out which scratchcards these correspond to
        extras = range(i+1, i+1+winners)        
        for card_num in extras:
            num_to_process[card_num] = 1 if (card_num not in num_to_process.keys()) else (num_to_process[card_num] + 1)

        total_processed += 1
        num_to_process[i] -= 1 

print(total_processed)    
