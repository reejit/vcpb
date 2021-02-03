from pyrogram import filters

try:
    from config.config import *
except ImportError:
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "TOKEN",
        help="Bot token",
        required=True,
    )
    parser.add_argument(
        "API_ID",
        help="Telegram api_id, get it from my.telegram.org/apps",
        type=int,
        required=True,
    )
    parser.add_argument(
        "API_HASH",
        help="Telegram api_hash, get it from my.telegram.org/apps",
        required=True,
    )
    parser.add_argument(
        "MONGO_FB_URI",
        help="MongoDB URI, if you don't provide the bot will lack some cool features",
        required=True,
    )
    parser.add_argument(
        "SUDO_USERS",
        help="List of user ids, separate by underscore (example: 1_3)",
        type=str,
        required=True,
    )
    parser.add_argument(
        "GROUP",
        help="Id of the group where the bot streams",
        type=int,
        required=True,
    )
    parser.add_argument(
        "USERS_MUST_JOIN",
        help="If provided, only members of the group can use the bot",
        type=bool,
        required=False,
        default=False,
    )
    parser.add_argument(
        "LANG",
        help="Bot language, choose from strings/",
        required=True,
    )
    parser.add_argument(
        "DUR_LIMIT",
        help="Video download duration limit (in minutes)",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    API_ID = args.API_ID
    API_HASH = args.API_HASH
    TOKEN = args.TOKEN
    MONGO_DB_URI = args.MONGO_DB_URI
    SUDO_USERS = list(map(int, args.sudo_users.split("_")))
    GROUP = args.GROUP
    USERS_MUST_JOIN = args.USERS_MUST_JOIN
    LANG = args.LANG
    DUR_LIMIT = args.DUR_LIMIT
    LOG_GROUP = GROUP if MONGO_DB_URI not in ("", None) else None
    SUDO_FILTER = filters.user(SUDO_USERS)

