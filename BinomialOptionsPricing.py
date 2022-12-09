#BinomialPricingModel
import numpy as np


def BinomialPricingModel(S, T, K, sigma, r, n, option_type):

    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = np.exp(-sigma * np.sqrt(dt))
    #d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)


    stock= np.zeros([n+1, n+1])

    for i in range(n+1):
        for j in range(i+1):
            stock[j, i] = S * (u ** (i - j)) * (d ** j)


    option_val = np.zeros([n+1,n+1])

    if option_type == "call":
        option_val[:,n] = np.maximum(np.zeros([n+1]), stock[:,n] - K)
    elif option_type =="put":
        option_val[:,n] = np.maximum(K-np.zeros([n+1], np.zeros([n+1])))
    

  

    for i in range(n-1,-1,-1):
        for j in range(i+1):
            option_val[j,i] = np.exp(-r * dt) * (p * option_val[j,i+1] + (1-p) * option_val[j+1,i+1])
    return option_val[0,0]
        


if __name__ == "__main__":
    print("Calculating example option price:")
    value = BinomialPricingModel(100, 1, 105, 0.2, 0.05, 50,"call")
    print(value)   
    



