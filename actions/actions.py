# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
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
         return "action_search_by_text"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            #request = requests.get('http://api.icndb.com/jokes/random').json() #make an api call
            #joke = request['value']['joke'] #extract a joke from returned json response

            # Codice per fare una api call
            #r = requests.post('http://127.0.0.1:5001/predict', data = {'id':'1_short_sleeve_top_3145741-64470548-2560-1440.jpg'})

            #get del valore contenuto negli slot product e colour 
            product_type = tracker.get_slot('product')
            color_value = tracker.get_slot('colour')

            print(product_type)
            print(color_value)
            
            #Chiamata all'API search con invio dei parametri "product_type" e "color_value"
            r = requests.post('http://127.0.0.1:5001/search', data = {'type': product_type, 'color': color_value})
            #print(r.text)
            lenght = len(r.text)
            print(len("[Query]"))
            if (lenght == len('["Query"]')):
                 dispatcher.utter_message(text="Non sono stati trovati articoli per la ricerca " + product_type + " di colore " + color_value)
            else:
                #return dei risultati della chiamata all'API search 
                dispatcher.utter_message(text=r.text)
            
            #reset di tutti gli slot 
            return [AllSlotsReset()]
