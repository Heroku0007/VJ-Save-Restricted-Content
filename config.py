import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("7571074864:AAGRtDkPyxwziFV42YqlsObo1LkOxKora-E")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23276244"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "eb5835a09739eba31d78971be7492d24")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7642353202"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
