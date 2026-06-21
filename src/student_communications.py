from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Message:
    id: int
    sender: str
    recipient: str
    content: str
    application_status: str

class StudentCommunications:
    def __init__(self):
        self.messages = []

    def send_message(self, sender: str, recipient: str, content: str, application_status: str) -> Message:
        message = Message(len(self.messages) + 1, sender, recipient, content, application_status)
        self.messages.append(message)
        return message

    def get_messages(self, application_status: str = None) -> List[Message]:
        if application_status:
            return [message for message in self.messages if message.application_status == application_status]
        return self.messages

    def send_notification(self, message: Message) -> None:
        print(f"Notification sent to {message.recipient} for message {message.id}")

    def categorize_messages(self, messages: List[Message]) -> Dict[str, List[Message]]:
        categorized_messages = {}
        for message in messages:
            if message.application_status not in categorized_messages:
                categorized_messages[message.application_status] = []
            categorized_messages[message.application_status].append(message)
        return categorized_messages
