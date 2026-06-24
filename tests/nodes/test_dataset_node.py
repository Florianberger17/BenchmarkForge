import sys
from pathlib import Path

# ---------------------------------------------------------
# Project root setup
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.agent.state import BenchmarkState
from src.agent.nodes.dataset_node import DatasetNode
from test_template import run_node


# =========================================================
# TEST
# =========================================================
def test_dataset_node():
    """
    Tests synthetic dataset generation node.
    """

    node = DatasetNode()

    state = BenchmarkState(
        scenario={
            "source_dataset": "data/generated/customer_master_clean.csv"
        },
        seed=42
    )

    result = run_node(node, state)

    # -----------------------------------------------------
    # Assertions
    # -----------------------------------------------------
    assert "dataset_clean" in result, "Missing dataset_clean"
    assert len(result["dataset_clean"]) > 0, "Dataset is empty"

    # Check basic structure
    first = result["dataset_clean"][0]
    assert "CustNo" in first, "Missing CustNo field"

    print("\n✅ Dataset Node test PASSED")


# =========================================================
# RUN DIRECTLY
# =========================================================
if __name__ == "__main__":
    test_dataset_node()