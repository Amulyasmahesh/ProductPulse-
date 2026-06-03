# Existing code
import pandas as pd

events_df = pd.read_csv("data/raw/events.csv")

print(events_df.head())

print("\nShape:")
print(events_df.shape)
print("\nColumns:")
print(events_df.columns)

print("\nData Types:")
print(events_df.dtypes)

print("\nMissing Values:")
print(events_df.isnull().sum())

print("\nDuplicates:")
print(events_df.duplicated().sum())
events_df["event_time"] = pd.to_datetime(
    events_df["event_time"]
)