# DIADEx: Data Imputation, Anomaly Detection and Explanation

In modern ML pipelines, data cleaning is crucial to ensure not only a good predictive performance but also that the produced model is safe and reliable. In this repository, we include two critical preprocessing steps and an explanation system. We focus on Missing Value Imputation (MVI) and Anomaly Detection (AD). Then, the detected anomalies are explained by PROTEUS.
The employed methodologies were funded by H.F.R.I.  

# Contents of the running example deliverable.ipynb

In deliverable.ipynb there is a concrete example that run the following pipeline:
- Reads a dataset with missing values
- Imputes the missing values with the methodology described below
- Detects anomalies in streaming fashion using the XSTREAM detector
- Explains the detected anomalies using PROTEUS

# Methods Description

## Imputation

The code in the imputation folder is responsible for filling in the missing data. Imputation is embedded inside auto-sklearn, and the enhanced auto-sklearn version is run on the missing dataset.

The best configuration is found through cross validation, and the imputation method that is contained inside the configuration is used to impute the whole dataset.

Based on the results in the paper [Paterakis et al. 2023] we embed the three best imputation methods:

1.  Denoise Auto-Encoder imputation
2.  MissForest imputation
3.  Mean-Mode imputation

In the paper, Mean-Mode has the best performance to training cost trade-off, denoise auto-encoders are the best method for real-world missing data, while MissForest is the best for simultated missing data.

Paterakis G., Fafalios S., Charonyktakis P., Christophides V., Tsamardinos I. Do we really need imputation in AutoML predictive modeling? (Under Submission)

Input:

1.  Features in dataframe format
2.  Outcome variable in series format
3.  Training time in minutes

Output:

1. the dataset with imputed values in pandas dataframe format.

## XSTREAM
The main goal of the code inside the XSTREAM folder is to use the XSTREAM algorithm, known for its ability to detect anomalies online, on different datasets. The aim is to analyze data in batches, find possible outliers, and create models for detection at the same time.

Based on the insights presented in the paper [Ntroumpogiannis et al. 2023], choosing XSTREAM as the algorithm for our project is a well-informed decision. The paper highlights XSTREAM's superior performance in various key areas, particularly in its effectiveness and efficiency when dealing with online anomaly detection. XSTREAM not only outperforms other online detectors but also shows greater efficacy compared to its offline version in many instances. This is especially relevant for real-time data streams where rapid and accurate anomaly detection is crucial. Additionally, XSTREAM demonstrates an advantageous trade-off between update speed and detection accuracy, making it suitable for environments with high-dimensional data and varying data distributions. Furthermore XSTREAM is shown to effectively handle non-normality and scale variance in data features. Therefore, implementing XSTREAM aligns with our goal of achieving reliable, efficient, and accurate anomaly detection in streaming data.

Ntroumpogiannis, A., Giannoulis, M., Myrtakis, N. et al. A meta-level analysis of online anomaly detectors. The VLDB Journal 32, 845–886 (2023). https://doi.org/10.1007/s00778-022-00773-x

[//]: # (### Running XSTREAM on Multiple Datasets)

[//]: # (To execute the XSTREAM analysis on all datasets located in the 'datasets' folder, use the following command:)

[//]: # ()
[//]: # (```bash)

[//]: # (python run_xstream.py)

[//]: # (```)

[//]: # ()
[//]: # (### Prerequisites)

[//]: # (- Ensure that all datasets are in CSV format and placed within the 'datasets' folder.)

### Output
- Upon successful execution, results will be stored in the 'Results' folder. 
- For each dataset, the following are generated:
  - A CSV file containing the original dataset augmented with anomaly scores and window numbers for each sample.
  - A series of detector model files, one for each window in the dataset.

The models and output CSV files are named systematically to correspond with their respective datasets and window numbers, facilitating easy identification and analysis.

## PROTEUS 

PROTEUS is an anomaly explanation sytem to produce global, predictive explanations for any detector as input.

PROTEUS is a novel AutoML engine specifically designed to support feature selection and classification on imbalanced datasets. Unlike existing anomaly explainers, PROTEUS outputs not only a small-sized feature subset serving as explanation but also a surrogate model fitted on this subset to explain unseen samples, as well as a reliable out-of-sample (predictive) performance estimation. To produce such output, PROTEUS AutoML relies on advanced design choices described in Section 3, such as supervised oversampling, group-based stratification, and a special variant of Cross-Validation with Bootstrap Bias Correction. Finally, PROTEUS introduces a novel visualization mechnanism inspired by spider plots, to facilitate the analyst into examing a detected anomaly.

More information can be found in the papers:

N. Myrtakis, I. Tsamardinos and V. Christophides. “On Predictive Explanation of Data Anomalies.” ArXiv abs/2110.09467 (2021). 
https://arxiv.org/pdf/2110.09467.pdf

N. Myrtakis, I. Tsamardinos and V. Christophides. “PROTEUS: Predictive Explanation of Anomalies.” 2021 IEEE 37th International Conference on Data Engineering (ICDE) (2021) 
https://ieeexplore.ieee.org/document/9458931

# Acknowledgements

The research work was supported by the Hellenic Foundation for Research and Innovation (H.F.R.I.) under the “First Call for H.F.R.I. Research Projects to support Faculty members and Researchers and the
procurement of high-cost research equipment grant” (Project Number: 1941); the ERC under the European Union’s Seventh Framework
Programme (FP/2007-2013) / ERC Grant Agreement n. 617393.

