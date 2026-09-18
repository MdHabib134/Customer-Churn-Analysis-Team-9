
# Customer Churn Analysis – Team 9

## Project Overview

This project analyses customer churn using the Telco Customer Churn dataset.

The overall project concept is to:

1. Prepare and clean the customer data.
2. Analyse customer characteristics and churn patterns.
3. Segment customers using K-Means clustering.
4. Develop predictive churn modelling.
5. Develop data-driven retention recommendations.

This repository contains the Stage 2 Data Preparation and Clustering Analysis deliverables.

## Dataset

The project uses the Telco Customer Churn dataset.

The original dataset contains:

- 7,043 customer records
- 21 columns
- Customer demographic information
- Account and contract information
- Service information
- Monthly and total charges
- Churn status

## Stage 2 – Data Preparation

The data preparation process included:

- Data quality assessment
- Missing-value checking
- Blank-value checking
- Duplicate checking
- Categorical variable encoding
- Training/testing split
- Numerical feature scaling

The original dataset contained 11 blank values in TotalCharges. Investigation showed that these records had zero tenure and no churn, so the blank TotalCharges values were treated as zero.

After cleaning:

- Missing values: 0
- Duplicate customer IDs: 0
- Completely duplicated rows: 0

The cleaned dataset was divided into:

- Training set: 5,634 customers
- Testing set: 1,409 customers

After categorical encoding, 45 processed features were produced.

StandardScaler was applied to:

- SeniorCitizen
- tenure
- MonthlyCharges
- TotalCharges

## Stage 2 – Clustering Analysis

K-Means clustering was used to identify distinct customer segments.

### Elbow Method

The elbow method was used to evaluate different values of K.

Based on the analysis, K = 4 was selected because the reduction in inertia becomes less pronounced after four clusters.

### K-Means Model

The final model used:

- Number of clusters: 4
- Random state: 42
- n_init: 10

### Cluster Sizes

| Cluster | Customers | Percentage |
|---|---:|---:|
| Cluster 0 | 738 | 10.48% |
| Cluster 1 | 1,214 | 17.24% |
| Cluster 2 | 1,605 | 22.79% |
| Cluster 3 | 2,077 | 29.49% |

### Observed Churn Rates

| Cluster | Observed Churn Rate |
|---|---:|
| Cluster 0 | 48.51% |
| Cluster 1 | 7.25% |
| Cluster 2 | 13.33% |
| Cluster 3 | 40.20% |

These are descriptive observations from the dataset and do not establish causal relationships.

## PCA Visualisation

PCA was used to reduce the 45-dimensional clustering dataset to two dimensions for visualisation.

Results:

- Principal Component 1: 27.32% variance explained
- Principal Component 2: 17.97% variance explained
- Combined variance explained: 45.29%

## Repository Structure

Customer-Churn-Analysis-Team-9

    README.md

    Data_Preparation
        Telco_Customer_Churn_Cleaned.csv
        training_set_preprocessed.csv
        testing_set_preprocessed.csv
        Data_Preparation_Documentation.md
        Scaling_Techniques_Documentation.docx

    Clustering_Analysis
        kmeans_model.pkl
        clustered_customer_data.csv
        elbow_method.png
        cluster_visualisation_pca.png
        Clustering_Analysis_Documentation.md

    Notebooks
        Stage_2_Data_Preparation_and_Clustering.ipynb

## Stage 2 Conclusion

The Stage 2 analysis successfully prepared the customer churn dataset and identified four customer segments using K-Means clustering.

The results provide a foundation for subsequent predictive churn modelling and development of retention recommendations.
