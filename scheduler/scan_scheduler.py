from datetime import datetime, timedelta

from config.settings import Settings


class ScanScheduler:

    def __init__(self):

        self.last_scan = None

        self.next_scan_at = None

    def should_scan(self):

        if self.last_scan is None:

            return True

        now = datetime.now()

        return (

            now - self.last_scan

        ) >= timedelta(

            minutes=Settings.SCAN_INTERVAL_MINUTES

        )

    def mark_scan_complete(self):

        self.last_scan = datetime.now()

        self.next_scan_at = (

            self.last_scan

            + timedelta(

                minutes=Settings.SCAN_INTERVAL_MINUTES

            )

        )

    def next_scan_time(self):

        if self.last_scan is None:

            return "Now"

        return self.next_scan_at.strftime("%I:%M %p")