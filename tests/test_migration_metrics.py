from src.evaluation.migration_metrics import compute_migration_accuracy


def test_migration_metrics_perfect_match():
    ground_truth = [
        {
            "CustomerID": "CUST000001",
            "Name": "Dowerg"
        },
        {
            "CustomerID": "CUST000002",
            "Name": "Davids AG & Co. OHG"
        }
    ]

    prediction = [
        {
            "CustomerID": "CUST000001",
            "Name": "Dowerg"
        },
        {
            "CustomerID": "CUST000002",
            "Name": "Davids AG & Co. OHG"
        }
    ]

    score = compute_migration_accuracy(prediction, ground_truth)

    print("\n--- PERFECT MATCH TEST ---")
    print("Score:", score)

    assert score == 1.0


def test_migration_metrics_partial_match():
    ground_truth = [
        {
            "CustomerID": "CUST000001",
            "Name": "Dowerg"
        },
        {
            "CustomerID": "CUST000002",
            "Name": "Davids AG & Co. OHG"
        },
        {
            "CustomerID": "CUST000003",
            "Name": "Thanel GmbH & Co. KG"
        }
    ]

    prediction = [
        {
            "CustomerID": "CUST000001",
            "Name": "Dowerg"
        },
        {
            "CustomerID": "CUST000002",
            "Name": "Davids AG & Co. OHG"
        }
    ]

    score = compute_migration_accuracy(prediction, ground_truth)

    print("\n--- PARTIAL MATCH TEST ---")
    print("Score:", score)

    assert 0.0 < score < 1.0


def test_migration_metrics_wrong_match():
    ground_truth = [
        {
            "CustomerID": "CUST000001",
            "Name": "Dowerg"
        }
    ]

    prediction = [
        {
            "CustomerID": "WRONG_ID",
            "Name": "Unknown"
        }
    ]

    score = compute_migration_accuracy(prediction, ground_truth)

    print("\n--- WRONG MATCH TEST ---")
    print("Score:", score)

    assert score == 0.0


if __name__ == "__main__":
    test_migration_metrics_perfect_match()
    test_migration_metrics_partial_match()
    test_migration_metrics_wrong_match()

    print("\nALL TESTS PASSED ✅")