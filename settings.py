from os import environ

SESSION_CONFIGS = [
    dict(
        name='val_kecil',
        app_sequence=['val_kecil'],
        num_demo_participants=4,
    ),
    dict(
        name='val_sedang',
        app_sequence=['val_sedang'],
        num_demo_participants=2,
    ),
    dict(
        name='val_besar',
        app_sequence=['val_besar'],
        num_demo_participants=4,
    ),
    dict(
        name='val_kecil_random',
        app_sequence=['val_kecil_random'],
        num_demo_participants=2,
    ),
    dict(
        name='val_sedang_random',
        app_sequence=['val_sedang_random'],
        num_demo_participants=2,
    ),
    dict(
        name='val_besar_random',
        app_sequence=['val_besar_random'],
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

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'admin'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3860349561509'
