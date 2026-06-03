import pandas as pd
import random
from faker import Faker

fake = Faker()

users_df = pd.read_csv("data/raw/users.csv")

events = []

event_types = [
    "signup",
    "login",
    "search",
    "view_product",
    "add_to_cart",
    "checkout",
    "purchase"
]

for _, user in users_df.iterrows():

    num_events = random.randint(10, 30)

    for _ in range(num_events):

        events.append({
            "user_id": user["user_id"],
            "event_name": random.choice(event_types),
            "event_time": fake.date_time_this_year(),
            "country": user["country"],
            "device": user["device"],
            "traffic_source": user["traffic_source"]
        })

events_df = pd.DataFrame(events)

events_df.to_csv(
    "data/raw/events.csv",
    index=False
)

print(events_df.head())

print("\nTotal Events:")
print(len(events_df))