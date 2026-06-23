"""
BenchmarkForge - Noise Engine (Phase 1)

Purpose:
    Minimal implementation that copies a clean dataset
    into a dirty dataset without modifications.

Goal:
    Verify pipeline, paths and export functionality
    before implementing actual noise injection.
"""

from pathlib import Path
import pandas as pd
import random
import yaml
from outdated_value_injection import OutdatedValueInjector

class NoiseEngine:
    """
    Minimal Noise Engine.
    """

    def load_config(self):
        project_root = Path(__file__).resolve().parents[2]
        config_path = project_root / "config/noise_config_v1.yaml"

        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)


    def load_noise_library(self):
        project_root = Path(__file__).resolve().parents[2]

        path = project_root / "artifacts/noise_library/typo_noise_v1.yaml"

        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)


    def inject_typo(self, value, patterns):

        if pd.isna(value):
            return value

        value = str(value)

        pattern = random.choice(patterns)["name"]

        if pattern == "character_duplication":
            if len(value) > 1:
                i = random.randint(0, len(value) - 1)
                return value[:i] + value[i] + value[i:]  # duplicate char

        if pattern == "character_deletion":
            if len(value) > 1:
                i = random.randint(0, len(value) - 1)
                return value[:i] + value[i+1:]

        if pattern == "character_swap":
            if len(value) > 1:
                i = random.randint(0, len(value) - 2)
                lst = list(value)
                lst[i], lst[i+1] = lst[i+1], lst[i]
                return "".join(lst)

        return value

    def inject_missing_value(self, value):
        return None


    def run(self):

        noise_lib = self.load_noise_library()

        patterns = noise_lib["patterns"]

        config = self.load_config()

        random.seed(config["seed"])

        noise_rate = config["noise_rate"]
        target_field = config["target_field"]

        # Missing value extension
        missing_value_rate = config.get("missing_value_rate", 0.0)
        missing_fields = config.get("missing_fields", [])

        project_root = Path(__file__).resolve().parents[2]

        input_file = (
            project_root /
            "data/generated/customer_master_clean.csv"
        )

        output_file = (
            project_root /
            "data/generated/customer_master_dirty.csv"
        )

        print("INPUT :", input_file)
        print("OUTPUT:", output_file)

        df = pd.read_csv(input_file)

        print(f"Loaded {len(df)} records")

        target_field = config["target_field"]
        noise_rate = config["noise_rate"]

        if target_field in df.columns:

            def apply_noise(value):

                if random.random() < noise_rate:
                    return self.inject_typo(value, patterns)

                return value

            df[target_field] = df[target_field].apply(apply_noise)


        # Missing value injection
        for field in missing_fields:

            if field in df.columns:

                def apply_missing(value):

                    if random.random() < missing_value_rate:
                        return self.inject_missing_value(value)

                    return value

                df[field] = df[field].apply(apply_missing)

        # Outdated Value Injection
        injector = OutdatedValueInjector(config["seed"])

        df = injector.apply(
            df,
            rate=config.get("outdated_value_rate", 0.1),
            field="LastOrderDate"
        )

        df.to_csv(
            output_file,
            index=False,
            encoding="utf-8"
        )
        

    print("Dirty dataset created")