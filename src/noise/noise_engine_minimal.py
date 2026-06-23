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


    # def inject_typo(self, value, suffix="X"):
    #     if pd.isna(value):
    #         return value
    #     return str(value) + suffix

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


    def run(self):

        noise_lib = self.load_noise_library()

        patterns = noise_lib["patterns"]

        config = self.load_config()

        random.seed(config["seed"])

        noise_rate = config["noise_rate"]
        target_field = config["target_field"]
        # suffix = config["noise_suffix"]

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
        # suffix = config["noise_suffix"]

        # if target_field in df.columns:

        #     def apply_noise(value):

        #         if random.random() < noise_rate:
        #             return self.inject_typo(value, suffix)

        #         return value

        # df[target_field] = df[target_field].apply(apply_noise)

        if target_field in df.columns:

            def apply_noise(value):

                if random.random() < noise_rate:
                    return self.inject_typo(value, patterns)

                return value

            df[target_field] = df[target_field].apply(apply_noise)


        df.to_csv(
            output_file,
            index=False,
            encoding="utf-8"
        )
        

    print("Dirty dataset created")