"""
BenchmarkForge - Synthetic Data Generator

Module:
    test_generator.py

Purpose:
    Provides basic unit tests for the Synthetic Data Generator pipeline.

Description:
    This test module ensures that the synthetic data generation process
    produces valid and non-empty datasets according to configuration.

    It primarily validates:
        - Successful execution of the generator
        - Correct record count
        - Basic schema presence checks

Scope:
    These tests are intentionally minimal for MVP stage.
    They serve as a smoke test rather than full schema validation.

Future Extensions:
    - Schema validation against SOURCE_CUSTOMER_V1
    - Deterministic output validation (seed-based regression tests)
    - Property-based testing for field generators
    - Data quality constraints validation
"""

from src.synthetic_data.generator_tool import (
    SyntheticCustomerDataGenerator
)


def test_generation():
    """
    Smoke test for Synthetic Customer Data Generator.

    Purpose:
        Ensures that the generator runs end-to-end without errors
        and produces at least one valid record.

    Steps:
        1. Initialize generator with test configuration
        2. Generate synthetic dataset
        3. Validate basic output structure

    Assertions:
        - Dataset is not empty
        - Required field "CustNo" exists in output records

    Returns:
        None

    Notes:
        This is a minimal MVP test. It does not validate schema compliance
        or business rules.
    """

    generator = SyntheticCustomerDataGenerator(
        "config/generator_config_v1.yaml"
    )

    records = generator.generate()

    assert len(records) > 0

    assert "CustNo" in records[0]


if __name__ == "__main__":

    test_generation()
    
    print("TEST PASSED")