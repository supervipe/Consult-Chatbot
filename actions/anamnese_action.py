from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
import json
import os 
import requests
from dotenv import load_dotenv

load_dotenv()

class ActionSelectIllness(Action):

    def name(self) -> Text:
        return "action_select_illness"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        api = os.getenv('API_URL')
        api += 'api/v1/listIllness'
        response = requests.get(api)
        list = response.json()
        jsonMessage = {
            "buttons": list,
            "many": 1
        }  
        dispatcher.utter_message(text="Okay, por favor selecione as suas doenças:",json_message=jsonMessage)

        return []

class ActionSelectAllergy(Action):

    def name(self) -> Text:
        return "action_select_allergy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api = os.getenv('API_URL')
        api += 'api/v1/listAllergy'
        response = requests.get(api)
        list = response.json()
        jsonMessage = {
            "buttons": list,
            "many": 1
        }  
        dispatcher.utter_message(text="Okay, por favor selecione as suas alergias:",json_message=jsonMessage)

        return []

class ActionSaveAnamnese(Action):

    def name(self) -> Text:
        return "action_save_anamnese"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        reversed_events = list(reversed(tracker.events))
        j1 = json.dumps(reversed_events[1])
        j2 = json.loads(j1)
        allergies = j2["text"]
        j3 = json.dumps(reversed_events[8])
        j4 = json.loads(j3)
        illnesses = j4["text"]
        tracker = tracker.current_state()['sender_id']
        api = os.getenv('API_URL')
        allergies = allergies.split(',')
        illnesses = illnesses.split(',')
        jsonAllergy = { 
            "nameAll": allergies
        }
        jsonIllness = {
            'nameAll': illnesses
        }
        try:
            api1 = api +  'api/v1/linkAllergy/' + tracker
            response = requests.post(api1, json=jsonAllergy)
            ok1 = response.json()
            api2 = api + 'api/v1/linkIllness/' + tracker
            response = requests.post(api2, json=jsonIllness)
            ok2 = response.json() 
            texto = "Pronto agora um pouco sobre o sistema:"
            dispatcher.utter_message(text=texto)
            return []
        except:
            texto = "Algo deu errado, tente novamente mais tarde!"
            dispatcher.utter_message(text=texto)
            return [Restarted()]
