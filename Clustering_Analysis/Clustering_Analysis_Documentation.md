
# Stage 2 - Clustering Analysis Documentation

## 1. Purpose

The purpose of the clustering analysis was to identify distinct customer segments within the Telco Customer Churn dataset.

K-Means clustering was selected as the clustering technique.

## 2. Clustering Dataset

The clustering model was trained using the prepared customer features.

The clustering dataset contained:

- 5,634 customers
- 45 processed features

The Churn target variable was excluded from the clustering features so that the clusters were created from customer characteristics rather than the outcome being predicted.

The clustering dataset was checked before modelling.

Results:

- Missing values = 0
- Infinite values = 0

## 3. Elbow Method

The elbow method was used to evaluate different values of K.

The following inertia values were obtained:

| Number of Clusters (K) | Inertia |
|---:|---:|
| 2 | 54,980.38 |
| 3 | 44,487.22 |
| 4 | 40,690.91 |
| 5 | 38,357.66 |
| 6 | 36,579.03 |
| 7 | 35,197.26 |
| 8 | 33,675.14 |
| 9 | 32,764.60 |
| 10 | 31,944.96 |

Based on the elbow plot, K = 4 was selected because the reduction in inertia becomes less pronounced after four clusters.

## 4. K-Means Model

A K-Means clustering model was trained using:

- Number of clusters = 4
- Random state = 42
- n_init = 10

The final model produced four customer clusters:

- Cluster 0
- Cluster 1
- Cluster 2
- Cluster 3

## 5. Cluster Sizes

The resulting cluster sizes were:

| Cluster | Customers | Percentage |
|---:|---:|---:|
| 0 | 738 | 10.48% |
| 1 | 1,214 | 17.24% |
| 2 | 1,605 | 22.79% |
| 3 | 2,077 | 29.49% |
| Total | 5,634 | 100% |

## 6. Cluster Profiles

### Cluster 0

- Customers: 738
- Percentage: 10.48%
- Average tenure: 26.78 months
- Average monthly charges: $79.51
- Average total charges: $2,209.09
- Observed churn rate: 48.51%
- Dominant contract: Month-to-month
- Dominant internet service: Fiber optic
- Dominant payment method: Electronic check

This segment is characterised by senior customers, relatively high monthly charges, month-to-month contracts and a high observed churn rate.

### Cluster 1

- Customers: 1,214
- Percentage: 17.24%
- Average tenure: 30.22 months
- Average monthly charges: $21.11
- Average total charges: $657.12
- Observed churn rate: 7.25%
- Dominant contract: Two year
- Dominant internet service: No internet service
- Dominant payment method: Mailed check

This segment is characterised by low monthly charges and no internet service, with a low observed churn rate.

### Cluster 2

- Customers: 1,605
- Percentage: 22.79%
- Average tenure: 58.57 months
- Average monthly charges: $89.53
- Average total charges: $5,243.79
- Observed churn rate: 13.33%
- Dominant contract: Two year
- Dominant internet service: Fiber optic
- Dominant payment method: Bank transfer (automatic)

This segment has the longest average tenure and the highest average total charges. It also has a high proportion of longer-term contracts.

### Cluster 3

- Customers: 2,077
- Percentage: 29.49%
- Average tenure: 15.68 months
- Average monthly charges: $66.35
- Average total charges: $1,015.95
- Observed churn rate: 40.20%
- Dominant contract: Month-to-month
- Dominant internet service: DSL
- Dominant payment method: Electronic check

This segment has the shortest average tenure and is predominantly month-to-month, with a relatively high observed churn rate.

## 7. PCA Visualisation

PCA was used to reduce the 45-dimensional clustering dataset to two principal components for visualisation.

The results were:

- Principal Component 1: 27.32% variance explained
- Principal Component 2: 17.97% variance explained
- Combined variance explained: 45.29%

The PCA plot provides a two-dimensional representation of the four K-Means clusters.

## 8. Cluster Churn Patterns

The observed churn rates were:

- Cluster 0: 48.51%
- Cluster 1: 7.25%
- Cluster 2: 13.33%
- Cluster 3: 40.20%

These results show that churn varies substantially between the identified customer segments.

The clustering results describe associations within the dataset and do not establish causal relationships.

## 9. Key Business Observations

The analysis indicates that customer segments differ in tenure, charges, contract type, service usage, payment method and observed churn.

Clusters 0 and 3 have predominantly month-to-month contracts and relatively high observed churn rates.

Cluster 2 has the longest average tenure, the highest average total charges and a relatively lower observed churn rate.

Cluster 1 has the lowest average monthly charges and the lowest observed churn rate.

These observations can be used as inputs for subsequent predictive modelling and retention recommendation development.

## 10. Output Files

The following clustering deliverables were generated:

- kmeans_model.pkl
- clustered_customer_data.csv
- elbow_method.png
- cluster_visualisation_pca.png

## 11. Conclusion

The K-Means analysis successfully divided the prepared customer data into four distinct customer segments. The elbow method provided evidence for selecting K = 4, and PCA was used to visualise the resulting clusters. Cluster profiling revealed meaningful differences in customer characteristics and observed churn patterns, providing a foundation for further predictive modelling and retention recommendations.
