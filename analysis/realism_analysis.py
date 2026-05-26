import pandas as pd
from pathlib import Path

strategies = {
    "Basic": "datasets/basic",
    "Constraint-Based": "datasets/constraint",
    "Chain-of-Thought": "datasets/cot",
    "Few-Shot": "datasets/fewshot"
}

results = []

for strategy_name, folder_path in strategies.items():

    csv_files = sorted(Path(folder_path).glob("*.csv"))

    all_throughput_values = []
    all_latency_values = []

    for file in csv_files:

        try:
            df = pd.read_csv(file)

            throughput_values = pd.to_numeric(
                df["throughput_mbps"],
                errors="coerce"
            )

            latency_values = pd.to_numeric(
                df["latency_ms"],
                errors="coerce"
            )

            all_throughput_values.extend(
                throughput_values.dropna().tolist()
            )

            all_latency_values.extend(
                latency_values.dropna().tolist()
            )

        except Exception as error:

            print(f"Could not read {file}")
            print(error)

    results.append({
        "Dataset": strategy_name,

        "Average Throughput":
            round(sum(all_throughput_values) /
                  len(all_throughput_values), 2),

        "Minimum Throughput":
            min(all_throughput_values),

        "Maximum Throughput":
            max(all_throughput_values),

        "Average Latency":
            round(sum(all_latency_values) /
                  len(all_latency_values), 2),

        "Minimum Latency":
            min(all_latency_values),

        "Maximum Latency":
            max(all_latency_values)
    })


glasgow = pd.read_csv(
    "glasgow_dataset.csv",
    sep=";"
)

download_speed = (
    glasgow["Download Speed (Mbps)"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

ping_latency = (
    glasgow["Ping (ms)"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

results.append({
    "Dataset": "Glasgow",

    "Average Throughput":
        round(download_speed.mean(), 2),

    "Minimum Throughput":
        download_speed.min(),

    "Maximum Throughput":
        download_speed.max(),

    "Average Latency":
        round(ping_latency.mean(), 2),

    "Minimum Latency":
        ping_latency.min(),

    "Maximum Latency":
        ping_latency.max()
})


summary = pd.DataFrame(results)

print("\nRealism Analysis Results\n")
print(summary)

summary.to_csv(
    "results/realism_analysis_results.csv",
    index=False
)

print("\nResults savedd to realism_analysis_results.csv")