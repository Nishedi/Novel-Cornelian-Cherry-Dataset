import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
import warnings

warnings.filterwarnings('ignore')

def load_and_preprocess_data(file_path, feature_cols, label_col='label', scaler_type='minmax', labels=[0, 1, 2, 3, 4]):
    try:
        df = pd.read_csv(file_path, skiprows=1)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku: {e}")
        return None, None
    df = df[df[label_col].isin(labels)]
    X_raw = df[feature_cols].values
    y = df[label_col].values

    if scaler_type == 'minmax':
        scaler = MinMaxScaler()
    elif scaler_type == 'standard':
        scaler = StandardScaler()
    else:
        raise ValueError("Nieznany typ skalera. Wybierz 'minmax' lub 'standard'.")

    X_scaled = scaler.fit_transform(X_raw)

    return X_scaled, y


def evaluate_classical_models(X, y, n_splits=5, random_state=42, output_file=None):
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    models = {
        "SVM": SVC(kernel='rbf', random_state=random_state),
        "Random-forest": RandomForestClassifier(n_estimators=100, random_state=random_state),
        "K-NN": KNeighborsClassifier(n_neighbors=5),
        "CNN(MLP)": MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500, random_state=random_state)
    }

    scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']

    print(f"{n_splits}-Fold CV, Seed: {random_state})")
    print(f"{'Model':<20} | {'Accuracy':<10} | {'Macro-F1':<10} | {'Macro-Prec':<10} | {'Macro-Recall':<12}")

    results = {}
    for name, model in models.items():

        scores = cross_validate(model, X, y, cv=cv, scoring=scoring, n_jobs=-1)

        acc = np.mean(scores['test_accuracy'])
        f1 = np.mean(scores['test_f1_macro'])
        prec = np.mean(scores['test_precision_macro'])
        rec = np.mean(scores['test_recall_macro'])

        results[name] = {'acc': acc, 'f1': f1, 'prec': prec, 'rec': rec}

        print(f"{name:<20} | {acc:.4f}     | {f1:.4f}     | {prec:.4f}     | {rec:.4f}")
        if output_file:
            with open(output_file, 'a') as f:
                f.write(f"{name},{acc:.4f},{f1:.4f},{prec:.4f},{rec:.4f}\n")


    return results


def calculate_average_metrics(csv_file_path):
    column_names = ['Model', 'Accuracy', 'Macro-F1', 'Macro-Prec', 'Macro-Recall']

    df = pd.read_csv(csv_file_path, header=None, names=column_names)

    df['Model'] = df['Model'].astype(str).str.strip()

    metrics = ['Accuracy', 'Macro-F1', 'Macro-Prec', 'Macro-Recall']
    for col in metrics:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna(subset=metrics)

    avg_metrics = df.groupby('Model').mean(numeric_only=True).round(4)

    avg_metrics = avg_metrics.sort_values(by='Accuracy', ascending=False)

    return avg_metrics
def create_latex_table(results, output_file='results/classical_baselines_results_avg.tex', caption="M", label="tab:M"):
    with open(output_file, 'w') as f:
        f.write("\\begin{table*}[h!]\n")
        f.write("\\centering\n")
        f.write("\\caption{")
        f.write(caption)
        f.write("}\n")

        f.write("\\begin{tabular}{lcccc}\n")
        f.write("\\toprule\n")
        f.write("\\textbf{Model} & \\textbf{Accuracy} & \\textbf{Macro-F1} & \\textbf{Macro-Prec} & \\textbf{Macro-Recall} \\\\\n")
        f.write("\\midrule\n")
        for model, metrics in results.iterrows():
            
            f.write(f"{model}&{metrics['Accuracy']}&{metrics['Macro-F1']}&{metrics['Macro-Prec']}&{metrics['Macro-Recall']}\\\\ \n")
    
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")

        f.write("\\label{")
        f.write(label)
        f.write("}\n")
        f.write("\\end{table*}\n")

if __name__ == "__main__":
    file_path_5_features = 'datasets/cornus_five_features.csv'
    features_5 = ['seed_mass', 'fruit_circ', 'seed_circ', 'fruit_len', 'seed_len']
    features_4 = ['seed_mass', 'fruit_circ', 'fruit_len', 'seed_len']
    features_3 = ['fruit_circ', 'fruit_len', 'seed_len']
    output_file = 'results/classical_baselines_results.csv'
    if output_file:
        with open(output_file, 'w') as f:
            f.write("Model,Accuracy,Macro-F1,Macro-Prec,Macro-Recall\n")

    X_5, y_5 = load_and_preprocess_data(file_path_5_features, feature_cols=features_5, scaler_type='minmax', labels=[3, 4])

    if X_5 is not None:


        seeds = [10, 25, 42, 55, 73, 88, 99, 101, 202, 303]
        all_rf_acc = []

        for seed in seeds:
            evaluate_classical_models(X_5, y_5, n_splits=5, random_state=seed, output_file=output_file)


    results = calculate_average_metrics(output_file)
    create_latex_table(results, output_file='results/classical_baselines_results_avg_3vs4_5_features.tex')


