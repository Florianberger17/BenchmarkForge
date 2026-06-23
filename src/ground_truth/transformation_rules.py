"""
BenchmarkForge - Transformation Rules

Purpose:
    Contains all business logic rules used by the MappingEngine.
"""

from datetime import datetime, timedelta


class TransformationRules:
    """
    Stateless business rule functions.
    """

    COUNTRY_MAPPING = {
        "DE": "DEU",
        "AT": "AUT",
        "CH": "CHE"
    }

    @staticmethod
    def normalize_country(country_code):
        if not country_code:
            return None

        return TransformationRules.COUNTRY_MAPPING.get(
            country_code,
            country_code
        )

    @staticmethod
    def build_street(street, house_no):
        if not house_no:
            return street

        return f"{street} {house_no}"

    @staticmethod
    def derive_status(last_business_date):
        if not last_business_date:
            return "inactive"

        cutoff = datetime.today() - timedelta(days=365 * 3)

        date_obj = datetime.strptime(
            str(last_business_date),
            "%Y-%m-%d"
        )

        return "active" if date_obj >= cutoff else "inactive"