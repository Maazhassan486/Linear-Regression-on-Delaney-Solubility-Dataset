
# Linear Regression on Delaney Solubility Dataset

This project demonstrates how to apply a simple linear regression model to predict a compound’s solubility (`logS`) using molecular descriptors such as `MolLogP`, `MolWt`, `NumRotatableBonds`, and `AromaticProportion`.

## Dataset

The dataset (in CSV format) contains columns like:
- **MolLogP** – Calculated octanol-water partition coefficient
- **MolWt** – Molecular weight
- **NumRotatableBonds** – Number of rotatable bonds
- **AromaticProportion** – Proportion of aromatic rings in the molecule
- **logS** – Experimental solubility (target variable)

An example of the data structure is as follows:

| MolLogP | MolWt   | NumRotatableBonds | AromaticProportion | logS   |
|---------|---------|--------------------|---------------------|--------|
| 2.5954  | 167.85  | 0                  | 0                   | -2.18  |
| 2.3765  | 133.405 | 0                  | 0                   | -2.00  |
| 2.5938  | 167.85  | 1                  | 0                   | -1.74  |

## Project Files

1. **`delaney_solubility_with_descriptors.csv`**  
   The dataset file with molecular descriptors and the target column `logS`.

2. **`model.py`** (example name)  
   - Reads the CSV dataset into a Pandas DataFrame.  
   - Splits the data into features (`x`) and target (`y`).  
   - Splits the data into training and testing sets.  
   - Trains a linear regression model on the training set.  
   - Evaluates the model using MSE (mean squared error) and R² (coefficient of determination).  
   - Prints out the evaluation metrics.  
   - Visualizes the model predictions for the training set in a scatter plot.

## Requirements

- **Python 3.x**
- **Pandas**  
  ```bash
  pip install pandas
  ```
- **scikit-learn**  
  ```bash
  pip install scikit-learn
  ```
- **Matplotlib**  
  ```bash
  pip install matplotlib
  ```

## How to Run

1. **Clone or download** this repository.  
2. **Navigate** to the project directory in your terminal or command prompt.
3. **Install** the required Python packages (if not already installed) using:
   ```bash
   pip install pandas scikit-learn matplotlib
   ```
4. **Run** the Python script:
   ```bash
   python model.py
   ```
   (Adjust the script name if yours differs.)

## Results

A sample output might look like this:

```
             method   mse_train   r2_train   mse_test   r2_test
0  Linear Regression   1.007536   0.764505   1.020695   0.789162
```

- **mse_train / mse_test** – Mean squared error on the training and testing sets. Lower is better.  
- **r2_train / r2_test** – R² score on the training and testing sets. Higher is better, with a maximum of 1.0 indicating a perfect fit.

In this example, the model achieves an R² of about 0.79 on the testing set, which suggests it captures a good portion of the variance in `logS`.

## Visualization

The code also creates a scatter plot comparing the actual `ytrain` values (on the y-axis) to the predicted `y_lr_train_pred` (on the x-axis). To view the plot, ensure you have a GUI backend for Matplotlib or run the script in an environment that supports plots (e.g., Jupyter Notebook or an IDE like PyCharm).

## Next Steps

- **Hyperparameter Tuning:**  
  Experiment with different regression techniques (e.g., Ridge, Lasso) or parameters to improve model performance.
- **Feature Engineering:**  
  Consider creating additional descriptors or transformations to capture more molecular properties.
- **Data Cleaning:**  
  Check for outliers or missing values in the dataset and handle them accordingly.
