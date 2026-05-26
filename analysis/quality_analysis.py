import pandas as pd
from pathlib import Path

expected_columns = [
    "timestamp",
    "user_id",
    "network_type",
    "throughput_mbps",
    "latency_ms"
]

strategies = {
    "Basic": "datasets/basic",
    "Constraint-Based": "datasets/constraint",
    "Chain-of-Thought": "datasets/cot",
    "Few-Shot": "datasets/fewshot"
}

results = []

for strategy_name, folder_path in strategies.items():

    csv_files = sorted(Path(folder_path).glob("*.csv"))

    rows_returned = []
    missing_values = 0
    duplicate_rows = 0
    invalid_values = 0
    format_errors = 0

    for file in csv_files:

        try:
            df = pd.read_csv(file)

            rows_returned.append(len(df))

            missing_values += df.isnull().sum().sum()

            duplicate_rows += df.duplicated().sum()

            if list(df.columns) != expected_columns:
                format_errors += 1

            throughput_check = pd.to_numeric(
                df["throughput_mbps"],
                errors="coerce"
            )

            latency_check = pd.to_numeric(
                df["latency_ms"],
                errors="coerce"
            )

            invalid_values += throughput_check.isna().sum()
            invalid_values += latency_check.isna().sum()

        except Exception as error:

            print(f"Could not read {file}")
            print(error)

            format_errors += 1

    average_rows = sum(rows_returned) / len(rows_returned)


    results.append({
        "Strategy": strategy_name,
        "Average Rows Returned": round(average_rows, 2),
        "Missing Values": int(missing_values),
        "Duplicate Rows": int(duplicate_rows),
        "Invalid Values": int(invalid_values),
        "Format Errors": int(format_errors)
    })

summary = pd.DataFrame(results)

print("\nStructural Quality Results\n")
print(summary)

summary.to_csv(
    "results/structural_quality_results.csv",
    index=False
)

print("\nResultss to quality_analysis_results.csv")