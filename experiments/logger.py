import os
import json
from datetime import datetime
from typing import Any, Dict


class ExperimentLogger:
    def __init__(self, base_dir: str = "experiments"):
        self.base_dir = base_dir

    def create_run_dir(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_dir = os.path.join(self.base_dir, f"run_{timestamp}")
        os.makedirs(run_dir, exist_ok=True)
        return run_dir

    def save_json(self, path: str, data: Any):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)

    def log_run(
        self,
        result: Dict[str, Any],
        config: Dict[str, Any],
        metadata: Dict[str, Any],
    ) -> str:

        run_dir = self.create_run_dir()

        self.save_json(os.path.join(run_dir, "result.json"), result)
        self.save_json(os.path.join(run_dir, "config.json"), config)
        self.save_json(os.path.join(run_dir, "metadata.json"), metadata)

        return run_dir