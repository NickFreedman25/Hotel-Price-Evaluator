import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

data = pd.read_csv('data/cleaned_hotels_data.csv')
#Train Data
df = pd.DataFrame(data)
#Test Data (last 20 rows)
df_2 = pd.DataFrame(data)
df_2 = df_2.tail(20)
df.drop(df.tail(20).index, inplace = True) 
df = df[df.columns[[3,4,5,7]]]
df_2 = df_2[df_2.columns[[3,4,5,7]]]
numerical_columns = df._get_numeric_data().columns
features = [col for col in numerical_columns if col != 'ratePlan']
numerical_columns_2 = df_2._get_numeric_data().columns
features_2 = [col for col in numerical_columns_2 if col != 'ratePlan']

X = df[features]
y = df.ratePlan

p = PolynomialFeatures()

features_poly = p.fit_transform(df[features])
poly_df = pd.DataFrame(features_poly, columns=p.get_feature_names())

features_poly_2 = p.fit_transform(df_2[features_2])
poly_df_2 = pd.DataFrame(features_poly_2, columns=p.get_feature_names())

X_train, X_test, y_train, y_test = train_test_split(poly_df, df.ratePlan, random_state=28)

ss = StandardScaler()
ss.fit(X_train)
X_train_sc = ss.transform(X_train)
X_test_sc = ss.transform(X_test)

scaled_test_data = ss.transform(poly_df_2)

y_train_log = np.log(y_train)
y_test_log = np.log(y_test)

lr = LinearRegression()
lasso = LassoCV()
ridge = RidgeCV()

lr.fit(X_train_sc, y_train_log)

y_pred = lr.predict(scaled_test_data)
y_pred = np.exp(y_pred)

pred_df = df_2
pred_df['predratePlan'] = y_pred
print(pred_df)


