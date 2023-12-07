import re 
from collections import Counter
from enum import Enum
from functools import total_ordering

STRENGTHS = [str(c) for c in list(range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']]

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
    

with open('input-7.txt', 'r') as f: 
    lines = f.readlines() 
    hands = [line.split() for line in lines] 
    counted_hands = [(hand[0], Counter(hand[0]).most_common(), hand[1]) for hand in hands]
    typed_hands = [(hand, get_hand_type(hand)) for hand in counted_hands] 
    sorted_hands = sorted(typed_hands, key = lambda t_hand: (t_hand[1], STRENGTHS.index(t_hand[0][0][0]), STRENGTHS.index(t_hand[0][0][1]), STRENGTHS.index(t_hand[0][0][2]), STRENGTHS.index(t_hand[0][0][3]), STRENGTHS.index(t_hand[0][0][4])))
    winnings = [(sorted_hands.index(s_hand) + 1) * int(s_hand[0][2]) for s_hand in sorted_hands]
    print(f'PART ONE: {sum(winnings)}')
