from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color),
                'round_number': '{}' .format(self.round_number)
        }
class SendBackWaitPage(WaitPage):
    pass


class P8(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2 """

    form_model = 'group'
    form_fields = ['sent_8']

    def is_displayed(self):
        return self.player.id_in_group == 8

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }

class P7(Page):
    """This page is only for P7"""

    form_model = 'group'
    form_fields = ['sent_7']

    def is_displayed(self):
        return self.player.id_in_group == 7

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class P6(Page):
    """This page is only for P6"""

    form_model = 'group'
    form_fields = ['sent_6']

    def is_displayed(self):
        return self.player.id_in_group == 6

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class P5(Page):
    """This page is only for P7"""

    form_model = 'group'
    form_fields = ['sent_5']

    def is_displayed(self):
        return self.player.id_in_group == 5

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class P4(Page):
    """This page is only for P4"""

    form_model = 'group'
    form_fields = ['sent_4']

    def is_displayed(self):
        return self.player.id_in_group == 4

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class P3(Page):
    """This page is only for P3"""

    form_model = 'group'
    form_fields = ['sent_3']

    def is_displayed(self):
        return self.player.id_in_group == 3

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class P2(Page):
    """This page is only for P2"""

    form_model = 'group'
    form_fields = ['sent_2']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'prompt': 'Please an amount from 0 to {}'.format(Constants.endowment_Decider-2),
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }


class P1(Page):
    """This page is only for P4"""

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        partner = self.player.get_others_in_group()[0]
        return {
                'your_color': '{}'.format(self.player.color),
                'partner_color': '{}'.format(partner.color)
        }



class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {

            'p2_transfer': self.group.sent_2,
            'p3_transfer': self.group.sent_3,
            'p4_transfer': self.group.sent_4,
            'p5_transfer': self.group.sent_5,
            'p6_transfer': self.group.sent_6,
            'p7_transfer': self.group.sent_7,
            'p8_transfer': self.group.sent_8,

            'p1_receiver': Constants.endowment_Receiver + self.group.sent_2,
            'p2_decider': Constants.endowment_Decider - self.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + self.group.sent_3,
            'p3_decider': Constants.endowment_Decider - self.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + self.group.sent_4,
            'p4_decider': Constants.endowment_Decider - self.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + self.group.sent_5,
            'p5_decider': Constants.endowment_Decider - self.group.sent_5,
            'p5_receiver': Constants.endowment_Receiver + self.group.sent_6,
            'p6_decider': Constants.endowment_Decider - self.group.sent_6,
            'p6_receiver': Constants.endowment_Receiver + self.group.sent_7,
            'p7_decider': Constants.endowment_Decider - self.group.sent_7,
            'p7_receiver': Constants.endowment_Receiver + self.group.sent_8,
            'p8_decider': Constants.endowment_Decider - self.group.sent_8,

            'p1.payoff': self.group.set_payoffs(),
            'p2.payoff': self.group.set_payoffs(),
            'p3.payoff': self.group.set_payoffs(),
            'p4.payoff': self.group.set_payoffs(),
            'p5.payoff': self.group.set_payoffs(),
            'p6.payoff': self.group.set_payoffs(),
            'p7.payoff': self.group.set_payoffs(),
            'p8.payoff': self.group.set_payoffs(),
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
    P1,
    SendBackWaitPage,
    P2,
    SendBackWaitPage,
    P3,
    SendBackWaitPage,
    P4,
    SendBackWaitPage,
    P5,
    SendBackWaitPage,
    P6,
    SendBackWaitPage,
    P7,
    SendBackWaitPage,
    P8,
    ResultsWaitPage,
    Results,
    OverallResults,
    Survey

]
