from src.evaluation.metrics import run_evaluation


def test_full_evaluation():
    print("\n--- FULL EVALUATION TEST ---")

    predicted_mapping = {
        "CustNo": "CustomerID",
        "CompanyName": "Name",
        "ZipCode": "PostalCode"
    }

    ground_truth_mapping = {
        "CustNo": "CustomerID",
        "CompanyName": "Name",
        "StreetAddress": "Street",
        "ZipCode": "PostalCode"
    }

    predicted_dataset = [
        {"CustomerID": "CUST001", "Name": "Company A"},
        {"CustomerID": "CUST002", "Name": "Company B"},
    ]

    ground_truth_dataset = [
        {"CustomerID": "CUST001", "Name": "Company A"},
        {"CustomerID": "CUST999", "Name": "Wrong Company"},
    ]

    result = run_evaluation(
        predicted_mapping,
        ground_truth_mapping,
        predicted_dataset,
        ground_truth_dataset,
    )

    print("Result:", result)

    # --- expected values ---
    assert "mapping_accuracy" in result
    assert "migration_accuracy" in result
    assert "overall_score" in result

    # mapping: 3 correct out of 4
    assert abs(result["mapping_accuracy"] - 0.75) < 1e-6

    # migration: 1 correct out of 2
    assert abs(result["migration_accuracy"] - 0.5) < 1e-6

    # overall: (0.75 + 0.5) / 2
    assert abs(result["overall_score"] - 0.625) < 1e-6

    print("TEST PASSED ✔")


def test_empty_ground_truth():
    print("\n--- EMPTY GROUND TRUTH TEST ---")

    result = run_evaluation(
        predicted_mapping={},
        ground_truth_mapping={},
        predicted_dataset=[],
        ground_truth_dataset=[],
    )

    print("Result:", result)

    assert result["mapping_accuracy"] == 0.0
    assert result["migration_accuracy"] == 0.0
    assert result["overall_score"] == 0.0

    print("TEST PASSED ✔")


if __name__ == "__main__":
    test_full_evaluation()
    test_empty_ground_truth()