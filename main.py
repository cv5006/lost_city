import random 

class Card: 
    def __init__(self, num):
        self.number = num
    
    def compare(self, card) -> bool:
        return self.number > card.number

class Deck:
    def __init__(self):
        self.cards = [] # Q: How to tell what this list will be filled with in python?

    def add(self, card: Card):  # 한 장 더하기
        self.cards.append(card)
    
    def pop_random(self) -> Card: # 랜덤으로 한 장 빼기
        return self.cards.pop(random.randint(0, len(self.cards))) # 랜덤으로 한 장 빼기; 뺀 한장 저장
    
    def pop_select(self, index) -> Card: # 지정한 카드 한 장 빼기 
        return self.cards.pop(index)  
    
    def shuffle(self) : # 카드 섞기
        random.shuffle(self.cards)
        
class Player: 
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.deck = Deck()

    def open_card(self) : # Open the first card
        return self.deck.pop_select(0)
        
class Table: 
    def __init__(self) :
        self.player1 = Player('hy')
        self.player2 = Player('hw')
        self.share_deck = Deck()
        for i in range(0, 11): # 카드 생성 
            self.share_deck.add(Card(i))
        
        self.share_deck.shuffle() # 카드 셔플 
    
    def player_greeting(self):
        print(f'Player {self.player1.name} says Hi!')
        print(f'Player {self.player2.name} says Hello!')

if __name__ == '__main__':
    ## Init game
    print('***** Game Start *****')
    table = Table()
    table.player_greeting()
    print()

    ## Play Round
    print('***** Round 1 *****')
    # Card Distribution
    print('Distribute Cards')
    card_for_player1 = table.share_deck.pop_random()
    table.player1.deck.add(card_for_player1)
    print(f'Player {table.player1.name} get {card_for_player1.number}')

    card_for_player2 = table.share_deck.pop_random()
    table.player2.deck.add(card_for_player2)
    print(f'Player {table.player1.name} get {card_for_player2.number}')
    print()

    # Card Comparision
    print('Compair Cards')
    card_of_player1 = table.player1.open_card()
    print(f'Player {table.player1.name} opened {card_for_player1.number}')

    card_of_player2 = table.player2.open_card()
    print(f'Player {table.player2.name} opened {card_for_player2.number}')
    
    if card_of_player1.compare(card_of_player2): # 플레이어 1의 카드가 더 큼.
        table.player1.score+=1
        print(f'Player {table.player1.name} get 1 point!')
    else :  # 플레이어 2의 카드가 더 큼.
        table.player2.score+=1
        print(f'Player {table.player2.name} get 1 point!')
    
    print('Round Ends')
    print()
    
    print('***** Game End *****')
    print('Final score:')
    print(f'Player {table.player1.name} : {table.player1.score}')
    print(f'Player {table.player2.name} : {table.player2.score}')
    winner = table.player1.name if (table.player1.score>table.player2.score) else table.player2.name
    print(f'Winner: {winner}')
    