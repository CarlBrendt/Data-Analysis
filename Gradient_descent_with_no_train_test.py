import pandas as pd
import math
from sklearn import linear_model
import numpy as np

def predict_using_sklearn():
    test_scores = pd.read_csv(r'C:\Users\Polina\Desktop\Python\Pandas\test_scores.csv')
    reg = linear_model.LinearRegression()
    reg.fit(test_scores[['math']], test_scores.cs)
    return reg.coef_, reg.intercept_

def gradient_descent(x,y):
    m_curr=b_curr=0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002
    cost_previous = 0
    for i in range(iterations):
        y_predicted = m_curr*x + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y -y_predicted)
        m_curr = m_curr- learning_rate*md
        b_curr = b_curr - learning_rate*bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        return m_curr, b_curr
    
if __name__ == '__main__':
    
    df = pd.read_csv(r"C:\Users\Polina\Desktop\Python\Pandas\test_scores.csv")
    x = np.array(df.math)
    y = np.array(df.cs)

    m, b = gradient_descent(x,y)
    print("Using gradient descent function: Coef {} Intercept {}".format(m, b))

    m_sklearn, b_sklearn = predict_using_sklearn()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))