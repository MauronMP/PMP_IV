from enum import Enum
 
class Regression_algorithm(Enum):
    Lasso = 'Lasso'
    Ridge = 'Ridge'
    RandomForestRegressor = 'RandomForestRegressor'
    KNeighborsRegressor = 'KNeighborsRegressor'