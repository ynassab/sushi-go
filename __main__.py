from skeleton import *
from time import sleep

drafthand1.show()
# drafthand2.show()
# drafthand3.show()

player1board.show()

while True:
    chosen_card = choose()
    drafthand1.show()
    player1board.show()
    print('waiting for other players ...')
    sleep(1)  # simulate players taking turns
    print('you chose:', chosen_card.name)
    player1board.flip()
    drafthand1.show()
    player1board.show()

    # end game and count points
    if len(drafthand1.cards) == 0:
        print('game over! time to count points!')

        total_points = 0

        # nigiri
        for card in player1board.cards:
            if 'nigiri' in card.name:
                print('\t', card.name, ':', card.points)
                total_points += card.points

        # dumplings
        num_dumplings = sum([1 for card in player1board.cards if 'dumpling' in card.name])
        if num_dumplings <= 5:
            dumpling_points = sum([i+1 for i in range(num_dumplings)])  # 1, 3, 6, 10, 15
        else:
            dumpling_points = 15  # doesn't go higher than 15
        if dumpling_points:  # i.e. non-zero
            print('\t', 'dumplings *', num_dumplings, ':', dumpling_points)
        total_points += dumpling_points

        # tempura
        num_tempura = sum([1 for card in player1board.cards if 'tempura' in card.name])
        tempura_points = num_tempura // 2 * 5  # every two tempura = 5 points
        if tempura_points:
            print('\t', 'tempura *', num_tempura, ':', tempura_points)
        total_points += tempura_points

        # sashimi
        num_sashimi = sum([1 for card in player1board.cards if 'sashimi' in card.name])
        sashimi_points = num_sashimi // 3 * 10  # every three sashimi = 10 points
        if sashimi_points:
            print('\t', 'sashimi *', num_sashimi, ':', sashimi_points)
        total_points += sashimi_points

        # total
        print('\t', 'total points : ', total_points)
        print('good game!')
        break
