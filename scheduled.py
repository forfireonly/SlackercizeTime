import os
import schedule
import time
import logging
#from slackclient import SlackClient
from slack import WebClient
import random
import emojis

logging.basicConfig(level=logging.DEBUG)

items = ['15 squats', '15 jumping jacks', '15 situps', '10 pushups',
         '15 lunges']

rand_item = items[random.randrange(len(items))]

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  updateMsg = slack_client.chat_postMessage(
     channel="#apps",
     text=msg
  )

  # check if the request was a success
  if updateMsg['ok'] is not True:
    logging.error(updateMsg)
  else:
    logging.debug(updateMsg)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  # # For testing
  msg = "Time to get up and stretch!!!" +"\n"+emojis.encode(':runner: Get up and get moving!') +  "\n Suggested exercise: " 
  schedule.every(1800).seconds.do(lambda: sendMessage(slack_client, msg+items[random.randrange(len(items))]))

  # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, msg))
  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler
   
