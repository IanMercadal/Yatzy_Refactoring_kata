class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)
        
    @staticmethod
    def chance(*dice):
        total = 0
        for number in dice:
            total += number
        return total

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50
    
    @staticmethod
    def ones(*dice):
        one = 1
        return dice.count(one) * one

    @staticmethod
    def twos(*dice):
        two = 2
        return dice.count(two) * two
    
    @staticmethod
    def threes(*dice):
        three = 3
        return dice.count(three) * three
    
    def fours(self):
        four = 4
        return self.dice.count(four) * four

    def fives(self):
        five = 50
        return self.dice.count(five) * five
    
    def sixes(self):
        six = 6
        return self.dice.count(six) * six
    
    @staticmethod
    def pair(*dice):
        pair = 2
        for numero in range (6, 0, -1):
            if dice.count(numero) >= pair:
                return pair * numero
            return 0
    
    @staticmethod
    def two_pairs(*dice):
        pair = 2
        pairs = 0
        total = 0
        numero = 1
        while pairs < 2 and numero <= 6:
            if dice.count(numero) >= 2:
                pairs += 1
                total += pair * numero
            numero += 1
        if pairs == 2:
            return total
        else:
            return 0
    
    @staticmethod
    def three_of_a_kind(*dice):
        three = 3
        for numero in range (6, 0, -1):
            if dice.count(numero) >= three:
                return three * numero
            return 0
    @staticmethod
    def four_of_a_kind(*dice):
        four = 4
        for numero in range (6, 0, -1):
            if dice.count(numero) >= four:
                return four * numero
            return 0
        
    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0