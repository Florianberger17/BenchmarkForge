from typing import Dict, Any


def compute_mapping_accuracy(
    predicted: Dict[str, Any],
    ground_truth: Dict[str, Any]
) -> float:
    """
    Computes simple attribute-level mapping accuracy.

    Args:
        predicted: predicted schema mapping
        ground_truth: correct schema mapping

    Returns:
        accuracy score between 0 and 1
    """

    if not ground_truth:
        return 0.0

    total = len(ground_truth)
    correct = 0

    for src_attr, true_target in ground_truth.items():
        pred_target = predicted.get(src_attr)

        if pred_target == true_target:
            correct += 1

    return correct / total