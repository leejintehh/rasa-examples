from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayShirtSize(Action):

    def name(self) -> Text:
        return "action_say_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_item = tracker.get_slot("food_item")
        food_quantity = tracker.get_slot("food_quantity")
        if not (food_item and food_quantity ):
            dispatcher.utter_message(text="No order received, would you like to submit an order?")
        else:
            dispatcher.utter_message(text=f"Your order is {food_quantity} {food_item}")
        return []
