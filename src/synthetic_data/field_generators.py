"""
BenchmarkForge - Synthetic Data Generator

Module:
    field_generators.py

Purpose:
    Provides low-level field generation functions for synthetic
    customer master data creation.

Description:
    This module encapsulates all logic required to generate
    individual attribute values for synthetic customer records.

    It uses a combination of:
        - Faker-based data generation
        - deterministic seeding
        - simple rule-based value generation

Responsibilities:
    - Generate realistic company names
    - Generate address components
    - Generate structured identifiers
    - Provide reproducible pseudo-random values

Notes:
    This module is schema-aware only indirectly via RecordBuilder.
"""

from faker import Faker
import random
from datetime import date, timedelta

faker = Faker("de_DE")


class FieldGenerators:
    """
    Generates synthetic values for individual customer attributes.

    All functions are deterministic when initialized with a seed.
    """

    def __init__(self, seed: int = 42):

        self.seed = seed

        Faker.seed(seed)
        random.seed(seed)

    def customer_number(self, index: int) -> str:
        """
        Generate a deterministic customer identifier.

        Args:
            index (int): Sequential record index.

        Returns:
            str: Unique customer ID (e.g., CUST000001)
        """

        return f"CUST{index:06d}"

    def company_name(self) -> str:

        return faker.company()

    def street(self) -> str:

        return faker.street_name()

    def house_number(self) -> str:

        return str(random.randint(1, 200))

    def zip_code(self) -> str:

        return faker.postcode()

    def town(self) -> str:

        return faker.city()

    def country_code(self) -> str:

        return random.choice(["DE", "AT", "CH"])

    def last_order_date(self):

        days_back = random.randint(0, 365 * 8)

        return date.today() - timedelta(days=days_back)

    def customer_type(self):

        return random.choice(
            [
                "Customer",
                "Prospect",
                "FormerCustomer",
            ]
        )