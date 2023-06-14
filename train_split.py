import pandas as pd

train = pd.read_csv('train_ctrUa4K.csv')
train = pd.read_csv('train_ctrUa4K.csv')
train['Gender']= train['Gender'].map({'Male':0, 'Female':1})
train['Married']= train['Married'].map({'No':0, 'Yes':1})
train['Loan_Status']= train['Loan_Status'].map({'N':0, 'Y':1})
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