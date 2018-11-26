from sympy import isprime,primerange
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
class Cities(object):
    def __init__(self,path):
        self.path=path
        self.cities=pd.read_csv(path)
        self.cities['isPrime']=self.cities.CityId.apply(isprime)
        self.prime_cities=self.cities.loc[self.cities.isPrime]
        self.cities.to_csv(path[:-4]+'_add_isPrime.csv')
        print("loaded all cities!")
    def visualization(self):
        plt.figure(figsize=(16,10))
        plt.subplot(111,adjustable='box',aspect=1.0)
        plt.plot(self.cities.X,self.cities.Y,'k,',alpha=0.3)
        plt.plot(self.cities.X[0],self.cities.Y[0],'bx')
        plt.xlim(0, 5100)
        plt.ylim(0, 3400)
        plt.xlabel('X', fontsize=16)
        plt.ylabel('Y', fontsize=16)
        plt.title('All cities (North Pole = Blue X)', fontsize=18)
        plt.savefig('../data/all cities figure.png')
        plt.show()

        plt.figure(figsize=(16, 10))
        plt.subplot(111, adjustable='box', aspect=1.0)
        plt.plot(self.prime_cities.X, self.prime_cities.Y, 'k,', alpha=0.3)
        plt.plot(self.cities.X[0], self.cities.Y[0], 'bx')
        plt.xlim(0, 5100)
        plt.ylim(0, 3400)
        plt.xlabel('X', fontsize=16)
        plt.ylabel('Y', fontsize=16)
        plt.title('All cities (Primes = Red Dots, North Pole = Blue X)', fontsize=18)
        plt.savefig('../data/all cities(prime city) figure.png')
        plt.show()

if __name__=="__main__":
    m=Cities("../data/cities.csv")
