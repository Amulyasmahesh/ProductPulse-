import pandas as pd

events_df = pd.read_csv("data/raw/events.csv")

print(events_df.head())

print("\nShape:")
print(events_df.shape)
print("\nEvent Counts")

print(events_df["event_name"].value_counts())
print("\nTop Countries")

print(events_df["country"].value_counts())
print("\nDevice Usage")

print(events_df["device"].value_counts())
print("\nTraffic Sources")

print(events_df["traffic_source"].value_counts())
events_df.shape
events_df["event_name"].value_counts()
signups = 14367
purchases = 14332

conversion_rate = (purchases/signups)*100

print(conversion_rate)