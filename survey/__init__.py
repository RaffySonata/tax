from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    session = subsession.session
    session.params = {}
    for p in subsession.get_players():
        # initialize an empty dict to store how much they made in each app
        p.participant.app_payoffs = {}
    for p in subsession.get_players():
        p.participant.app_row = {}
    for p in subsession.get_players():
        p.participant.selected_round = {}

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics Survey
    usia = models.IntegerField(label="Usia Anda (Tahun):",
                               min=18, max=60)
    gender = models.StringField(widget=widgets.RadioSelect,
                                label="Jenis kelamin:",
                                choices=["Pria", "Wanita"])
    edukasi = models.StringField(widget=widgets.RadioSelect,
                                 label="Tingkat Pendidikan yang sedang atau telah Anda tempuh:",
                                 choices=["Diploma 3 (D3)",
                                          "Sarjana/Diploma 4 (S1/D4)",
                                          "Magister (S2)",
                                          "Doktoral (S3)",
                                          ])
    provinsi = models.IntegerField(label="Tempat asal Provinsi",
                                   choices=[[1, 'ACEH'], [2, 'BALI'], [3, 'BANTEN'], [4, 'BENGKULU'],
                                            [5, 'DI YOGYAKARTA'], [6, 'DKI JAKARTA'],
                                            [7, 'GORONTALO'], [8, 'JAMBI'], [9, 'JAWA BARAT'], [10, 'JAWA TENGAH'],
                                            [11, 'JAWA TIMUR'],
                                            [12, 'KALIMANTAN BARAT'], [13, 'KALIMANTAN SELATAN'],
                                            [14, 'KALIMANTAN TENGAH'],
                                            [15, 'KALIMANTAN TIMUR'], [16, 'KALIMANTAN UTARA'],
                                            [17, 'KEPULAUAN BANGKA BELITUNG'],
                                            [18, 'KEPULAUAN RIAU'], [19, 'LAMPUNG'], [20, 'MALUKU'],
                                            [21, 'MALUKU UTARA'], [22, 'NUSA TENGGARA BARAT'],
                                            [23, 'NUSA TENGGARA TIMUR'], [24, 'PAPUA'], [25, 'PAPUA BARAT'],
                                            [26, 'PAPUA BARAT DAYA'],
                                            [27, 'PAPUA PEGUNUNGAN'], [28, 'PAPUA SELATAN'], [29, 'PAPUA TENGAH'],
                                            [30, 'RIAU'], [31, 'SULAWESI BARAT'],
                                            [32, 'SULAWESI SELATAN'], [33, 'SULAWESI TENGAH'],
                                            [34, 'SULAWESI TENGGARA'], [35, 'SULAWESI UTARA'],
                                            [36, 'SUMATERA BARAT'], [37, 'SUMATERA SELATAN'], [38, 'SUMATERA UTARA']])


    # PAGES


class demographic(Page):
    form_model = 'player'
    form_fields = ['provinsi', 'usia', 'gender', 'edukasi']

class Closing(Page):
    pass


page_sequence = [demographic]
