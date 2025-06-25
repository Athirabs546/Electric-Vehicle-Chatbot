from typing import Any, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3  # or use another database like PostgreSQL or MySQL
from rasa_sdk.events import SlotSet

class ActionSaveUserDetails(Action):
    def name(self) -> str:
        return "action_save_user_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        name = tracker.get_slot("user_name")
        email = tracker.get_slot("user_email")
        phone = tracker.get_slot("user_phone")

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    name TEXT,
                    email TEXT,
                    phone TEXT
                )
            """)
            cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()
            conn.close()

            dispatcher.utter_message(text="Your details have been saved successfully.")
        except Exception as e:
            dispatcher.utter_message(text=f"Oops! Something went wrong while saving your data: {str(e)}")

        return [
            SlotSet("user_name", None),
            SlotSet("user_email", None),
            SlotSet("user_phone", None)
        ]


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
