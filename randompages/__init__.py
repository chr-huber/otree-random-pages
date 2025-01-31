from otree.api import *


doc = """
Random Page Sequence
"""


class C(BaseConstants):
    NAME_IN_URL = 'randompages'
    PLAYERS_PER_GROUP = None
    # NUM_ROUNDS = 1
    PAGES = ['1', '2', '3']
    NUM_ROUNDS = len(PAGES)


def creating_session(subsession):
  import random
  if subsession.round_number == 1:
    for p in subsession.get_players():
      round_numbers = list(range(1, C.NUM_ROUNDS+1))
      random.shuffle(round_numbers)
      print("Player ", p.id_in_subsession, "page sequence: ", round_numbers)
      p.participant.vars['page_rounds'] = dict(zip(C.PAGES, round_numbers))
      print("Player ", p.id_in_subsession, "zipped list: ", p.participant.vars['page_rounds'])



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class Page1(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['page_rounds']['1']

class Page2(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['page_rounds']['2']

class Page3(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['page_rounds']['3']


page_sequence = [Page1, Page2, Page3]
