# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionTipoTarjeta(Action):

    def name(self) -> Text:
       return "action_tipo_tarjeta"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tipo_tarjeta = tracker.latest_message['entities'][0]['value']
        if str(tipo_tarjeta)=="credito":
            message='Se creara una tarjeta de credito'
        else: 
            if str(tipo_tarjeta)=="debito":
                message='Se creara una tarjeta de debito'
            else:
                message='Error, ingrese nuevamente! (debito/credito)'
        dispatcher.utter_message(text=str(message))
        return []

class ActionTipoTarjeta(Action):

    def name(self) -> Text:
       return "action_DNI"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DNI = tracker.latest_message['entities'][0]['value']
        if str(DNI).contains(database)": #si ya existe el DNI
            message='DNI ingresado correctamente. Ingrese nombre: '
        else: 
            message='Ya existe una cuenta asociada a ese DNI'
        dispatcher.utter_message(text=str(message))
        return []

    
