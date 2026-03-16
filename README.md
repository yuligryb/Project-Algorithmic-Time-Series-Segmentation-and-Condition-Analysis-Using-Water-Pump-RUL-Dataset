# Water Pump RUL Algorithmic Analysis

This project analyzes time-series sensor data from a water pump machine using classical algorithms.

The goal is to study machine behavior and relate sensor activity to Remaining Useful Life (RUL).

Algorithms implemented:

- Divide-and-Conquer Segmentation
- Recursive Clustering
- Kadane Maximum Subarray

The dataset used is the Water Pump RUL Predictive Maintenance dataset from Kaggle.


## Installation

Install required libraries:

pip install pandas numpy matplotlib


## Running the Project

Place the dataset file `water_pump_rul.csv` inside the `data/` folder.

Run the program:

python main.py


## Project Structure

main.py  
Runs the complete analysis.

segmentation.py  
Implements the divide-and-conquer segmentation algorithm.

clustering.py  
Implements the recursive clustering algorithm.

kadane.py  
Implements Kadane’s maximum subarray algorithm.

toy_examples.py  
Contains small test cases to verify the algorithms.


## Output

Segmentation plots are saved in:

results/segmentation_plots

The terminal will display:

- Segmentation complexity scores
- Cluster majority counts
- Kadane analysis results