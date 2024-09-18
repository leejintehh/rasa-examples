from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayOrder(Action):

    def name(self) -> Text:
        return "action_say_current_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_item = tracker.get_slot("food_item")
        food_quantity = tracker.get_slot("food_quantity")
        if not (food_item and food_quantity ):
            dispatcher.utter_message(text="No current order")
        else:
            dispatcher.utter_message(text=f"Your current order is {food_quantity} {food_item}, is this correct?")
        return []



#MySQL submit order to DB
class ActionSubmitOrder(Action):

    def name(self) -> Text:
        return "action_submit_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import mysql.connector

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database='rasa'
        )

        mycursor = mydb.cursor()

        food_item = tracker.get_slot("food_item")
        food_quantity = tracker.get_slot("food_quantity")
        if food_item and food_quantity:
            sql = "INSERT INTO orders (food, quantity) VALUES (%s, %s)"
            val = (food_item, food_quantity)
            mycursor.execute(sql, val)
            mydb.commit()
            dispatcher.utter_message(text=f"order submitted!")
        return []