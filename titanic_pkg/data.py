import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Data:

    def lecture_df(self):
        self.df_titanic = sns.load_dataset('titanic')
        return self.df_titanic

    def viz_info(self):
        self.lecture_df()
        self.df_titanic.info()
        return self.df_titanic.describe()

    def viz_barplot(self):
        self.lecture_df()
        return sns.barplot(data=self.df_titanic, x='sex', y='survived')

    def viz_distplot(self):
        self.lecture_df()
        return sns.distplot(self.df_titanic['age'])
