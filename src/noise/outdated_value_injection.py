from datetime import datetime, timedelta
import random


class OutdatedValueInjector:
    """
    Minimal implementation for outdated value injection.
    Shifts dates backwards based on probability.
    """

    def __init__(self, seed=42):
        random.seed(seed)

    def shift_date(self, date_str, max_years=5):
        """
        Shift a date backwards in time.
        """

        if not date_str:
            return date_str

        try:
            date_obj = datetime.strptime(str(date_str), "%Y-%m-%d")
        except ValueError:
            return date_str

        years_back = random.randint(1, max_years)

        return (date_obj - timedelta(days=365 * years_back)).strftime("%Y-%m-%d")

    def apply(self, df, rate=0.2, field="LastBusinessActivityDate"):
        """
        Apply outdated value injection to dataframe.
        """

        if field not in df.columns:
            return df

        def apply_shift(value):

            if random.random() < rate:
                return self.shift_date(value)

            return value

        df[field] = df[field].apply(apply_shift)

        return df