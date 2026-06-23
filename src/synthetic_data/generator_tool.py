"""
BenchmarkForge - Synthetic Data Generator

Module:
    generator_tool.py

Purpose:
    Main orchestration component for synthetic customer data generation.

Description:
    This module implements the end-to-end pipeline for generating
    synthetic customer datasets based on SOURCE_CUSTOMER_V1 schema.

    It orchestrates:
        - Configuration loading
        - Record generation
        - Dataset assembly
        - Export process

Pipeline:
    Config → RecordBuilder → FieldGenerators → Exporter → Dataset

Notes:
    This tool is designed to be callable as a standalone module
    and later integrated into a LangGraph agent system.
"""

from pathlib import Path
import yaml

from .record_builder import RecordBuilder
from .exporter import Exporter


class SyntheticCustomerDataGenerator:
    """
    Orchestrates the synthetic data generation pipeline.
    """

    def __init__(self, config_path):
        """
        Initialize generator with configuration file.

        Args:
            config_path (str):
                Path to YAML configuration file.
        """

        with open(config_path, "r") as f:

            self.config = yaml.safe_load(f)

        self.seed = self.config["dataset"]["seed"]
        self.size = self.config["dataset"]["size"]

    def generate(self):

        builder = RecordBuilder(self.seed)

        records = []

        for i in range(1, self.size + 1):

            records.append(
                builder.build_customer(i)
            )

        return records

    def run(self):
        """
        Execute full synthetic data generation pipeline.

        Steps:
            1. Load configuration
            2. Initialize record builder
            3. Generate synthetic records
            4. Export dataset to file system

        Returns:
            None
        """

        records = self.generate()

        output_path = self.config["output"]["path"]

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file.parent.mkdir(parents=True, exist_ok=True)

        Exporter.to_csv(
            records,
            output_path
        )

        print(
            f"Generated {len(records)} records"
        )

        print(
            f"Saved to: {output_path}"
        )


if __name__ == "__main__":

    generator = SyntheticCustomerDataGenerator(
        "config/generator_config_v1.yaml"
    )

    generator.run()