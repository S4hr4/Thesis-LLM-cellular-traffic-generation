from openai import OpenAI

client = OpenAI(
    api_key=" ---- "
)

prompt = """
Generate synthetic 5G cellular network traffic data in CSV format.

Columns:
timestamp,user_id,network_type,throughput_mbps,latency_ms

Before generating the dataset:

1. Consider realistic throughput values in 5G networks.
2. Consider realistic latency values in 5G networks.
3. Consider realistic variation between users.
4. Use this reasoning internally when generating the data.

Generate exactly 500 rows.

Return only raw CSV.
Do not include explanations.
Do not use markdown.
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.8
)

csv_data = response.choices[0].message.content

lines = csv_data.strip().splitlines()
rows_returned = len(lines) - 1 

print(f"Rows returned: {rows_returned}")

with open("datasets/cot/run10.csv", "w") as file:
    file.write(csv_data)

print("Chain-of-thought dataset succeded to generate brollan;))")