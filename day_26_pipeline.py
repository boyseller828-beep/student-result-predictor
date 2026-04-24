from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split\



Pipeline = Pipeline([("imputer",SimpleImputer(strategy="mean")),("scaler",StandardScaler()),("model",LogisticRegression())])

Pipeline.fit(x_train,y_train)





















