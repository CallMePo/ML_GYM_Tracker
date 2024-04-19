import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../../src/features/")
from DataTransformation import LowPassFilter
from scipy.signal import argrelextrema
from sklearn.metrics import mean_absolute_error

pd.options.mode.chained_assignment = None


# Plot settings
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (20, 5)
plt.rcParams["figure.dpi"] = 100
plt.rcParams["lines.linewidth"] = 2


# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------
df = pd.read_pickle("../../data/interim/01_data_processed.pkl")
df=df[df['label'] !='rest']

acc_r = df["acc_x"] **2 + df["acc_y"] **2 + df["acc_z"] **2
gyr_r = df["gyr_x"] **2 + df["gyr_y"] **2 + df["gyr_z"] **2
df["acc_r"] = np.sqrt(acc_r)
df["gyr_r"] = np.sqrt(gyr_r)
# --------------------------------------------------------------
# Split data
# --------------------------------------------------------------
bench_df = df[df["label"] == "bench"]
squat_df = df[df["label"] == "squat"]
dead_df = df[df["label"] == "dead"]
ohp_df = df[df["label"] == "ohp"]
row_df = df[df["label"] == "row"]

# --------------------------------------------------------------
# Visualize data to identify patterns
# --------------------------------------------------------------
plot_df = bench_df

plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["acc_x"].plot(figsize=(20, 5), title="Bench Press", legend=True)
plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["acc_y"].plot(figsize=(20, 5), title="Bench Press", legend=True)
plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["acc_z"].plot(figsize=(20, 5), title="Bench Press", legend=True)
plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["acc_r"].plot(figsize=(20, 5), title="Bench Press", legend=True)

plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["gyr_x"].plot(figsize=(20, 5), title="Bench Press", legend=True)
plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["gyr_y"].plot(figsize=(20, 5), title="Bench Press", legend=True)
plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["gyr_z"].plot(figsize=(20, 5), title="Bench Press", legend=True)
plot_df[plot_df["set"] == plot_df["set"].unique()[0]]["gyr_r"].plot(figsize=(20, 5), title="Bench Press", legend=True)

# --------------------------------------------------------------
# Configure LowPassFilter
# --------------------------------------------------------------
fs = 1000/200
lowpass = LowPassFilter()
# --------------------------------------------------------------
# Apply and tweak LowPassFilter
# --------------------------------------------------------------
bench_set = bench_df[bench_df["set"] == bench_df["set"].unique()[0]]
squat_set = squat_df[squat_df["set"] == squat_df["set"].unique()[0]]
dead_set = dead_df[dead_df["set"] == dead_df["set"].unique()[0]]
ohp_set = ohp_df[ohp_df["set"] == ohp_df["set"].unique()[0]]
row_set = row_df[row_df["set"] == row_df["set"].unique()[0]]

# --------------------------------------------------------------
# Create function to count repetitions
# --------------------------------------------------------------
column = "acc_r"
lowpass.low_pass_filter(
    bench_set, col=column, sampling_frequency=fs, cutoff_frequency=0.4, order=5
)[column + "_lowpass"].plot(figsize=(20, 5), legend=True)

# --------------------------------------------------------------
# Create benchmark dataframe
# --------------------------------------------------------------


# --------------------------------------------------------------
# Evaluate the results
# --------------------------------------------------------------