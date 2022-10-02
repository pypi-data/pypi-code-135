print("""
import pandas as pd 
import numpy as np
from numpy import array
from numpy import diag
from numpy import dot

from math import*

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')
pd.options.display.float_format = '{:.6f}'.format

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler ;  
from sklearn import metrics
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

from sklearn.decomposition import PCA
from sklearn.impute import KNNImputer
from sklearn.neighbors import NearestNeighbors

from scipy.sparse import csr_matrix
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cophenet
from scipy.linalg import svd

!pip3 install numpy
!pip3 install scikit-surprise

import pandas as pd
from surprise import Reader
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import NormalPredictor
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore
from surprise import KNNBaseline
from surprise import SVD
from surprise import BaselineOnly
from surprise import SVDpp
from surprise import NMF
from surprise import SlopeOne
from surprise import CoClustering
from surprise.accuracy import rmse
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise.model_selection import GridSearchCV

from collections import defaultdict

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


#----------------------------------------------------------------------------------------------------------------------------------
### USL - InClass (Day 1) - Questions [v1.0 - 020221]
Load the csv file and print the first five observations.

df_cust = pd.read_csv('wholesale_cust.csv')
df_cust.head()
print(df_cust.shape)
df_cust.describe().T
The data definition is as follows:

Region: City of the retailer

Vegetables: Annual spending on vegetables

Personal_care: Annual spending on personal care products

Milk: Annual spending on milk and milk products

Grocery: Annual spending on grocery

Plasticware: Annual spending on plasticware (container, bottles, dishes and so on)

Let's begin with some hands-on practice exercises
	
1. Is there any retailer whose entry is recorded more than once? If yes, do the needful.
df_cust[df_cust.duplicated()]
df_cust=df_cust.drop_duplicates()
df_cust.shape
	
2. Identify the different cities to which the retailers belong. Also, visualize their count in different cities.
sns.barplot(x=df_cust.Region.unique(), y=df_cust.Region.value_counts())
plt.show()
df_cust.Region.value_counts()
	
3. Identify the extreme observations in the data using a visualization technique.
Encoder=LabelEncoder()
df_cust['Region_Encoded']=Encoder.fit_transform(df_cust['Region']);
df_cust = df_cust.drop('Region',axis=1)
df_cust.head()
sns.barplot(x=df_cust.Region_Encoded.unique(), y=df_cust.Region_Encoded.value_counts())
plt.show()
df_cust.Region_Encoded.value_counts()
df_cust.boxplot()
	
4. Use the appropriate technique to remove the observations greater than 3*IQR above the third quartile.
Q1 = df_cust.quantile(0.25)
Q3 = df_cust.quantile(0.75)
IQR = Q3 - Q1
df=df_cust[~(df_cust > (Q3 + 3 * IQR)).any(axis=1)]
df.shape
	
5. Transform the numerical variables such that the values will be between 0 and 1.
Scaler=MinMaxScaler() ;
df_scaled=pd.DataFrame(data = Scaler.fit_transform(df), columns = df.columns)
df_scaled.head()
​
	
6. Perform K-Means clustering with varying K from 2 to 4, and identify the optimal number of clusters using the Silhouette plot.
n_clusters = [2, 3, 4]
for K in n_clusters:
    cluster = KMeans (n_clusters= K, random_state= 10)
    predict = cluster.fit_predict(df_scaled)
    score = silhouette_score(df_scaled, predict, random_state= 10)
    print ("For {} clusters the silhouette score is {})".format(K, score))
	
7. Consider the numerical variables to create two clusters and visualize them using the variables 'Vegetables' and 'Personal_care'.
C2=df_scaled[['Vegetables', 'Personal_care']]
C2.head()
n_clusters = [2, 3, 4]
for K in n_clusters:
    cluster = KMeans (n_clusters= K, random_state= 10)
    predict = cluster.fit_predict(C2)
    score = silhouette_score(C2, predict, random_state= 10)
    print ("For {} clusters the silhouette score is {})".format(K, score))
	
8. Draw insights from the clusters formed in the previous question with respect to each variable in the data.
n_clusters = [2, 3, 4]
for K in n_clusters:
    fig, (ax1) = plt.subplots(1)
    fig.set_size_inches(18, 7)
    model = KMeans(n_clusters = K, random_state = 10)
    cluster_labels = model.fit_predict(C2)
    silhouette_avg = silhouette_score(C2, cluster_labels)
    sample_silhouette_values = silhouette_samples(C2, cluster_labels)
​
    y_lower = 10
    for i in range(K):
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        ith_cluster_silhouette_values.sort()
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
        color = cm.nipy_spectral(float(i) / K)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10 
    ax1.set_title("Silhouette Plot")
    ax1.set_xlabel("Silhouette coefficient")
    ax1.set_ylabel("Cluster label")
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax1.set_yticks([])  
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8])
    colors = cm.nipy_spectral(cluster_labels.astype(float) / K)
  
    plt.suptitle(("Silhouette Analysis for K-Means Clustering with n_clusters = %d" % K), fontsize=14,fontweight='bold')
​
# display the plot
plt.show()
	
9. Group the retailers from Oneonta into 1 to 5 clusters and find the optimal number of clusters using within cluster sum of squares.
df_Oneonta=df_cust[df_cust.Region_Encoded == 1]
​
wcss  = []
for i in range(1,6):
    kmeans = KMeans(n_clusters = i, random_state = 10)
    kmeans.fit(df_Oneonta)
    wcss.append(kmeans.inertia_)
​
plt.plot(range(1,6), wcss)
plt.title('Elbow Plot', fontsize = 15)
plt.xlabel('No. of clusters (K)', fontsize = 15)
plt.ylabel('WCSS', fontsize = 15)
plt.show()
	
10. Group the retailers from Oneonta into the optimal number of clusters obtained in Q9. Also, find the number of retailers in each cluster.
n_clusters = [2, 3]
for K in n_clusters:
    cluster = KMeans (n_clusters= K, random_state= 10)
    predict = cluster.fit_predict(df_Oneonta)
    score = silhouette_score(df_Oneonta, predict, random_state= 10)
    print ("For {} clusters the silhouette score is {})".format(K, score))



#----------------------------------------------------------------------------------------------------------------------------------
### USL - Faculty Notebook (Day 1) - [v1.0 - 220121]

Read the dataset and print the first five observations.
# load the csv file
# store the data in 'df_cust'
df_cust = pd.read_csv('customer.csv')
​
# display first five observations using head()
df_cust.head()
Let us now see the number of variables and observations in the data.

# use 'shape' to check the dimension of data
df_cust.shape
Interpretation: The data has 200 observations and 5 variables.


2.2 Check the Data Type
Check the data type of each variable. If the data type is not as per the data definition, change the data type.

# use 'dtypes' to check the data type of a variable
df_cust.dtypes
Interpretation: All the variables are numeric except Cust_Number. The variable Sex is categorical as per the data definition, but it is considered as an interger.

Change the data type of 'Sex' to object.

# change the data type of 'Sex' to object
df_cust['Sex'] = df_cust['Sex'].astype('object')
Recheck the data type after the conversion.

# recheck the data types of all variables
df_cust.dtypes
Interpretation: Now all the variables have correct data type.


2.3 Remove Insignificant Variables
The column Cust_Number contains the unique ID of each customer, which is redundant for further analysis. Thus, we drop the column.

# drop the column 'Cust_Number' using drop()
# 'axis = 1' drops the specified column
df_cust = df_cust.drop('Cust_Number',axis=1)

2.4 Outlier Analysis and Treatment
Check the outliers in all the variables and treat them using appropriate techniques.

# consider the numeric variables
df_num = df_cust.drop(['Sex'], axis = 1)
​
# plot the boxplot for each numerical variable 
# set the number of rows in the subplot using the parameter, 'nrows'
# set the number of columns in the subplot using the parameter, 'ncols'
# 'figsize' sets the figure size
fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize=(15, 4))
​
# use for loop to plot the boxplot for each variable
for variable, subplot in zip(df_num.columns, ax.flatten()):
    
    # use boxplot() to plot the graph
    # pass the axes for the plot to the parameter, 'ax'
    sns.boxplot(df_cust[variable], ax = subplot)
​
# display the plot
plt.show()
We can see that an outlier is present in the variable Yearly_Income. Before clustering, we remove this outlier.

# consider the observations with yearly income less than 130000
df_cust = df_cust[df_cust['Yearly_Income'] < 130000]

2.5 Missing Value Treatment
First run a check for the presence of missing values and their percentage for each column. Then choose the right approach to treat them.

# sort the variables on the basis of total null values in the variable
# 'isnull().sum()' returns the number of missing values in each variable
# 'ascending = False' sorts values in the descending order
# the variable with highest number of missing values will appear first
Total = df_cust.isnull().sum().sort_values(ascending=False)          
​
# calculate percentage of missing values
# 'ascending = False' sorts values in the descending order
# the variable with highest percentage of missing values will appear first
Percent = (df_cust.isnull().sum()*100/df_cust.isnull().count()).sort_values(ascending=False)   
​
# concat the 'Total' and 'Percent' columns using 'concat' function
# pass a list of column names in parameter 'keys' 
# 'axis = 1' concats along the columns
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data
Interpretation: The above output shows that there are no missing values in the data.


2.6 Scale the Data
We perform kmeans on the variables Cust_Spend_Score and Yearly_Income.
# consider the features 'Cust_Spend_Score' and 'Yearly_Income'
X_filtered = df_cust[['Cust_Spend_Score', 'Yearly_Income']]
​
# print top 5 observations of X
X_filtered.head()
We scale the variables to get all the variables in the same range. With this, we can avoid a problem in which some features come to dominate solely because they tend to have larger values than others.

# initialize the StandardScaler
X_norm = StandardScaler()
​
# normalize all the columns of the dataframe 'X_filtered'
num_norm = X_norm.fit_transform(X_filtered)
​
# create a dataframe of scaled numerical variables
# pass the required column names to the parameter 'columns'
X = pd.DataFrame(num_norm, columns = X_filtered.columns)
​
X.head()

3. K-Means Clustering
Let us perform the centroid-based clustering algorithm (i.e. K-Means). Such algorithms are efficient but sensitive to initial conditions and outliers. K-means is the most widely-used centroid-based clustering algorithm.

Here we consider two techniques (elbow/scree plot and Silhouette score) to decide the optimal value of K to perform the K-means clustering.


3.1 Optimal Value of K Using Elbow Plot
Elbow plot is plotted with the value of K on the x-axis and the WCSS (Within Cluster Sum of Squares) on the y-axis. The value of K corresponding to the elbow point represents the optimal value for K.

# create several cluster combinations ranging from 1 to 20 and observe the wcss (Within Cluster Sum of Squares) for each cluster
# consider an empty list to store the WCSS
wcss  = []
​
# use for loop to perform K-means with different values of K
# set the 'random_state' to obtain the same centroid initialization for each code run
# fit the model on scaled data
# append the value of WCSS for each K to the list 'wcss'
# the 'inertia_' retuns the WCSS for specific value of K
for i in range(1,21):
    kmeans = KMeans(n_clusters = i, random_state = 10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
Let us plot the elbow plot and identify the elbow point.

# visualize the elbow plot to get the optimal value of K
​
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Elbow Plot', fontsize = 15)
plt.xlabel('No. of clusters (K)', fontsize = 15)
plt.ylabel('WCSS', fontsize = 15)
​
# display the plot
plt.show()
# visualize the elbow plot to get the optimal value of K
plt.plot(range(1,21), wcss)
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Elbow Plot', fontsize = 15)
plt.xlabel('No. of clusters (K)', fontsize = 15)
plt.ylabel('WCSS', fontsize = 15)
​
# plot a vertical line at the elbow
plt.axvline(x = 5, color = 'red')
​
# display the plot
plt.show()
Interpretation: We can see that the for K = 5, there is an elbow in the plot. Before this elbow point, the WCSS is decreasing rapidly and after K = 5, the WCSS is decreasing slowly.

Now, let us use the silhouette score method to identify the optimal value of K.


3.2 Optimal Value of K Using Silhouette Score
The Silhouette score can also be used to identify the optimal number of clusters. We plot the Silhouette score for different values of K. The K with the highest Silhouette score represents the optimal value for the number of clusters (K).

# create a list for different values of K
n_clusters = [2, 3, 4, 5, 6]
​
# use 'for' loop to build the clusters
# 'random_state' returns the same sample each time you run the code  
# fit and predict on the scaled data
# 'silhouette_score' function computes the silhouette score for each K
for K in n_clusters:
    cluster = KMeans (n_clusters= K, random_state= 10)
    predict = cluster.fit_predict(X)
    score = silhouette_score(X, predict, random_state= 10)
    print ("For {} clusters the silhouette score is {})".format(K, score))
Visualize the silhouette scores
# consider the number of clusters
n_clusters = [2, 3, 4, 5, 6]
​
# consider an array of the data
X = np.array(X)
​
# for each value of K, plot the silhouette plot the clusters formed
for K in n_clusters:
    
    # create a subplot with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    # set the figure size
    fig.set_size_inches(18, 7)
​
    # the 1st subplot is the silhouette plot
    # initialize the cluster with 'K' value and a random generator
    model = KMeans(n_clusters = K, random_state = 10)
    
    # fit and predict on the scaled data
    cluster_labels = model.fit_predict(X)
​
    # the 'silhouette_score()' gives the average value for all the samples
    silhouette_avg = silhouette_score(X, cluster_labels)
    
    # Compute the silhouette coefficient for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)
​
    y_lower = 10
    for i in range(K):
        
        # aggregate the silhouette scores for samples belonging to cluster i, and sort them
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        
        # sort the silhouette coefficient
        ith_cluster_silhouette_values.sort()
        
        # calculate the size of the cluster
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
​
        # color each cluster 
        color = cm.nipy_spectral(float(i) / K)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)
​
        # label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
​
        # compute the new y_lower for next plot
        y_lower = y_upper + 10 
​
    # set the axes and plot label
    ax1.set_title("Silhouette Plot")
    ax1.set_xlabel("Silhouette coefficient")
    ax1.set_ylabel("Cluster label")
​
    # plot the vertical line for average silhouette score of all the values
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
​
    # clear the y-axis ticks
    ax1.set_yticks([])  
    
    # set the ticks for x-axis 
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8])
​
    
    # 2nd plot showing the actual clusters formed
    # consider different color for each cluster
    colors = cm.nipy_spectral(cluster_labels.astype(float) / K)
    
    # plot a scatter plot to visualize the clusters
    ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7, c=colors, edgecolor='k')
​
    # label the cluster centers
    centers = model.cluster_centers_
    
    # display the cluster center with cluster number
    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50, edgecolor='k')
    
    # add the axes and plot title
    ax2.set_title("Clusters")
    ax2.set_xlabel("Spending Score")
    ax2.set_ylabel("Annual Income")
    
    # set the common title for subplots
    plt.suptitle(("Silhouette Analysis for K-Means Clustering with n_clusters = %d" % K), fontsize=14, 
                 fontweight='bold')
​
# display the plot
plt.show()
Interpretation: The above plot shows the silhouette plot and the clusters formed for each value of K. The plot shows that there are outliers (where the silhouette coefficient is less than 0) for K = 2,3,4. Also for K = 6, the 6th cluster has the silhouette score less than the average silhouette score. Thus we can not consider the K values as 2,3,4 and 6.

Also from the above output, we can see that the silhouette score is maximum for k = 5 and from the plot, we can see that there are no outliers for 5 clusters and all the clusters have silhouette coefficients greater than the average silhouette score. Thus we choose K = 5 as the optimal value of k.


3.3 Build the Clusters
Let us build the 5 clusters using K-menas clustering.

# build a K-Means model with 5 clusters
new_clusters = KMeans(n_clusters = 5, random_state = 10)
​
# fit the model
new_clusters.fit(X)
​
# append the cluster label for each point in the dataframe 'df_cust'
df_cust['Cluster'] = new_clusters.labels_
# head() to display top five rows
df_cust.head()
Check the size of each cluster
df_cust.Cluster.value_counts()
Plot a barplot to visualize the cluster sizes

# use 'seaborn' library to plot a barplot for cluster size
sns.countplot(data= df_cust, x = 'Cluster')
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Size of Cluster', fontsize = 15)
plt.xlabel('Clusters', fontsize = 15)
plt.ylabel('Number of Customers', fontsize = 15)
​
# add values in the graph
# 'x' and 'y' assigns the position to the text
# 's' represents the text on the plot
plt.text(x = -0.05, y =39, s = np.unique(new_clusters.labels_, return_counts=True)[1][0])
plt.text(x = 0.95, y =24, s = np.unique(new_clusters.labels_, return_counts=True)[1][1])
plt.text(x = 1.95, y =37, s = np.unique(new_clusters.labels_, return_counts=True)[1][2])
plt.text(x = 2.95, y =22, s = np.unique(new_clusters.labels_, return_counts=True)[1][3])
plt.text(x = 3.95, y =81, s = np.unique(new_clusters.labels_, return_counts=True)[1][4])
​
# display the plot
plt.show()
The 5th cluster is the largest cluster containing 80 observations.


3.4 Analyze the Clusters
Let us visualize the clusters by considering the variables 'Cust_Spend_Score' and 'Yearly_Income'.
# plot the lmplot to visualize the clusters
# pass the different markers to display the points in each cluster with different shapes
# the 'hue' parameter returns colors for each cluster
sns.lmplot(x = 'Cust_Spend_Score', y = 'Yearly_Income', data = df_cust, hue = 'Cluster', 
                markers = ['*', ',', '^', '.', '+'], fit_reg = False, size = 10)
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('K-means Clustering (for K=5)', fontsize = 15)
plt.xlabel('Spending Score', fontsize = 15)
plt.ylabel('Annual Income', fontsize = 15)
​
# display the plot
plt.show()
Now let us understand the summary statistics for each cluster.

Cluster 1
Check the size of the cluster
# size of a cluster 1
len(df_cust[df_cust['Cluster'] == 0])
Compute the statistical summary for the customers in this cluster
# statistical summary of the numerical variables
df_cust[df_cust.Cluster==0].describe()
# summary of the categorical variable
df_cust[df_cust.Cluster==0].describe(include = object)
Interpretation: The above summary shows that the average yearly income of the customers in this cluster is 85210.53 dollars. On average, their spending score is 83 and the average age is 32 years. Approximately 55% of the customers are female.

Here the spending score is high along with the high income.

Cluster 2
Check the size of the cluster
# size of a cluster 2
len(df_cust[df_cust['Cluster'] == 1])
Compute the statistical summary for the customers in this cluster
# statistical summary of the numerical variables
df_cust[df_cust.Cluster==1].describe()
# summary of the categorical variable
df_cust[df_cust.Cluster==1].describe(include = object)
Interpretation: The above summary shows that the average yearly income of the customers in this cluster is 26304.35 dollars. On average, their spending score is 22 and the average age is 45 years. Approximately 61% of the customers are female.

Here the spending score is low along with the less income.

Cluster 3
Check the size of the cluster
# size of a cluster 3
len(df_cust[df_cust['Cluster'] == 2])
Compute the statistical summary for the customers in this cluster
# statistical summary of the numerical variables
df_cust[df_cust.Cluster==2].describe()
# summary of the categorical variable
df_cust[df_cust.Cluster==2].describe(include = object)
Interpretation: The above summary shows that the average yearly income of the customers in this cluster is 85916.67 dollars. On average, their spending score is 19 and the average age is 41 years. Approximately 52% of the customers are male.

Here the spending score is low as compared to the high annual income. This group represent middle-aged customers, who tend to spend less and invest more.

Cluster 4
Check the size of the cluster
# size of a cluster 4
len(df_cust[df_cust['Cluster'] == 3])
Compute the statistical summary for the customers in this cluster
# statistical summary of the numerical variables
df_cust[df_cust.Cluster==3].describe()
# summary of the categorical variables
df_cust[df_cust.Cluster==3].describe(include = object)
Interpretation: The above summary shows that the average yearly income of the customers in this cluster is 25095.24 dollars. On average, their spending score is 82 and the average age is 25 years. Approximately 57% of the customers are female.

Here the spending score is high, but the yearly income is low. This group represent young adults, who tend to spend more despite of the less salary.

Cluster 5
Check the size of the cluster
# size of a cluster 5
len(df_cust[df_cust['Cluster'] == 4])
Compute the statistical summary for the customers in this cluster
# statistical summary of the numerical variables
df_cust[df_cust.Cluster==4].describe()
# summary of the categorical variables
df_cust[df_cust.Cluster==4].describe(include = object)
Interpretation: The above summary shows that the average yearly income of the customers in this cluster is 54687.5 dollars. On average, their spending score is 51 and the average age is 43 years. Here, 60% of the customers are female.

This group has a mediocre spending score along with the average income.




#----------------------------------------------------------------------------------------------------------------------------------
### USL - Faculty Notebook (Day 2) [v1.0 - 280121] 

2.1 Understand the Data
Read the dataset and print the first five observations.
# load the excel file
# store the data in 'df_prod'
df_prod = pd.read_excel('purchase.xlsx')
​
# display first five observations using head()
df_prod.head()
Here each product is the identifier for the observation. Thus, we set the variable Products as the row index.

# load the excel file 
# set the 1st column as index 
df_prod = pd.read_excel('purchase.xlsx', index_col = 0)
​
# display first five observations using head()
df_prod.head()
Let us now see the number of variables and observations in the data.

# use 'shape' to check the dimension of data
df_prod.shape
Interpretation: The data has 5977 observations and 8 variables.


2.2 Check the Data Type
Check the data type of each variable. If the data type is not as per the data definition, change the data type.

# use 'dtypes' to check the data type of a variable
df_prod.dtypes
Interpretation: All the variables have correct data type as per the data definition.


2.3 Remove Insignificant Variables
The column Prod_id contains the unique ID of each product, which is redundant for further analysis. Thus, we drop the column.

# drop the column 'Prod_id' using drop()
# 'axis = 1' drops the specified column
df_prod = df_prod.drop('Prod_id',axis=1)

2.4 Outlier Analysis and Treatment
Check the outliers in all the variables and treat them using appropriate techniques.

# consider the numeric variables
df_num = df_prod.drop(['Cust_id', 'Customer_Segment'], axis = 1)
​
# plot the boxplot for each numerical variable 
# set the number of rows in the subplot using the parameter, 'nrows'
# set the number of columns in the subplot using the parameter, 'ncols'
# 'figsize' sets the figure size
fig, ax = plt.subplots(nrows = 2, ncols = 3, figsize=(15, 8))
​
# use for loop to plot the boxplot for each variable
for variable, subplot in zip(df_num.columns, ax.flatten()):
    
    # use boxplot() to plot the graph
    # pass the axes for the plot to the parameter, 'ax'
    sns.boxplot(df_prod[variable], ax = subplot)
​
# display the plot
plt.show()
We can see that the outliers are present in all the variables except Order_Quan. Before clustering, we remove the outliers using IQR method.

# calculate the first quartile
Q1 = df_prod.quantile(0.25)
​
# calculate the third quartile
Q3 = df_prod.quantile(0.75)
​
# The Interquartile Range (IQR) is defined as the difference between the third and first quartile
# calculate IQR for each numeric variable
IQR = Q3 - Q1
​
# retrieve the dataframe without the outliers
# '~' returns the values that do not satisfy the given conditions 
# i.e. it returns values between the range [Q1-1.5*IQR, Q3+1.5*IQR]
# '|' is used as 'OR' operator on multiple conditions   
# 'any(axis=1)' checks the entire row for atleast one 'True' entry (those rows represents outliers in the data)
df_prod = df_prod[~((df_prod < (Q1 - 1.5 * IQR)) | (df_prod > (Q3 + 1.5 * IQR))).any(axis=1)]
​
# check the shape of the data
df_prod.shape
We again plot the boxplot for each variable to recheck the outliers.

# consider the numeric variables
df_num = df_prod.drop(['Cust_id', 'Customer_Segment'], axis = 1)
​
# plot the boxplot for each numerical variable 
# set the number of rows in the subplot using the parameter, 'nrows'
# set the number of columns in the subplot using the parameter, 'ncols'
# 'figsize' sets the figure size
fig, ax = plt.subplots(nrows = 2, ncols = 3, figsize=(15, 8))
​
# use for loop to plot the boxplot for each variable
for variable, subplot in zip(df_num.columns, ax.flatten()):
    
    # use boxplot() to plot the graph
    # pass the axes for the plot to the parameter, 'ax'
    sns.boxplot(df_prod[variable], ax = subplot)
​
# display the plot
plt.show()
Interpretation: Observing the range of the boxplot, we say that the outliers are removed from the original data. The new 'outliers' that we can see in some of the variables are moderate outliers that lied within the min/max range before removing the actual outliers.

Also, the number of observations is reduced from 5977 to 5192. Thus, we have removed the potential outliers.


2.5 Missing Value Analysis and Treatment
Check the presence of missing values in the data and treat them.

# sorting the variables on the basis of total null values in the variable
# 'isnull().sum()' returns the number of missing values in each variable
# 'ascending = False' sorts values in the descending order
# the variable with highest number of missing values will appear first
Total = df_prod.isnull().sum().sort_values(ascending = False)          
​
# calculate percentage of missing values
# 'ascending = False' sorts values in the descending order
# the variable with highest percentage of missing values will appear first
Percent = (df_prod.isnull().sum()*100/df_prod.isnull().count()).sort_values(ascending = False)   
​
# concat the 'Total' and 'Percent' columns using 'concat' function
# pass a list of column names in parameter 'keys' 
# 'axis = 1' concats along the columns
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data
Interpretation: The above output shows that there are no missing values in the data.


3. Hierarchical Clustering
It is the hierarchy based clustering method. Agglomerative and Divisive clustering are the two types of hierarchical clustering.

In this session, we consider the Agglomerative clustering. In this method, each data point is considered as a single cluster and these clusters are grouped to form bigger clusters and eventually the single cluster of all the observations is created.


3.1 Scale the Data
Each of the variables in the data has a different value range. Some features can dominate solely; because they tend to have larger values than others. To avoid this problem, we can scale the variables to get them in the same range.

To group the data, we do not need the variables 'Cust_id' and 'Customer_Segment', so we remove these variables and use the remaining variables to build the model.

# select the variables for model building and store it in 'features'
features = df_prod[['Sales', 'Order_Quan', 'Profit', 'Shipping_Cost', 'Product_Base_Margin']]
# instantiate the 'StandardScaler'
scaler = StandardScaler()
​
# fit_transform() transforms the data by first computing the mean and sd and later scaling the data
# name the standardized data as 'features_scaled'
features_scaled = scaler.fit_transform(features)
Now, we use the scaled data for model building.


3.2 Build the Model
To perform hierarchical clustering, we need to specify the number of required clusters to the AgglomerativeClustering() from the scikit-learn library.

To find the optimal number of clusters, we consider two methods: Dendrogram and Silhouette Score Method.

First, we find the linkage matrix. It represents the distance between the clusters based on the given linkage method. There are several linkage methods like single, complete, average, centroid ward. Here we use the ward linkage to calculate the linkage matrix. For most of the datasets, this method returns most explicit clusters.

# instantiate linkage object with scaled data and consider 'ward' linkage method 
link_mat = linkage(features_scaled, method = 'ward')     
​
# print first 10 observations of the linkage matrix 'link_mat'
print(link_mat[0:10])
Interpretation: The values in the first two columns below n (= 5192) are simply the indices of the observations that are clustered in pairs to form a new cluster. This new cluster is assigned the index value 'n+i' (for ith row). The intermediate clusters going forward, are indexed successively.

The third column represents the cophenetic distances (the height at which the clusters are merged for the first time) between the clusters at each row i, and the fourth column gives the number of observations in that cluster.

For example: The 5th row represents the grouping of 1656th observations and 5195th cluster. Since the dataset is large, most of the observations are merged at 0 height. The new cluster contains 3 data points (i.e. 5195th cluster is a cluster of 2 observations).


3.3 Plot the Dendrogram
A dendrogram is a visualization in the form of a tree, that represents the order and distances of merges during the hierarchical clustering. The structure of the dendrogram depends on the linkage method used in to calculate the distances between the clusters.

It plots each observation on the x-axis as one cluster in the first step of clustering; i.e. we will have 5192 points on x-axis and ward distance on y-axis.

We use the dendrogram to find the optimal number of clusters. The number of clusters 'K' that remains constant for the larger distance on the dendrogram represents the optimal value.

# plot the dendrogram
# pass the linkage matrix
dendro = dendrogram(link_mat)
​
# annotate the distance on the y-axis for distance > 20
# 'dendro' returns the dictionary containing x,y coordinates and the color list for each merge
# the 'icoord' returns the x-coordinates for the rectangle that represents the merging
# the 'dcoord' returns the y-coordinates (distance) for the each corner of the rectangle that represents the merging
for i, d, c in zip(dendro['icoord'], dendro['dcoord'], dendro['color_list']):
    
    # consider 'x' as the x-coordinate of the average distance on the merging line
    x = sum(i[1:3])/2
    
    # consider 'y' as the distance at which the merging occurs 
    y = d[1]
    
    # pass the if-condition for annotation
    if y > 20:
        
        # plot the bullet and annotate the merging distance 'y'
        plt.plot(x, y, 'o', c=c)
        
        # pass the conditions to annotate the distance
        plt.annotate("%.3g" % y, (x, y), xytext=(0, -5), textcoords='offset points', va='top', ha='center')
​
        
# plot the line to cut the dendrogram
plt.axhline(y = 100)
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Dendrogram', fontsize = 15)
plt.xlabel('Index', fontsize = 15)
plt.ylabel('Distance', fontsize = 15)
​
# display the plot
plt.show()
Interpretation:

1) x-axis contains the observations and the y-axis contains the distances computed using the 'ward' method.

2) Horizontal lines show the merging of the clusters.

3) The topmost line in the dendrogram refers to a single cluster of all the data points.

The above dendrogram shows that the number of clusters (=2) is constant from the distance 63.4 to 156. Thus, we can consider the value 'two' as the optimal number of clusters. The horizontal black line in the dendrogram intersects the vertical lines at two unique points. The different colors below the line correspond to the different clusters.

Let us calculate the Cophenetic correlation coefficient to study the quality of clusters formed using dendrogram.
# calculate the euclidean distance between the observations 
eucli_dist = euclidean_distances(features_scaled)
​
# the above code will return the matrix of 5192x5192
# consider only the array of upper triangular matrix
# k=1 considers the upper triangular values without the diagonal elements
dist_array = eucli_dist[np.triu_indices(5192, k = 1)]
​
# pass the linkage matrix and actual distance
# 1st output of the cophenet() is the correlation coefficient
coeff, cophenet_dist = cophenet(link_mat, dist_array)
​
# print the cophenetic correlation coefficient
print(coeff)
Interpretation: The value of cophenetic correlation coefficient is 0.7772. The value close to 1 indicates the best linkage quality. Here we can say that the linkage quality is good.


3.4 Silhouette Score Method
The Silhouette score can also be used to identify the optimal number of clusters. We plot the Silhouette score for different values of K. The K with the highest Silhouette score represents the optimal value for the number of clusters (K).

# consider different values of K
K = [2,3,4,5,6]
​
# consider an empty list tot store the Silhouette score
silhouette_scores = [] 
​
# consider a for loop to perform clustering for different values of K
for i in K:
    
    # instantiate clustering for each value of K
    model = AgglomerativeClustering(n_clusters = i) 
    
    # calculate the Silhouette score and append to the list 'silhouette_scores'
    silhouette_scores.append(silhouette_score(features_scaled, model.fit_predict(features_scaled))) 
    
# plot the Silhouette score for different K
plt.bar(K, silhouette_scores) 
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Silhouette Score for Values of K', fontsize = 15)
plt.xlabel('Number of Clusters', fontsize = 15) 
plt.ylabel('Silhouette Scores', fontsize = 15)
​
# display the plot
plt.show()
Interpretation: The above plot shows that the Silhouette score for K = 2 is the highest. This imlpies that K = 2 is the optimal value for number of clusters.

Both the dendrogram and Silhouette score method returns K = 2 as the optimal value for the number of clusters. Now we retrieve the clusters and let us visualize the data.


4. Retrieve the Clusters
Let us use AgglomerativeClustering() to form two clusters.

# instantiate clustering method with 2 clusters and 'ward' linkage method
clusters = AgglomerativeClustering(n_clusters=2, linkage='ward')
​
# fit the model on the scaled data
clusters.fit(features_scaled)
# add a column containing cluster number to the original data
df_prod['Cluster'] = clusters.labels_
​
# print head() of the newly formed dataframe
df_prod.head()
Check the size of each cluster.

# check the size of each cluster
df_prod['Cluster'].value_counts()
# plot the countplot for the cluster size
sns.countplot(data = df_prod, x = 'Cluster')
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Size of Cluster', fontsize = 15)
plt.xlabel('Cluster', fontsize = 15)
plt.ylabel('No. of Products', fontsize = 15)
​
# display the plot
plt.show()
Now let us visualize the clusters. As we have more than 2 features, we consider only the variables Sales and Profit to visualize the clusters.

# plot the scatterplot to visualize the clusters
sns.scatterplot(x = 'Sales', y = 'Profit', data = df_prod, hue = 'Cluster')
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Hierarchical Clustering', fontsize = 15)
plt.xlabel('Sales', fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
​
# display the plot
plt.show()
Interpretation: The largest cluster is shown by the orange color in the above plot.


4.1 Analysis of Cluster_1
Check the size of the cluster
# size of a cluster_1
df_prod['Cluster'].value_counts()[0]
Classify products belonging to the cluster
# first 10 products in the cluster_1
df_prod[df_prod.Cluster == 0].head(10)
Compute the statistical summary for the products in this cluster
# statistical summary of the numerical variables
df_prod[df_prod.Cluster==0].describe()
# summary of the categorical variables
df_prod[df_prod.Cluster==0].describe(include = object)
Interpretation: The above summary shows that the average sales of the products in this cluster is 8854.20 dollars. On average, the order quantity is 33. The customer with ID Cust_1445 has placed 9 orders. Approximately 40% of the orders are from corporate companies.

# check the count of different products belonging to cluster_1
df_prod[df_prod.Cluster==0].index.value_counts()
Interpretation: The above output shows that the majority of the products in this cluster are technical items (telephone and communication, vending machine, computer peripherals and so on). Thus, we can segment this cluster under Technology.


4.2 Analysis of Cluster_2
Check the size of the cluster
# size of a cluster_2
df_prod['Cluster'].value_counts()[1]
Classify products belonging to the cluster
# first 10 products in the cluster_2
df_prod[df_prod.Cluster == 1].head(10)
Compute the statistical summary for the products in this cluster
# statistical summary of the numerical variables
df_prod[df_prod.Cluster==1].describe()
# summary of the categorical variables
df_prod[df_prod.Cluster==1].describe(include = object)
Interpretation: The above summary shows that the average sales of the products in this cluster is 634.44 dollars. On average, the order quantity is 25. The customer with ID Cust_1337 has placed 14 orders in the last year. Approximately 46% of the orders are from corporate companies.

# check the count of different products belonging to cluster_2
df_prod[df_prod.Cluster==1].index.value_counts()
Interpretation: The above output shows that the majority of the products in this cluster are stationary items (paper, pen and art supplies, binders and bineder accessories and so on). Thus, we can segment this cluster under Stationary.


5. DBSCAN
DBSCAN is a density-based clustering method. It can create non-linear clusters. This method considers a high-density region as a cluster and the low-density points are considered as outliers. We do not need to provide the required number of clusters to the algorithm.

Let us cluster the scaled data.

# instantiate DBSCAN with epsilon and minimum points 
# pass the epsilon radius for neighbourhood
# pass the number of minimum points
model = DBSCAN(eps = 0.8, min_samples = 15)
​
# fit the model on the scaled data
model.fit(features_scaled)
# display the unique clusters formed by DBSCAN
(set(model.labels_))
Interpretation: From the above output we can see that the DBSCAN algorithm has created 3 clusters. The data points labeled as -1 are the outliers identified by DBSCAN.

# add a column containing cluster number to the original data
df_prod['Cluster_DBSCAN'] = model.labels_
​
# print head() of the newly formed dataframe
df_prod.head()
Check the size of each cluster.

# check the size of each cluster
df_prod['Cluster_DBSCAN'].value_counts()
# plot the countplot for the cluster size
sns.countplot(data = df_prod, x = 'Cluster_DBSCAN')
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('Size of Cluster', fontsize = 15)
plt.xlabel('Cluster', fontsize = 15)
plt.ylabel('No. of Products', fontsize = 15)
​
# display the plot
plt.show()
Interpretation: From the above output we can see that a cluster with 4875 is the largest cluster and other clusters are very small.

Now let us visualize the clusters. As we have more than 2 features, we consider only the variables Sales and Profit to visualize the clusters.

# plot the lmplot to visualize the clusters
# pass the 'Cluster_DBSCAN' to the hue parameter to display each cluster in a different color
# pass the different marker styles to visualize each cluster with a different marker
sns.lmplot(x = 'Sales', y = 'Profit', data = df_prod, hue = 'Cluster_DBSCAN', markers = ['o','+','^',','], 
           fit_reg = False, size = 12)
​
# set the axes and plot labels
# set the font size using 'fontsize'
plt.title('DBSCABN (eps = 0.8, min_samples = 15) ', fontsize = 15)
plt.xlabel('Sales', fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
​
# display the plota
plt.show()
Interpretation: The above plot shows the clusters created by DBSCAN. The blue circles correspond to the outliers and the observations in the largest cluster are denoted by the orange '+'. Other clusters are too small compared to the largest cluster.

We can see some of the points are overlapped. This is because the dimension of the original data is greater than 2 and we have considered only 2 variables to plot the clusters.

Now let us check the products belonging to each cluster.

Cluster 1
Let us identify the products in the cluster 1.

# check the count of different products belonging to cluster_1
df_prod[df_prod.Cluster_DBSCAN==0].index.value_counts()
Interpretation: We can see that the 1st cluster with 4875 observations contains stationary as well as technical products. Thus we can segment this cluster as 'Basket Class'.

Cluster 2
Let us identify the products in the cluster 2.

# check the count of different products belonging to cluster_2
df_prod[df_prod.Cluster_DBSCAN==1].index.value_counts()
Interpretation: We can see that the 2nd cluster with 27 observations contains 26 technical products. Thus we can segment this cluster under 'Technology'.

Cluster 3
Let us identify the products in the cluster 3.

# check the count of different products belonging to cluster_3
df_prod[df_prod.Cluster_DBSCAN==2].index.value_counts()
Interpretation: We can see that the 3rd cluster with 19 observations contains 15 statinary products. Thus we can segment this cluster under 'Stationary'.

Outliers identified by DBSCAN
# check the count of different products identified as outliers
df_prod[df_prod.Cluster_DBSCAN==-1].index.value_counts()
Interpretation: We can see that the algorithm has identified most of the technical products as the outliers.

Here we can see that the DBSCAN algorithm has not grouped the product like hierarchical clustering. Thus we can conclude that the DBSCAN algorithm is working poorly on this dataset.




#----------------------------------------------------------------------------------------------------------------------------------
### Untitled

plt.rcParams['figure.figsize'] = [15,8]
df = pd.read_csv('ML3 data.csv')
df.head()
df.shape
#Imputing Data, where Missing Values > 90%
S=df.isnull().sum()/df.shape[0]*100
df = df.drop(S[S>90].index,axis=1)
​
df.shape
impute_knn = KNNImputer(n_neighbors=2)
X=impute_knn.fit_transform(df)
df_new=pd.DataFrame(X, columns=df.columns)
S=df_new.isnull().sum()/df_new.shape[0]*100
S[S>0].index
df_new.describe(include='number').T
X_std = StandardScaler().fit_transform(df_new)
cov_matrix = np.cov(X_std.T)
print('Covariance Matrix \n%s', cov_matrix)
eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
print('Eigen Vectors \n%s', eig_vecs)
print('\n Eigen Values \n%s', eig_vals)
print('Eigen Vectors \n%s', eig_vecs)
print('\n Eigen Values \n%s', eig_vals)
tot = sum(eig_vals)
var_exp = [( i /tot ) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print("Cumulative Variance Explained", cum_var_exp)
plt.figure(figsize=(15 , 10))
plt.bar(range(605), var_exp, alpha = 0.5, align = 'center', label = 'Individual explained variance')
plt.step(range(605), cum_var_exp, where='mid', label = 'Cumulative explained variance')
plt.axhline(y=95, color='red')
plt.axvline(x=337, color='green')
plt.plot(337, 95, marker="o", markersize=20, markeredgecolor="black", markerfacecolor="none")
plt.annotate('95% Data explained',(337,95),textcoords="offset points",xytext=(-15,5),ha='right')
plt.ylabel('Explained Variance Ratio')
plt.xlabel('Principal Components')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
cum_var_exp[337]
pca=PCA()
df_pca= pca.fit_transform(X_std)
df_pca.shape


#----------------------------------------------------------------------------------------------------------------------------------
### DBSCAN

data=pd.read_csv("cluster_data.csv")
data.head()

for columns in data:
    print(columns,"--> # of missing value", data[columns].isna().sum() )
The dataset does not contain missing values.
# Apply Principle Component Anaylsis for visualizing the data in 2D space.
​
pca = PCA()
pca_data = pca.fit_transform(data)
pca_data = pd.DataFrame(pca_data, columns=["pc"+str(i+1) for i in range(len(data.columns))])
print("pca.explained variance ratio:\n ", " ".join(map("{:.3f}".format, pca.explained_variance_ratio_)))
plt.plot(np.cumsum(pca.explained_variance_ratio_));
pca_data1 = pca_data[["pc1","pc2"]].copy()
data1 = data.copy() # data1 is created, we do not want to change original data as adding the cluster column.
PCA is used to visualize the data.
From the Explanied Variance Ratio graph, the first two principle component can explain 97.5% of the all variance. Also, there is an elbow after the second principle component, so pc1 and pc2 are enough for representing this data.
DBSCAN
Find optimal parameter setting for DBSCAN.
epsilon = [1,1.25,1.5,1.75, 2,2.25,2.5,2.75, 3,3.25,3.5,3.75, 4]
min_samples = [10,15,20,25]
​
​
sil_avg = []
max_value = [0,0,0,0]
​
for i in range(len(epsilon)):
    for j in range(len(min_samples)):
​
        db = DBSCAN(min_samples = min_samples[j], eps =epsilon[i]).fit(data)
        #cluster_labels=dbscan.fit_predict(data) 
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
​
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)
​
​
        silhouette_avg = metrics.silhouette_score(data, labels)
        if silhouette_avg > max_value[3]:
            max_value=(epsilon[i], min_samples[j], n_clusters_, silhouette_avg)
        sil_avg.append(silhouette_avg)
​
print("epsilon=", max_value[0], 
      "\nmin_sample=", max_value[1],
      "\nnumber of clusters=", max_value[2],
      "\naverage silhouette score= %.4f" % max_value[3])
The model (epsilon = 3.5 and min_sample = 20) which has 0.6695 maximum average silhouette score has the optimal number of cluster; 4.
# Apply DBSCAN
​
db = DBSCAN(eps=3.5, min_samples=20).fit(data)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
​
# Number of clusters in labels, ignoring noise.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
​
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(data, labels))
# Plot result
​
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]
​
    class_member_mask = (labels == k)
​
    xy = pca_data1[class_member_mask & core_samples_mask]
    plt.plot(xy.iloc[:, 0], xy.iloc[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)
​
    xy = pca_data1[class_member_mask & ~core_samples_mask]
    plt.plot(xy.iloc[:, 0], xy.iloc[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)
​
plt.title('The visualization of the clustered data; estimated number of clusters: %d' % n_clusters_)
plt.xlabel("pc1:"+"{:.2f}".format(pca.explained_variance_ratio_[0]*100)+" %")
plt.ylabel("pc2:"+"{:.2f}".format(pca.explained_variance_ratio_[1]*100)+" %")
plt.show()
4 clusters are identified by DBSCAN algorithm. The result is plotted in terms of pc1 and pc2. Black points in the graph represent the outliers.


#----------------------------------------------------------------------------------------------------------------------------------
###  Building_Recommender_System_with_Surprise


Importing data
GroupLens Research has collected and made available rating data sets from the MovieLens web site (http://movielens.org). The data sets were collected over various periods of time, depending on the size of the set.

We are using Small: 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. Last updated 9/2018.

Download: ml-latest-small.zip (size: 1 MB)

df = pd.read_csv ("https://raw.githubusercontent.com/singhsidhukuldeep/Recommendation-System/master/data/ratings.csv")
df.head()
df.tail()
df.drop(['timestamp'], axis=1, inplace=True)
df.columns = ['userID', 'item', 'rating']
df.head()
df.shape
df.info()
print('Dataset shape: {}'.format(df.shape))
print('-Dataset examples-')
print(df.iloc[::20000, :])
EDA
Ratings Distribution
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
​
data = df['rating'].value_counts().sort_index(ascending=False)
trace = go.Bar(x = data.index,
               text = ['{:.1f} %'.format(val) for val in (data.values / df.shape[0] * 100)],
               textposition = 'auto',
               textfont = dict(color = '#000000'),
               y = data.values,
               )
# Create layout
layout = dict(title = 'Distribution Of {} ratings'.format(df.shape[0]),
              xaxis = dict(title = 'Rating'),
              yaxis = dict(title = 'Count'))
# Create plot
fig = go.Figure(data=[trace], layout=layout)
fig.show()
Ratings Distribution By Item
# Number of ratings per book
data = df.groupby('item')['rating'].count().clip(upper=50)
​
# Create trace
trace = go.Histogram(x = data.values,
                     name = 'Ratings',
                     xbins = dict(start = 0,
                                  end = 50,
                                  size = 2))
# Create layout
layout = go.Layout(title = 'Distribution Of Number of Ratings Per Item (Clipped at 50)',
                   xaxis = dict(title = 'Number of Ratings Per Item'),
                   yaxis = dict(title = 'Count'),
                   bargap = 0.2)
​
# Create plot
fig = go.Figure(data=[trace], layout=layout)
fig.show()
df.groupby('item')['rating'].count().reset_index().sort_values('rating', ascending=False)[:10]
Ratings Distribution By User
# Number of ratings per user
data = df.groupby('userID')['rating'].count().clip(upper=50)
​
# Create trace
trace = go.Histogram(x = data.values,
                     name = 'Ratings',
                     xbins = dict(start = 0,
                                  end = 50,
                                  size = 2))
# Create layout
layout = go.Layout(title = 'Distribution Of Number of Ratings Per User (Clipped at 50)',
                   xaxis = dict(title = 'Ratings Per User'),
                   yaxis = dict(title = 'Count'),
                   bargap = 0.2)
​
# Create plot
fig = go.Figure(data=[trace], layout=layout)
fig.show()
df.groupby('userID')['rating'].count().reset_index().sort_values('rating', ascending=False)[:10]
Dimensionality
To reduce the dimensionality of the dataset, we will filter out rarely rated movies and rarely rating users

min_ratings = 5
filter_items = df['item'].value_counts() > min_ratings
filter_items = filter_items[filter_items].index.tolist()
​
min_user_ratings = 5
filter_users = df['userID'].value_counts() > min_user_ratings
filter_users = filter_users[filter_users].index.tolist()
​
df_new = df[(df['item'].isin(filter_items)) & (df['userID'].isin(filter_users))]
print('The original data frame shape:\t{}'.format(df.shape))
print('The new data frame shape:\t{}'.format(df_new.shape))
Surprise
To load a dataset from a pandas dataframe, we will use the load_from_df() method, we will also need a Reader object, and the rating_scale parameter must be specified. The dataframe must have three columns, corresponding to the user ids, the item ids, and the ratings in this order. Each row thus corresponds to a given rating.

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df_new[['userID', 'item', 'rating']], reader)
Basic algorithms
With the Surprise library, we will benchmark the following algorithms

NormalPredictor
NormalPredictor algorithm predicts a random rating based on the distribution of the training set, which is assumed to be normal. This is one of the most basic algorithms that do not do much work.
BaselineOnly
BasiclineOnly algorithm predicts the baseline estimate for given user and item.
k-NN algorithms
KNNBasic
KNNBasic is a basic collaborative filtering algorithm.
KNNWithMeans
KNNWithMeans is basic collaborative filtering algorithm, taking into account the mean ratings of each user.
KNNWithZScore
KNNWithZScore is a basic collaborative filtering algorithm, taking into account the z-score normalization of each user.
KNNBaseline
KNNBaseline is a basic collaborative filtering algorithm taking into account a baseline rating.
Matrix Factorization-based algorithms
SVD
SVD algorithm is equivalent to Probabilistic Matrix Factorization (http://papers.nips.cc/paper/3208-probabilistic-matrix-factorization.pdf)
SVDpp
The SVDpp algorithm is an extension of SVD that takes into account implicit ratings.
NMF
NMF is a collaborative filtering algorithm based on Non-negative Matrix Factorization. It is very similar with SVD.
Slope One
Slope One is a straightforward implementation of the SlopeOne algorithm. (https://arxiv.org/abs/cs/0702144)
Co-clustering
Co-clustering is a collaborative filtering algorithm based on co-clustering (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.6458&rep=rep1&type=pdf)
We use rmse as our accuracy metric for the predictions.

benchmark = []
# Iterate over all algorithms
​
algorithms = [SVD(), SVDpp(), SlopeOne(), NMF(), NormalPredictor(), KNNBaseline(), KNNBasic(), KNNWithMeans(), KNNWithZScore(), BaselineOnly(), CoClustering()]
​
print ("Attempting: ", str(algorithms), '\n\n\n')
​
for algorithm in algorithms:
    print("Starting: " ,str(algorithm))
    # Perform cross validation
    results = cross_validate(algorithm, data, measures=['RMSE'], cv=3, verbose=False)
    # results = cross_validate(algorithm, data, measures=['RMSE','MAE'], cv=3, verbose=False)
    
    # Get results & append algorithm name
    tmp = pd.DataFrame.from_dict(results).mean(axis=0)
    tmp = tmp.append(pd.Series([str(algorithm).split(' ')[0].split('.')[-1]], index=['Algorithm']))
    benchmark.append(tmp)
    print("Done: " ,str(algorithm), "\n\n")
​
print ('\n\tDONE\n')
surprise_results = pd.DataFrame(benchmark).set_index('Algorithm').sort_values('test_rmse')
surprise_results
SVDpp is performing best but it is taking a lot of time so we will use SED instean but apply GridSearch CV.

# param_grid = {
#     "n_epochs": [5, 10, 15, 20, 30, 40, 50, 100],
#     "lr_all": [0.001, 0.002, 0.005],
#     "reg_all": [0.02, 0.08, 0.4, 0.6]
# }
​
# smaller grid for testing
param_grid = {
    "n_epochs": [10, 20],
    "lr_all": [0.002, 0.005],
    "reg_all": [0.02]
}
gs = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], refit=True, cv=5)
​
gs.fit(data)
​
training_parameters = gs.best_params["rmse"]
​
print("BEST RMSE: \t", gs.best_score["rmse"])
print("BEST MAE: \t", gs.best_score["mae"])
print("BEST params: \t", gs.best_params["rmse"])
from datetime import datetime
print(training_parameters)
reader = Reader(rating_scale=(1, 5))
​
print("\n\n\t\t STARTING\n\n")
start = datetime.now()
​
print("> Loading data...")
data = Dataset.load_from_df(df_new[['userID', 'item', 'rating']], reader)
print("> OK")
​
print("> Creating trainset...")
trainset = data.build_full_trainset()
print("> OK")
​
​
startTraining = datetime.now()
print("> Training...")
​
algo = SVD(n_epochs = training_parameters['n_epochs'], lr_all = training_parameters['lr_all'], reg_all = training_parameters['reg_all'])
​
algo.fit(trainset)
​
endTraining = datetime.now()
print("> OK \t\t It Took: ", (endTraining-startTraining).seconds, "seconds")
​
end = datetime.now()
print (">> DONE \t\t It Took", (end-start).seconds, "seconds" )
## SAVING TRAINED MODEL
from surprise import dump
import os
model_filename = "./model.pickle"
print (">> Starting dump")
# Dump algorithm and reload it.
file_name = os.path.expanduser(model_filename)
dump.dump(file_name, algo=algo)
print (">> Dump done")
print(model_filename)
## LOAD SAVED MODEL
def load_model(model_filename):
    print (">> Loading dump")
    from surprise import dump
    import os
    file_name = os.path.expanduser(model_filename)
    _, loaded_model = dump.load(file_name)
    print (">> Loaded dump")
    return loaded_model
# predicitng
from pprint import pprint as pp
model_filename = "./model.pickle"
def itemRating(user, item):
    uid = str(user)
    iid = str(item) 
    loaded_model = load_model(model_filename)
    prediction = loaded_model.predict(user, item, verbose=True)
    rating = prediction.est
    details = prediction.details
    uid = prediction.uid
    iid = prediction.iid
    true = prediction.r_ui
    ret = {
        'user': user, 
        'item': item, 
        'rating': rating, 
        'details': details,
        'uid': uid,
        'iid': iid,
        'true': true
        }
    pp (ret)
    print ('\n\n')
    return ret
print(itemRating(user = "610", item = "10"))




#----------------------------------------------------------------------------------------------------------------------------------
### Book Recommendation system using K Nearest Neighbor

Read the dataset with the necessary features
# Read Three Data sets [books, users. ratings] dada
​
books = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
users = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']
ratings.head()  # Rating is from 0-10
# Shape of data ( ratings data :- User,Item and rating)
print(ratings.shape)
print(list(ratings.columns))
# Distribution of rating
plt.rc("font", size=15)
ratings.bookRating.value_counts(sort=False).plot(kind='bar')
plt.title('Rating Distribution\n')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.savefig('system1.png', bbox_inches='tight')
plt.show()
print(books.shape)
print(list(books.columns))
print(users.shape)
print(list(users.columns))
# Distribution of Age
users.Age.hist(bins=[0, 10, 20, 30, 40, 50, 100])
plt.title('Age Distribution\n')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('system2.png', bbox_inches='tight')
plt.show()
To ensure statistical significance, users with less than 200 ratings, and books with less than 100 ratings are excluded.
counts1 = ratings['userID'].value_counts()
ratings = ratings[ratings['userID'].isin(counts1[counts1 >= 200].index)]
counts = ratings['bookRating'].value_counts()
ratings = ratings[ratings['bookRating'].isin(counts[counts >= 100].index)]
Collaborative Filtering Using k-Nearest Neighbors (kNN)
kNN is a machine learning algorithm to find clusters of similar users based on common book ratings, and make predictions using the average rating of top-k nearest neighbors. For example, we first present ratings in a matrix with the matrix having one row for each item (book) and one column for each user,

combine_book_rating = pd.merge(ratings, books, on='ISBN')
columns = ['yearOfPublication', 'publisher', 'bookAuthor', 'imageUrlS', 'imageUrlM', 'imageUrlL']
combine_book_rating = combine_book_rating.drop(columns, axis=1)
combine_book_rating.head(10)
We then group by book titles and create a new column for total rating count.

combine_book_rating = combine_book_rating.dropna(axis = 0, subset = ['bookTitle'])
​
book_ratingCount = (combine_book_rating.
     groupby(by = ['bookTitle'])['bookRating'].
     count().
     reset_index().
     rename(columns = {'bookRating': 'totalRatingCount'})
     [['bookTitle', 'totalRatingCount']]
    )
book_ratingCount.head()
We combine the rating data with the total rating count data, this gives us exactly what we need to find out which books are popular and filter out lesser-known books.

rating_with_totalRatingCount = combine_book_rating.merge(book_ratingCount, left_on = 'bookTitle', right_on = 'bookTitle', how = 'left')
rating_with_totalRatingCount.head()
pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(book_ratingCount['totalRatingCount'].describe())
The median book has been rated only once. Let’s look at the top of the distribution

print(book_ratingCount['totalRatingCount'].quantile(np.arange(.9, 1, .01)))
popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
rating_popular_book.head()
rating_popular_book.shape
Filter to users in US and Canada only
combined = rating_popular_book.merge(users, left_on = 'userID', right_on = 'userID', how = 'left')
​
us_canada_user_rating = combined[combined['Location'].str.contains("usa|canada")]
us_canada_user_rating=us_canada_user_rating.drop('Age', axis=1)
us_canada_user_rating.head()
Cosine Similarity
image.png

Implementing kNN
We convert our table to a 2D matrix, and fill the missing values with zeros (since we will calculate distances between rating vectors). We then transform the values(ratings) of the matrix dataframe into a scipy sparse matrix for more efficient calculations.

Finding the Nearest Neighbors We use unsupervised algorithms with sklearn.neighbors. The algorithm we use to compute the nearest neighbors is “brute”, and we specify “metric=cosine” so that the algorithm will calculate the cosine similarity between rating vectors. Finally, we fit the model.

​

us_canada_user_rating = us_canada_user_rating.drop_duplicates(['userID', 'bookTitle'])
us_canada_user_rating_pivot = us_canada_user_rating.pivot(index = 'bookTitle', columns = 'userID', values = 'bookRating').fillna(0)
us_canada_user_rating_matrix = csr_matrix(us_canada_user_rating_pivot.values)
​


model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
model_knn.fit(us_canada_user_rating_matrix)

us_canada_user_rating_pivot.iloc[query_index,:].values.reshape(1,-1)
query_index = np.random.choice(us_canada_user_rating_pivot.shape[0])
print(query_index)
distances, indices = model_knn.kneighbors(us_canada_user_rating_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)

us_canada_user_rating_pivot.index[query_index]
for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {0}:\n'.format(us_canada_user_rating_pivot.index[query_index]))
    else:
        print('{0}: {1}, with distance of {2}:'.format(i, us_canada_user_rating_pivot.index[indices.flatten()[i]], distances.flatten()[i]))




#----------------------------------------------------------------------------------------------------------------------------------
### apriori based recommendation

dataset
#transactions =  dataset.values.tolist()
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
transactions
# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2) 
# Visualising the results
results = list(rules)
results
for item in results:
​
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
​
    #second index of the inner list
    print("Support: " + str(item[1]))
​
    #third index of the list located at 0th
    #of the third index of the inner list
​
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")


#----------------------------------------------------------------------------------------------------------------------------------
### user-usercolabfilter

Load the movielens-100k dataset UserID::MovieID::Rating::Timestamp
data = Dataset.load_builtin('ml-100k') 
trainset, testset = train_test_split(data, test_size=.15)

# Use user_based true/false to switch between user-based or item-based collaborative filtering
algo = KNNWithMeans(k=50, sim_options={'name': 'pearson_baseline', 'user_based': True})
algo.fit(trainset)
# we can now query for specific predicions
uid = str(196)  # raw user id
iid = str(302)  # raw item id
# get a prediction for specific users and items.
pred = algo.predict(uid, iid, verbose=True)
# run the trained model against the testset
test_pred = algo.test(testset)
test_pred
# get RMSE
print("User-based Model : Test Set")
accuracy.rmse(test_pred, verbose=True)


#----------------------------------------------------------------------------------------------------------------------------------
### SVD

# define a matrix that needs to be decomposed thru SVD
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# applying Singular-value decomposition
U, s, VT = svd(A)
print(U)
print(s)
print(VT)
# create n x n Sigma matrix
Sigma = diag(s)
print(Sigma)
# reconstruct the matrix from u,s,vt
B = U.dot(Sigma.dot(VT))
print(B)


#----------------------------------------------------------------------------------------------------------------------------------
### similarty measures

from math import*
from math import*
  
def euclidean_distance(x,y):
  
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  
print(euclidean_distance([0,3,4,5],[7,6,3,-1]))
sqrt(pow((0-7),2)+pow((3-6),2)+pow((4-3),2)+pow((5--1),2))
from math import*
  
def manhattan_distance(x,y):
  
  return sum(abs(a-b) for a,b in zip(x,y))
  
print(manhattan_distance([0,3,4,5],[7,6,3,-1]))
abs(0-7)+abs(3-6)+abs(4-3)+abs(5--1)
from math import*
 
def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
 
print(cosine_similarity([0,3,4,5],[7,6,3,-1]))
(0*7)+(3*6)+(4*3)+(5*-1)
sqrt((0*0)+(3*3)+(4*4)+(5*5))/sqrt((7*7)+(6*6)+(3*3)+(-1*1))
((0*7)+(3*6)+(4*3)+(5*-1))/sqrt((0*0)+(3*3)+(4*4)+(5*5))/sqrt((7*7)+(6*6)+(3*3)+(-1*1))
from math import*
  
def jaccard_similarity(x,y):
  
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
  
print(jaccard_similarity([0,3,4,5],[7,6,3,-1]))


#----------------------------------------------------------------------------------------------------------------------------------
### matrix factorization_detailed

First train an SVD algorithm on the movielens dataset.
data = Dataset.load_builtin('ml-100k')

trainset = data.build_full_trainset()
trainset
trainset.ur
algo = SVD()
algo.fit(trainset)
# Than predict ratings for all pairs (u, i) that are NOT in the training set.
testset = trainset.build_anti_testset()
testset
predictions = algo.test(testset)
predictions
def get_top_n(predictions, n=10):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
​
    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
​
    return top_n
top_n = get_top_n(predictions, n=10)
top_n
# Print the recommended items for each user
for uid, user_ratings in top_n.items():
    print(uid, [iid for (iid, _) in user_ratings])


#----------------------------------------------------------------------------------------------------------------------------------
### KNNRecommendation

Nearest Neighbor item based Collaborative Filtering
image.png

Source: https://towardsdatascience.com

##Dataset url: https://grouplens.org/datasets/movielens/latest/
​
import pandas as pd
import numpy as np
movies_df = pd.read_csv('movies.csv',usecols=['movieId','title'],dtype={'movieId': 'int32', 'title': 'str'})
rating_df=pd.read_csv('ratings.csv',usecols=['userId', 'movieId', 'rating'],
    dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
movies_df.head()
rating_df.head()
df = pd.merge(rating_df,movies_df,on='movieId')
df.head()
combine_movie_rating = df.dropna(axis = 0, subset = ['title'])
movie_ratingCount = (combine_movie_rating.
     groupby(by = ['title'])['rating'].
     count().
     reset_index().
     rename(columns = {'rating': 'totalRatingCount'})
     [['title', 'totalRatingCount']]
    )
movie_ratingCount.head()
​
rating_with_totalRatingCount = combine_movie_rating.merge(movie_ratingCount, left_on = 'title', right_on = 'title', how = 'left')
rating_with_totalRatingCount.head()
pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(movie_ratingCount['totalRatingCount'].describe())
popularity_threshold = 50
rating_popular_movie= rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
rating_popular_movie.head()
rating_popular_movie.shape
## First lets create a Pivot matrix
​
movie_features_df=rating_popular_movie.pivot_table(index='title',columns='userId',values='rating').fillna(0)
movie_features_df.head()
from scipy.sparse import csr_matrix
​
movie_features_df_matrix = csr_matrix(movie_features_df.values)
​
from sklearn.neighbors import NearestNeighbors
​
​
model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
model_knn.fit(movie_features_df_matrix)
movie_features_df.shape
query_index = np.random.choice(movie_features_df.shape[0])
print(query_index)
distances, indices = model_knn.kneighbors(movie_features_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)
​
movie_features_df.head()
for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {0}:\n'.format(movie_features_df.index[query_index]))
    else:
        print('{0}: {1}, with distance of {2}:'.format(i, movie_features_df.index[indices.flatten()[i]], distances.flatten()[i]))
Cosine Similarity
image.png


#----------------------------------------------------------------------------------------------------------------------------------
### item-item collab filtering

from surprise import KNNWithMeans
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split
# Load the movielens-100k dataset  UserID::MovieID::Rating::Timestamp
data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=.15)
# Use user_based true/false to switch between user-based or item-based collaborative filtering
algo = KNNWithMeans(k=50, sim_options={'name': 'pearson_baseline', 'user_based': False})
algo.fit(trainset)
# run the trained model against the testset
test_pred = algo.test(testset)
test_pred
# get RMSE
print("Item-based Model : Test Set")
accuracy.rmse(test_pred, verbose=True)


#----------------------------------------------------------------------------------------------------------------------------------
### Session4_FacultyNoteBook

Recommendation System
	
Recommender systems aim to predict users’ interests and recommend product items that quite likely are interesting for them.

Recommendation system will help businesses improve their shopper's,user experience or on website,youtub,amazon and result in better customer acquisition and retention.

Types of recommendation system
	
There are majorly six types of recommender systems which work primarily in the Media and Entertainment industry::

1. Popularity based recommendation system
2. Content-based recommendation system
3. Collaborative recommendation system
4. Matrix factorization recommendation system
5. Association Rule
6. Hybrid-recommendation system

Popularity based recommendation system
	
This model is not actually personalized - it simply recommends to a user the most popular items that the user has not previously consumed i.e. even though you know the behaviour of the user you cannot recommend items accordingly.
	
Read the movie_dataset.csv.
Import the basic libraries
import pandas as pd
import numpy as np
Reading the movie_dataset.csv
data=pd.read_csv('book.csv')
data.head(2)
Popularity Based Recommendation System
# Top 10 books interms of average rating 
​
pd.DataFrame(data.groupby('bookTitle')['bookRating'].mean().sort_values(ascending=False))
# some books may get high average rating , but it is not reviewed by many users
# Hence we need to consider the review count also for better recommendation
popularity_table=data.groupby('bookTitle').agg({'bookRating':'mean','totalRatingCount':'count'})
#popularity_table['rating_per_count']=popularity_table['bookRating']/popularity_table['totalRatingCount']
#popularity_table.sort_values('rating_per_count',ascending=False)
#consider the books for recommendation only if it has 100 rating counts
top_popularity_table=popularity_table[popularity_table['totalRatingCount']>100]
#Top 10 books to recommed based on popularity
top_popularity_table.sort_values('bookRating',ascending=False).head(10)
So, I hope you now have enough idea about the popularity based recommendation system lets get into Content-based recommendation system

Content-based recommendation system
	
This method uses only information about the description and attributes of the items users has previously consumed to model user's preferences. In other words, these algorithms try to recommend items that are similar to those that a user liked in the past (or is examining in the present). In particular, various candidate items are compared with items previously rated by the user and the best-matching items are recommended..
	
Read the movie_metadata.csv dataset.
A simple Content Based Recommendation System
​
Content Based Recommendation
data1=pd.read_csv('movie_metadata.csv')
data1.head(2)
data1.columns
genres=data1['genres'].str.split('|',expand=True)
genres=genres.iloc[:,0:3]
genres=genres.fillna('Others')
genres.columns=['genre1','genre2','genre3']
genres.head(2)
data1=pd.concat([data1,genres],axis=1)
#movie_feat=['movie_title','genre1','genre2','genre3','language','content_rating',
           #'imdb_score','num_user_for_reviews','movie_facebook_likes']
movie_feat=['movie_title','genre1','genre2','genre3','content_rating','imdb_score']
data2=data1[movie_feat]
data2.head(2)
data2=data2.drop_duplicates()
data2.index=data2['movie_title']
data2=data2.drop('movie_title',axis=1)
data2.head(2)
data3=pd.get_dummies(data2)
data3=data3.dropna()
from sklearn.neighbors import NearestNeighbors
rec_model = NearestNeighbors(metric = 'cosine')
rec_model.fit(data3)
query_movie_index=200
dist, ind = rec_model.kneighbors(data3.iloc[query_movie_index, :].values.reshape(1, -1), n_neighbors = 6)
list(data3.index[ind[0]])[1:]
for i in range(0, len(dist[0])):
    if i == 0:
        print('Top 5 Recommendations for the user who watched the movie :',data3.index[query_movie_index])
    else:
        print(i, data3.index[ind[0][i]])
#data3.loc[data3.index[ind][0]]

Collaborative recommendation system
	
Collaborative filtering is currently one of the most frequently used approaches and usually provides better results than content-based recommendations. Some examples of this are found in the recommendation systems of Youtube, Netflix, and Spotify.
Collaborative Filtering, which is also known as User-User Filtering. As hinted by its alternate name, this technique uses other users to recommend items to the input user. It attempts to find users that have similar preferences and opinions as the input and then recommends items that they have liked to the input. There are several methods of finding similar users (Even some making use of Machine Learning), and the one we will be using here is going to be based on the Pearson Correlation Function.


	
Read the ratings.csv dataset.
​
Collaborative Based Recommendation
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split, cross_validate
from surprise import KNNWithMeans,SVDpp
from surprise import accuracy
ratings = pd.read_csv('ratings.csv')
reader = Reader(rating_scale=(1, 5))
ratings.head(3)
rating_data = Dataset.load_from_df(ratings[['userId','movieId','rating']],reader)
[trainset, testset] = train_test_split(rating_data, test_size=.15,shuffle=True)
trainsetfull = rating_data.build_full_trainset()
print('Number of users: ', trainsetfull.n_users, '\n')
print('Number of items: ', trainsetfull.n_items, '\n')
# my_k = 15
# my_min_k = 5
# my_sim_option = {'name':'pearson', 'user_based':False}
# algo = KNNWithMeans(k = my_k, min_k = my_min_k, sim_options = my_sim_option, verbose = True)
# results = cross_validate(
#     algo = algo, data = rating_data, measures=['RMSE'], 
#     cv=5, return_train_measures=True
#     )
# print(results['test_rmse'].mean())
alg=SVDpp()
alg.fit(trainsetfull)
#algo.fit(trainsetfull)
algo.predict(uid = 50, iid =2)
item_id=ratings['movieId'].unique()
item_id10=ratings.loc[ratings['userId']==10,'movieId']
item_id_pred=np.setdiff1d(item_id,item_id10)
item_id_pred
testset=[[50,iid,4] for iid in item_id_pred]
pred=alg.test(testset)
pred
pred_ratings=np.array([pred1.est for pred1 in pred])
i_max=pred_ratings.argmax()
iid=item_id_pred[i_max]
print("Top item for user 10 has iid {0} with predicted rating {1}".format(iid,pred_ratings[i_max]))


#----------------------------------------------------------------------------------------------------------------------------------
###  Session3-CaseStudy _ MCA

Dataset Information
Steel Plates Faults Data Set A dataset of steel plates' faults, classified into 7 different types. The goal was to train machine learning for automatic pattern recognition.

The dataset consists of 27 features describing each fault (location, size, ...) and 7 binary features indicating the type of fault (on of 7: Pastry, Z_Scratch, K_Scatch, Stains, Dirtiness, Bumps, Other_Faults). The latter is commonly used as a binary classification target ('common' or 'other' fault.)

Attribute Information
V1: X_Minimum
V2: X_Maximum
V3: Y_Minimum
V4: Y_Maximum
V5: Pixels_Areas
V6: X_Perimeter
V7: Y_Perimeter
V8: Sum_of_Luminosity
V9: Minimum_of_Luminosity
V10: Maximum_of_Luminosity
V11: Length_of_Conveyer
V12: TypeOfSteel_A300
V13: TypeOfSteel_A400
V14: Steel_Plate_Thickness
V15: Edges_Index
V16: Empty_Index
V17: Square_Index
V18: Outside_X_Index
V19: Edges_X_Index
V20: Edges_Y_Index
V21: Outside_Global_Index
V22: LogOfAreas
V23: Log_X_Index
V24: Log_Y_Index
V25: Orientation_Index
V26: Luminosity_Index
V27: SigmoidOfAreas
V28: Pastry
V29: Z_Scratch
V30: K_Scatch
V31: Stains
V32: Dirtiness
V33: Bumps
Class: Other_Faults
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
steel = pd.read_csv('steel_fault.csv')
steel.head()
steel.info()
steel.V14.nunique()
X = steel.drop('Class', axis=1)
y = steel['Class']
In the original dataset, there are two classes to predict. First let us find out the optimal number of clusters in the model.

from sklearn.cluster import KMeans
​
wcss = []
​
for k in range(1,10):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
# Visualization of k values:
​
plt.plot(range(1,10), wcss, color='red')
plt.title('Graph of k values and WCSS')
plt.xlabel('k values')
plt.ylabel('wcss values')
plt.show()
From the above plot we can see either 2 or 3 cluster would be appropriate for the data. Given what we know about the original classes, this seems about appropriate. Let us try clustering using two clusters. This way we can compare the clusters with the original class variable and see if they match up.

cluster = KMeans(n_clusters=2).fit(X)
y_cluster = pd.Series(cluster.labels_)
y_cluster.value_counts()
y.value_counts()
# re-labelling the y_cluster data
y_cluster = y_cluster.apply(lambda x: 2 if x==1 else 1)
from sklearn.metrics import accuracy_score
accuracy_score(y, y_cluster)
#Appending the y_cluster values to the Original Dataframe
steel['y_cluster']=y_cluster
Now let us try a decision tree classifier with the same data

from sklearn.tree import DecisionTreeClassifier
X = steel.drop(['Class','y_cluster'], axis=1)
y = steel['y_cluster']
​
from sklearn.model_selection import train_test_split
# Splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7,test_size=0.3,random_state=100)
model1 = DecisionTreeClassifier()
model1 = model1.fit(X_train, y_train)
ypred = model1.predict(X_test)
accuracy_score(y_test, ypred)
Accuracy is 100% on this data. The model may be over fitting. Let us try an ensemble bagging classifier.

from sklearn.ensemble import BaggingClassifier
model2 = BaggingClassifier()
model2 = model2.fit(X_train, y_train)
ypred = model2.predict(X_test)
accuracy_score(y_test, ypred)
Yet again the classification yields very good results.

The dataset has 33 independent features. We could also try dimensionality reduction by applying PCA on the data and trying if our classification yields similar results as before.

# import the necessary libraries
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import zscore
# standardise the data
​
X_std = StandardScaler().fit_transform(X)
# covariance matrix
cov_matrix = np.cov(X_std.T)
print('Covariance Matrix \n%s', cov_matrix)
eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
print('Eigen Vectors \n%s', eig_vecs)
print('\n Eigen Values \n%s', eig_vals)
tot = sum(eig_vals)
var_exp = [( i /tot ) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print("Cumulative Variance Explained", cum_var_exp)
len(cum_var_exp[cum_var_exp > 99])
Thus we can see that 99% of the variance is explained by the first 22 principal components

pca1 = PCA(n_components=22).fit_transform(X)
Now let us try the decision tree classifier again

model_pca = DecisionTreeClassifier()
model_pca = model_pca.fit(pca1, y)
y_pred = model_pca.predict(pca1)
accuracy_score(y, y_pred)
As we can see above, the accuracy remains unchanged inspite of reduced number of features.

DT After Applying MCA
pip install prince
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
X.columns
## Distinguish between categorical and numeric column names
​
cat = []
num = []
for i in X.columns:
    if X[i].nunique() < X.shape[0]/4:
        cat.append(i)
    else:
        num.append(i)
## Distinguish between categorical and numeric columns of train & test data
​
X_train_cat = X_train[cat]
X_train_num = X_train[num]
X_test_cat = X_test[cat]
X_test_num = X_test[num]
## Apply MCA
​
import prince
from sklearn.metrics import make_scorer
mca = prince.MCA()
​
mca_X_train = mca.fit_transform(X_train_cat)
mca_X_test = mca.fit_transform(X_test_cat)
main_mca_X_train = pd.concat([mca_X_train,X_train_num],axis = 1)
main_mca_X_test = pd.concat([mca_X_test,X_test_num],axis = 1)
from sklearn.metrics import make_scorer
from sklearn.metrics import explained_variance_score
​
explained_var = make_scorer(explained_variance_score)
explained_var
from sklearn import tree
model2=tree.DecisionTreeClassifier()
model2.fit(main_mca_X_train,y_train)
y_pred_DT_2 = model2.predict(main_mca_X_test)
from sklearn.metrics import confusion_matrix
cm_mCA= confusion_matrix(y_test, y_pred_DT_2)
sns.heatmap(cm_mCA, annot=True)
plt.show()
ac_mCA = accuracy_score(y_test, y_pred_DT_2)
print("Accuracy Score:", ac_mCA)
from sklearn.metrics import classification_report
​
classification_2=classification_report(y_test,y_pred_DT_2)
print(classification_2)



#----------------------------------------------------------------------------------------------------------------------------------
### ML-3-Session-5-Faculty-Notebook-V1

Market Basket Analysis
	
Market Basket Analysis is the process of discovering frequent item sets in large transactional database is called market basket analysis.
Example:
Market basket analysis might tell a retailer that customers often purchase colgate toothpaste and brush together, so putting both items on promotion at the same time would not create a significant increase in revenue, while a promotion involving just one of the items would likely drive sales of the other.


Assosciation Rules
	
Association Rules are widely used to analyze retail basket or transaction data, and are intended to identify strong rules discovered in transaction data using measures of interestingness, based on the concept of strong rules.
Assosciation rules are produced using algorithms like :
Apriori Algorithm

Eclat Algorithm

FP-growth Algorithm

There are various metrics in place to help us understand the strength of assosciation between antecedent and consequent:
Support:
It is calculated to check how much popular a given item is. It is measured by the proportion of transactions in which an itemset appears

Confidence:
It is calculated to check how likely if item X is purchased when item Y is purchased. This is measured by the proportion of transactions with item X, in which item Y also appears.

Lift:
It is calculated to measure how likely item Y is purchased when item X is purchased, while controlling for how popular item Y is. The formula for lift is: (lift = support (X ->Y) / (support(X) * support(Y)).

Levarage or Piatetsky-Snapiro:
It computes the difference between the observed frequency of X & Y appearing together and the frequency that we would expect if A and C are independent.

Conviction:
It can be interpreted as the ratio of the expected frequency that X occurs without Y (that is to say, the frequency that the rule makes an incorrect prediction) if X and Y were independent divided by the observed frequency of incorrect predictions.


Apriori Algorithm
	
Apriori is an algorithm for frequent item set mining and association rule learning over relational databases. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database.
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
	
Read the Market.csv
df = pd.read_csv("Market.csv")
df.head()
df.info()
df.shape
df.columns.size
unique column extraction operation
​
unique_row_items = []
for index, row in df.iterrows():
    items_series = list(row.str.split(','))
    for item_serie in items_series:
        for item in item_serie:
            if item not in unique_row_items:
                unique_row_items.append(item)
​
unique_row_items
Building Apriori Algorithm
df_apriori = pd.DataFrame(columns=unique_row_items)
df_apriori
match the data in hand and convert them to onehotencoding and add to dataframe
​
for index, row in df.iterrows():
    items = str(row[0]).split(',')
    #print(items)
    one_hot_encoding = np.zeros(len(unique_row_items),dtype=int)
    for it in items:
        for i,column in enumerate(df_apriori.columns):
            #print(i,column,it)
            if it == column:
                one_hot_encoding[i] = 1
    df_apriori.at[index] = one_hot_encoding
    #print(one_hot_encoding)
​
df_apriori
df_apriori.info()
df_apriori=df_apriori.astype('int')
freq_items = apriori(df_apriori, min_support = 0.2, use_colnames = True, verbose = 1)
freq_items
freq_items.head()
Building Assosciation Rules
df_association_rules = association_rules(freq_items, metric = "confidence", min_threshold = 0.2)
df_association_rules
df_association_rules.sort_values("confidence",ascending=False)
df_association_rules
df_association_rules["antecedents"].apply(lambda x: str(x))
cols = ['antecedents','consequents']
df_association_rules[cols] = df_association_rules[cols].applymap(lambda x: tuple(x))
print (df_association_rules)
df_association_rules = (df_association_rules.explode('antecedents')
         .reset_index(drop=True)
         .explode('consequents')
         .reset_index(drop=True))
df_association_rules
df_association_rules["product_group"] = df_association_rules["antecedents"].apply(lambda x: str(x)) + "," + df_association_rules["consequents"].apply(lambda x: str(x))
df_association_rules
df1 = df_association_rules.loc[:,["product_group","confidence","lift"]].sort_values("confidence",ascending=False)
import seaborn as sns
sns.set(font_scale=0.4) 
sns.set(rc={'figure.figsize':(21.7,5.27)})
sns.barplot(x="product_group",y="confidence",data=df1);
import seaborn as sns
sns.set(font_scale=0.4) 
sns.set(rc={'figure.figsize':(21.7,5.27)})
sns.barplot(x="product_group",y="confidence",hue="lift",data=df1);
import seaborn as sns
sns.set(font_scale=0.4) 
sns.set(rc={'figure.figsize':(21.7,5.27)})
sns.barplot(x="product_group",y="confidence",hue="lift",data=df1);
df1.plot.bar()
conclusion
80% of customers who buy MAGGI (Instant soup) buy it in tea.

TEA and MAGGI products increase their sales by 2.17 times mutually.

66% of customers who buy SUGAR buy it in bread.

42% of customers who buy COFFEE buy sugar and CORNFLAKES. At the same time, 33% of these sales are in bread.


Hybrid Recommender Systems
	
Hybrid recommendation filtering algorithm is mix between content based and collaborative filtering.
Content Boosted Collaborative Filtering using Item Item Similarity and Supervised learning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
	
Read the ratings, movie.csv
ratings = pd.read_csv('ratings.csv')
ratings.head()
ratings.shape
movies = pd.read_csv('movies.csv')
movies.head()
movies.shape
from sklearn.model_selection import train_test_split
trainDF, tempDF = train_test_split(ratings, test_size=0.2, random_state=100)
testDF = tempDF.copy()
tempDF.rating = np.nan
tempDF.head()
testDF = testDF.dropna()
testDF.head()
ratings = pd.concat([trainDF, tempDF]).reset_index()
ratings
ratings.head()
ratings.shape
Matrix Factorization via Singular Value Decomposition
# We want the format of ratings matrix to be one row per user and one column per movie. 
#we can pivot ratings_df to get that and call the new variable R_df.
R_df = ratings.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
R_df.tail()
from scipy.sparse.linalg import svds
U, sigma, Vt = svds(R_df, k = 50)
#diag
sigma = np.diag(sigma)
#I also need to add the user means back to get the predicted 5-star ratings
all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) 
preds_df = pd.DataFrame(all_user_predicted_ratings, columns = R_df.columns)
preds_df.head()
sigma
# return the movies with the highest predicted rating that the specified user hasn’t already rated
#Take specific user row from matrix from predictions
def recommend_movies_simple(predictions_df, userID, movies_df, original_ratings_df, num_recommendations=5):
    
    # Get and sort the user's predictions
    user_row_number = userID - 1 # UserID starts at 1, not 0
    sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)
    
    # Get the user's data and merge in the movie information.
    user_data = original_ratings_df[original_ratings_df.userId == (userID)]
    #Added title and genres
    user_full = (user_data.merge(movies_df, how = 'left', left_on = 'movieId', right_on = 'movieId').
                     sort_values(['rating'], ascending=False)
                 )
​
    print ('User {0} has already rated {1} movies.'.format(userID, user_full.shape[0]))
    print ('Recommending the highest {0} predicted ratings movies not already rated.'.format(num_recommendations))
    
    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    # select the movie which are in user list and remove those movies from our movies list
    # Then merge with the sorted user predictions with the movieIds with left join
    # Rename the columns to 'predictions'
    recommendations = (movies_df[~movies_df['movieId'].isin(user_full['movieId'])].
         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left', left_on = 'movieId', right_on = 'movieId').
         rename(columns = {user_row_number: 'Predictions'}))
    #sort the prediction values
    recommendations = (recommendations.sort_values('Predictions', ascending = False).
                       iloc[:num_recommendations, :-1]
                      )
​
    return user_full, recommendations, sorted_user_predictions, user_data, user_full
​
already_rated, predictions, sorted_user_predictions, user_data, user_full = recommend_movies_simple(preds_df, 2, movies, ratings, 10)
already_rated.head()
predictions
user_data
user_full
sorted_user_predictions
sorted_user_predictions


#----------------------------------------------------------------------------------------------------------------------------------
### Faculty_Notebook-Day03

PCA
Dimensionality Reduction
Objectives:-
1) Signal-noise ratio
2) Data correlation and information redundancy
from IPython.display import Image
Image('snr.PNG')
Correlation can be removed by rotating the data point or coordinate
Signal and Noise
The terms signal and noise are used in many different contexts, but we'll explore what they mean in a physical engineering or statistical sense.
The terms actually come from radio engineering, in which a signal is the noise-free signal and noise is the white noise you hear when you can't tune a radio to a particular station.
Signal processing is the statistical technique used to extract information from the raw signal
Signal to Noise Ratio(SNR)
In order to determine the strength of a signal it is necessary to calculate what is called the signal-to-noise-ratio (SNR).
The higher the ratio, the easier it becomes to detect a true signal or extract useful information from the raw signal.
Thus, it is defined as the ratio as the power (P) of a signal to the power (P) of the background noise.
The knowledge of this ratio has many important applications in applied mathematics, analytical chemistry, electronics, and the geosciences.
In electronics, signal and noise are measured in decibels, a measure of volume.
In other disciplines, the SNR is also known as the effect size.
from IPython.display import Image
Image('snrformula.PNG')
from IPython.display import Image
Image('snr3.PNG')
MAXIMIZE SNR
Keep one signal dimension, discard one noisy dimension
from IPython.display import Image
Image('snr4.PNG')
In simple words, principal component analysis is a method of extracting important variables (in form of components) from a large set of variables available in a data set.
It extracts low dimensional set of features from a high dimensional data set with a motive to capture as much information as possible.
With fewer variables, visualization also becomes much more meaningful.
PCA is more useful when dealing with 3 or higher dimensional data.
from IPython.display import Image
Image('iris.png')
What are principal components ?
A principal component is a normalized linear combination of the original predictors in a data set. In image above, PC1 and PC2 are the principal components.

Let’s say we have a set of predictors as X¹, X²...,Xp

The principal component can be written as:

Z¹ = Φ¹¹X¹ + Φ²¹X² + Φ³¹X³ + .... +Φp¹Xp
where,Z¹ is first principal component
Φp¹ is the loading vector comprising of loadings (Φ¹, Φ²..) of first principal component.
The loadings are constrained to a sum of square equals to 1.
This is because large magnitude of loadings may lead to large variance.
It also defines the direction of the principal component (Z¹) along which data varies the most.
It results in a line in p dimensional space which is closest to the n observations. Closeness is measured using average squared euclidean distance.
X¹..Xp are normalized predictors. Normalized predictors have mean equals to zero and standard deviation equals to one.
Therefore,First principal component is a linear combination of original predictor variables which captures the maximum variance in the data set.

It determines the direction of highest variability in the data. Larger the variability captured in first component, larger the information captured by component.

No other component can have variability higher than first principal component.

The first principal component results in a line which is closest to the data i.e. it minimizes the sum of squared distance between a data point and the line.

Second principal component (Z²) is also a linear combination of original predictors which captures the remaining variance in the data set and is uncorrelated with Z¹.

In other words, the correlation between first and second component should is zero.

It can be represented as:

Z² = Φ¹²X¹ + Φ²²X² + Φ³²X³ + .... + Φp2Xp
If the two components are uncorrelated, their directions should be orthogonal (image below).

This image is based on a simulated data with 2 predictors.

Notice the direction of the components, as expected they are orthogonal. This suggests the correlation b/w these components in zero.

from IPython.display import Image
Image('5.PNG')
All succeeding principal component follows a similar concept i.e. they capture the remaining variation without being correlated with the previous component.
In general, for n × p dimensional data, min(n-1, p) principal component can be constructed.
The directions of these components are identified in an unsupervised way i.e. the response variable(Y) is not used to determine the component direction.
Therefore, it is an unsupervised approach.
Eigenvectors:
Eigenvectors and Eigenvalues are in itself a big domain, let’s restrict ourselves to the knowledge of the same which we would require here.
So, consider a non-zero vector v.
It is an eigenvector of a square matrix A, if Av is a scalar multiple of v.
Or simply: Av = ƛv
Here, v is the eigenvector and ƛ is the eigenvalue associated with it.
Covariance Matrix:
This matrix consists of the covariances between the pairs of variables.
The (i,j)th element is the covariance between i-th and j-th variable.
Implement PCA in Python
PCA: algorithm
1) Subtract mean
2) Calculate the covariance matrix
3) Calculate eigenvectors and eigenvalues of the covariance matrix
4) Rank eigenvectors by its corresponding eigenvalues
5) Obtain P with its column vectors corresponding to the top k eigenvectors
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# importing ploting libraries
import matplotlib.pyplot as plt 
from scipy.stats import zscore
from sklearn import datasets
%matplotlib inline
Step 1: Normalize the data
First step is to normalize the data that we have so that PCA works properly.
This is done by subtracting the respective means from the numbers in the respective column.
So if we have two dimensions X and Y, all X become 𝔁- and all Y become 𝒚-. This produces a dataset whose mean is zero.
iris = datasets.load_iris()
X = iris.data
X_std = StandardScaler().fit_transform(X)
Step 2: Calculate the covariance matrix
cov_matrix = np.cov(X_std.T)
print('Covariance Matrix \n%s', cov_matrix)
Understand the data using pair plot
X_std_df = pd.DataFrame(X_std)
axes = pd.plotting.scatter_matrix(X_std_df)
plt.tight_layout()
Step 3: Calculate the eigenvalues and eigenvectors
eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
print('Eigen Vectors \n%s', eig_vecs)
print('\n Eigen Values \n%s', eig_vals)
eigen_pairs = [(np.abs(eig_vals[i]), eig_vecs[ :, i]) for i in range(len(eig_vals))]
tot = sum(eig_vals)
var_exp = [( i /tot ) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print("Cumulative Variance Explained", cum_var_exp)
plt.figure(figsize=(6 , 4))
plt.bar(range(4), var_exp, alpha = 0.5, align = 'center', label = 'Individual explained variance')
plt.step(range(4), cum_var_exp, where='mid', label = 'Cumulative explained variance')
plt.ylabel('Explained Variance Ratio')
plt.xlabel('Principal Components')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
# First three principal components explain 99% of the variance in the data. The first three PCA is shown below
# The three PCA will have to be named because they represent composite of original dimensions
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
​
# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
​
## Get the min and max of the two dimensions and extend the margins by .5 on both sides to get the data points away
## from the origin in the plot
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
​
## plot frame size
plt.figure(2, figsize=(8, 6))
plt.clf()
​
# Plot the training points (scatter plot, all rows first and second column only)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
​
​
## plotting the axes with ticks
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
​
​
from sklearn.metrics import confusion_matrix
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
DT Classifier Before Applying PCA
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(X_train,y_train)
​
y_pred_DT = model.predict(X_test)
cm_DT= confusion_matrix(y_test, y_pred_DT)
cm_DT
sns.heatmap(cm_DT, annot=True)
plt.show()
classification=classification_report(y_test,y_pred_DT)
print(classification)
ac = accuracy_score(y_test, y_pred_DT)
print("Accuracy Score:", ac)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.Set1,alpha = 1, edgecolor='k')
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0], X_test[:, 1], c=y_pred_DT, cmap=plt.cm.Set1,alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0][y_test == 0], X_test[:, 1][y_test == 0], c='red',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 1], X_test[:, 1][y_test == 1], c='blue',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 2], X_test[:, 1][y_test == 2], c='yellow',alpha = 1, edgecolor='k')
​
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0][y_pred_DT == 0], X_test[:, 1][y_pred_DT == 0], c='red',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT == 1], X_test[:, 1][y_pred_DT == 1], c='blue',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT == 2], X_test[:, 1][y_pred_DT == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
DT After Applying PCA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.decomposition import PCA
pca = PCA()
X_train_2 = pca.fit_transform(X_train)
X_test_2 = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_  
explained_variance
from sklearn import tree
model2=tree.DecisionTreeClassifier()
model2.fit(X_train_2,y_train)
​
y_pred_DT_2 = model2.predict(X_test_2)
from sklearn.metrics import confusion_matrix
cm_PCA= confusion_matrix(y_test, y_pred_DT_2)
sns.heatmap(cm_PCA, annot=True)
plt.show()
ac_PCA = accuracy_score(y_test, y_pred_DT_2)
print("Accuracy Score:", ac_PCA)
classification_2=classification_report(y_test,y_pred_DT_2)
print(classification_2)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.Set1,alpha = 1, edgecolor='k')
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0], X_test[:, 1], c=y_pred_DT_2, cmap=plt.cm.Set1,alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0][y_test == 0], X_test[:, 1][y_test == 0], c='red',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 1], X_test[:, 1][y_test == 1], c='blue',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 2], X_test[:, 1][y_test == 2], c='yellow',alpha = 1, edgecolor='k')
​
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0][y_pred_DT_2 == 0], X_test[:, 1][y_pred_DT_2 == 0], c='red',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT_2 == 1], X_test[:, 1][y_pred_DT_2 == 1], c='blue',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT_2 == 2], X_test[:, 1][y_pred_DT_2 == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
Pros and Cons of PCA :-
Pros :-
Remove Noise
Can deal with large datasets
Cons :-
hard to interpret
sample dependent
linear
DT After Applying LDA
# create the lda model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm_LDA= confusion_matrix(y_test, y_pred)
sns.heatmap(cm_LDA, annot=True)
plt.show()
ac_LDA = accuracy_score(y_test, y_pred)
print("Accuracy Score:", ac_LDA)
classification_2=classification_report(y_test,y_pred)
print(classification_2)
Hyperparameter tunning of LDA
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# define model
model = LinearDiscriminantAnalysis()
# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# define grid
grid = dict()
grid['solver'] = ['svd', 'lsqr', 'eigen']
#grid['shrinkage'] = np.arange(0, 1, 0.01)
# define search
search = GridSearchCV(model, grid, scoring='accuracy', cv=cv, n_jobs=-1)
# perform the search
results = search.fit(X_train, y_train)
# summarize
print('Mean Accuracy: %.3f' % results.best_score_)
print('Config: %s' % results.best_params_)
model = LinearDiscriminantAnalysis(solver = 'svd')
model1 = model.fit(X_train,y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm_LDA= confusion_matrix(y_test, y_pred)
sns.heatmap(cm_LDA, annot=True)
plt.show()
ac_LDA = accuracy_score(y_test, y_pred)
print("Accuracy Score:", ac_LDA)
classification_2=classification_report(y_test,y_pred)
print(classification_2)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.Set1,alpha = 1, edgecolor='k')
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap=plt.cm.Set1,alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0][y_test == 0], X_test[:, 1][y_test == 0], c='red',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 1], X_test[:, 1][y_test == 1], c='blue',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 2], X_test[:, 1][y_test == 2], c='yellow',alpha = 1, edgecolor='k')
​
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0][y_pred == 0], X_test[:, 1][y_pred == 0], c='red',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred == 1], X_test[:, 1][y_pred == 1], c='blue',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred == 2], X_test[:, 1][y_pred == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
DT After Applying Kernel-PCA
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np 
​
gamma=15 
n_components=2
sq_dists = pdist(X_train, 'sqeuclidean')    
# Convert pairwise distances into a square matrix.
mat_sq_dists = squareform(sq_dists)    
# Compute the symmetric kernel matrix.
K = exp(-gamma * mat_sq_dists)    
# Center the kernel matrix.
N = K.shape[0]
one_n = np.ones((N,N)) / N
K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)    
# Obtaining eigenpairs from the centered kernel matrix
# scipy.linalg.eigh returns them in ascending order
eigvals, eigvecs = eigh(K)
eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]    
# Collect the top k eigenvectors (projected examples)
X_train_kpca = np.column_stack([eigvecs[:, i] for i in range(n_components)])
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np 
def rbf_kernel_pca(X, gamma, n_components):
    
    RBF kernel PCA implementation.    
    Parameters
    ------------
    X: {NumPy ndarray}, shape = [n_examples, n_features]  
    gamma: float
        Tuning parameter of the RBF kernel    
    n_components: int
        Number of principal components to return    
    Returns
    ------------
    X_pc: {NumPy ndarray}, shape = [n_examples, k_features]
        Projected dataset   
   
    # Calculate pairwise squared Euclidean distances
    # in the MxN dimensional dataset.
    sq_dists = pdist(X, 'sqeuclidean')    
    # Convert pairwise distances into a square matrix.
    mat_sq_dists = squareform(sq_dists)    
    # Compute the symmetric kernel matrix.
    K = exp(-gamma * mat_sq_dists)    
    # Center the kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)    
    # Obtaining eigenpairs from the centered kernel matrix
    # scipy.linalg.eigh returns them in ascending order
    eigvals, eigvecs = eigh(K)
    eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]    
    # Collect the top k eigenvectors (projected examples)
    X_pc = np.column_stack([eigvecs[:, i]
                           for i in range(n_components)])    
    return X_pc
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.decomposition import PCA
#kpca = rbf_kernel_pca(X, gamma=15, n_components=2)
X_train_2 = rbf_kernel_pca(X_train, gamma=1, n_components=3)
X_test_2 = rbf_kernel_pca(X_test, gamma=1, n_components=3)
from sklearn import tree
model2=tree.DecisionTreeClassifier()
model2.fit(X_train_2,y_train)
​
y_pred_DT_2 = model2.predict(X_test_2)
from sklearn.metrics import confusion_matrix
cm_kpca= confusion_matrix(y_test, y_pred_DT_2)
sns.heatmap(cm_kpca, annot=True)
plt.show()
ac_cm_kpca = accuracy_score(y_test, y_pred_DT_2)
print("Accuracy Score:", ac_cm_kpca)
classification_2=classification_report(y_test,y_pred_DT_2)
print(classification_2)
Parameter tunning in Kennel-PCA
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import KernelPCA
from sklearn import tree
​
kpca=KernelPCA(fit_inverse_transform=True, n_jobs=-1) 
param_grid = [{
        "kpca__gamma": np.linspace(0.03, 0.05, 10),
        "kpca__kernel": ["rbf", "sigmoid", "linear", "poly"]
    }]
grid_search = GridSearchCV(kpca, param_grid, cv=3, scoring='accuracy')
X_kpca_train = kpca.fit_transform(X_train)
X_preimage = kpca.inverse_transform(X_kpca_train)
from sklearn.metrics import mean_squared_error
mean_squared_error(X_train, X_preimage)
type(X_kpca_train)
from sklearn import tree
model2=tree.DecisionTreeClassifier()
model2.fit(X_kpca_train,y_train)
​
X_kpca_test = kpca.fit_transform(X_test)
y_pred_DT_3 = model2.predict(X_kpca_test)
from sklearn.metrics import confusion_matrix
cm_kpca= confusion_matrix(y_test, y_pred_DT_3)
sns.heatmap(cm_kpca, annot=True)
plt.show()
ac_cm_kpca = accuracy_score(y_test, y_pred_DT_3)
print("Accuracy Score:", ac_cm_kpca)
classification_2=classification_report(y_test,y_pred_DT_3)
print(classification_2)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0][y_test == 0], X_test[:, 1][y_test == 0], c='red',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 1], X_test[:, 1][y_test == 1], c='blue',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 2], X_test[:, 1][y_test == 2], c='yellow',alpha = 1, edgecolor='k')
​
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
ax[1].scatter(X_test[:, 0][y_pred_DT_3 == 0], X_test[:, 1][y_pred_DT_3 == 0], c='red',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT_3 == 1], X_test[:, 1][y_pred_DT_3 == 1], c='blue',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT_3 == 2], X_test[:, 1][y_pred_DT_3 == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Predicted label')
plt.show()
fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15, 5))
​
# Plot the training points (scatter plot, all rows first and second column only)
ax[0].scatter(X_test[:, 0][y_test == 0], X_test[:, 1][y_test == 0], c='red',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 1], X_test[:, 1][y_test == 1], c='blue',alpha = 1, edgecolor='k')
ax[0].scatter(X_test[:, 0][y_test == 2], X_test[:, 1][y_test == 2], c='yellow',alpha = 1, edgecolor='k')
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title('Actual label')
​
ax[1].scatter(X_test[:, 0][y_pred_DT == 0], X_test[:, 1][y_pred_DT == 0], c='red',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT == 1], X_test[:, 1][y_pred_DT == 1], c='blue',alpha = 1,  edgecolor='k')
ax[1].scatter(X_test[:, 0][y_pred_DT == 2], X_test[:, 1][y_pred_DT == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[1].set_xlabel('PC1')
ax[1].set_ylabel('PC2')
ax[1].set_title('Classification Before PCA')
​
​
ax[2].scatter(X_test[:, 0][y_pred_DT_2 == 0], X_test[:, 1][y_pred_DT_2 == 0], c='red',alpha = 1,  edgecolor='k')
ax[2].scatter(X_test[:, 0][y_pred_DT_2 == 1], X_test[:, 1][y_pred_DT_2 == 1], c='blue',alpha = 1,  edgecolor='k')
ax[2].scatter(X_test[:, 0][y_pred_DT_2 == 2], X_test[:, 1][y_pred_DT_2 == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[2].set_xlabel('PC1')
ax[2].set_ylabel('PC2')
ax[2].set_title('Classification After PCA')
​
​
ax[3].scatter(X_test[:, 0][y_pred_DT == 0], X_test[:, 1][y_pred_DT == 0], c='red',alpha = 1,  edgecolor='k')
ax[3].scatter(X_test[:, 0][y_pred_DT == 1], X_test[:, 1][y_pred_DT == 1], c='blue',alpha = 1,  edgecolor='k')
ax[3].scatter(X_test[:, 0][y_pred_DT == 2], X_test[:, 1][y_pred_DT == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[3].set_xlabel('PC1')
ax[3].set_ylabel('PC2')
ax[3].set_title('Classification After LDA')
​
​
ax[4].scatter(X_test[:, 0][y_pred_DT_3 == 0], X_test[:, 1][y_pred_DT_3 == 0], c='red',alpha = 1,  edgecolor='k')
ax[4].scatter(X_test[:, 0][y_pred_DT_3 == 1], X_test[:, 1][y_pred_DT_3 == 1], c='blue',alpha = 1,  edgecolor='k')
ax[4].scatter(X_test[:, 0][y_pred_DT_3 == 2], X_test[:, 1][y_pred_DT_3 == 2], c='yellow',alpha = 1,  edgecolor='k')
ax[4].set_xlabel('PC1')
ax[4].set_ylabel('PC2')
ax[4].set_title('Classification After Kernel-PCA')
plt.show()
​

#----------------------------------------------------------------------------------------------------------------------------------
### Bulk All From past

import pandas as pd;  import numpy as np;   import seaborn as sns ; import matplotlib.pyplot as plt ; import matplotlib.cm as cm
from warnings import filterwarnings ; filterwarnings('ignore') ; np.set_printoptions(suppress = True)
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder; from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans, AgglomerativeClustering, FeatureAgglomeration , DBSCAN
from sklearn.metrics import confusion_matrix,accuracy_score,roc_auc_score,average_precision_score,precision_recall_curve,plot_confusion_matrix
from sklearn.metrics import precision_score,r2_score,explained_variance_score,f1_score,classification_report,silhouette_score,silhouette_samples
from sklearn.linear_model import LogisticRegression; from scipy.cluster.hierarchy import linkage, dendrogram, cophenet
from sklearn.svm import SVC,LinearSVC ; from sklearn.model_selection import GridSearchCV, train_test_split;
from sklearn.decomposition import PCA; from scipy.stats import zscore; from sklearn import datasets
df['ABC']=df['Sex'].astype('object') ; df=df.drop('ABC', axis=1) ; plt.rcParams['figure.figsize'] = [15,8]
df_num = df_cust.drop(['Sex', 'Cust_Number'], axis = 1); fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize=(15, 4))
for variable, subplot in zip(df_num.columns, ax.flatten()):
    sns.boxplot(df_num[variable], ax=subplot)
    
Q1=df.quantile(0.25);Q3=df.quantile(0.75);IQR=Q3-Q1;df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]
# Missing Value Treatment
Total = df_cust.isnull().sum().sort_values(ascending=False) 
Percent = (df_cust.isnull().sum()*100/df_cust.isnull().count()).sort_values(ascending=False)   
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data
# Scale the Data
X_filtered = df_cust[['Cust_Spend_Score', 'Yearly_Income']]
X_norm = StandardScaler(); num_norm = X_norm.fit_transform(X_filtered);X = pd.DataFrame(num_norm, columns = X_filtered.columns)
# Optimal Value of K Using Elbow Plot
wcss  = [];
for i in range(1,21):
    kmeans = KMeans(n_clusters = i, random_state = 10);    kmeans.fit(X);    wcss.append(kmeans.inertia_)
plt.plot(range(1,21), wcss); plt.axvline(x = 5, color = 'red'); plt.title('Elbow Plot', fontsize = 15)
plt.xlabel('No. of clusters (K)', fontsize = 15); plt.ylabel('WCSS', fontsize = 15)
# Optimal Value of K Using Silhouette Score
n_clusters = [2, 3, 4, 5, 6];
for K in n_clusters:
    cluster = KMeans (n_clusters= K, random_state= 10); predict = cluster.fit_predict(X)
    score = silhouette_score(X, predict,random_state= 10);print ("For {} clusters the silhouette score is {})".format(K, score))
# visualize using Silhoette Method   
n_clusters = [2, 3, 4, 5, 6]; X = np.array(X)
for K in n_clusters:
    fig, (ax1, ax2) = plt.subplots(1, 2);                   fig.set_size_inches(18, 7) ;     y_lower = 10
    model = KMeans(n_clusters = K, random_state = 10) ;     cluster_labels = model.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels);   sample_silhouette_values = silhouette_samples(X, cluster_labels)
    for i in range(K):
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i];    ith_cluster_silhouette_values.sort();
        size_cluster_i = ith_cluster_silhouette_values.shape[0] ;         y_upper = y_lower + size_cluster_i;
        color = cm.nipy_spectral(float(i) / K); ax1.fill_betweenx(np.arange(y_lower, y_upper),0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i));    y_lower = y_upper + 10 
    ax1.set_title("Silhouette Plot");    ax1.set_xlabel("Silhouette coefficient");     ax1.set_ylabel("Cluster label")
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--");ax1.set_yticks([]);ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8])
    colors=cm.nipy_spectral(cluster_labels.astype(float)/K); ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30,lw=0,alpha=0.7,c=colors,edgecolor='k')
    centers = model.cluster_centers_
    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50, edgecolor='k')
    ax2.set_title("Clusters");     ax2.set_xlabel("Spending Score");     ax2.set_ylabel("Annual Income")
    plt.suptitle(("Silhouette Analysis for K-Means Clustering with n_clusters = %d" % K), fontsize=14, fontweight='bold')
new_clusters=KMeans(n_clusters=5,random_state=10);new_clusters.fit(X);df_cust['Cluster']=new_clusters.labels_;df_cust.Cluster.value_counts()
sns.countplot(data= df_cust, x = 'Cluster'); plt.title('Size of Cluster', fontsize = 15) ; plt.xlabel('Clusters', fontsize = 15);
plt.ylabel('Number of Customers', fontsize = 15)
plt.text(x = -0.05, y =39, s = np.unique(new_clusters.labels_, return_counts=True)[1][0])
plt.text(x = 0.95, y =24, s = np.unique(new_clusters.labels_, return_counts=True)[1][1])
plt.text(x = 1.95, y =37, s = np.unique(new_clusters.labels_, return_counts=True)[1][2])
plt.text(x = 2.95, y =22, s = np.unique(new_clusters.labels_, return_counts=True)[1][3])
plt.text(x = 3.95, y =81, s = np.unique(new_clusters.labels_, return_counts=True)[1][4])
#Analyze the Clusters
sns.lmplot(x ='Cust_Spend_Score',y ='Yearly_Income',data=df_cust,hue='Cluster',markers=['*',',','^','.','+'],fit_reg=False,size=10)
plt.title('K-means Clustering (for K=5)', fontsize = 15); plt.xlabel('Spending Score', fontsize = 15); plt.ylabel('Annual Income', fontsize = 15)
len(df_cust[df_cust['Cluster']==0]);df_cust[df_cust.Cluster==0].describe();df_cust[df_cust.Cluster==0].describe(include=object);df_prod[df_cust.Cluster == 0].head(10)
len(df_cust[df_cust['Cluster']==1]);df_cust[df_cust.Cluster==1].describe();df_cust[df_cust.Cluster==1].describe(include=object);df_prod[df_cust.Cluster == 1].head(10)
len(df_cust[df_cust['Cluster']==2]);df_cust[df_cust.Cluster==2].describe();df_cust[df_cust.Cluster==2].describe(include=object);df_prod[df_cust.Cluster == 2].head(10)
len(df_cust[df_cust['Cluster']==3]);df_cust[df_cust.Cluster==3].describe();df_cust[df_cust.Cluster==3].describe(include=object);df_prod[df_cust.Cluster == 3].head(10)
len(df_cust[df_cust['Cluster']==4]);df_cust[df_cust.Cluster==4].describe();df_cust[df_cust.Cluster==4].describe(include=object);df_prod[df_cust.Cluster == 4].head(10)
# Hierarchical Clustering
1. Scale the Data; 2 Build the Model; 3 Plot the Dendrogram; 4 Silhouette Score Method
link_mat = linkage(features_scaled, method = 'ward')     
dendro = dendrogram(link_mat)
for i, d, c in zip(dendro['icoord'], dendro['dcoord'], dendro['color_list']):
    x = sum(i[1:3])/2;        y = d[1]; 
    if y > 20:
        plt.plot(x, y, 'o', c=c)
        plt.annotate("%.3g" % y, (x, y), xytext=(0, -5), textcoords='offset points', va='top', ha='center')
plt.axhline(y = 100); plt.title('Dendrogram', fontsize = 15) ; plt.xlabel('Index', fontsize = 15) ; plt.ylabel('Distance', fontsize = 15)
eucli_dist = euclidean_distances(features_scaled) ; dist_array = eucli_dist[np.triu_indices(5192, k = 1)]
coeff, cophenet_dist = cophenet(link_mat, dist_array);     print(coeff)
#using Silhoette Method
K = [2,3,4,5,6]
silhouette_scores = [] 
for i in K:
    model = AgglomerativeClustering(n_clusters = i) 
    silhouette_scores.append(silhouette_score(features_scaled, model.fit_predict(features_scaled))) 
plt.bar(K, silhouette_scores) ;  plt.title('Silhouette Score for Values of K', fontsize = 15)
plt.xlabel('Number of Clusters', fontsize = 15)  ; plt.ylabel('Silhouette Scores', fontsize = 15)
# Retrieve the Clusters
clusters = AgglomerativeClustering(n_clusters=2, linkage='ward') ; clusters.fit(features_scaled) ; df_prod['Cluster'] = clusters.labels_
df_prod.head(); df_prod['Cluster'].value_counts()
# plot the countplot for the cluster size
sns.countplot(data = df_prod, x = 'Cluster') ; plt.title('Size of Cluster', fontsize = 15)
plt.xlabel('Cluster', fontsize = 15) ; plt.ylabel('No. of Products', fontsize = 15)
# plot the scatterplot to visualize the clusters-
sns.scatterplot(x = 'Sales', y = 'Profit', data = df_prod, hue = 'Cluster') ; 
plt.title('Hierarchical Clustering', fontsize = 15) ; plt.xlabel('Sales', fontsize = 15) ; plt.ylabel('Profit', fontsize = 15)
#DBSCAN
model = DBSCAN(eps = 0.8, min_samples = 15) ; model.fit(features_scaled) ; (set(model.labels_));
df_prod['Cluster_DBSCAN'] = model.labels_; df_prod.head() ; df_prod['Cluster_DBSCAN'].value_counts();
# plot the countplot for the cluster size
sns.countplot(data = df_prod, x = 'Cluster_DBSCAN'); plt.title('Size of Cluster', fontsize = 15)
plt.xlabel('Cluster', fontsize = 15); plt.ylabel('No. of Products', fontsize = 15)

sns.lmplot(x='Sales',y='Profit',data=df_prod,hue ='Cluster_DBSCAN',markers=['o','+','^',','],fit_reg = False, size = 12)
plt.title('DBSCABN (eps = 0.8, min_samples = 15) ', fontsize = 15); 
plt.xlabel('Sales', fontsize = 15) ; plt.ylabel('Profit', fontsize = 15)

""")