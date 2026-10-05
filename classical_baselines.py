import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
import warnings
from src.utils import load_dataset

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

def load_and_preprocess_data2(dataset_name="cornus4f", target_classes = ["0", "1"], target_features = [0, 2, 3]):
    X, y = load_dataset(dataset_name, target_classes, target_features)
    return X, y

def evaluate_classical_models_train_test(X, y, test_size=0.2, random_state=42, output_file=None):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    models = {
        "SVM": SVC(kernel='rbf', random_state=random_state),
        "Random-forest": RandomForestClassifier(n_estimators=100, random_state=random_state),
        "K-NN": KNeighborsClassifier(n_neighbors=5),
        "CNN(MLP)": MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500, random_state=random_state)
    }

    print(f"Train-Test Split ({1 - test_size:.2f}/{test_size:.2f}), Seed: {random_state}")
    print(f"{'Model':<20} | {'Accuracy':<10} | {'Macro-F1':<10} | {'Macro-Prec':<10} | {'Macro-Recall':<12}")

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='macro')
        prec = precision_score(y_test, y_pred, average='macro', zero_division=0)
        rec = recall_score(y_test, y_pred, average='macro', zero_division=0)

        results[name] = {'acc': acc, 'f1': f1, 'prec': prec, 'rec': rec}

        print(f"{name:<20} | {acc:.4f}     | {f1:.4f}     | {prec:.4f}     | {rec:.4f}")

        if output_file:
            with open(output_file, 'a') as f:
                f.write(f"{name},{acc:.4f},{f1:.4f},{prec:.4f},{rec:.4f}\n")

    return results


def evaluate_classical_models_train_test_averaged(X, y, seeds, test_size=0.2, output_file=None):
    accumulated_results = {
        "SVM": {'acc': [], 'f1': [], 'prec': [], 'rec': []},
        "Random-forest": {'acc': [], 'f1': [], 'prec': [], 'rec': []},
        "K-NN": {'acc': [], 'f1': [], 'prec': [], 'rec': []},
        "CNN(MLP)": {'acc': [], 'f1': [], 'prec': [], 'rec': []}
    }

    for seed in seeds:
        # Podział danych dla aktualnego seeda
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=seed, stratify=y
        )

        models = {
            "SVM": SVC(kernel='rbf', random_state=seed),
            "Random-forest": RandomForestClassifier(n_estimators=100, random_state=seed),
            "K-NN": KNeighborsClassifier(n_neighbors=5),
            "CNN(MLP)": MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500, random_state=seed)
        }

        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            accumulated_results[name]['acc'].append(accuracy_score(y_test, y_pred))
            accumulated_results[name]['f1'].append(f1_score(y_test, y_pred, average='macro'))
            accumulated_results[name]['prec'].append(precision_score(y_test, y_pred, average='macro', zero_division=0))
            accumulated_results[name]['rec'].append(recall_score(y_test, y_pred, average='macro', zero_division=0))

    print(f"Train-Test Split ({1 - test_size:.2f}/{test_size:.2f}), Averaged over {len(seeds)} seeds")
    print(f"{'Model':<20} | {'Accuracy':<10} | {'Macro-F1':<10} | {'Macro-Prec':<10} | {'Macro-Recall':<12}")

    final_results = {}

    # Obliczanie średnich i zapis
    for name in accumulated_results.keys():
        avg_acc = np.mean(accumulated_results[name]['acc'])
        avg_f1 = np.mean(accumulated_results[name]['f1'])
        avg_prec = np.mean(accumulated_results[name]['prec'])
        avg_rec = np.mean(accumulated_results[name]['rec'])

        final_results[name] = {'acc': avg_acc, 'f1': avg_f1, 'prec': avg_prec, 'rec': avg_rec}

        print(f"{name:<20} | {avg_acc:.4f}     | {avg_f1:.4f}     | {avg_prec:.4f}     | {avg_rec:.4f}")

        if output_file:
            with open(output_file, 'a') as f:
                f.write(f"{name},{avg_acc:.4f},{avg_f1:.4f},{avg_prec:.4f},{avg_rec:.4f}\n")

    return final_results
def load_and_preprocess_iris_data(label_col='species', scaler_type='minmax'):
    df = load_iris()

    X_raw = df.data
    y = df.target


    if scaler_type == 'minmax':
        scaler = MinMaxScaler()
    elif scaler_type == 'standard':
        scaler = StandardScaler()
    else:
        raise ValueError("Nieznany typ skalera. Wybierz 'minmax' lub 'standard'.")

    X_scaled = scaler.fit_transform(df.data)

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
    # file_path_5_features = 'datasets/cornus_five_features.csv'
    # features_5 = ['seed_mass', 'fruit_circ', 'seed_circ', 'fruit_len', 'seed_len']
    # features_4 = ['seed_mass', 'fruit_circ', 'fruit_len', 'seed_len']
    # features_3 = ['fruit_circ', 'fruit_len', 'seed_len']
    # output_file = 'results/classical_baselines_results.csv'
    # if output_file:
    #     with open(output_file, 'w') as f:
    #         f.write("Model,Accuracy,Macro-F1,Macro-Prec,Macro-Recall\n")
    #
    # X_5, y_5 = load_and_preprocess_data(file_path_5_features, feature_cols=features_5, scaler_type='minmax', labels=[3, 4])
    # X_5, y_5 = load_and_preprocess_iris_data()
    #
    # if X_5 is not None:
    #
    #
    #     seeds = [10, 25, 42, 55, 73, 88, 99, 101, 202, 303]
    #     all_rf_acc = []
    #
    #     for seed in seeds:
    #         evaluate_classical_models(X_5, y_5, n_splits=5, random_state=seed, output_file=output_file)
    #
    #
    # results = calculate_average_metrics(output_file)
    # create_latex_table(results, output_file='results/classical_baselines_results_avg_3vs4_5_features.tex')

    X, y = load_and_preprocess_data2()
    seeds = [42, 89, 123, 456, 768]
    evaluate_classical_models_train_test_averaged(X,y, seeds = seeds)


