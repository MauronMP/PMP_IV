from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from pmp_iv.forest_prediction.eda import *
from sklearn.model_selection import train_test_split
from pmp_iv.enums.regression_algorithm import *

class model_building():
    
    def __init__(self):
        self.data_csv = EDA()
        X = EDA().weather()
        Y = EDA().by_property('area')
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,Y,test_size=0.20,shuffle=True,random_state=1)
        
    def scaler_standard(self, X_train, X_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
    
        return X_train_scaled, X_test_scaled
           
    def regresion_todos(self):
        X_train_scaled, X_test_scaled = self.scaler_standard(self.X_train, self.X_test)
        rSquare_mae = []
        
        for i_regresion in (Lasso(), Ridge(), RandomForestRegressor(), KNeighborsRegressor()):
            i_regresion.fit(X_train_scaled, self.y_train)
            i_regresion_prediccion = i_regresion.predict(X_test_scaled)
            mae = mean_absolute_error(self.y_test, i_regresion_prediccion)
            r2 = r2_score(self.y_test, i_regresion_prediccion)
            rSquare_mae.append([r2,mae])
            
        j = 0
        for i in Regression_algorithm:
            rSquare_mae[j].append(i.value)
            j+=1
            
        return rSquare_mae
    
    def get_best_results(self):
        listado_resultados = self.regresion_todos()
        listado_resultados = sorted(listado_resultados, key = lambda x: (-x[0]))
        return listado_resultados[0][2]