import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.agent.nodes.noise_node import NoiseNode
from src.agent.state import BenchmarkState

from test_template import run_node


def test_noise_node():

    node = NoiseNode()

    state = BenchmarkState()

    result = run_node(node, state)

    assert "dataset_path_dirty" in result

    print("\n✅ Noise Node test PASSED")


if __name__ == "__main__":

    test_noise_node()