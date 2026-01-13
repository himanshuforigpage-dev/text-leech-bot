import os

API_ID    = os.environ.get("API_ID", "21025319")
API_HASH  = os.environ.get("API_HASH", "cfc533caac028e0e284dae2d571ad5b0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8457341970:AAEL7ez7cFFWDOx2n1BKiuYCUJwvibCK4U4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set
