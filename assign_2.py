import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean



class knn:
    def __init__(self,df):
        self.data, self.target = self.df_data(self,df)
        self.k = [1,3,5,10,20]
        pass
    def df_data(self,df):
        data = []
        target = []
        for row in df:
            a = []
            for col in len(df[row]):
                if col != len(df[row])-1:
                    a.append(df[row][col])
                else:
                    if df[row][col]=='Iris-setosa':
                        target.append(0)
                    elif df[row][col]=='Iris-versicolor':
                        target.append(1)
                    else:
                        target.append(2)
            data.append(a)
        return data,target
    def find_class(self,train_data,train_target,test_data,test_target,j,k):
        dist = {}
        splLen = test_data[j][0]
        splWid = test_data[j][1]
        ptlLen = test_data[j][2]
        ptlWid = test_data[j][3]
        for i in range(len(train_data)):
            euclidean_dist = euclidean(test_data[j], train_data[i])
            dist[i]=euclidean_dist
        distances = dict(sorted(dist.items(), key=lambda item: item[1]))
        h = 0
        ans = {}
        cnt = 0
        a = 0
        for key,value in distances.items():
            if h<k:
                if key in ans:
                    ans[key] = ans[key]+1
                else:
                    ans[key]=1
                if cnt<ans[key]:
                    a = key
                    cnt = ans[key]
                h+=1
            else:
                break
        return a
        pass
    def algo_basic(self):
        split_ratio = 0.7
        split_index = int(split_ratio * len(df))
        train_data = self.data[:split_index, :]
        train_target = self.target[:split_index, :]
        test_data = self.data[split_index:, :]
        test_target = self.target[split_index:, :]
        accuracy = {}
        for k in self.k:
            predicted_class = []
            c = 0
            for j in range(len(test_data)):
                predicted_class = self.find_class(train_data,train_target,test_data,test_target,j,k)
            for j in range(len(test_target)):
                if predicted_class==test_target[j]:
                    c+=1
            accuracy[k]=float(c/len(test_target))
        self.print_accuracy(accuracy)
        pass 
    
   
if __name__== '__main__' :
    df = pd.read_csv('C:\6th semester\Machine learning lab\Iris.csv')
    cols_to_normalize = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm','PetalWidthCm']
    df[cols_to_normalize] = (df[cols_to_normalize] - df[cols_to_normalize].mean()) / df[cols_to_normalize].std()   
    
    df_shuffled = df.sample(frac=1, random_state=42)  # Set a random seed for reproducibility
    solution = knn(df)
    
    
    
    print()
    
# first i will take data as dataframe and then i will make it as list of list
# now in main function i will take this data and do z_score normalisation
# split the data in to test and train (ue randon number) - now i will send this data to train         
# now going back to the class - i will take each and every value in the test sample and calculate their distance
# from all the other points and based on k value take k-nearrest neighours of that and store whether they are right or wrong
# i will store the accracy for each k value and plot using matplotlib and find the best k and plot confusion metrics as well
#

    
