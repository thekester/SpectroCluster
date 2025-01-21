import gradio as gr
import pandas as pd
import soundfile as sf
import os
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("results/clustered_features.csv")
data_folder = "data/synthetic_signals"

def plot_signal(file_name):
    file_path = os.path.join(data_folder, file_name)
    signal, sr = sf.read(file_path)
    t = np.linspace(0, len(signal) / sr, num=len(signal))

    plt.figure(figsize=(8, 4))
    plt.plot(t, signal)
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    plt.title(f"Signal {file_name}")
    plt.grid(True)
    
    return plt

def get_cluster_info(cluster_id):
    cluster_files = df[df["kmeans_cluster"] == cluster_id]["file"].tolist()
    return cluster_files

iface = gr.Interface(
    fn=plot_signal,
    inputs=gr.Dropdown(choices=df["file"].tolist(), label="Choisissez un signal"),
    outputs="plot"
)

iface.launch()
