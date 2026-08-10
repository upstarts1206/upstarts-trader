from datetime import datetime, timedelta

from config.settings import Settings


class ScanScheduler:

    def __init__(self):

        self.last_scan = None

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

    def next_scan_time(self):

        if self.last_scan is None:

            return "Now"

        next_scan = self.last_scan + timedelta(

            minutes=Settings.SCAN_INTERVAL_MINUTES

        )

        return next_scan.strftime("%I:%M %p")