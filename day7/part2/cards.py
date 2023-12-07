#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

class CardHand:
    """
    A class to represent a card hand.

    ...

    Instance Attributes
    -------------------
    hand : str
        hand of cards
    bid : int
        bid for the hand of cards
    type : str
        type of hand

    Class Attributes
    ----------------
    ORDER : dict(str:int)
        order of hand types
    STRENGTH : dict(str:int)
        strength of cards
    """

    ORDER = {"high card":1,"one pair":2,"two pair":3,
             "three of a kind":4,"full house":5,
             "four of a kind":6,"five of a kind":7}

    STRENGTH = {"J":1,"2":2,"3":3,"4":4,"5":5,
                "6":6,"7":7,"8":8,"9":9,
                "T":10,"Q":11,"K":12,
                "A":13}

    def __init__(self,hand,bid):
        self.hand = hand
        self.bid = bid 

        # substitute jokers
        unique = set(hand)
        if ("J" in unique):
            unique.remove("J")
            max_card = "J"
            max_num = 0
            while (unique):
                card = unique.pop()
                num_card = hand.count(card)
                if (num_card >= max_num):
                    max_card = card
                    max_num = num_card

            hand = hand.replace("J",max_card)

        unique = set(hand)
        num_unique = len(unique)
        match num_unique:
            case 1:
                self.type = "five of a kind"
            case 2:
                num = hand.count(unique.pop())
                if (num in {1,4}):
                    self.type = "four of a kind"
                else:
                    self.type = "full house"
            case 3:
                num1 = hand.count(unique.pop())
                num2 = hand.count(unique.pop())
                if (num1==2 or num2==2):
                    self.type = "two pair"
                else:
                    self.type = "three of a kind"
            case 4:
                self.type = "one pair"
            case 5:
                self.type = "high card"

    def __eq__(self,other):
        return self.hand == other.hand

    def __neq__(self,other):
        return self.hand != other.hand

    def __lt__(self,other):
        equal_type = (self.type == other.type)
        if (equal_type):
            for ii,card in enumerate(self.hand):
                equal_cards = (card == other.hand[ii])
                if (not equal_cards):
                    return CardHand.STRENGTH[card] < CardHand.STRENGTH[other.hand[ii]]
        else:
            return CardHand.ORDER[self.type] < CardHand.ORDER[other.type]

    def __gt__(self,other):
        equal_type = (self.type == other.type)
        if (equal_type):
            for ii,card in enumerate(self.hand):
                equal_cards = (card == other.hand[ii])
                if (not equal_cards):
                    return CardHand.STRENGTH[card] > CardHand.STRENGTH[other.hand[ii]]
        else:
            return CardHand.ORDER[self.type] > CardHand.ORDER[other.type]

    def __le__(self,other):
        equal_type = (self.type == other.type)
        if (equal_type):
            for ii,card in enumerate(self.hand):
                equal_cards = (card == other.hand[ii])
                if (not equal_cards):
                    return CardHand.STRENGTH[card] <= CardHand.STRENGTH[other.hand[ii]]
        else:
            return CardHand.ORDER[self.type] <= CardHand.ORDER[other.type]

    def __ge__(self,other):
        equal_type = (self.type == other.type)
        if (equal_type):
            for ii,card in enumerate(self.hand):
                equal_cards = (card == other.hand[ii])
                if (not equal_cards):
                    return CardHand.STRENGTH[card] >= CardHand.STRENGTH[other.hand[ii]]
        else:
            return CardHand.ORDER[self.type] >= CardHand.ORDER[other.type]


hands = []
with open(fname,"r") as file:
    for line in file:
        hand,bid = line.split()
        card_hand = CardHand(hand,int(bid))
        hands.append(card_hand)

hands.sort()
print(sum([card_hand.bid*(ii+1) for ii,card_hand in enumerate(hands)]))
