import pandas as pd
import numpy as np
import random
import os
import matplotlib.pyplot as plt

from segmentation import segment_signal
from clustering import recursive_cluster
from kadane import kadane_algorithm


# -------------------------------
# Create results folder if needed
# -------------------------------

os.makedirs("results/segmentation_plots", exist_ok=True)

for f in os.listdir("results/segmentation_plots"):
    os.remove(os.path.join("results/segmentation_plots", f))

# -------------------------------
# Load dataset
# -------------------------------

df = pd.read_csv("data/rul_hrs.csv")

df = df.iloc[:10000]

sensor_cols = [c for c in df.columns if "sensor" in c]


# -------------------------------
# Convert RUL to categories
# -------------------------------

Q10 = df["rul"].quantile(0.10)
Q50 = df["rul"].quantile(0.50)
Q90 = df["rul"].quantile(0.90)


def classify_rul(r):

    if r < Q10:
        return 0
    elif r < Q50:
        return 1
    elif r < Q90:
        return 2
    else:
        return 3


df["rul_class"] = df["rul"].apply(classify_rul)


# -------------------------------
# TASK 1 — Segmentation
# -------------------------------


selected_sensors = random.sample(sensor_cols, 10)

segmentation_scores = {}

for sensor in selected_sensors:

    signal = df[sensor].values
    segments = []
    threshold = 0.5 * np.var(signal)
    segment_signal(signal, 0, len(signal), threshold, segments)
    segmentation_scores[sensor] = len(segments)

    # ---- Plot segmentation ----

    plt.figure()
    plt.plot(signal)

    for s, e in segments:
        plt.axvline(s, color="red")

    plt.title(sensor)
    plt.savefig("results/segmentation_plots/" + sensor + ".png")
    plt.close()

print("\nSegmentation Complexity Scores")
for k, v in segmentation_scores.items():
    print(k, ":", v)

# -------------------------------
# TASK 2 — Clustering
# -------------------------------

data = df[sensor_cols].values
clusters = recursive_cluster(data, 4)
cluster_results = []

for cluster_indices in clusters:

    classes = df.iloc[cluster_indices]["rul_class"]
    counts = classes.value_counts()
    cluster_results.append(counts)

print("\nCluster Majority Counts")

for i, c in enumerate(cluster_results):
    print("\nCluster", i)
    print(c)


# -------------------------------
# TASK 3 — Kadane Analysis
# -------------------------------

kadane_results = {}

for sensor in sensor_cols:

    signal = df[sensor].values
    d = np.abs(np.diff(signal))
    x = d - np.mean(d)

    start, end, total = kadane_algorithm(x)
    classes = df.iloc[start:end + 1]["rul_class"]
    majority = classes.value_counts().idxmax()
    kadane_results[sensor] = majority

print("\nKadane Majority Class Per Sensor")

for sensor, cls in kadane_results.items():
    print(sensor, "-> class", cls)

print("\nSelected sensors:", selected_sensors)