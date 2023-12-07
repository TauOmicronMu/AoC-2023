import re 
from collections import Counter
from enum import Enum
from functools import total_ordering

STRENGTHS = ['J'] + [str(c) for c in list(range(2, 10)) + ['T', 'Q', 'K', 'A']]

@total_ordering
class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5  
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __gt__(self, other): 
        if self.__class__ is other.__class__: 
            return self.value > other.value
        return NotImplemented 

def get_hand_type(hand): 
    counter = hand[1] 
    highest_count = counter[0][1]
    if highest_count == 5:
        return HandType.FIVE_OF_A_KIND
    
    second_highest_count = counter[1][1]    
    
    if highest_count == 4: 
        return HandType.FOUR_OF_A_KIND

    if highest_count == 3: 
        if second_highest_count == 2:
            return HandType.FULL_HOUSE
        return HandType.THREE_OF_A_KIND

    if highest_count == 2:
        if second_highest_count == 2: 
            return HandType.TWO_PAIR
        return HandType.ONE_PAIR    

    return HandType.HIGH_CARD 
    
#  Ensures that the leftmost non-joker is what jokers should be replaced with
def sorted_counter(counter):
    return sorted(counter.items(), key=lambda c: (-c[1], STRENGTHS.index(c[0])))

def replace_jokers(hand):
    counter = hand[1] 
    
    if 'J' not in dict(counter).keys():
        return hand 

    jokers = [j for j in counter if j[0] == 'J'][0]
    if jokers[1] == 5:
        return (hand[0], [('A', 5)], hand[2])
 
    counter.remove(jokers)
    counter[0] = (counter[0][0], counter[0][1] + jokers[1]) 
    
    return hand 
    

with open('input-7.txt', 'r') as f: 
    lines = f.readlines() 
    hands = [line.split() for line in lines] 
    counted_hands = [(hand[0], sorted_counter(Counter(hand[0])), hand[1]) for hand in hands]

    #  Replace all jokers with the most common, strongest card(s) 
    replaced_hands = [replace_jokers(hand) for hand in counted_hands]
    
    typed_hands = [(hand, get_hand_type(hand)) for hand in replaced_hands] 
    sorted_hands = sorted(typed_hands, key = lambda t_hand: (t_hand[1], STRENGTHS.index(t_hand[0][0][0]), STRENGTHS.index(t_hand[0][0][1]), STRENGTHS.index(t_hand[0][0][2]), STRENGTHS.index(t_hand[0][0][3]), STRENGTHS.index(t_hand[0][0][4])))
    
    for hand in sorted_hands:
        print(hand)

    winnings = [(sorted_hands.index(s_hand) + 1) * int(s_hand[0][2]) for s_hand in sorted_hands]
    print(f'PART TWO: {sum(winnings)}')
