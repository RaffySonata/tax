from os import environ

SESSION_CONFIGS = [
    dict(
        name='compound_kecil',
        app_sequence=['intro','compound_practice','compound_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='compound_kecil_random',
        app_sequence=['intro','compound_practice_random','compound_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='compound_sedang',
        app_sequence=['intro', 'compound_practice', 'compound_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='compound_sedang_random',
        app_sequence=['intro', 'compound_practice_random', 'compound_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='compound_besar',
        app_sequence=['intro', 'compound_practice', 'compound_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='compound_besar_random',
        app_sequence=['intro', 'compound_practice_random', 'compound_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='val_kecil',
        app_sequence=['intro','val_practice','val_kecil'],
        num_demo_participants=2,
    ),
    dict(
        name='val_sedang',
        app_sequence=['intro','val_practice','val_sedang'],
        num_demo_participants=2,
    ),
    dict(
        name='val_besar',
        app_sequence=['intro','val_practice','val_besar'],
        num_demo_participants=2,
    ),
    dict(
        name='val_kecil_random',
        app_sequence=['intro','val_practice_random','val_kecil_random'],
        num_demo_participants=2,
    ),
    dict(
        name='val_sedang_random',
        app_sequence=['intro','val_practice_random','val_sedang_random'],
        num_demo_participants=2,
    ),
    dict(
        name='val_besar_random',
        app_sequence=['intro','val_practice_random','val_besar_random'],
        num_demo_participants=2,
    ),
    dict(
        name='val_practice',
        app_sequence=['val_practice'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_FIELDS = [
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
]

PARTICIPANT_FIELDS = [
    'app_payoffs',
    'app_row',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'quiz_num_correct',
    'selected_round',
    'task_rounds',
    'time_pressure',
    'wait_page_arrival',
    'umr_list',
    'iw_lists',
    'sw_lists',
    'endowment_lists',
    'iw_type',
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'Rp'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'admin'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3860349561509'
