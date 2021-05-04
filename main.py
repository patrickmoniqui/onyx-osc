"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import udp_client

FADER_GRANDMASTER = 2202
FADER_1 = 4000

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="192.168.0.138",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  fader(client, FADER_1, 255)

#   for x in range(4200, 4210, 1):
#     type = "/Mx/fader/"+str(x)
#     value = 255
#     client.send_message(type, value)
#     print('sending: ' + type + " : " + str(value))
#     time.sleep(0)

def fader(client, num, value):
    client.send_message(num, value)
