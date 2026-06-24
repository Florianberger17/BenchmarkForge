import sys
from pathlib import Path

# ---------------------------------------------------------
# Ensure project root is on PYTHONPATH
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.agent.state import BenchmarkState


def run_node(node, initial_state=None):
    """
    Standard execution wrapper for all BenchmarkForge nodes.

    This enables:
    - direct Python execution (no pytest required)
    - consistent debug output
    - reusable node testing pattern
    """

    state = initial_state or BenchmarkState()

    print("\n====================================")
    print(f"RUNNING NODE: {node.__class__.__name__}")
    print("====================================")

    # Execute node
    result = node(state)

    # -----------------------------------------------------
    # Debug Output
    # -----------------------------------------------------
    print("\n--- NODE OUTPUT KEYS ---")
    for k in result.keys():
        print(f"- {k}")

    print("\n--- FULL RESULT ---")
    print(result)

    return result


def print_state_summary(result: dict):
    """
    Helper function to quickly inspect state changes.
    """
    print("\n--- STATE SUMMARY ---")

    for k, v in result.items():
        if isinstance(v, (dict, list)):
            print(f"{k}: {type(v)} (len={len(v)})")
        else:
            print(f"{k}: {v}")