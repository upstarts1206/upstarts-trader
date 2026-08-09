from datetime import datetime


class SessionEngine:

    def detect(self):

        hour = datetime.utcnow().hour

        # UTC Times

        if 0 <= hour < 8:
            return "Asia"

        elif 8 <= hour < 13:
            return "London"

        elif 13 <= hour < 21:
            return "New York"

        return "After Hours"