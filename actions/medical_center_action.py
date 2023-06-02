from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
import json
import os 
import requests
from dotenv import load_dotenv

load_dotenv()


class ActionSearchMedicalCenter(Action):

    def name(self) -> Text:
        return "search_medical_center"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        reversed_events = list(reversed(tracker.events))
        j1 = json.dumps(reversed_events[1])
        j2 = json.loads(j1)
        typeOfMedicalCenter = {
            "health_plan": j2["text"]
        }
        api = os.getenv('API_URL')
        api += 'api/v1/getByHealthPlan'
        response = requests.get(api, json=typeOfMedicalCenter)
        medical_Center = response.json()  
        print(medical_Center)      
        dispatcher.utter_message(json_message=medical_Center)

        texto = "Você está se sentindo mal ou doente?"
        jsonMessage = {
            "buttons": ['Sim', 'Não'],
            "many": 0
        }

        dispatcher.utter_message(text=texto, json_message=jsonMessage)

        return []

class ActionTypesMedicalCenter(Action):

    def name(self) -> Text:
        return "types_medical_center"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text="Okay, posso aranjar alguns opções de centros médicos, mas primeiro selecione se quer um dos SUS ou de um plano de saúde específico:"
        jsonMessage = {
            "buttons": ['Unimed', 'Hapvida', "SUS"],
            "many": 0
        }

        dispatcher.utter_message(text=text, json_message=jsonMessage)

# class ActionSuggestCenter(Action):

#     def name(self) -> Text:
#         return "action_suggest_center"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         texto = "Vá para o hospital"
#         dispatcher.utter_message(text=texto)

#         return []