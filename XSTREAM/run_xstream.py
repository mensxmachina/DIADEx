import numpy as np
from .xstream.Chains import Chains
import pandas as pd
from sklearn.metrics import average_precision_score
import pickle
import glob
import os

def run_xstream(folder_path, filename, results_path):
    data = pd.read_csv(folder_path+filename+'.csv')
    data['scores'] = np.full(len(data), 0)
    data['window'] = np.full(len(data), 0)

    window_size = 128
    start_index = 0
    end_index = window_size

    n_windows = int(len(data) / window_size)
    k = 100
    nchains = 100
    depth = 10

    for i in range(n_windows-1):
        train_data = data.iloc[start_index:end_index]
        test_data = data.iloc[start_index+window_size:end_index+window_size]
        
        # Exclude 'scores' and 'window' columns when passing to the Chains model
        cf = Chains(k=k, nchains=nchains, depth=depth)
        cf.fit(train_data.drop(['scores', 'window', 'is_anomaly'], axis=1).to_numpy())
        scores = -cf.score(test_data.drop(['scores', 'window'], axis=1).to_numpy())

        # Assign scores and window number
        data.loc[start_index+window_size:end_index+window_size-1, 'scores'] = scores
        data.loc[start_index+window_size:end_index+window_size-1, 'window'] = i+1

        # Save the model for the current window
        with open(results_path+f"{filename}_window_{i+1}_model.pkl", "wb") as f:
            pickle.dump(cf, f)

        start_index += window_size
        end_index += window_size

    average_precision = average_precision_score(data['is_anomaly'], data['scores'])
    print("Average Precision Score:", average_precision)

    data.to_csv(results_path+filename+'_updated.csv')


def main():
    folder_path = 'datasets/'  # Replace with the path to your folder
    results_path = 'Results/'
    # Iterate over .csv files in the folder
    for file_path in glob.glob(os.path.join(folder_path, '*.csv')):
        # Extract the base filename without extension
        filename = os.path.splitext(os.path.basename(file_path))[0]

        # Run your function on the filename
        run_xstream(folder_path, filename, results_path)

if __name__ == "__main__":
    main()