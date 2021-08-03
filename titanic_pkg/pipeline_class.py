from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.compose import make_column_selector as selector
from sklearn.impute import SimpleImputer

from titanic_pkg.preprocessing import Preprocessing
from titanic_pkg.data import Data


class PipelineClass():

    def __init__(self):
        self.df_titanic = Data().lecture_df()
        self.X_train, self.X_test, self.y_train, self.y_test = Preprocessing().select_x_y()


    def creation_pipeline(self):
        numeric_transformer = Pipeline(steps=[('scaler', RobustScaler())])

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))])

        preprocessor = ColumnTransformer(transformers=[
            ('num', numeric_transformer, selector(dtype_include=["int", "float"])),
            ('cat', categorical_transformer, selector(dtype_exclude=["int", "float"]))
        ],remainder='passthrough')

        reg = Pipeline(steps=[('preprocessor',
                            preprocessor), ('regressor', RandomForestClassifier())])

        return reg

    def fit_predict(self):
        reg = self.creation_pipeline()
        reg.fit(self.X_train, self.y_train)
        y_pred = reg.predict(self.X_test)
        return y_pred

    def fit_score(self):
        reg = self.creation_pipeline()
        reg.fit(self.X_train, self.y_train)
        score = reg.score(self.X_test, self.y_test)
        return score
