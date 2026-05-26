from openai import OpenAI

client = OpenAI(
    api_key=" ---- "
)

prompt = """
Generate synthetic 5G cellular network traffic data in CSV format.

Columns:
timestamp,user_id,network_type,throughput_mbps,latency_ms

Example rows:

timestamp,user_id,network_type,throughput_mbps,latency_ms
2025-04-06T08:30:00Z,user_1,5G,907,30
2025-04-06T08:32:00Z,user_2,5G,557,38
2025-04-06T08:33:00Z,user_3,5G,879,15

Generate exactly 500 new rows following similar patterns.

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

with open("datasets/fewshot/run10.csv", "w") as file:
    file.write(csv_data)

print("Few-shot dataset succeded to generate brollan;))")