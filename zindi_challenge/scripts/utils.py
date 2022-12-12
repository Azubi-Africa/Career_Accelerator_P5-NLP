import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
# preprocessing.OneHotEncoder, preprocessing.StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import compose # ColumnTransformer
# Config
from zindi_challenge.scripts.config import *
# Models
from sklearn import linear_model 
from sklearn import svm 
from sklearn import ensemble 

#######################################################################

# DATA GATHERING
## Needed functions

## Main function
def data_gathering():
    """This function will load and aggregate all the data then will output a pandas DataFrame
    """
    list_of_dataframes = [] # to store temporarily the loaded Dframes to later concat them
    list_of_csv_filepaths = []
    # list_of_json_filepaths = [] #uncomment if needed, Add other variables below if needed

    # Load CSV files
    for fp in list_of_csv_filepaths:
        df = pd.read_csv(fp)
        list_of_dataframes.append(df)


    # Load other files (Json, txt, etc)
    ## Do like above. you can load manually if some files need special arguments, during loading.
    ## You may write loading functions at the section `## Needed functions` and call them here.



    # Concatenate all the dataframes
    global_df = pd.concat(list_of_dataframes, axis=0)

    return global_df


# PROCESSING
## Needed functions
def remove_rows_with_Nan(data):
    """
    """
    return data[ ~data.isna().any(axis=1) ]


## Main function
def processing(dataset:pd.DataFrame = data_gathering()):
    """This function will process the dataset then return a dataset ready-for-modelling
    """

    numerical_cols = dataset.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = dataset.select_dtypes(exclude=np.number).columns.tolist()

    # categorical_attributes = list(forest_fire.select_dtypes(include=['object']).columns)
    # numerical_attributes = list(dataset.select_dtypes(include=['float64', 'int64']).columns)

    num_pipeline = Pipeline([('imputer', SimpleImputer(strategy='median')),
                            ('drop_attributes', AttributeDeleter()),
                            ('std_scaler', preprocessing.StandardScaler()),
                            ])
    full_pipeline = compose.ColumnTransformer([('num', num_pipeline, numerical_attributes),
                                    ('cat', OneHotEncoder(), categorical_attributes),
                                    ])

    train = full_pipeline.fit_transform(dataset)
    
    columns_to_keep = []
    df_dataset_processed = None
    return df_dataset_processed[columns_to_keep]


# MODELLING
## Needed functions

## Main function
def modelling(y_col):
    """This function will take training data as input then return train models
    """
    # Use the processing function to retrieve the processed dataset
    df_dataset_processed = processing()

    # Separate X and y
    X, y = df_dataset_processed.drop(columns=y_col) ,df_dataset_processed[y_col]
    
    # Instantiate ML models

    # Train ML models
    model = linear_model.LogisticRegression().fit(X, y)
    return model