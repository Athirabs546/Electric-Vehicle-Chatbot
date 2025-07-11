import csv
import re
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction

# Submit Action
class ActionSubmitUserDetails(Action):
    def name(self) -> str:
        return "action_submit_user_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[EventType]:

        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phone_number = tracker.get_slot("phone_number")

        # Save to CSV
        with open("user_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone_number])

        dispatcher.utter_message(text=f"Thanks {name}, your details have been saved!")

        return []

# Form Validator
class ValidateUserDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_details_form"

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        # Simple regex for email validation
        if re.match(r"[^@]+@[^@]+\.[^@]+", slot_value):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text="That doesn't look like a valid email. Please enter a valid email address.")
            return {"email": None}

    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        # Check if it's a 10-digit number
        if re.match(r"^[6-9]\d{9}$", slot_value):
            return {"phone_number": slot_value}
        else:
            dispatcher.utter_message(text="That doesn't seem like a valid phone number. Please enter a 10-digit Indian phone number.")
            return {"phone_number": None}
