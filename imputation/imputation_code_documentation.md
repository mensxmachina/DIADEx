# Documentation for Imputation

The code in the imputation folder is responsible for filling in the missing data. Imputation is embedded inside auto-sklearn, and the enhanced auto-sklearn version is run on the missing dataset.

The best configuration is found through cross validation, and the imputation method that is contained inside the configuration is used to impute the whole dataset.

Based on the results in the paper \[2\] we embed the three best imputation methods:

1.  Denoise Auto-Encoder imputation
2.  MissForest imputation
3.  Mean-Mode imputation

In the paper, Mean-Mode has the best performance to training cost trade-off, denoise auto-encoders are the best method for real-world missing data, while MissForest is the best for simultated missing data.

\[2\] Paterakis G., Fafalios S., Charonyktakis P., Christophides V., Tsamardinos I. Do we really need imputation in AutoML predictive modeling? Under Submission

Input:

1.  Features in dataframe format
2.  Outcome variable in series format
3.  Training time in minutes

Output:

1\. the dataset with imputed values in pandas dataframe format.
