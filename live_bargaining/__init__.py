from otree.api import *
import random

doc = """
For oTree beginners, it would be simpler to implement this as a discrete-time game 
by using multiple rounds, e.g. 10 rounds, where in each round both players can make a new proposal,
or accept the value from the previous round.

However, the discrete-time version has more limitations
(fixed communication structure, limited number of iterations).

Also, the continuous-time version works smoother & faster, 
and is less resource-intensive since it all takes place in 1 page.
"""


class C(BaseConstants):
    NAME_IN_URL = 'live_bargaining'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    TAX = 200
    TAX2 = 10
    PROFIT = 400
    SALARY = 200
    OFFICER_COST = 10
    SELLER_ROLE = 'Importir'
    BUYER_ROLE = 'Petugas Pajak'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    deal_price = models.IntegerField()
    is_finished = models.BooleanField(initial=False)
    chance = models.IntegerField(initial=0)
    penalty = models.IntegerField(initial=0)

class Player(BasePlayer):
    amount_proposed = models.IntegerField()
    amount_accepted = models.IntegerField()
    pay = models.IntegerField(initial=0)
    chance = models.IntegerField(initial=0)
    bribe = models.IntegerField(initial=0, label="Iuran kepada auditor")
    category = models.PositiveIntegerField(choices=[[0, 'Barang Mewah'], [1, 'Barang Non-Mewah']],
                                            widget=widgets.RadioSelectHorizontal,
                                           label="katagori barang")
    payment = models.IntegerField(initial=0)


class Bargain(Page):
    timeout_seconds = 10000
    @staticmethod
    def vars_for_template(player: Player):
        return dict(other_role=player.get_others_in_group()[0].role)

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    @staticmethod
    def live_method(player: Player, data):

        group = player.group
        [other] = player.get_others_in_group()

        if 'amount' in data:
            try:
                amount = int(data['amount'])
            except Exception:
                print('Invalid message received', data)
                return
            if data['type'] == 'accept':
                if amount == other.amount_proposed:
                    player.amount_accepted = amount
                    group.deal_price = amount
                    group.is_finished = True
                    return {0: dict(finished=True)}
            if data['type'] == 'propose':
                player.amount_proposed = amount
            if data['type'] == 'reject':
                if amount == other.amount_proposed:
                    player.amount_accepted = 0
                    group.deal_price = 0
                    group.is_finished = True
                    return {0: dict(finished=True)}

        proposals = []
        for p in [player, other]:
            amount_proposed = p.field_maybe_none('amount_proposed')
            if amount_proposed is not None:
                proposals.append([p.id_in_group, amount_proposed])
        return {0: dict(proposals=proposals)}

    @staticmethod
    def error_message(player: Player, values):
        group = player.group
        if not group.is_finished:
            return "Game not finished yet"

    @staticmethod
    def is_displayed(player: Player):
        """Skip this page if a deal has already been made"""
        group = player.group
        deal_price = group.field_maybe_none('deal_price')
        return deal_price is None

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        group = player.group
        if timeout_happened:
            player.amount_accepted = 0
            player.amount_proposed = 0
            group.deal_price = 0
        pay = group.deal_price
        if player.role == "Importir":
            if pay == 0:
                player.pay = C.PROFIT - C.TAX
            else:
                player.pay = C.PROFIT - C.TAX2 - pay
        else:
            if pay == 0:
                player.pay = C.SALARY
            else:
                player.pay = C.SALARY + pay - C.OFFICER_COST


class Results(Page):
    @staticmethod
    def is_displayed(player):
        return player.role == "Petugas Pajak"
    form_model = 'player'
    form_fields = ['bribe','category']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        group = player.group
        players = group.get_players()
        if player.bribe == 0:
            player.chance = random.randint(1,400)
        else:
            if player.bribe > 180:
                player.bribe = 180
            rand = random.randint(1,400)
            player.chance = rand + player.bribe
        group.chance = sum([p.chance for p in players])


class ResultsWaitPage(WaitPage):
    pass

class Investigation(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        if group.chance < 200:
            group.penalty = 300
        player.payment = player.pay - group.penalty
        if player.payment < 0:
            player.payment = 0



page_sequence = [Bargain, Results, ResultsWaitPage, Investigation]
