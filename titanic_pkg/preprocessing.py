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
        # return self.df_titanic

    def fill_na_age(self):
        age_mean = self.df_titanic.groupby('who').age.mean()
        self.df_titanic['age'] = self.df_titanic['age'].replace(np.nan, 'YES')

        for i in range(len(self.df_titanic.age)):
            if self.df_titanic.age[i] == 'YES':
                if self.df_titanic.who[i] == 'child':
                    self.df_titanic.age[i] = age_mean.child
                elif self.df_titanic.who[i] == 'man':
                    self.df_titanic.age[i] = age_mean.man
                else:
                    self.df_titanic.age[i] = age_mean.woman
        # return self.df_titanic

    def change_type_category(self):
        self.df_titanic[['survived', 'pclass']] = self.df_titanic[['survived',
                                                 'pclass']].astype('category')
        # return self.df_titanic

    def select_x_y(self):
        self.drop_columns()
        self.fill_na_age()
        self.change_type_category()
        y = self.df_titanic["survived"]
        X = self.df_titanic.drop(["survived"], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        return X_train, X_test, y_train, y_test
