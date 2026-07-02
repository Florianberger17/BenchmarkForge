# import os
# import json
# import shutil
# from datetime import datetime


# class BenchmarkPackageBuilder:
#     """
#     Collects all generated artifacts from a pipeline run
#     and builds a reproducible benchmark package.
#     """

#     def __init__(
#         self,
#         run_result: dict,
#         output_root: str = "benchmark_packages"
#     ):
#         self.run_result = run_result
#         self.output_root = output_root

#         self.package_id = datetime.now().strftime("package_%Y%m%d_%H%M%S")
#         self.package_path = os.path.join(output_root, self.package_id)

#         os.makedirs(self.package_path, exist_ok=True)

#     # -----------------------------------------------------
#     # MAIN ENTRY
#     # -----------------------------------------------------

#     def build(self):
#         self._copy_artifacts()
#         self._write_metadata()

#         print(f"\nBenchmark package created at: {self.package_path}")

#         return self.package_path

#     # -----------------------------------------------------
#     # ARTIFACT COLLECTION
#     # -----------------------------------------------------

#     def _copy_artifacts(self):
#         """
#         Extracts known artifacts from pipeline result
#         and copies them into package folder.
#         """

#         artifacts = self._extract_artifacts()

#         for name, path in artifacts.items():
#             if not path:
#                 continue

#             if os.path.exists(path):
#                 dest_path = os.path.join(self.package_path, os.path.basename(path))
#                 shutil.copy2(path, dest_path)

#     def _extract_artifacts(self) -> dict:
#         """
#         Maps run output to file artifacts.
#         """

#         return {
#             "dataset_dirty": self.run_result.get("dataset_dirty"),
#             "dataset_ground_truth": self.run_result.get("ground_truth_path"),
#             "scenario": self.run_result.get("scenario", {}).get("scenario_path"),
#         }

#     # -----------------------------------------------------
#     # METADATA
#     # -----------------------------------------------------

#     def _write_metadata(self):
#         metadata = {
#             "package_id": self.package_id,
#             "created_at": datetime.now().isoformat(),
#             "source_run_keys": list(self.run_result.keys()),
#         }

#         metadata_path = os.path.join(self.package_path, "package.json")

#         with open(metadata_path, "w", encoding="utf-8") as f:
#             json.dump(metadata, f, indent=2, default=str)


import os
import json
import shutil
from datetime import datetime


class BenchmarkPackageBuilder:
    """
    Builds a fully self-contained benchmark package
    according to Benchmark Package Spec v1.0.
    """

    def __init__(
        self,
        run_result: dict,
        output_root: str = "benchmark_packages"
    ):
        self.run_result = run_result
        self.output_root = output_root

        self.package_id = datetime.now().strftime("package_%Y%m%d_%H%M%S")
        self.package_path = os.path.join(output_root, self.package_id)

        # Create full directory structure
        self._create_structure()

    # =====================================================
    # STRUCTURE
    # =====================================================

    def _create_structure(self):
        os.makedirs(self.package_path, exist_ok=True)

        os.makedirs(os.path.join(self.package_path, "data"), exist_ok=True)
        os.makedirs(os.path.join(self.package_path, "ground_truth"), exist_ok=True)
        os.makedirs(os.path.join(self.package_path, "schemas"), exist_ok=True)
        os.makedirs(os.path.join(self.package_path, "runtime"), exist_ok=True)

    # =====================================================
    # PUBLIC API
    # =====================================================

    def build(self):
        self._copy_data()
        self._copy_schemas()
        self._copy_scenario()
        self._write_ground_truth()
        self._write_manifest()
        self._write_runtime_metadata()

        print(f"\nBenchmark package created at: {self.package_path}")

        return self.package_path

    # =====================================================
    # COPY DATASETS
    # =====================================================

    # def _copy_data(self):
    #     dirty = self.run_result.get("dataset_dirty")
    #     clean = self.run_result.get("dataset_clean")

    #     if dirty and os.path.exists(dirty):
    #         shutil.copy2(
    #             dirty,
    #             os.path.join(self.package_path, "data", "dataset_dirty.csv")
    #         )

    #     if clean and os.path.exists(clean):
    #         shutil.copy2(
    #             clean,
    #             os.path.join(self.package_path, "data", "dataset_clean.csv")
    #         )

    # def _copy_data(self):
    #     dirty = self.run_result.get("dataset_dirty")
    #     clean = self.run_result.get("dataset_clean")

    #     # 🔧 FIX: normalize lists
    #     if isinstance(clean, list):
    #         clean = None
    #     if isinstance(dirty, list):
    #         dirty = None

    #     if dirty and os.path.exists(dirty):
    #         shutil.copy2(
    #             dirty,
    #             os.path.join(self.package_path, "data", "dataset_dirty.csv")
    #         )

    #     if clean and os.path.exists(clean):
    #         shutil.copy2(
    #             clean,
    #             os.path.join(self.package_path, "data", "dataset_clean.csv")
    #         )

    def _copy_data(self):
        base = "data/generated"

        clean = os.path.join(base, "customer_master_clean.csv")
        dirty = os.path.join(base, "customer_master_dirty.csv")

        if os.path.exists(clean):
            shutil.copy2(
                clean,
                os.path.join(self.package_path, "data", "dataset_clean.csv")
            )

        if os.path.exists(dirty):
            shutil.copy2(
                dirty,
                os.path.join(self.package_path, "data", "dataset_dirty.csv")
            )


    # =====================================================
    # SCHEMAS
    # =====================================================

    def _copy_schemas(self):
        scenario = self.run_result.get("scenario", {})
        schema = scenario.get("schema_mapping", {})

        source_schema = schema.get("source_schema_path")
        target_schema = schema.get("target_schema_path")

        if source_schema and os.path.exists(source_schema):
            shutil.copy2(
                source_schema,
                os.path.join(self.package_path, "schemas", "source_schema.yaml")
            )

        if target_schema and os.path.exists(target_schema):
            shutil.copy2(
                target_schema,
                os.path.join(self.package_path, "schemas", "target_schema.yaml")
            )

    # =====================================================
    # SCENARIO
    # =====================================================

    def _copy_scenario(self):
        scenario_path = "artifacts/scenarios/scenario_v1.yaml"

        if os.path.exists(scenario_path):
            shutil.copy2(
                scenario_path,
                os.path.join(self.package_path, "scenario.yaml")
            )

    # =====================================================
    # GROUND TRUTH
    # =====================================================

    def _write_ground_truth(self):
        gt_path = self.run_result.get("ground_truth_path")

        if gt_path and os.path.exists(gt_path):
            shutil.copy2(
                gt_path,
                os.path.join(self.package_path, "ground_truth", "ground_truth.json")
            )

    # =====================================================
    # MANIFEST
    # =====================================================

    def _write_manifest(self):
        scenario = self.run_result.get("scenario", {})

        manifest = {
            "package_id": self.package_id,
            "version": "1.0",
            "created_at": datetime.now().isoformat(),

            "task_type": scenario.get("task_type"),
            "scenario_id": scenario.get("scenario_id"),

            "reproducibility": {
                "seed": scenario.get("seed", 42),
                "deterministic": True
            },

            "entry_points": {
                "dataset_dirty": "data/dataset_dirty.csv",
                "dataset_clean": "data/dataset_clean.csv",
                "ground_truth": "ground_truth/ground_truth.json",
                "scenario": "scenario.yaml"
            }
        }

        path = os.path.join(self.package_path, "manifest.json")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, default=str)

    # =====================================================
    # RUNTIME METADATA
    # =====================================================

    def _write_runtime_metadata(self):
        metadata = {
            "generated_by": "BenchmarkForge",
            "created_at": datetime.now().isoformat(),
            "source_run_keys": list(self.run_result.keys())
        }

        path = os.path.join(self.package_path, "runtime", "run_metadata.json")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, default=str)