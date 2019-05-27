from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is a standard 2-player control game where the amount sent by player 1 gets
tripled. The control game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'control'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'control/instructions.html'
    table_template = 'control/table.html'

    # Initial amount allocated to players+
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


    department = models.StringField()


    age = models.StringField(choices=[ '<24','25-34','35-44','45-54', '>55' ],widget=widgets.RadioSelect)


    gender = models.StringField(choices=[ 'Female','Male' ],widget=widgets.RadioSelect)


    average_monthly_income = models.StringField(widget = widgets.RadioSelect)
    def average_monthly_income_choices(self):
        choices = [ '500-1000','1000-2000','2000-3000','3000-4000','4000-5000','5000+']
        return choices

    Choice_of_investment_options = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options_choices(self):
        choices = ['8₺ with probability 1/10 , 6,4₺ with probability 9/10', '15,4₺ with probability 1/10 , 0,4₺ with probability 9/10']
        return choices

    Choice_of_investment_options2 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options2_choices(self):
        choices = ['8₺ with probability 2/10 , 6,4₺ with probability 8/10', '15,4₺ with probability 2/10 , 0,4₺ with probability 8/10']
        return choices

    Choice_of_investment_options3 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options3_choices(self):
        choices = ['8₺ with probability 3/10 , 6,4₺ with probability 7/10', '15,4₺ with probability 3/10 , 0,4₺ with probability 7/10']
        return choices
    Choice_of_investment_options4 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options4_choices(self):
        choices = ['8₺ with probability 4/10 , 6,4₺ with probability 6/10', '15,4₺ with probability 4/10 , 0,4₺ with probability 6/10']
        return choices
    Choice_of_investment_options5 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options5_choices(self):
        choices = ['8₺ with probability 5/10 , 6,4₺ with probability 5/10', '15,4₺ with probability 5/10 , 0,4₺ with probability 5/10']
        return choices
    Choice_of_investment_options6 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options6_choices(self):
        choices = ['8₺ with probability 6/10 , 6,4₺ with probability 4/10', '15,4₺ with probability 6/10 , 0,4₺ with probability 4/10']
        return choices
    Choice_of_investment_options7 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options7_choices(self):
        choices = ['8₺ with probability 7/10 , 6,4₺ with probability 3/10', '15,4₺ with probability 7/10 , 0,4₺ with probability 3/10']
        return choices
    Choice_of_investment_options8 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options8_choices(self):
        choices = ['8₺ with probability 8/10 , 6,4₺ with probability 2/10', '15,4₺ with probability 8/10 , 0,4₺ with probability 2/10']
        return choices
    Choice_of_investment_options9 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options9_choices(self):
        choices = ['8₺ with probability 9/10 , 6,4₺ with probability 1/10', '15,4₺ with probability 2/10 , 0,4₺ with probability 8/10']
        return choices
    Choice_of_investment_options10 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options10_choices(self):
        choices = ['8₺ with probability 0/10 , 6,4₺ with probability 10/10', '15,4₺ with probability 0/10 , 0,4₺ with probability 10/10']
        return choices
