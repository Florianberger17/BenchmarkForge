from src.evaluation.mapping_metrics import compute_mapping_accuracy


def test_mapping_metrics():
    ground_truth = {
        "CustNo": "CustomerID",
        "CompanyName": "Name",
        "ZipCode": "PostalCode"
    }

    prediction = {
        "CustNo": "CustomerID",
        "CompanyName": "Name",
        "ZipCode": "Zip"
    }

    score = compute_mapping_accuracy(prediction, ground_truth)

    assert 0.0 <= score <= 1.0, "Score must be between 0 and 1"

    print("\n==============================")
    print("Mapping Metric Test Result")
    print("==============================")
    print(f"Accuracy Score: {score:.2f}")

    if score == 1.0:
        print("STATUS: PERFECT MATCH ✅")
    elif score >= 0.7:
        print("STATUS: GOOD MATCH ⚠️")
    else:
        print("STATUS: POOR MATCH ❌")


if __name__ == "__main__":
    try:
        test_mapping_metrics()
        print("\nTEST RESULT: SUCCESS ✅")
    except AssertionError as e:
        print("\nTEST RESULT: FAILED ❌")
        print(f"Assertion Error: {e}")
    except Exception as e:
        print("\nTEST RESULT: CRASHED 💥")
        print(f"Unexpected Error: {e}")