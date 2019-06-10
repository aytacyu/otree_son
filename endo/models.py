from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools

doc = """
This is a standard 2-player endo game where the amount sent by player 1 gets
tripled. The endo game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'endo'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'endo/instructions.html'
    table_template = 'endo/table.html'

    # Initial amount allocated to players
    endowment_Decider = c(9)
    endowment_Receiver = c(1)
    multiplier = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            colors = itertools.cycle(['BLUE', 'RED'])
            for p in self.get_players():
                p.color = next(colors)
        else:
            for p in self.get_players():
                p.color = p.in_round(self.round_number - 1).color
        self.group_randomly()

    def assign_groups(self):
        all_players = self.get_players()
        blue_players = [p for p in all_players if p.color == 'BLUE']
        red_players = [p for p in all_players if p.color == 'RED']
        player_iter_list = self.get_players()
        print("before:{}".format(player_iter_list))
        player_iter_list.sort(key=lambda x: x.WTP, reverse=True)
        print("after:{}".format(player_iter_list))
        group_matrix = []
        for pl in player_iter_list:
            print(("searching for player:{}".format(pl.participant.id_in_session)))

            if pl in all_players:
                all_players.remove(pl)
                if pl.color == "RED":
                    red_players.remove(pl)
                else:
                    blue_players.remove(pl)


                if pl.WTP > random.randint(0, 10):
                    print(("player:{} won".format(pl)))
                    if pl.color == 'RED':
                        print(("player:{} is red".format(pl)))
                        if len(red_players) > 0:
                            partner = random.choice(red_players)
                        else:
                            partner = random.choice(blue_players)
                    elif pl.color == 'BLUE':
                        print(("player:{} is blue".format(pl)))
                        if len(blue_players) > 0:
                            partner = random.choice(blue_players)
                        else:
                            partner = random.choice(red_players)
                else:
                    print(("player:{} lost".format(pl)))
                    partner = random.choice(all_players)

                print("partner : {}".format(partner))
                print(("all players:{}".format(all_players)))
                all_players.remove(partner)
                if partner.color == "RED":
                    red_players.remove(partner)
                else:
                    blue_players.remove(partner)

                group_matrix.append([pl, partner])

                print(("blue players :{}".format(blue_players)))
                print(("red players:{}".format(red_players)))
                print("group matrix: {}".format(group_matrix))

        self.set_group_matrix(group_matrix)
        print(self.get_group_matrix())


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=c(0), max=Constants.endowment_Decider - 2,
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = (Constants.endowment_Decider - self.sent_amount) * (
                Constants.endowment_Receiver + self.sent_back_amount)
        p2.payoff = (Constants.endowment_Decider - self.sent_back_amount) * (
                Constants.endowment_Receiver + self.sent_amount)


class Player(BasePlayer):
    color = models.StringField()
    WTP = models.CurrencyField(initial=0)
    overall_payoff = models.CurrencyField(initial=0)

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]

    department = models.StringField()

    age = models.StringField(choices=['<24', '25-34', '35-44', '45-54', '>55'], widget=widgets.RadioSelect)

    gender = models.StringField(choices=['Female', 'Male'], widget=widgets.RadioSelect)

    average_monthly_income = models.StringField(widget=widgets.RadioSelect)

    def average_monthly_income_choices(self):
        choices = ['500-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000+']
        return choices

    Choice_of_investment_options = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options_choices(self):
        choices = ['8₺ with probability %10 , 6,4₺ with probability %90',
                   '15,4₺ with probability %10 , 0,4₺ with probability %90']
        return choices

    Choice_of_investment_options2 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options2_choices(self):
        choices = ['8₺ with probability %20 , 6,4₺ with probability %80',
                   '15,4₺ with probability %20 , 0,4₺ with probability %80']
        return choices

    Choice_of_investment_options3 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options3_choices(self):
        choices = ['8₺ with probability %30 , 6,4₺ with probability %70',
                   '15,4₺ with probability %30 , 0,4₺ with probability %70']
        return choices

    Choice_of_investment_options4 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options4_choices(self):
        choices = ['8₺ with probability %40 , 6,4₺ with probability %60',
                   '15,4₺ with probability %40 , 0,4₺ with probability %60']
        return choices

    Choice_of_investment_options5 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options5_choices(self):
        choices = ['8₺ with probability %50 , 6,4₺ with probability %50',
                   '15,4₺ with probability %50 , 0,4₺ with probability %50']
        return choices

    Choice_of_investment_options6 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options6_choices(self):
        choices = ['8₺ with probability %60 , 6,4₺ with probability %40',
                   '15,4₺ with probability %60 , 0,4₺ with probability %40']
        return choices

    Choice_of_investment_options7 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options7_choices(self):
        choices = ['8₺ with probability %70 , 6,4₺ with probability %30',
                   '15,4₺ with probability %70 , 0,4₺ with probability %30']
        return choices

    Choice_of_investment_options8 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options8_choices(self):
        choices = ['8₺ with probability %80 , 6,4₺ with probability %20',
                   '15,4₺ with probability %80 , 0,4₺ with probability %20']
        return choices

    Choice_of_investment_options9 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options9_choices(self):
        choices = ['8₺ with probability %90 , 6,4₺ with probability %10',
                   '15,4₺ with probability %90 , 0,4₺ with probability %10']
        return choices

    Choice_of_investment_options10 = models.StringField(widget=widgets.RadioSelect)

    def Choice_of_investment_options10_choices(self):
        choices = ['8₺ with probability %100 , 6,4₺ with probability %0',
                   '15,4₺ with probability %100 , 0,4₺ with probability %0']
        return choices
