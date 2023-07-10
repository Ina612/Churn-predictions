<h1> :star: Customer Churn Predictions :star: </h1>
<h2> :sparkles: Data source: </h2>

The [dataset](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset) is taken from Kaggle

**Description of the dataset:**

The data is labeled. The features are the following:
- CistomerID
- Age, from 18 to 65
- Gender: Male or Female
- Tenure, from 1 to 60
- Usage Frequency, from 1 to 30
- Support Calls, from 0 to 10
- Subscription Type: Standard, Basic, Premium
- Contract Length: Monthly, Annual, Quarterly
- Total Spend: from 100 to 1000

<h2> :sparkles: Data pre-processing </h2>

For pre-processing, we
1. Checked for the data types of the column and corrected them;
2. Looked through nulls and use mean to impute them;
3. Dropped the columns that we didn't need: CustomerID;
4. Converted the columns to numeric and categorical.

<h3> :dizzy: Correlation matrix of the pre-processed data </h3>

- Strong positive correlation: **Support Calls**
- Strong negative correlation: **Total Spend, Usage Frequency, Tenure**
- Somewhat positively correlated: **Payment Delay**
 <p> </p>
 
![Correlation matrix](https://github.com/Ina612/imgs/blob/main/Correlation%20churn.png)

<h2> :sparkles: ML </h2>

The target variable we want to predict here is customer Churn. 
The models we decided to take are Random Forest and XGBoost. 

First, we as we have string features, we need to encode the data.

```
LE = LabelEncoder()

for col in Categorical_col:
    df[col] = LE.fit_transform(df[col])
```			     
The features we decided to take for the model training are the following:
```	
features = ['Support Calls', 'Total Spend', 'Usage Frequency', 'Tenure', 'Payment Delay']
x = df.loc[:, features]
y = df.loc[:, ['Churn']]
```	

The results with random search were: 
| Metric | Random Forest | XGBoost |
| ------------- | ------------- | ------------- |
| Accuracy  | 93% | 92-93%  |
| F1-Score  | 95%  | 95-96% |

So, we can deploy XGBoost classifier. 

<h2> :sparkles: FastAPI deployment </h2>

- There is [app.py](https://github.com/Ina612/Churn-predictions/blob/main/app.py) with the code to run using FastAPI and uvicorn. 
- [encodings.py](https://github.com/Ina612/Churn-predictions/blob/main/encodings.py) should be added to the same directory and specifies the datatypes. 
- [label_encoder.pkl](https://github.com/Ina612/Churn-predictions/blob/main/label_encoder.pkl) is the downloaded label encoder
- [best_model.pkl](https://github.com/Ina612/Churn-predictions/blob/main/best_model.pkl) is the downloaded xgboost classifier

See the [requirements](https://github.com/Ina612/Churn-predictions/blob/main/requirements.txt) for running the model.
