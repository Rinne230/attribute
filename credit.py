import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

orifile = pd.read_csv("./data/credit/credit.csv")

cols = ['checking_balance','credit_history', 'purpose', 'savings_balance', 'employment_length', 'personal_status', 
        'other_debtors','property','installment_plan','housing','job','telephone','foreign_worker']
col_dict = {
"checking_balance" : {"1 - 200 DM" : 0,"< 0 DM" : 1,"> 200 DM" : 2,"unknown" : 3 },
"credit_history" : {"critical" : 0,"delayed" : 1,"fully repaid this bank" : 2,"fully repaid" : 3,"repaid" : 4 },
"purpose" : {"business" : 0,"car (new)" : 1,"car (used)" : 2,"domestic appliances" : 3,"education" : 4,"furniture" : 5,"others" : 6,"radio/tv" : 7,"repairs" : 8,"retraining" : 9 },
"savings_balance" : {"101 - 500 DM" : 0,"501 - 1000 DM" : 1,"< 100 DM" : 2,"> 1000 DM" : 3,"unknown" : 4 },
"employment_length" : {"0 - 1 yrs" : 0,"1 - 4 yrs" : 1,"4 - 7 yrs" : 2,"> 7 yrs" : 3,"unemployed" : 4 },
"personal_status" : {"divorced male" : 0,"female" : 1,"married male" : 2,"single male" : 3 },
"other_debtors" : {"co-applicant" : 0,"guarantor" : 1,"none" : 2 },
"property" : {"building society savings" : 0,"other" : 1,"real estate" : 2,"unknown/none" : 3 },
"installment_plan" : {"bank" : 0,"none" : 1,"stores" : 2 },
"housing" : {"for free" : 0,"own" : 1,"rent" : 2 },
"job" : {"mangement self-employed" : 0,"skilled employee" : 1,"unemployed non-resident" : 2,"unskilled resident" : 3 },
"telephone" : {"none" : 0,"yes" : 1 },
"foreign_worker" : {"no" : 0,"yes" : 1 } 
}

for col in cols:
    orifile[col] = orifile[col].map(col_dict[col])
orifile.to_csv("./data/credit/solvedcredit.csv")

y = orifile['default']
del orifile['default']
X = orifile
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
credit_model = DecisionTreeClassifier(min_samples_leaf = 6)
credit_model.fit(X_train, y_train)
credit_pred = credit_model.predict(X_test)
print(metrics.classification_report(y_test, credit_pred))
print(metrics.confusion_matrix(y_test, credit_pred))
print(metrics.accuracy_score(y_test, credit_pred))
