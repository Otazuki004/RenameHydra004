import logging
import pymongo
from pyrogram import Client


FORMAT = "[Hydra1] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


OWNER_ID = 1087528282
PREFIX = ["/","!","*","$","#","?",">",]

mongo = pymongo.MongoClient("mongodb+srv://owoyemi96:<kqCL6a9wEYwxy026>@durlarstv.und7ncd.mongodb.net/?retryWrites=true&w=majority")
db = mongo["Hydra1"]

ND = Client("Hydra1",
     api_id=int(10187126),
     api_hash="ff197c0d23d7fe54c89b44ed092c1752",
     bot_token="6196780979:AAEn9mTjzwGLeevJBC2h5dhpixKkuHtMEfU",
     plugins=dict(root="Hydra1"),)




