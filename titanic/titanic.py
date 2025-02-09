# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %% [markdown]
# # 1. Citire data frames si explorare

# %%
train_df = pd.read_csv("titanic/train.csv", index_col=0)
test_df = pd.read_csv("titanic/test.csv", index_col=0)
test_df.keys().size, train_df.keys().size

# %%
test_target_df = pd.read_csv("titanic/gender_submission.csv")
test_target_df

# %%
train_df.head(10)

# %%
features_train = train_df
features_train['Gender'] = features_train['Sex'] == 'male'
features_train = features_train.drop("Sex", axis=1)
features_train 

# %%
features_train = features_train.drop(columns=["Name", "Ticket"], axis=1) #, "Fare", 
features_train

# %%


# %%
features_train[features_train["Embarked"].isna()]

# %%
features_train["Cabin"].unique()

# %%
def first_letter(row):
    return str(row['Cabin'])[0].upper()

features_train["Cabin_short"] =  features_train.apply(first_letter, axis=1)
features_train = features_train.drop(columns="Cabin", axis=1)
features_train

# %%
features_train['Cabin_short'].unique(), features_train['Cabin_short'].nunique()

# %%
from sklearn.preprocessing import LabelEncoder, LabelBinarizer

# %%
transformer = LabelEncoder()

# %%
transformer

# %%
features_train['New_Cabin'] = transformer.fit_transform(features_train['Cabin_short'])

# %%
features_train['New_Cabin'].nunique()

# %%
binarizer_transformer = LabelBinarizer()
binarizer_transformer

# %%
# binarizer_transformer.fit_transform(features_train['Cabin_short'])
# features_train['Cabin_short'].shape

# %%
new_transformer = LabelEncoder()

# %%
features_train["New_Embarked"] = new_transformer.fit_transform(features_train["Embarked"])

# %%
features_train = features_train.drop(columns=["Cabin_short", "Embarked"], axis=1)
features_train

# %%
sns.heatmap(features_train.corr(),cmap="coolwarm")

# %%
features_train[features_train['Age'].isna() != False]

# %%
features_train["Age"].fillna(features_train["Age"].mean(), inplace=True)

# %%
features_train

# %%
from sklearn.neighbors import KNeighborsClassifier

# %%
model = KNeighborsClassifier()
model

# %%
features_train.count()

# %%
target_train = features_train["Survived"]
target_train.count()

# %%
features_train =  features_train.drop(columns=["Survived"])
features_train.head(2)

# %%
model.fit(features_train, target_train)