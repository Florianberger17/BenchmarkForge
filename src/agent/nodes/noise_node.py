from pathlib import Path

from src.agent.state import BenchmarkState
from src.noise.noise_engine_minimal import NoiseEngine


class NoiseNode:
    """
    Executes the Noise Engine and creates a dirty dataset.
    """

    def __call__(self, state: BenchmarkState) -> dict:

        print("NOISE NODE STARTED")

        engine = NoiseEngine()

        engine.run()

        return {
            "dataset_path_dirty":
                "data/generated/customer_master_dirty.csv"
        }