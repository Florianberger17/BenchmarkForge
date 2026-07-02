# import yaml
# from pathlib import Path


# class TaskGenerator:
#     """
#     Converts scenario definitions into schema-aware benchmark tasks.
#     """

#     def __init__(self, scenario_path):

#         project_root = Path(__file__).resolve().parents[3]
#         full_path = project_root / scenario_path

#         with open(full_path, "r", encoding="utf-8") as f:
#             self.scenario = yaml.safe_load(f)

#         # Load schemas
#         self.source_schema = self._load_yaml(
#             self.scenario["schema_mapping"]["source_schema_path"]
#         )

#         self.target_schema = self._load_yaml(
#             self.scenario["schema_mapping"]["target_schema_path"]
#         )

#     def _load_yaml(self, path):
#         project_root = Path(__file__).resolve().parents[3]
#         full_path = project_root / path

#         with open(full_path, "r", encoding="utf-8") as f:
#             return yaml.safe_load(f)

#     def generate_task(self):

#         task = {
#             "task_id": self.scenario["scenario_id"],
#             "task_type": self.scenario["task_type"],

#             "instruction": (
#                 "Migrate customer data from SOURCE schema "
#                 "to TARGET schema according to mapping rules."
#             ),

#             "input_dataset": self.scenario["source_dataset"],
#             "ground_truth": self.scenario["ground_truth"],

#             "schemas": {
#                 "source": self.source_schema,
#                 "target": self.target_schema
#             }
#         }

#         return task

import yaml
from pathlib import Path


class TaskGenerator:
    """
    Converts scenario definitions into schema-aware benchmark tasks.
    """

    def __init__(self, scenario_path):

        project_root = Path(__file__).resolve().parents[3]
        full_path = project_root / scenario_path

        with open(full_path, "r", encoding="utf-8") as f:
            self.scenario = yaml.safe_load(f)

        # Load schemas
        self.source_schema = self._load_yaml(
            self.scenario["schema_mapping"]["source_schema_path"]
        )

        self.target_schema = self._load_yaml(
            self.scenario["schema_mapping"]["target_schema_path"]
        )

    def _load_yaml(self, path):
        project_root = Path(__file__).resolve().parents[3]
        full_path = project_root / path

        with open(full_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    # =====================================================
    # Build internal task representation
    # =====================================================

    def generate_task(self):

        task = {
            "task_id": self.scenario["scenario_id"],
            "task_type": self.scenario["task_type"],

            "instruction": (
                "Migrate customer data from the SOURCE schema "
                "to the TARGET schema according to the provided schemas."
            ),

            "input_dataset": self.scenario["source_dataset"],

            "schemas": {
                "source": self.source_schema,
                "target": self.target_schema
            }
        }

        return task

    # =====================================================
    # Export task as Markdown
    # =====================================================

    def export_markdown(self, output_dir):

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        task = self.generate_task()

        md = f"""# Benchmark Task

## Task ID

{task["task_id"]}

## Task Type

{task["task_type"]}

## Objective

{task["instruction"]}

## Input

The benchmark package provides the following input:

- data/dataset_dirty.csv
- schemas/source_schema.yaml
- schemas/target_schema.yaml

## Expected Output

Create the following files:

- migrated_dataset.csv
- mapping.json
- documentation.md

## Notes

- Preserve customer identities.
- Apply the target schema.
- Handle noisy values correctly.
- Produce deterministic results.
"""

        output_file = output_dir / "task.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md)

        return output_file