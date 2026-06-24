from pathlib import Path

from src.synthetic_data.generator_tool import SyntheticCustomerDataGenerator
from src.agent.state import BenchmarkState


class DatasetNode:
    """
    Generates synthetic clean dataset based on scenario configuration.
    """

    def __call__(self, state: BenchmarkState) -> dict:
        """
        Execute dataset generation step.
        """

        # -----------------------------------------------------
        # 1. Determine config path
        # -----------------------------------------------------
        config_path = "config/generator_config_v1.yaml"

        generator = SyntheticCustomerDataGenerator(config_path)

        # -----------------------------------------------------
        # 2. Generate dataset
        # -----------------------------------------------------
        records = generator.generate()

        # -----------------------------------------------------
        # 3. Inject into state
        # -----------------------------------------------------
        return {
            "dataset_clean": records,
            "dataset_path_clean": state.scenario.get(
                "source_dataset", None
            ),
        }