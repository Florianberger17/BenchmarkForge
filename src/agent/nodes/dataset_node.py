from pathlib import Path

from src.synthetic_data.generator_tool import SyntheticCustomerDataGenerator
from src.agent.state import BenchmarkState


class DatasetNode:
    """
    Generates synthetic clean dataset based on scenario configuration.
    """

    # def __call__(self, state: BenchmarkState) -> dict:
    #     """
    #     Execute dataset generation step.
    #     """

    #     # -----------------------------------------------------
    #     # 1. Determine config path
    #     # -----------------------------------------------------
    #     config_path = "config/generator_config_v1.yaml"

    #     generator = SyntheticCustomerDataGenerator(config_path)

    #     # -----------------------------------------------------
    #     # 2. Generate dataset
    #     # -----------------------------------------------------
    #     records = generator.generate()

    #     # -----------------------------------------------------
    #     # 3. Inject into state
    #     # -----------------------------------------------------
    #     return {
    #         "dataset_clean": records,
    #         "dataset_path_clean": scenario.get("source_dataset", None),
    #     }

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
        # 3. SAFE STATE ACCESS (FIX)
        # -----------------------------------------------------
        scenario = state.scenario or {}

        # -----------------------------------------------------
        # 4. Inject into state
        # -----------------------------------------------------
        return {
            "dataset_clean": records,

            # FIX: safe access via local variable
            "dataset_path_clean": scenario.get("source_dataset", None),
        }