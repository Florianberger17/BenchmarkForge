import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.agent.graph import run_pipeline


def test_graph():

    result = run_pipeline()

    assert result is not None

    print("\n✅ Graph test PASSED")


if __name__ == "__main__":
    test_graph()