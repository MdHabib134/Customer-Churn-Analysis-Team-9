
# Stage 2 - Data Preparation Documentation

## 1. Dataset Overview

The Customer Churn Analysis project uses the Telco Customer Churn dataset.

The original dataset contains:

- 7,043 customer records
- 21 columns
- Customer demographic information
- Account and contract information
- Service information
- Monthly and total charges
- Customer churn status

## 2. Data Quality Assessment

The dataset was inspected for missing values, blank values, duplicate customer records and infinite numerical values.

The initial missing-value check identified 11 blank values in the TotalCharges column.

Further investigation showed that all 11 affected customers had:

- Tenure = 0 months
- Churn = No

Because these records represented valid new customers and the TotalCharges value logically corresponded to zero accumulated charges, the blank TotalCharges values were converted to 0.0.

After treatment:

- Missing values = 0
- Blank values = 0

Duplicate checking also confirmed:

- Duplicate customer IDs = 0
- Completely duplicated rows = 0

## 3. Numerical Variables

The numerical variables used in the analysis were:

- SeniorCitizen
- tenure
- MonthlyCharges
- TotalCharges

## 4. Categorical Variables

Categorical variables were encoded before modelling.

The categorical variables included:

- gender
- Partner
- Dependents
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod

One-hot encoding was applied to convert categorical variables into numerical features.

After encoding:

- Training feature set = 5,634 records × 45 features
- Testing feature set = 1,409 records × 45 features

## 5. Training and Testing Split

The cleaned dataset was divided into training and testing datasets.

The resulting datasets were:

- Training set: 5,634 customers
- Testing set: 1,409 customers

The split preserved the observed churn distribution:

Training:
- No churn: 73.46%
- Churn: 26.54%

Testing:
- No churn: 73.46%
- Churn: 26.54%

## 6. Numerical Feature Scaling

Standardisation was applied to the numerical variables.

The StandardScaler technique was used to transform the numerical features so that they have approximately:

- Mean = 0
- Standard deviation = 1

The scaled numerical variables were:

- SeniorCitizen
- tenure
- MonthlyCharges
- TotalCharges

The scaling step is important because K-Means clustering uses distance calculations. Without appropriate scaling, variables with larger numerical ranges could have a disproportionate influence on the clustering results.

The scaling results were verified after transformation:

- Mean of scaled numerical features ≈ 0
- Standard deviation of scaled numerical features ≈ 1

## 7. Final Prepared Dataset

The final processed training dataset contained:

- 5,634 customers
- 45 processed features
- Churn target variable stored separately

The final processed testing dataset contained:

- 1,409 customers
- 45 processed features
- Churn target variable stored separately

## 8. Output Files

The following files were generated:

- training_set_preprocessed.csv
- testing_set_preprocessed.csv

These files are stored in the Data_Preparation folder.

## 9. Data Preparation Conclusion

The data preparation process produced clean and model-ready datasets. Missing values and blank values were addressed, duplicate records were checked, categorical variables were encoded, the data was divided into training and testing sets, and numerical variables were standardised. The resulting datasets are suitable for subsequent clustering and predictive modelling activities.
