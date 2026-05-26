from openai import OpenAI

client = OpenAI(
    api_key=" ---- "
)

prompt = """
Generate synthetic 5G cellular network traffic data in CSV format.

Columns:
timestamp,user_id,network_type,throughput_mbps,latency_ms

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

with open("datasets/basic/run10.csv", "w") as file:
    file.write(csv_data)

print("Basic prompt dataset succeded to generate brollan;))")