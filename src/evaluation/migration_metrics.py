# from typing import List, Dict, Any, Set, Tuple


# def _extract_identity(row: Dict[str, Any]) -> Tuple[Any, Any]:
#     """
#     Extracts unique identity from a record.
#     """
#     return row.get("CustomerID"), row.get("Name")


# def compute_migration_accuracy(
#     predicted: List[Dict[str, Any]],
#     ground_truth: List[Dict[str, Any]],
# ) -> float:
#     """
#     Evaluates correctness of migrated dataset.

#     Metric consists of:
#     1. Count match (same number of records)
#     2. Identity match (CustomerID + Name)
#     """

#     if not ground_truth:
#         return 0.0

#     # --- Extract identities ---
#     gt_ids: Set[Tuple[Any, Any]] = {
#         _extract_identity(row) for row in ground_truth
#     }

#     pred_ids: Set[Tuple[Any, Any]] = {
#         _extract_identity(row) for row in predicted
#     }

#     # --- 1. Count score ---
#     count_score = 1.0 if len(predicted) == len(ground_truth) else 0.0

#     # --- 2. Identity score ---
#     correct_matches = pred_ids.intersection(gt_ids)
#     identity_score = len(correct_matches) / len(gt_ids)

#     # --- 3. Final score ---
#     return (count_score + identity_score) / 2

from typing import List, Dict, Any, Set, Tuple


def _extract_identity(row: Dict[str, Any]) -> Tuple[Any, Any]:
    """
    Extracts unique identity from a record.
    """
    return row.get("CustomerID"), row.get("Name")


def compute_migration_accuracy(
    predicted: List[Dict[str, Any]],
    ground_truth: List[Dict[str, Any]],
) -> float:
    """
    Evaluates correctness of migrated dataset.

    Accuracy is based on identity matching:
    - CustomerID
    - Name

    Returns a score between 0.0 and 1.0.
    """

    if not ground_truth:
        return 0.0

    gt_ids: Set[Tuple[Any, Any]] = {
        _extract_identity(row)
        for row in ground_truth
    }

    pred_ids: Set[Tuple[Any, Any]] = {
        _extract_identity(row)
        for row in predicted
    }

    correct_matches = pred_ids.intersection(gt_ids)

    return len(correct_matches) / len(gt_ids)