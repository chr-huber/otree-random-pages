from otree.api import *


doc = """
Random Page Sequence with Blocks
"""


class C(BaseConstants):
    NAME_IN_URL = 'randompagesblocks'
    PLAYERS_PER_GROUP = None
    # NUM_ROUNDS = 1

    BLOCKS = ['A', 'B']  # define BLOCKS
    PAGES = [1, 2, 3]         # define PAGES

    NUM_ROUNDS = len(PAGES)*len(BLOCKS)
    print("---")
    print("New session:")
    print("There are", NUM_ROUNDS, "rounds in total, split into", len(BLOCKS), "blocks with", len(PAGES), "pages each:")

    PAGES_BLOCKS = []
    for b in BLOCKS:
        for p in PAGES:
            PAGES_BLOCKS.append(b + str(p))
    print(PAGES_BLOCKS)
    print("---")


def creating_session(subsession):
  
  import random

  if subsession.round_number == 1:
  
    for p in subsession.get_players():
  
        round_numbers = list(range(1, C.NUM_ROUNDS+1))

        # randomize blocks
        block_numbers = list(range(1, len(C.BLOCKS)+1))
        random.shuffle(block_numbers)
        print("Player", p.id_in_subsession, "block sequence:", block_numbers)

        # randomize page within each block 
        page_numbers = list(range(1, len(C.PAGES)+1))
        random.shuffle(page_numbers)
        print("Player", p.id_in_subsession, "page sequence within blocks:", page_numbers)

        # generate round order from randomized blocks and pages:
        round_numbers_randomized = []
        for block in block_numbers:
            for page in page_numbers:
                round_numbers_randomized.append(len(page_numbers) * block + page - len(page_numbers))    

        print("Player", p.id_in_subsession , "round sequence:", round_numbers_randomized, "which translates to pages", [C.PAGES_BLOCKS[i-1] for i in round_numbers_randomized])

        p.participant.vars['round_numbers_randomized_dict'] = dict(zip(C.PAGES_BLOCKS, round_numbers_randomized))
        print("Player", p.id_in_subsession, "round dictionary:", p.participant.vars['round_numbers_randomized_dict'])
        print("---")

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class PageA1(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['round_numbers_randomized_dict']['A1']

class PageA2(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['round_numbers_randomized_dict']['A2']

class PageA3(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['round_numbers_randomized_dict']['A3']

class PageB1(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['round_numbers_randomized_dict']['B1']

class PageB2(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['round_numbers_randomized_dict']['B2']

class PageB3(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['round_numbers_randomized_dict']['B3']


page_sequence = [PageA1, PageA2, PageA3, PageB1, PageB2, PageB3]
