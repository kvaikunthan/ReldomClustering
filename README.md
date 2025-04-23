# Bunge Lab Clustering

## Setup

Make sure you have [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) installed.

1. **Clone the repository**

```bash
git clone https://github.com/kvaikunthan/ReldomClustering
cd ReldomClustering
```

2. **Create the environment**

```bash
conda env create -f environment.yml
```

3. **Activate the environment**

```bash
conda activate analogy
```

## Notebook Overview

- `main.ipynb` – Data preprocessing and KMeans clustering
- `pca.ipynb` – Principal Component Analysis (PCA) of clustered data
- `2D.ipynb` – 2D scatter plot of participants