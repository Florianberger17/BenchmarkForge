from typing import Dict, Any
import json
from pathlib import Path

from src.evaluation.mapping_metrics import compute_mapping_accuracy
from src.evaluation.migration_metrics import compute_migration_accuracy


def compute_overall_score(mapping_score: float, migration_score: float) -> float:
    """
    Simple weighted aggregation (equal weights for now).
    """
    return (mapping_score + migration_score) / 2


def run_evaluation(
    predicted_mapping: Dict[str, Any],
    ground_truth_mapping: Dict[str, Any],
    predicted_dataset: list,
    ground_truth_dataset: list,
) -> Dict[str, Any]:
    """
    Runs full evaluation pipeline and returns unified report.
    """

    # --- individual metrics ---
    mapping_score = compute_mapping_accuracy(
        predicted_mapping,
        ground_truth_mapping,
    )

    migration_score = compute_migration_accuracy(
        predicted_dataset,
        ground_truth_dataset,
    )

    # --- aggregate ---
    overall_score = compute_overall_score(mapping_score, migration_score)

    return {
        "mapping_accuracy": mapping_score,
        "migration_accuracy": migration_score,
        "overall_score": overall_score,
    }


def save_evaluation_report(
    report: Dict[str, Any],
    output_path: str,
) -> None:
    """
    Saves evaluation report as JSON.
    """

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)