
## XSTREAM Description
The main goal of the code inside the XSTREAM folder is to use the XSTREAM algorithm, known for its ability to detect anomalies online, on different datasets. The aim is to analyze data in batches, find possible outliers, and create models for detection at the same time.

Based on the insights presented in the paper [1], choosing XSTREAM as the algorithm for our project is a well-informed decision. The paper highlights XSTREAM's superior performance in various key areas, particularly in its effectiveness and efficiency when dealing with online anomaly detection. XSTREAM not only outperforms other online detectors but also shows greater efficacy compared to its offline version in many instances. This is especially relevant for real-time data streams where rapid and accurate anomaly detection is crucial. Additionally, XSTREAM demonstrates an advantageous trade-off between update speed and detection accuracy, making it suitable for environments with high-dimensional data and varying data distributions. Furthermore XSTREAM is shown to effectively handle non-normality and scale variance in data features. Therefore, implementing XSTREAM aligns with our goal of achieving reliable, efficient, and accurate anomaly detection in streaming data.

[1] Ntroumpogiannis, A., Giannoulis, M., Myrtakis, N. et al. A meta-level analysis of online anomaly detectors. The VLDB Journal 32, 845–886 (2023). https://doi.org/10.1007/s00778-022-00773-x

## Running XSTREAM on Multiple Datasets

To execute the XSTREAM analysis on all datasets located in the 'datasets' folder, use the following command:

```bash
python run_xstream.py
```

### Prerequisites
- Ensure that all datasets are in CSV format and placed within the 'datasets' folder.

### Output
- Upon successful execution, results will be stored in the 'Results' folder. 
- For each dataset, the following are generated:
  - A CSV file containing the original dataset augmented with anomaly scores and window numbers for each sample.
  - A series of detector model files, one for each window in the dataset.

The models and output CSV files are named systematically to correspond with their respective datasets and window numbers, facilitating easy identification and analysis.
