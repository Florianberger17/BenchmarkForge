# print("SOURCE SCHEMA ID:", task["schemas"]["source"]["schema_id"])
# print("TARGET SCHEMA ID:", task["schemas"]["target"]["schema_id"])

# assert task["schemas"]["source"]["schema_id"] == "SOURCE_CUSTOMER_V1"
# assert task["schemas"]["target"]["schema_id"] == "TARGET_ERP_CUSTOMER_V1"

from src.agent.nodes.task_node import TaskGenerator


def test_task_generator():

    generator = TaskGenerator("artifacts/scenarios/scenario_v1.yaml")

    task = generator.generate_task()

    print("\nTASK CREATED:\n", task)

    print("\nSOURCE SCHEMA ID:", task["schemas"]["source"]["schema_id"])
    print("TARGET SCHEMA ID:", task["schemas"]["target"]["schema_id"])

    assert task["schemas"]["source"]["schema_id"] == "SOURCE_CUSTOMER_V1"
    assert task["schemas"]["target"]["schema_id"] == "TARGET_ERP_CUSTOMER_V1"


if __name__ == "__main__":
    test_task_generator()