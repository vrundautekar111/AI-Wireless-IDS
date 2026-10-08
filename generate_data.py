import numpy as np
import pandas as pd

np.random.seed(42)

N = 3000

rows = []

for _ in range(N):

    attack = np.random.choice(
        [0, 1],
        p=[0.65, 0.35]
    )

    if attack == 0:

        packet_rate = np.random.normal(80, 20)
        deauth_rate = np.random.normal(0.5, 0.4)
        failed_auth = np.random.normal(2, 1.5)
        unique_src = np.random.normal(4, 2)
        signal = np.random.normal(-48, 8)
        duration = np.random.normal(120, 35)
        retry_rate = np.random.normal(4, 2)

    else:

        packet_rate = np.random.normal(280, 80)
        deauth_rate = np.random.normal(35, 15)
        failed_auth = np.random.normal(18, 8)
        unique_src = np.random.normal(18, 7)
        signal = np.random.normal(-62, 12)
        duration = np.random.normal(35, 15)
        retry_rate = np.random.normal(25, 10)

    rows.append([
        max(packet_rate, 1),
        max(deauth_rate, 0),
        max(failed_auth, 0),
        max(unique_src, 1),
        signal,
        max(duration, 1),
        max(retry_rate, 0),
        attack
    ])


columns = [
    "packet_rate",
    "deauth_rate",
    "failed_auth_attempts",
    "unique_source_count",
    "avg_signal_dbm",
    "connection_duration_sec",
    "retry_rate",
    "label"
]


df = pd.DataFrame(
    rows,
    columns=columns
)


df.to_csv(
    "wireless_intrusion_data.csv",
    index=False
)


print("=" * 50)
print("WIRELESS IDS DATASET CREATED")
print("=" * 50)

print("\nDataset shape:")
print(df.shape)

print("\nFirst 5 records:")
print(df.head())

print("\nClass distribution:")
print(df["label"].value_counts())

print("\nDataset saved as:")
print("wireless_intrusion_data.csv")