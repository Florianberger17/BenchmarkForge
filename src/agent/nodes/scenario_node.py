from pathlib import Path
import yaml

from src.agent.state import BenchmarkState


class ScenarioNode:
    """
    Loads and interprets scenario definitions.

    This node is the entry point of the LangGraph pipeline.
    """

    def __init__(self, scenario_path: str):
        """
        Args:
            scenario_path: relative path to scenario YAML
        """
        self.project_root = Path(__file__).resolve().parents[3]
        self.scenario_path = self.project_root / scenario_path

    # =========================================================
    # MAIN EXECUTION FUNCTION (LangGraph Node)
    # =========================================================
    def __call__(self, state: BenchmarkState) -> dict:
        """
        Loads scenario and injects into pipeline state.
        """

        # ----------------------------
        # 1. Load YAML
        # ----------------------------
        with open(self.scenario_path, "r", encoding="utf-8") as f:
            scenario = yaml.safe_load(f)

        # ----------------------------
        # 2. Load Schemas
        # ----------------------------
        source_schema = self._load_yaml(
            scenario["schema_mapping"]["source_schema_path"]
        )

        target_schema = self._load_yaml(
            scenario["schema_mapping"]["target_schema_path"]
        )

        # ----------------------------
        # 3. Extract parameters
        # ----------------------------
        scenario_id = scenario.get("scenario_id")
        task_type = scenario.get("task_type")
        seed = scenario.get("seed", 42)

        # ----------------------------
        # 4. Inject into state
        # ----------------------------
        return {
            "scenario": scenario,
            "scenario_id": scenario_id,
            "task_type": task_type,
            "seed": seed,
            "source_schema": source_schema,
            "target_schema": target_schema,
        }

    # =========================================================
    # HELPER
    # =========================================================
    def _load_yaml(self, path: str):
        full_path = self.project_root / path

        with open(full_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)