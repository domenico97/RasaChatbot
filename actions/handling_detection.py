import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused
import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

logger = logging.getLogger(__name__)

class customAction(Action):

     def name(self) -> Text:
         return "action_detection"

     def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

          #request = requests.get('http://api.icndb.com/jokes/random').json() #make an api call
          #joke = request['value']['joke'] #extract a joke from returned json response

          #get del valore contenuto nello slot image 
          image_value = tracker.get_slot('image')
          print(image_value)
          if "detection" in image_value:
               #Chiamata all'API detection con invio del parametro "image_value"
               r = requests.post('http://127.0.0.1:5001/detection', data = {'image': image_value})
          
               #lenght = len(r.text)
               response = r.text
               print(response)
               #print(r.text)
               if (r.text == "Null"):
                    dispatcher.utter_message(image="https://imgresizer.eurosport.com/unsafe/1200x0/filters:format(jpeg):focal(1286x278:1288x276)/origin-imgresizer.eurosport.com/2021/06/04/3145741-64470548-2560-1440.jpg", text="Mi dispiace, ma non sono stato in grado di individuare nulla. Carica foto simili a quella mostrata di seguito")
               else:
                    #return dei risultati della chiamata all'API search 
                    msg = { "type": "detection_results", "payload": { "title": "Detection results", "src": r.text } }
                    dispatcher.utter_message(text="Seleziona uno degli oggetti individuati: ",attachment = msg)

          elif "prediction" in image_value:
               # Estraggo il tipo e il colore se l'utente ha dato qualche preferenza prima di selezionare la foto
               product_type = tracker.get_slot('product')
               color_value = tracker.get_slot('colour')

               image_value = image_value.rpartition('_')[2]
               print(image_value)
               
               #print(product_type)
               #print(color_value)

               if(product_type==None):
                    product_type = "Default"
               
               if(color_value==None):
                    color_value = "Default"

               # Call API predict
               r = requests.post('http://127.0.0.1:5001/predict', data = {'id':image_value,'color':color_value,'type': product_type})
               print(r.text)
               if (r.text == "Null"):
                    dispatcher.utter_message(text="Mi dispiace, ma la ricerca non ha prodotto risultati.")
               else: 
                    msg = { "type": "prediction_results", "payload": { "title": "Prediction results", "src": r.text } }
                    dispatcher.utter_message(text="Risultati della ricerca: ",attachment = msg)
            

          #reset di tutti gli slot 
          return [AllSlotsReset()]
