import pandas as pd

train = pd.read_csv('train_ctrUa4K.csv')
train.head()

# MISSING VALUES
train.isnull().sum()

# MISSING VALUE IMPUTATION (REMOVING THE ROWS WITH MISSING VALUES
train = train.dropna()
train.isnull().sum()


# DATA PREPARATION

X = train[['Gender', 'Married', 'ApplicantIncome', 'LoanAmount', 'Credit_History']]
y = train.Loan_Status
X.shape, y.shape
# TRAIN SPLITTING

from sklearn.model_selection import train_test_split
x_train, x_cv, y_train, y_cv = train_test_split(X,y, test_size = 0.2, random_state = 10)

# MODEL BUILDING
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=4, random_state = 10)
model.fit(x_train, y_train)

# VALIDATION

from sklearn.metrics import accuracy_score
pred_cv = model.predict(x_cv)
accuracy_score(y_cv,pred_cv)