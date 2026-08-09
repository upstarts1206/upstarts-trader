class ConfidenceEngine:

    def calculate(self, score):

        """
        Convert a weighted decision score into a confidence percentage.
        """

        return max(0, min(score, 100))