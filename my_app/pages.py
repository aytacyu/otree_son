from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Survey(Page):
    form_model = "player"
    form_fields = ["name", "age"]


class Results(Page):
    pass


page_sequence = [Survey, Results]
