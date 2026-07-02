from src.agent.state import BenchmarkState
from src.ground_truth.ground_truth_minimal import main as run_ground_truth


class GroundTruthNode:
    """
    Executes Ground Truth generation pipeline.

    This node runs the existing file-based Ground Truth pipeline
    (ground_truth_minimal.py) and writes the resulting files to disk.
    """

    # def __call__(self, state: BenchmarkState) -> dict:

    #     print("GROUND TRUTH NODE STARTED")

    #     # Execute existing pipeline (file-based)
    #     run_ground_truth()

    #     # Hardcoded output path (based on ground_truth_minimal.py)
    #     return {
    #         "ground_truth_path": "data/generated/customer_master_ground_truth.json"
    #     }

    def __call__(self, state: BenchmarkState) -> dict:

        print("GROUND TRUTH NODE STARTED")

        scenario = state.scenario or {}

        # Input dataset (clean)
        input_file = scenario.get(
            "source_dataset",
            "data/generated/customer_master_clean.csv"
        )

        # Execute Ground Truth pipeline with explicit input
        run_ground_truth()

        # FIX: deterministic output path
        output_file = "data/generated/customer_master_ground_truth.json"

        return {
            "ground_truth_path": output_file
        }