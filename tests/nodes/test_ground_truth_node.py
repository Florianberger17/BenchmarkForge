import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.agent.nodes.ground_truth_node import GroundTruthNode
from src.agent.state import BenchmarkState

from test_template import run_node


def test_ground_truth_node():

    node = GroundTruthNode()

    state = BenchmarkState()

    # Minimal required state setup (currently not used by file-based pipeline,
    # but kept for future compatibility)
    state.scenario = {
        "name": "customer_master_test",
        "type": "synthetic_benchmark"
    }

    state.dataset_path_dirty = "data/generated/customer_master_dirty.csv"

    result = run_node(node, state)

    assert "ground_truth_path" in result
    assert result["ground_truth_path"] is not None

    print("\n✅ Ground Truth Node test PASSED")


if __name__ == "__main__":
    test_ground_truth_node()