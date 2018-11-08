import Presence
import time

class richpresence():
    def __init__(self, bot):
        self.bot = bot

client_id = '497480630687367188'
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Giovanni x Natsuki", details="Xenzai x Rem/ Nakune x Koneko Btw Don't judge me!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
