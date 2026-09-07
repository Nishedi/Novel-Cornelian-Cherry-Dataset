import pandas as pd
import scipy.stats as stats
from statsmodels.multivariate.manova import MANOVA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
def load_dataset(file_path):
    try:
        # skip first line
        dataset = pd.read_csv(file_path, skiprows=1)
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

dataset = load_dataset('../datasets/cornus_five_features.csv')

def filter_dataset_by_species(dataset, species):
    if dataset is not None:
        filtered_dataset = dataset[dataset['label'] == species]
        return filtered_dataset
    else:
        print("Dataset is None. Cannot filter.")
        return None

def compute_meatric_for_dataset(dataset, feature):
    if dataset is not None:
        mean = dataset[feature].mean()
        std_dev = dataset[feature].std()
        return mean, std_dev
    else:
        print("Dataset is None. Cannot compute metrics.")
        return None, None

species = [0,1,2,3,4]
species_name =['Raciborski','Paczoski','Dublany','Kresowiak','Slowianin']
features_to_analyze = ['seed_mass', 'fruit_circ','seed_circ', 'fruit_len', 'seed_len']
for s in species:
    filtered_data = filter_dataset_by_species(dataset, s)
    if filtered_data is not None:
        for feature in features_to_analyze:
            mean, std_dev = compute_meatric_for_dataset(filtered_data, feature)
            if mean is not None and std_dev is not None:
                print(f"Species {species_name[s]}, Feature '{feature}': Mean = {mean:.2f}, Std Dev = {std_dev:.2f}")
            else:
                print(f"Could not compute metrics for species {s} and feature '{feature}'.")
    else:
        print(f"Could not filter dataset for species {s}.")

print("\nSHAPIRO-WILK")
for s in species:
    filtered_data = filter_dataset_by_species(dataset, s)
    if filtered_data is not None:
        print(f"\nKultywar: {species_name[s]}")
        for feature in features_to_analyze:
            data_to_test = filtered_data[feature].dropna()
            stat, p_val = stats.shapiro(data_to_test)
            print(f"  {feature}: stat={stat:.4f}, p-value={p_val:.4f}")

print("\nANOVA")
for feature in features_to_analyze:
    groups = [filter_dataset_by_species(dataset, s)[feature].dropna() for s in species]
    stat, p_val = stats.f_oneway(*groups)
    print(f"{feature}: F-stat = {stat:.4f}, p-value = {p_val:.4e}")

print("\nMANOVA")
if dataset is not None:
    formula = 'seed_mass + fruit_circ + seed_circ + fruit_len + seed_len ~ C(label)'
    try:
        manova = MANOVA.from_formula(formula, data=dataset)
        print(manova.mv_test())
    except Exception as e:
        print(f"Błąd podczas wykonywania MANOVA: {e}")

if dataset is not None:

    plt.figure(figsize=(8, 6))
    corr_matrix = dataset[features_to_analyze].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
    plt.title('Feature Correlation Matrix for Cornus mas dataset')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png', dpi=300)
    plt.close()
    print("Zapisano: correlation_matrix.png")

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(dataset[features_to_analyze])
    y = dataset['label'].values

    clf = SVC(kernel='rbf', C=1.0, gamma='scale')
    clf.fit(X_pca, y)

    x_min, x_max = X_pca[:, 0].min() - 0.5, X_pca[:, 0].max() + 0.5
    y_min, y_max = X_pca[:, 1].min() - 0.5, X_pca[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(10, 8))
    cmap_background = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#FFFFAA', '#FFAAFF'])
    cmap_points = ListedColormap(['red', 'green', 'blue', 'yellow', 'magenta'])

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_background)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap=cmap_points, edgecolors='k', s=50)

    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap_points(i),
                          markersize=10, markeredgecolor='k') for i in range(5)]
    plt.legend(handles, species_name, title="Cultivars", loc='best')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Decision Boundaries (SVM on 2D PCA projection)')
    plt.tight_layout()
    plt.savefig('decision_boundaries.png', dpi=300)
    plt.close()
    print("Zapisano: decision_boundaries.png")