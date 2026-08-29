Cornus Mas subspecies dataset
--------------------

**Dataset version 1 Characteristics:**

:Number of Instances: 450 (90 in each of five classes)
:Number of Attributes: 5 numeric, predictive attributes and the class
:Attribute Information:
    - fruit circumference in cm
    - stone circumference in cm
    - fruit length in cm
    - stone length in cm
    - class:
            - Cornus mas-Raciborski (label 0)
            - Cornus mas-Paczoski   (label 1)
            - Cornus mas-Dublany    (label 2)
            - Cornus mas-Kresowiak  (label 3)
            - Cornus mas-Slowianin  (label 4)
:File name: cornus_four_features.csv

**Dataset version 2 Characteristics:**

Second dataset version contains additional feature: stone mass in grams. The dataset is reduced to 350 instances due to missing values in the new feature.
:Number of Instances: 350 (70 in each of five classes)
:Number of Attributes: 6 numeric, predictive attributes and the class
:Attribute Information:
    - stone mass in grams
    - fruit circumference in cm
    - stone circumference in cm
    - fruit length in cm
    - stone length in cm
    - class:
            - Cornus mas-Raciborski (label 0)
            - Cornus mas-Paczoski   (label 1)
            - Cornus mas-Dublany    (label 2)
            - Cornus mas-Kresowiak  (label 3)
            - Cornus mas-Slowianin  (label 4)
:File name: cornus_five_features.csv

**File description:**
First row contains class names in order from 0 to 4, second row contains attribute names, and the rest of the rows contain data instances. The last column is the class label.

*Important!* Skip first line while loading

--------------------
**Statistical Analysis (Version 2 Dataset)**

**Descriptive Statistics (Mean ± Std Dev)**

| Cultivar | stone_mass (g) | fruit_circ (cm) | stone_circ (cm) | fruit_len (cm) | stone_len (cm) |
| :--- |:---------------| :--- |:-------------------| :--- |:---------------|
| Raciborski | 0.36 ± 0.05    | 1.39 ± 0.13 | 0.64 ± 0.04        | 2.18 ± 0.19 | 1.52 ± 0.10    |
| Paczoski | 0.41 ± 0.05    | 1.34 ± 0.11 | 0.66 ± 0.05        | 2.59 ± 0.19 | 1.74 ± 0.10    |
| Dublany | 0.42 ± 0.09    | 1.50 ± 0.11 | 0.64 ± 0.06        | 2.51 ± 0.17 | 1.80 ± 0.15    |
| Kresowiak | 0.42 ± 0.08    | 1.39 ± 0.11 | 0.68 ± 0.05        | 2.18 ± 0.19 | 1.55 ± 0.13    |
| Slowianin | 0.48 ± 0.18    | 1.52 ± 0.26 | 0.65 ± 0.04        | 2.82 ± 0.40 | 1.81 ± 0.22    |


**Shapiro-Wilk Normality Test (p-values)**

| Cultivar | stone_mass | fruit_circ | stone_circ | fruit_len | stone_len |
| :--- |:-----------| :--- |:-----------| :--- |:----------|
| Raciborski | 0.2894     | 0.1405 | 0.0274     | 0.2648 | 0.6937    |
| Paczoski | 0.1285     | 0.2359 | 0.1103     | 0.5262 | 0.1322    |
| Dublany | 0.5325     | 0.2308 | 0.1187     | 0.0124 | 0.0505    |
| Kresowiak | 0.8126     | 0.5069 | 0.4693     | 0.7820 | 0.2064    |
| Slowianin | < 0.0001   | < 0.0001 | 0.0564     | < 0.0001 | < 0.0001  |


**One-Way ANOVA for Individual Features**

| Feature    | F-Statistic | p-value |
|:-----------| :--- | :--- |
| stone_mass | 11.7932 | 5.4498e-09 |
| fruit_circ | 15.8350 | 6.5444e-12 |
| stone_circ | 10.0253 | 1.0966e-07 |
| fruit_len  | 89.0115 | 6.7607e-52 |
| stone_len  | 63.7302 | 2.6520e-40 |


**MANOVA (Multivariate Analysis of Variance) for C(label)**

| Test Statistic | Value | Num DF | Den DF | F Value | Pr > F |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Wilks' lambda | 0.1475 | 20.00 | 1131.9189 | 44.1837 | < 0.0001 |
| Pillai's trace | 1.3327 | 20.00 | 1376.0000 | 34.3741 | < 0.0001 |
| Hotelling-Lawley trace | 2.9717 | 20.00 | 742.7925 | 50.5062 | < 0.0001 |
| Roy's greatest root | 1.7339 | 5.00 | 344.0000 | 119.2909 | < 0.0001 |