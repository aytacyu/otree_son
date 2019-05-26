from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2 """

    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1
    def vars_for_template(self):
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2)
        }


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):

        return {

            'earnings': Constants.endowment_Receiver + self.group.sent_amount,
            'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2)
        }
    """
    def sent_back_amount_max(self):
        return 1 + self.group.sent_amount
    """

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'player1_period1_amount': Constants.endowment_Decider - self.group.sent_amount,
            'player1_period2_amount': Constants.endowment_Receiver + self.group.sent_back_amount,
            'player2_period1_amount': Constants.endowment_Receiver + self.group.sent_amount,
            'player2_period2_amount': Constants.endowment_Decider - self.group.sent_back_amount
        }

class OverallResults(Page):
    """This page displays the end of game data """

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        return {
            'overall_earnings': cumulative_payoff
        }


class Survey(Page):
    """This page displays the questionnaire for each player"""

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['department','age','gender','average_monthly_income',
                   'Choice_of_investment_options',
                   'Choice_of_investment_options2',
                   'Choice_of_investment_options3',
                   'Choice_of_investment_options4',
                   'Choice_of_investment_options5',
                   'Choice_of_investment_options6',
                   'Choice_of_investment_options7',
                   'Choice_of_investment_options8',
                   'Choice_of_investment_options9',
                   'Choice_of_investment_options10'
                   ]

page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
    OverallResults,
    Survey
]
