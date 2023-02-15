import logging
import pymongo
from pyrogram import Client


FORMAT = "[Hydra1] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


OWNER_ID = 1985665341
PREFIX = ["/","!","*","$","#","?",">",]

mongo = pymongo.MongoClient("mongodb+srv://Otazuki_004:<password>@hydra.od82ic1.mongodb.net/?retryWrites=true&w=majority")
db = mongo["Hydra1"]

ND = Client("Hydra1",
     api_id=int(10187126),
     api_hash="ff197c0d23d7fe54c89b44ed092c1752",
     bot_token="5401792933:AAFhqJuX2veBDEB5sNJnWCCW0Fp_czoXzbo",
     plugins=dict(root="Hydra1"),)




