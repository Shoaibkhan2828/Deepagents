import json
import uuid
import datetime
import os

class SessionManager:
    def __init__(self, user_id=None, metadata=None, log_dir="logs"):
        self.session_id = f"sess_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
        self.conversation = []
        self.counter = 0
        self.user_data = {"user_id": user_id} if user_id else {}
        if metadata:
            self.user_data.update(metadata)
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def add_turn(self, bot_message, user_message):
        """Add a turn in the conversation."""
        self.conversation.append({
            "turn": len(self.conversation) + 1,
            "bot": bot_message,
            "user": user_message
        })
        self.counter += 1

    def set_user_data(self, key, value):
        """Set or update user-related data."""
        self.user_data[key] = value

    def save_log(self):
        """Save session log as JSON."""
        log = {
            "session_id": self.session_id,
            "timestamp": str(datetime.datetime.now()),
            "user": self.user_data,
            "conversation": self.conversation
        }
        file_path = os.path.join(self.log_dir, f"{self.session_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(log, f, indent=4)
        return file_path
