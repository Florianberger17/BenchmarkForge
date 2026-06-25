import os
import json
import shutil
from datetime import datetime


class BenchmarkPackageBuilder:
    """
    Collects all generated artifacts from a pipeline run
    and builds a reproducible benchmark package.
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

        os.makedirs(self.package_path, exist_ok=True)

    # -----------------------------------------------------
    # MAIN ENTRY
    # -----------------------------------------------------

    def build(self):
        self._copy_artifacts()
        self._write_metadata()

        print(f"\nBenchmark package created at: {self.package_path}")

        return self.package_path

    # -----------------------------------------------------
    # ARTIFACT COLLECTION
    # -----------------------------------------------------

    def _copy_artifacts(self):
        """
        Extracts known artifacts from pipeline result
        and copies them into package folder.
        """

        artifacts = self._extract_artifacts()

        for name, path in artifacts.items():
            if not path:
                continue

            if os.path.exists(path):
                dest_path = os.path.join(self.package_path, os.path.basename(path))
                shutil.copy2(path, dest_path)

    def _extract_artifacts(self) -> dict:
        """
        Maps run output to file artifacts.
        """

        return {
            "dataset_dirty": self.run_result.get("dataset_dirty"),
            "dataset_ground_truth": self.run_result.get("ground_truth_path"),
            "scenario": self.run_result.get("scenario", {}).get("scenario_path"),
        }

    # -----------------------------------------------------
    # METADATA
    # -----------------------------------------------------

    def _write_metadata(self):
        metadata = {
            "package_id": self.package_id,
            "created_at": datetime.now().isoformat(),
            "source_run_keys": list(self.run_result.keys()),
        }

        metadata_path = os.path.join(self.package_path, "package.json")

        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, default=str)