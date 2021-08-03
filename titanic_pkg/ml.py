from titanic_pkg.preprocessing import Preprocessing
from titanic_pkg.data import Data
from titanic_pkg.pipeline_class import PipelineClass

class ML:
    def __init__(self) :
        self.df_titanic = Data().lecture_df()
        self.X_train, self.X_test, self.y_train, self.y_test = Preprocessing().select_x_y()
        self.reg = PipelineClass().creation_pipeline()

    def fit_predict(self):
        self.reg.fit(self.X_train, self.y_train)
        y_pred = self.reg.predict(self.X_test)
        return y_pred

    def fit_score(self):
        self.reg.fit(self.X_train, self.y_train)
        score = self.reg.score(self.X_test, self.y_test)
        return score
