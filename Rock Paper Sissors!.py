import random
def play():
    user = input("What you got?'r' for rock, 'p' for paper, 's' for sissors")
    computer = random.choice (['r', 'p', 's'])
    
    if user == computer:
        return 'AWWWW IT\'S A TIE...'
    
    if is_win (user, computer):
        return 'WOOHOO YOU WIN!'
    return 'HAHAHA YOU LOST!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True