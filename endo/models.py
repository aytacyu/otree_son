from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools


doc = """
This is a standard 2-player endoo game where the amount sent by player 1 gets
tripled. The endo game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'endo'
    players_per_group = None
    num_rounds = 2

    instructions_template = 'endo/instructions.html'
    table_template = 'endo/table.html'


    # Initial amount allocated to players
    endowment_Decider = c(9)
    endowment_Receiver = c(1)
    multiplier = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.color = random.choice(['RED', 'BLUE']);

        else:
            for p in self.get_players():
                p.color = p.in_round(self.round_number - 1).color
        self.group_randomly()


    def assign_sequence(self):
        all_players = self.get_players()
        blue_players = [p for p in all_players if p.color == 'BLUE']
        red_players = [p for p in all_players if p.color == 'RED']
        player_iter_list = self.get_players()
        print("before:{}".format(player_iter_list))
        player_iter_list.sort(key=lambda x: x.WTP, reverse=True)
        print("after:{}".format(player_iter_list))

        blue_players.sort(key=lambda x: x.WTP, reverse=True)
        red_players.sort(key=lambda x: x.WTP, reverse=True)

        rand_num = random.randint(0, 10)
        index = 1
        for pl in player_iter_list:
            print(("searching for player:{}".format(pl.participant.id_in_session)))
            #if pl in all_players:
            all_players.remove(pl)
            if pl.color == "RED":
                red_players.remove(pl)
            else:
                blue_players.remove(pl)
            print("WTP is : {}, random number is : {}".format(pl.WTP, rand_num))
            if pl.WTP > rand_num:
                print(("player:{} won".format(pl)))
                if pl.color == 'RED':
                    print(("player:{} is red".format(pl)))
                    if len(red_players) > 0:
                        partner = red_players[0]
                        # partner = random.choice(red_players)
                    else:
                        partner = blue_players[-1]
                        # partner = random.choice(blue_players)
                elif pl.color == 'BLUE':
                    print(("player:{} is blue".format(pl)))
                    if len(blue_players) > 0:
                        partner = blue_players[0]
                        # partner = random.choice(blue_players)
                    else:
                        partner = red_players[-1]
                        # partner = random.choice(red_players)
            else:
                print(("player:{} lost".format(pl)))
                # partner = random.choice(all_players)

                if pl.color == 'RED':
                    print(("player:{} is red".format(pl)))
                    if len(blue_players) > 0:
                        partner = blue_players[-1]
                        # partner = random.choice(red_players)
                    else:
                        partner = red_players[0]
                        # partner = random.choice(blue_players)
                elif pl.color == 'BLUE':
                    print(("player:{} is blue".format(pl)))
                    if len(red_players) > 0:
                        partner = red_players[-1]
                        # partner = random.choice(blue_players)
                    else:
                        partner = blue_players[0]
                        # partner = random.choice(red_players)

            print("partner : {}".format(partner))
            print(("all players:{}".format(all_players)))
            all_players.remove(partner)
            if partner.color == "RED":
                red_players.remove(partner)
            else:
                blue_players.remove(partner)
            print(("blue players :{}".format(blue_players)))
            print(("red players:{}".format(red_players)))

            print(pl.sequence)
            print(partner.sequence)
            if pl.sequence == 0:
                pl.sequence = index
                #print(("player:{} set to sequence P{}".format(pl.participant.id_in_session),pl.sequence))
                partner.sequence = index +1
                index =index + 2
            else:
                partner.sequence = pl.sequence + 1
                index = index + 1
            print(pl.sequence)
            print(partner.sequence)
            #print(("player:{} set to sequence P{}".format(partner.participant.id_in_session), partner.sequence))

        all_players.sort(key=lambda x: x.sequence, reverse=True)
        print(player.sequence for player in all_players)


class Group(BaseGroup):
    sent_2 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P2""",
    )
    sent_3 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P3""",
    )
    sent_4 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P4""",
    )
    sent_5 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P5""",
    )
    sent_6 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P6""",
    )
    sent_7 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P7""",
    )
    sent_8 = models.CurrencyField(
        min=0, max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P8""",
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p5 = self.get_player_by_id(5)
        p6 = self.get_player_by_id(6)
        p7 = self.get_player_by_id(7)
        p8 = self.get_player_by_id(8)

        p1.payoff = 2 * (Constants.endowment_Receiver + self.sent_2)
        p2.payoff = (Constants.endowment_Decider - self.sent_2) * (Constants.endowment_Receiver + self.sent_3)
        p3.payoff = (Constants.endowment_Decider - self.sent_3) * (Constants.endowment_Receiver + self.sent_4)
        p4.payoff = (Constants.endowment_Decider - self.sent_4) * (Constants.endowment_Receiver + self.sent_5)
        p5.payoff = (Constants.endowment_Decider - self.sent_5) * (Constants.endowment_Receiver + self.sent_6)
        p6.payoff = (Constants.endowment_Decider - self.sent_6) * (Constants.endowment_Receiver + self.sent_7)
        p7.payoff = (Constants.endowment_Decider - self.sent_7) * (Constants.endowment_Receiver + self.sent_8)
        p8.payoff = (Constants.endowment_Decider - self.sent_8) * (
                    self.sent_2 + self.sent_3 + self.sent_4 + self.sent_5 + self.sent_6 + self.sent_7 + self.sent_8) / 7


class Player(BasePlayer):
    color = models.StringField()
    WTP = models.CurrencyField(initial=0)
    overall_payoff = models.CurrencyField(initial=0)

    sequence = models.IntegerField(initial=0)

    department = models.StringField()


    age = models.StringField(choices=[ '<24','25-34','35-44','45-54', '>55' ],widget=widgets.RadioSelect)


    gender = models.StringField(choices=[ 'Female','Male' ],widget=widgets.RadioSelect)


    average_monthly_income = models.StringField(widget = widgets.RadioSelect)
    def average_monthly_income_choices(self):
        choices = [ '500-1000','1000-2000','2000-3000','3000-4000','4000-5000','5000+']
        return choices

    Choice_of_investment_options = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options_choices(self):
        choices = ['8₺ with probability %10 , 6,4₺ with probability %90', '15,4₺ with probability %10 , 0,4₺ with probability %90']
        return choices

    Choice_of_investment_options2 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options2_choices(self):
        choices = ['8₺ with probability %20 , 6,4₺ with probability %80', '15,4₺ with probability %20 , 0,4₺ with probability %80']
        return choices

    Choice_of_investment_options3 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options3_choices(self):
        choices = ['8₺ with probability %30 , 6,4₺ with probability %70', '15,4₺ with probability %30 , 0,4₺ with probability %70']
        return choices
    Choice_of_investment_options4 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options4_choices(self):
        choices = ['8₺ with probability %40 , 6,4₺ with probability %60', '15,4₺ with probability %40 , 0,4₺ with probability %60']
        return choices
    Choice_of_investment_options5 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options5_choices(self):
        choices = ['8₺ with probability %50 , 6,4₺ with probability %50', '15,4₺ with probability %50 , 0,4₺ with probability %50']
        return choices
    Choice_of_investment_options6 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options6_choices(self):
        choices = ['8₺ with probability %60 , 6,4₺ with probability %40', '15,4₺ with probability %60 , 0,4₺ with probability %40']
        return choices
    Choice_of_investment_options7 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options7_choices(self):
        choices = ['8₺ with probability %70 , 6,4₺ with probability %30', '15,4₺ with probability %70 , 0,4₺ with probability %30']
        return choices
    Choice_of_investment_options8 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options8_choices(self):
        choices = ['8₺ with probability %80 , 6,4₺ with probability %20', '15,4₺ with probability %80 , 0,4₺ with probability %20']
        return choices
    Choice_of_investment_options9 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options9_choices(self):
        choices = ['8₺ with probability %90 , 6,4₺ with probability %10', '15,4₺ with probability %90 , 0,4₺ with probability %10']
        return choices
    Choice_of_investment_options10 = models.StringField(widget=widgets.RadioSelect)
    def Choice_of_investment_options10_choices(self):
        choices = ['8₺ with probability %100 , 6,4₺ with probability %0', '15,4₺ with probability %100 , 0,4₺ with probability %0']
        return choices