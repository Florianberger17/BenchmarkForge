from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class BenchmarkState(BaseModel):
    """
    Shared state across all LangGraph nodes in BenchmarkForge.

    This state represents the full lifecycle:
    Scenario → Dataset → Noise → Ground Truth → Task → Evaluation
    """

    # =========================================================
    # 1. Scenario Layer (Entry Point)
    # =========================================================
    scenario: Optional[Dict[str, Any]] = Field(default=None)
    scenario_id: Optional[str] = None
    task_type: Optional[str] = None

    # =========================================================
    # 2. Schema Layer
    # =========================================================
    source_schema: Optional[Dict[str, Any]] = None
    target_schema: Optional[Dict[str, Any]] = None

    # =========================================================
    # 3. Dataset Layer
    # =========================================================
    dataset_clean: Optional[List[Dict[str, Any]]] = None
    dataset_dirty: Optional[List[Dict[str, Any]]] = None

    dataset_path_clean: Optional[str] = None
    dataset_path_dirty: Optional[str] = None

    # =========================================================
    # 4. Noise Layer
    # =========================================================
    noise_config: Optional[Dict[str, Any]] = None
    noise_applied: bool = False

    # =========================================================
    # 5. Ground Truth Layer
    # =========================================================
    ground_truth: Optional[Any] = None
    ground_truth_path: Optional[str] = None

    # =========================================================
    # 6. Task Layer (Agent Input)
    # =========================================================
    task: Optional[Dict[str, Any]] = None
    instruction: Optional[str] = None
    task_id: Optional[str] = None

    # =========================================================
    # 7. Execution Metadata
    # =========================================================
    seed: Optional[int] = None
    logs: List[str] = Field(default_factory=list)

    # =========================================================
    # 8. Agent + Evaluation Layer
    # =========================================================
    agent_output: Optional[Dict[str, Any]] = None
    evaluation_result: Optional[Dict[str, Any]] = None

    # =========================================================
    # VALIDATION HELPERS
    # =========================================================
    def add_log(self, message: str):
        """Append log entry for debugging pipeline execution."""
        self.logs.append(message)

    def is_valid_for_execution(self) -> bool:
        """
        Minimal consistency check before running pipeline.
        """
        return self.scenario is not None and self.dataset_clean is not None