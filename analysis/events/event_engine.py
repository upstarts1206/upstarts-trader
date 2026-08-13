from analysis.events.event import MarketEvent


class EventEngine:

    def generate(self, df):

        events = []

        for _, candle in df.iterrows():

            timestamp = candle["timestamp"]

            close = candle["close"]

            # -------------------------
            # BOS
            # -------------------------

            if candle["bos"]:

                events.append(

                    MarketEvent(

                        event_type=f"{candle['bos_direction']} BOS",

                        timestamp=timestamp,

                        price=close,

                    )

                )

            # -------------------------
            # CHOCH
            # -------------------------

            if candle["choch"]:

                events.append(

                    MarketEvent(

                        event_type=f"{candle['choch_direction']} CHOCH",

                        timestamp=timestamp,

                        price=close,

                    )

                )

            # -------------------------
            # Fair Value Gap
            # -------------------------

            if candle["fvg"]:

                events.append(

                    MarketEvent(

                        event_type=f"{candle['fvg']} FVG",

                        timestamp=timestamp,

                        price=close,

                    )

                )

            # -------------------------
            # Liquidity Sweep
            # -------------------------

            if candle["liquidity_sweep"]:

                events.append(

                    MarketEvent(

                        event_type=f"{candle['liquidity_side']} Sweep",

                        timestamp=timestamp,

                        price=close,

                    )

                )

        return events