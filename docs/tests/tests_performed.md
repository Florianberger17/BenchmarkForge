# List withe relevant Tests:

## Synthetic Data Generator:
- Sanity Check -> Bash: "python -m tests.test_generator" -> Passed (2026/06/24)
- Synthetic Record Creation -> Bash "python -m src.synthetic_data.generator_tool" -> Generated "customer_master_clean.csv" (2026/06/24)

## Noise Engine:
- Noise Injection -> Bash: "python src/noise/run_noise_engine.py" -> Generated "customer_master_dirty.csv" (2026/06/24)

## Ground Truth Generator:
- Record Generation -> Bash: "python src/ground_truth/ground_truth_minimal.py" -> Generated "customer_master_ground_truth.csv" + "customer_master_ground_truth.json" (2026/06/24)

## Task Generator:
- Functionality -> Bash: "python -m tests.test_task_generator" -> Console Output created (2026/06/24)

## Nodes & Agent Workflow:
- Scenario Node -> Bash: "python tests/nodes/test_scenario_node.py" -> Passed (2026/06/24)
- Dataset Node -> Bash: "python tests/nodes/test_dataset_node.py" -> Passed (2026/06/24)
