from pathlib import Path
import pandas as pd
import os

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
        # scenario = state.scenario or {}

        # # -----------------------------------------------------
        # # 4. Inject into state
        # # -----------------------------------------------------
        # return {
        #     "dataset_clean": records,

        #     # FIX: safe access via local variable
        #     "dataset_path_clean": scenario.get("source_dataset", None),
        # }


        # 3. SAFE STATE ACCESS
        scenario = state.scenario or {}

        # 4. WRITE CLEAN DATASET TO FILE
        output_path = "data/generated/customer_master_clean.csv"

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        pd.DataFrame(records).to_csv(output_path, index=False)

        # 5. RETURN CONSISTENT ARTIFACT CONTRACT
#         return {
#             "dataset_clean": records,
#             "dataset_path_clean": output_path
# }
        return {
            "dataset_path_clean": "data/generated/customer_master_clean.csv"
        }