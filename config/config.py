# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1876563
API_HASH = "2dd374b69b88a46467e6e3c5df524a62"

# Get this from @Botfather
TOKEN = "1673331571:AAEiUSsK_YJ5r2necalTREelFs8lafm1HGs"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb+srv://nolol:nolol@cluster0.wgu7k.mongodb.net/nolol?retryWrites=true&w=majority"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1229057875,
    1083049180,
    1392620345
]

# The ID of the group where your bot streams
GROUP = -1001248104416

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 15

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "-521883165" else None
SUDO_FILTER = filters.user(SUDO_USERS)
