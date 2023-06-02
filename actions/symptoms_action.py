from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
import json
import os 
import requests
from dotenv import load_dotenv

load_dotenv()

class ActionSelectSymptoms(Action):

    def name(self) -> Text:
        return "action_select_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api = os.getenv('API_URL')
        api += 'api/v1/getSymptoms'
        response = requests.get(api)
        list = response.json()  
        jsonMessage = {
            "buttons": list,
            "many": 1
        }      
        dispatcher.utter_message(text="Okay, então por favor me informe o que você está sentindo:", json_message=jsonMessage)

        return []

class ActionSuggestCenter(Action):

    def name(self) -> Text:
        return "action_suggest_center"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reversed_events = list(reversed(tracker.events))
        j1 = json.dumps(reversed_events[1])
        j2 = json.loads(j1)
        symptoms = j2["text"]
        tracker_user = tracker.current_state()['sender_id']
        api = os.getenv('API_URL')
        symptoms = symptoms.split(',')
        jsonAllergy = { 
            "nameAll": symptoms
        }
        try:
            api += 'api/v1/python/' + tracker_user
            response = requests.post(api, json=jsonAllergy)
            ok = response.json()
            print(ok)
            dispatcher.utter_message(text="Pronto foi cadastrado seus sintomas.")
            return []
        except:
            texto = "Algo deu errado, tente novamente mais tarde!"
            dispatcher.utter_message(text=texto)
            return [Restarted()]
