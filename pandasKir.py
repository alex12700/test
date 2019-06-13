import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("D:/data/titanic_train.csv", delimiter=';')

print(data.head())
#print(data) # display
#print(data.loc[(data['Fare'] >= 5) & (data['Fare'] <= 20),'PassengerId'].count())

data1 = data.loc[(data['Survived'] == True, 'Fare')]
data1.plot.box()
plt.show()