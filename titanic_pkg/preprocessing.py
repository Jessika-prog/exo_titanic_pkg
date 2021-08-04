from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from titanic_pkg.data import Data


class Preprocessing():


    def __init__(self):
        self.df_titanic = Data().lecture_df()

    def drop_columns(self):
        self.df_titanic = self.df_titanic.drop(['alive', 'deck', 'embark_town', 'class', 'adult_male', 'sibsp', 'parch'],
        axis=1)

    def fill_na_age(self):
        the_who = ['child','man','woman']
        for i in the_who :
            self.df_titanic.loc[self.df_titanic.who ==i,'age']= self.df_titanic.loc[self.df_titanic.who ==i,'age'].fillna(self.df_titanic.loc[self.df_titanic.who ==i,'age'].mean())


    def change_type_category(self):
        self.df_titanic[['survived', 'pclass']] = self.df_titanic[['survived',
                                                 'pclass']].astype('category')

    def select_x_y(self):
        self.drop_columns()
        self.fill_na_age()
        self.change_type_category()
        y = self.df_titanic["survived"]
        X = self.df_titanic.drop(["survived"], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        return X_train, X_test, y_train, y_test
