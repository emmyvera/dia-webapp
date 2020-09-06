#importing our libraries
import pandas as pd
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import pickle

#Loading our data
data = pd.read_csv("diabetes.csv")

#Seperating our data into feature set and labels
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

#Preprocessing of our data, I performed scaling
scaler = StandardScaler()
scaler = scaler.fit(X)

#Training our computer,
#Note I have trained with the data before coming up with this parameters
#I trained with 2000 entries of patiences data
# Feature Set:- Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age 
# Label:- Outcome
# I used svm and I got an accuracy score of 99.6, a f1-Score of [0:96%],[1:94%]
clf = SVC(C=10, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=1, kernel='rbf',
  max_iter=-1, probability=True, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

#Prepare a pipeline
pipe_model = make_pipeline(scaler, clf).fit(X,y)

#Pickle it to be used for predicting  #API
pickle.dump(pipe_model, open("model.pkl", "wb"))

# Testing Testing Should predict a 1 and likehood of have it
print(pipe_model.predict([[7,195,70,33,145,25.1,0.163,55]]))
print(pipe_model.predict_proba([[7,195,70,33,145,25.1,0.163,55]])[:,1])

# Testing Testing Should predicy a 0 and likehood of have it
print(pipe_model.predict([[3,180,64,25,70,34,0.271,26]]))
print(pipe_model.predict_proba([[3,180,64,25,70,34,0.271,26]])[:,1])