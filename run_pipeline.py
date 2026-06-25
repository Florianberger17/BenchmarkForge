# import json
# import argparse
# from datetime import datetime
# import os

# from src.agent.graph import build_graph
# from src.agent.state import BenchmarkState


# def run_pipeline(config_path: str | None = None):
#     # -------------------------------------------------
#     # Optional config (aktuell minimal gehalten)
#     # -------------------------------------------------
#     config = {}

#     if config_path:
#         with open(config_path, "r", encoding="utf-8") as f:
#             config = json.load(f)

#     # -------------------------------------------------
#     # Initial state
#     # -------------------------------------------------
#     initial_state = BenchmarkState()

#     # -------------------------------------------------
#     # Build & run graph
#     # -------------------------------------------------
#     graph = build_graph()
#     result = graph.invoke(initial_state)

#     # -------------------------------------------------
#     # Save output
#     # -------------------------------------------------
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     output_path = f"experiments/run_{timestamp}.json"

#     # Create folder if not existent
#     os.makedirs("experiments", exist_ok=True)

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(result, f, indent=2, default=str)

#     print("\n====================================")
#     print("PIPELINE FINISHED")
#     print("====================================")
#     print("Output:", output_path)

#     return result


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--config", required=False)

#     args = parser.parse_args()

#     run_pipeline(args.config)

import os
import json
from datetime import datetime

from src.agent.graph import build_graph
from src.agent.state import BenchmarkState

# Integration of Package Builder
from src.benchmark.package_builder import BenchmarkPackageBuilder


# =========================================================
# EXPERIMENT LOGGING
# =========================================================

def create_experiment_dir(base_dir: str = "experiments") -> str:
    """
    Creates a new experiment folder with timestamp.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = os.path.join(base_dir, f"run_{timestamp}")

    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir


def save_experiment_metadata(exp_dir: str, result: dict):
    """
    Stores full pipeline output as JSON.
    """
    output_path = os.path.join(exp_dir, "result.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=str)

    print(f"\nExperiment saved to: {output_path}")


# =========================================================
# PIPELINE EXECUTION
# =========================================================

def run_pipeline():
    graph = build_graph()

    initial_state = BenchmarkState()

    print("\n====================================")
    print("START PIPELINE")
    print("====================================")

    result = graph.invoke(initial_state)

    print("\n====================================")
    print("PIPELINE FINISHED")
    print("====================================")

    # Integration of Package Builder
    builder = BenchmarkPackageBuilder(result)
    package_path = builder.build()

    print(f"\nPACKAGE CREATED: {package_path}")

    print("Creating experiment log...")

    exp_dir = create_experiment_dir()
    save_experiment_metadata(exp_dir, result)

    return result


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    run_pipeline()