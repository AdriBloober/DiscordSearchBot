from ressources.api import Api
from ressources.config import load, get_config
from discord.ext import commands as dc_commands
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = {}


def get_prefix(_, message):
    config_obejct = get_config()
    if str(message.guild.id) in config_obejct.prefixes:
        return config_obejct.prefixes[str(message.guild.id)]
    return "§"


load()
db = declarative_base()
engine = None
try:
    engine = create_engine(get_config().SQLALCHEMY_DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
except Exception as e:
    print("ERROR!")
    print(e)
    print("Exiting!")
    exit(1)
client = dc_commands.Bot(command_prefix=get_prefix, help_command=None)

api = Api()

from ressources import basic_messages, commands, main, permissions
from ressources.database import user
db.metadata.create_all(engine)
