from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is a standard 2-player my_trust game where the amount sent by player 1 gets
tripled. The my_trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'my_trust/instructions.html'

    # Initial amount allocated to players
    endowment_Decider = c(9)
    endowment_Receiver = c(1)
    multiplier = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment_Decider-2,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=c(0), max=Constants.endowment_Decider-2,
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = (Constants.endowment_Decider - self.sent_amount) *( Constants.endowment_Receiver + self.sent_back_amount )
        p2.payoff = (Constants.endowment_Decider - self.sent_back_amount) *( Constants.endowment_Receiver + self.sent_amount )


class Player(BasePlayer):

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
