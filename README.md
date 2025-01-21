# SpectroCluster

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)

**SpectroCluster** is an open-source application for analyzing vibratory and acoustic signals. It leverages modern unsupervised machine learning algorithms to automatically extract features from signals, cluster them, and detect anomalies. This aids in predictive maintenance and system optimization across various industries.

---

## Features

- **Signal Generation**: Create synthetic vibratory signals for testing and development.
- **Feature Extraction**: Automatically extract time-domain and frequency-domain features from signals.
- **Clustering**: Apply multiple clustering algorithms (K-Means, DBSCAN, HDBSCAN, GMM) to discover patterns.
- **Dimensionality Reduction**: Use UMAP and PCA for visualization of high-dimensional data.
- **Outlier Detection**: Identify anomalies in data using clustering techniques.
- **Visualization**: Interactive interfaces to visualize clusters and signal waveforms using Gradio and Matplotlib.
- **Progress Tracking**: Real-time progress bars and status updates using ProgressTable during lengthy operations.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/thekester/SpectroCluster.git
   cd SpectroCluster
   ```

2. **Set up the environment:**
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows use: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     ```

3. **Initialize data and run the project:**
   - Run the demo script to execute the complete analysis pipeline:
     ```bash
     python demo.py
     ```

---

## Usage

- **Generate Signals**:  
  Run `python generate_signals.py` to create synthetic vibratory signals.

- **Extract Features**:  
  After generating signals, run `python extract_features.py` to compute features from the signals.

- **Clustering and Analysis**:  
  Run `python clustering.py` to apply clustering algorithms and visualize results.  
  Use `python test_algorithms.py`, `python detect_outliers.py`, and `python visualize_clusters.py` for further analysis and visualization.

- **View All File Contents**:  
  Use `python content.py` to recursively list file contents (excluding certain directories and file types) with progress tracking.

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check [issues page](https://github.com/thekester/SpectroCluster/issues).

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

SpectroCluster is a collaborative and evolving project. Whether you're a data scientist, researcher, or developer, your contributions and feedback help make this tool more robust and versatile for vibratory signal analysis and anomaly detection. 🌟
