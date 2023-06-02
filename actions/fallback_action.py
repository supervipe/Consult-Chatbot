from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted


class ActionCustomFallback(Action):

    def __init__(self):
        self.cont = True

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if self.cont:
            dispatcher.utter_message(text="Desculpa não consegui entender! Você poderia reformular o que falou?")
            self.cont = False
        else:
            dispatcher.utter_message(template="utter_greet")
            self.cont = True
        return [Restarted()]