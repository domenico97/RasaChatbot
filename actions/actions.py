# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class customAction(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            prova = "OK VA BENE"
            print(prova)
            #request = requests.get('http://api.icndb.com/jokes/random').json() #make an api call
            #joke = request['value']['joke'] #extract a joke from returned json response
            r = requests.post('http://127.0.0.1:5001/predict', data = {'id':'1_short_sleeve_top_3145741-64470548-2560-1440.jpg'})
            print("SONO QUI")
            print(r.text)
            dispatcher.utter_message(r.text) #send the message back to the user
           
            return []
