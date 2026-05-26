from openai import OpenAI

client = OpenAI(
    api_key=" ---- "
)

prompt = """
Generate synthetic 5G cellular network traffic data in CSV format.

Columns:
timestamp,user_id,network_type,throughput_mbps,latency_ms

Requirements:

- network_type must always be 5G
- throughput_mbps must be between 10 and 1000
- latency_ms must be between 5 and 200
- values should be realistic for 5G cellular networks
- no missing values

Generate exactly 500 rows.

Return only raw CSV.
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

with open("datasets/constraint/run10.csv", "w") as file:
    file.write(csv_data)

print("Constraint-based dataset succeded to generate brollan;))")