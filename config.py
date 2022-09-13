from sample_config import Config


class Development(Config):
  #get this values from the my.telegram.org
  APP_ID = 18466214
  API_HASH = "770052b34e735a5c72da2b45eef7d714"
  # the name to display in your alive message
  ALIVE_NAME = "All Mighty"
  # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
  DB_URI = "postgresql://postgres:seemenaked@localhost:5432/catuserbot"
  #After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
  STRING_SESSION = "Your value"
  #create a new bot in @botfather and fill the following vales with bottoken and username respectively
  TG_BOT_TOKEN = "5460765136:AAFfode_K8nd2Tqw13yiT7xAWxc6cCVTpNQ"
  TG_BOT_USERNAME = "@cat97_bot"
  #create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
  PRIVATE_GROUP_BOT_API_ID = -1001642905642
  #command handler 
  COMMAND_HAND_LER = "."
  #sudo enter the id of sudo users userid's in that array
  SUDO_USERS = []
  # command hanler for sudo
  SUDO_COMMAND_HAND_LER = "."
