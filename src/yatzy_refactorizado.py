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
    def small_straight(*dice):
        for numero in range (1, 6):
            if dice.count(numero) != 1:
                return 0
            return Yatzy.chance(*dice)

    @staticmethod
    def large_straight(*dice):
        for numero in range (2, 7):
            if dice.count(numero) != 1:
                return 0
            return Yatzy.chance(*dice)
    ## Aquí van dos clases static que no se muy bien que hacen