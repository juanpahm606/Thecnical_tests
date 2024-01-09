import numpy as np
class LinearRegression():
    def __init__(self):
        self.w=np.random.rand() 
        self.b=np.random.rand() 
        self.history=np.zeros(90000)
    def loss_function(self,x,y):
        chi_cuadrado=0
        for i in range(len(x)):
            chi_cuadrado=(1/len(x))*(0.5*((self.b+self.w*x[i])-y[i])**2)
            #print(chi_cuadrado)
        #print(chi_cuadrado)
        return chi_cuadrado
    def grad(self,x,y):
        grad_b=0
        grad_w=0
        for i in range(len(x)):                                
            grad_b+=(self.b+self.w*x[i]-y[i])*(2/len(x))
            grad_w+=(self.b+self.w*x[i]-y[i])*x[i]*(2/len(x))
        return grad_b,grad_w
    def optimizer(self,grad_b,grad_w):
        self.b=self.b-0.001*grad_b
        self.w=self.w-0.001*grad_w
        return self.b,self.w
    def fit(self,x,y):
        #b=0
        #w=0
        epochs=90000
        for i in range(1,epochs):
            self.loss_function(x,y)
            chi_cuadrado=self.loss_function(x,y)
            self.history[i]=chi_cuadrado
            self.grad(x,y)
            grad_b,grad_w=self.grad(x,y)
            self.optimizer(grad_b,grad_w)
        return self.b,self.w
    def predict(self,x,y,b,w):
        #X=np.arange(0.1,10, 0.1)
        Y=np.zeros(len(x))
        #epochs=30000
        #self.b, self.w=self.fit(x,y)
        for i in range(len(x)):
            Y[i]=w*x[i]+b
        self.Y=Y
        return self.Y
    def score(self,y,Y):
        return 1-(np.sum((self.Y-y)**2))/(np.sum((self.Y-np.mean(self.Y))**2))

pass