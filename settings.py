from os import environ

SESSION_CONFIG_DEFAULTS = {
    "real_world_currency_per_point": 1.00,
    "participation_fee": 0.00,
    "doc": "",
}

SESSION_CONFIGS = [
    {
        "name": "my_session_1",
        "display_name": "my_session_1",
        "num_demo_participants": 1,
        "app_sequence": ["my_app"],
    }
]
LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "USD"
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ""
ROOMS = [{"name": "my_room", "display_name": "my_room"}]

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

SECRET_KEY = "blahblah"

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ["otree"]
