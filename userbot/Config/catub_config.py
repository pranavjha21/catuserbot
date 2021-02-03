# Config values will be loaded from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import Config  # noqa
else:
    if os.path.exists("config.py"):
        from config import Development as Config  # noqa

STRING_SESSION = os.environ.get("STRING_SESSION", None)        
STRING_SESSION_2 = os.environ.get("STRING_SESSION_2", None)
STRING_SESSION_3 = os.environ.get("STRING_SESSION_3", None)
