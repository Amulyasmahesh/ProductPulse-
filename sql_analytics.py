import pandas as pd
import sqlite3

events = pd.read_csv("data/raw/events.csv")

conn = sqlite3.connect("productpulse.db")

events.to_sql(
    "events",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created")
query = """
SELECT
event_name,
COUNT(*) as total_events
FROM events
GROUP BY event_name
ORDER BY total_events DESC
"""

result = pd.read_sql(query, conn)

print(result)
query = """
SELECT
country,
COUNT(*) as users
FROM events
GROUP BY country
ORDER BY users DESC
"""

result = pd.read_sql(query, conn)

print(result)
query = """
SELECT
device,
COUNT(*) as users
FROM events
GROUP BY device
ORDER BY users DESC
"""

result = pd.read_sql(query, conn)

print(result)
query = """
SELECT
event_name,
COUNT(DISTINCT user_id) as users
FROM events
GROUP BY event_name
ORDER BY users DESC
"""

result = pd.read_sql(query, conn)

print(result)