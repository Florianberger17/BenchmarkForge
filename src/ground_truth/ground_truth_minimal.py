"""
BenchmarkForge - Minimal Ground Truth Runner

Purpose:
    Minimal end-to-end test of file I/O for Ground Truth generation.
    No mapping, no config, no abstraction.
"""

from pathlib import Path
import pandas as pd
from src.ground_truth.mapping_engine import MappingEngine
# from mapping_engine import MappingEngine      # Only for direct use via console
import json

def main():

    print("RUN START")

    # HARD-CODED PATHS (intentional for debugging)
    input_file = Path("data/generated/customer_master_clean.csv")
    output_file = Path("data/generated/customer_master_ground_truth.csv")

    print("INPUT FILE:", input_file.resolve())
    print("OUTPUT FILE:", output_file.resolve())

    # Validate input exists
    if not input_file.exists():
        print("ERROR: Input file does not exist!")
        return

    # Read data
    df = pd.read_csv(input_file)
    print("ROWS LOADED:", len(df))

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    records = df.to_dict(orient="records")

    transformed = []

    # for r in records:
    #     transformed.append(transform_record(r))
    
    engine = MappingEngine()

    for r in records:
        transformed.append(engine.transform_record(r))

    ground_truth_bundle = {
        "metadata": {
            "dataset": "customer_master",
            "source_schema": "SOURCE_CUSTOMER_V1",
            "target_schema": "TARGET_ERP_CUSTOMER_V1",
            "version": "1.0"
            },
        "records": transformed
    }

    json_output_file = output_file.with_suffix(".json")

    with open(json_output_file, "w", encoding="utf-8") as f:
        json.dump(ground_truth_bundle, f, indent=2, ensure_ascii=False)

    pd.DataFrame(transformed).to_csv(output_file, index=False)

    print("CSV SAVED:", output_file.resolve())
    print("JSON SAVED:", json_output_file.resolve())

    # json_output_file = output_file.with_suffix(".json")

    print("SUCCESS: File written")
    print("RUN END")


if __name__ == "__main__":
    main()