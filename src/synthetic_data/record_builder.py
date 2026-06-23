"""
BenchmarkForge - Synthetic Data Generator

Module:
    record_builder.py

Purpose:
    Assembles full synthetic customer records using field-level generators.

Description:
    This module acts as a composition layer that combines individual
    attribute generators into complete customer records that conform
    to SOURCE_CUSTOMER_V1 schema.

Responsibilities:
    - Assemble complete customer records
    - Ensure schema compliance (source schema level)
    - Coordinate field generation logic

Notes:
    This module does not introduce noise or data corruption.
"""

from .field_generators import FieldGenerators


class RecordBuilder:
    """
    Builds complete synthetic customer records.
    """

    def __init__(self, seed: int = 42):

        self.gen = FieldGenerators(seed)

    def build_customer(self, index: int):
        """
        Create a synthetic customer record.

        Args:
            index (int):
                Sequential identifier used for deterministic generation.

        Returns:
            dict:
                Customer record following SOURCE_CUSTOMER_V1 schema.
        """

        return {
            "CustNo": self.gen.customer_number(index),
            "CompanyName": self.gen.company_name(),
            "StreetAddress": self.gen.street(),
            "HouseNo": self.gen.house_number(),
            "ZipCode": self.gen.zip_code(),
            "Town": self.gen.town(),
            "CountryCode": self.gen.country_code(),
            "LastOrderDate": self.gen.last_order_date(),
            "CustomerType": self.gen.customer_type(),
        }