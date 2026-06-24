import sys
from pathlib import Path

# ---------------------------------------------------------
# Ensure project root is importable
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.agent.nodes.scenario_node import ScenarioNode
from src.agent.state import BenchmarkState
from test_template import run_node


# =========================================================
# TEST FUNCTION
# =========================================================
def test_scenario_node():
    """
    Executes Scenario Node in isolation.
    """

    node = ScenarioNode("artifacts/scenarios/scenario_v1.yaml")

    result = run_node(node)

    # -----------------------------------------------------
    # Assertions (lightweight, no pytest)
    # -----------------------------------------------------
    assert "scenario" in result, "Scenario missing"
    assert "source_schema" in result, "Source schema missing"
    assert "target_schema" in result, "Target schema missing"
    assert result.get("scenario_id") is not None

    print("\n✅ Scenario Node test PASSED")


# =========================================================
# DIRECT EXECUTION ENTRYPOINT
# =========================================================
if __name__ == "__main__":
    test_scenario_node()