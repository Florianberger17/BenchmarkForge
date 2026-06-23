"""
BenchmarkForge - Synthetic Data Generator

Module:
    exporter.py

Purpose:
    Responsible for exporting synthetic datasets into persistent storage formats.

Description:
    Provides a clean abstraction layer for dataset serialization.
    Currently supports CSV export, but designed for future extensibility.

Responsibilities:
    - Serialize synthetic datasets
    - Persist data to filesystem
    - Maintain encoding consistency

Future Extensions:
    - JSON export
    - Parquet export
    - Database export
"""

import pandas as pd


class Exporter:
    """
    Handles dataset export operations.
    """

    @staticmethod
    def to_csv(records, path):
        """
        Export synthetic records to CSV format.

        Args:
            records (list[dict]):
                List of synthetic customer records.

            path (str):
                Output file path.

        Returns:
            None
        """

        df = pd.DataFrame(records)

        df.to_csv(
            path,
            index=False,
            encoding="utf-8"
        )