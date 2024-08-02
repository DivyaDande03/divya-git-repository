import pandas as pd
iris_df = pd.read_csv('iris.csv')
print(iris_df.head(10)) #display first 10 rows
print(iris_df.dtypes) #display datatypes

summary_stats = iris_df.describe()
print(summary_stats) #summary statistics
#mean_sepal_lenght = iris_df.groupby('species')[sepal.lenght'].mean().reset_index()
mean_sepal_length = ['Species', 'mean_sepal_length']
#print("\nMean sepal length for each species:")
print(mean_sepal_length)

#missing_values = iris_df.isnull().sum()
#print("Missing values:\n", missing_values) #missing values

#iris_df.fillna(iris_df.mean(), inplace=True) #replace missing values with the mean of the respective column(if any)
# Identify numeric columns
#numeric_columns = df.select_dtypes(include='number').columns
#df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
# Verify that there are no missing values left
#print("\nMissing values in each column after imputation:")
#print(df.isnull().sum())


# Check for missing values
print("Missing values in each column before imputation:")
print(iris_df.isnull().sum())

# Identify numeric columns
numeric_columns = iris_df.select_dtypes(include='number').columns

# Replace missing values in numeric columns with the mean of each column
iris_df[numeric_columns] = iris_df[numeric_columns].fillna(iris_df[numeric_columns].mean())

# Verify that there are no missing values left
print("\nMissing values in each column after imputation:")
print(iris_df.isnull().sum())

#filtered_by_sepal_length = iris_df[iris_df['sepal_length'] > 5.0]
#print("filtered dataset where sepal length is greater than 5.0:")
#print(filtered_by_sepal_length)

# Filter the dataset to include only rows where the sepal length is greater than 5.0
iris_df_filtered = iris_df[iris_df['Sepal.Length'] > 5.0]
print("Original dataset shape:", iris_df.shape)
print("Filtered dataset shape:", iris_df_filtered.shape)

# Filter the dataset to include only rows of the species 'Setosa'
iris_df_setosa = iris_df[iris_df['Species'] == 'setosa']
print("Original dataset shape:", iris_df.shape)
print("Filtered dataset shape:", iris_df_setosa.shape)

print("Filtered dataset with only rows of the species Setosa:", (iris_df[iris_df['Species'] == 'setosa']).shape)

print(iris_df.groupby('Species')['Petal.Length'].agg(['mean', 'median', 'std']))

print(iris_df['Species'].value_counts())

print(iris_df.groupby('Species')['Petal.Width'].agg(['min', 'max']))

print(iris_df.groupby('Species')['Sepal.Width'].mean().sort_values(ascending=False).head(5))

#scaler = MinMaxScaler()
#iris_df_normalized = iris_df.copy()
#iris_df_normalized[iris_df.columns[:-1]] = scaler.fit_transform(iris_df[iris_df.columns[:-1]])
#print(iris_df_normalized.head())

#sepal_length_percentiles = iris_df.groupby('species')['sepal length (cm)'].quantile([0.25, 0.50, 0.75]).unstack()
#print(sepal_length_percentiles)
#7.1 Calculate the 25th, 50th, and 75th percentiles of sepal length for each species
percentiles = iris_df.groupby('Species')['Sepal.Length'].quantile([0.25, 0.5, 0.75])
print(percentiles)
#7.2 Calculate the range (max - min) of petal length for each species
petal_length_range = iris_df.groupby('Species')['Petal.Length'].agg(['min', 'max']).apply(lambda x: x['max'] - x['min'], axis=1)
print(petal_length_range)

#8

species_info = {
    'setosa': {'habitat': 'Mediterranean regions', 'color': 'Red', 'size': 'Small'},
    'versicolor': {'habitat': 'Alpine meadows', 'color': 'White', 'size': 'Medium'},
    'virginica': {'habitat': 'Coastal regions', 'color': 'Orange', 'size': 'Large'}
}

species_df = pd.DataFrame(species_info).T.reset_index().rename(columns={'index': 'species'})

print(species_df)

#iris_df_merged = pd.merge(iris_df, species_info, on='species')
#print(iris_df_merged.head())

"""def categorize_petal_length(length):
    if length < 2.0:
        return 'small'
    elif 2.0 <= length < 4.0:
        return 'medium'
    else:
        return 'large'
"""
#9.1 Define a custom function to categorize flowers based on petal length
def categorize_flowers(petal_length):
    if petal_length < 3:
       return 'small'
    elif petal_length < 5:
        return 'medium'
    else:
        return 'large'
    
# Apply the custom function to the petal length column
iris_df['flower_size'] = iris_df['Petal.Length'].apply(categorize_flowers)
print(iris_df.head())  

#6.1 Normalize the numerical features
numerical_features = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
for feature in numerical_features:
    iris_df[feature] = (iris_df[feature] - iris_df[feature].min()) / (iris_df[feature].max() - iris_df[feature].min())
print(iris_df.head())
#6.2 Create a new column that is the ratio of petal length to petal width
iris_df['petal_ratio'] = iris_df['Petal.Length'] / iris_df['Petal.Width']
print(iris_df.head())

