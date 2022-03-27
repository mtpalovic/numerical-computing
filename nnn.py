#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import random
random.seed(43)


import matplotlib.pyplot as plt


# In[4]:


np.random.seed(43)
a = np.random.randn(1000,4)
a


# In[5]:


np.random.seed(43)
b = np.random.randn(1000,4)
b


# In[6]:


np.random.seed(43)
c = np.random.randn(1000,1)
c


# In[31]:


class nn(object):
    """
    Class constructor.
    """
    def __init__(self,x0:np.ndarray,y0:np.ndarray,lr:float=0.001,n_iters:int=1000):
        """
        Constructor method.
        """
        self.x0 = x0
        self.y0 = y0
        assert(type(x0)==np.ndarray and type(y0)==np.ndarray)
        
        
        
        self.lr = lr
        self.n_iters = n_iters
        
        
        self.m, self.n = np.shape(self.x0)[0], np.shape(self.x0)[1]
    
        self.w = None
        self.b = None
        
        
    
        
    def init_params(self):
        w = np.random.randn(self.n,1)
        b = 0
        
        return w,b
    
    
    
    
    def sigmoid(self,z):
        """Non-linear activation function.
        :return: 
        :rtype: 
        """
        return 1/(1+np.exp(-z))
    
    
    
    
    def forward_propagate(self):
        
        self.w,self.b = self.init_params()
        
        if np.shape(self.x0)[1] == np.shape(self.w)[0]:
            
            
            A = self.sigmoid(np.matmul(self.x0,self.w)+self.b)
        
            cost = (-1/self.m)*np.sum(self.y0*np.log(A)+(1-self.y0)*(np.log(1-A)))
            
            
            d_w = (1/self.m)*np.matmul(self.x0.T,(A-self.y0))
            d_b = (1/self.m)*np.sum(A-self.y0)
        
            
            gradients = {
                "d_w":d_w,
                "d_b":d_b
                }
        
        else:
            
            print(f"{np.shape(self.x0)[1]} not equal to {np.shape(self.w)[0]}")
        
        
        
        return cost, gradients
    
    
    
    def fwd_propagate(self):
        
        h = np.zeros((1000,1))
        
        for i in range(len(self.x0)):
        
            for j in range(len(self.w[0])):
        
                for k in range(len(self.w)):
        
                    h[i][j] += self.x0[i][k]*self.w[k][j]
        
        B = self.sigmoid(h + self.b)
        
        
        
        c_m = 0
        for z in range(self.m):
            c_m += (self.y0[z]*np.log(B[z])+(1-self.y0[z])*(np.log(1-B[z])))
        
        cost = (-1/self.m)*c_m
        cost = float(cost)
        
        
        
        
        d_w1 = (1/self.m)*np.matmul((self.x0).T,(B-self.y0))
        
        d_b1 = 0
        for e in range(self.m):
            d_b1 += (1/self.m)*np.sum(B[e]-self.y0[e])
        
        gradients = {
                "d_w1":d_w1,
                "d_b1":d_b1
            }
        
        return cost, gradients
    
    
    
    
    def gradient_descent(self):
        """The below functions runs gradient descent.
        :return: Optimal parameters w,b
        :rtype: np.array
        """
        
        costs = self.create_array()
        
        for i in range(self.n_iters):
            c,g = self.forward_propagate()
            
            self.w = self.w - self.lr*g["d_w"]
            self.b = self.b - self.lr*g["d_b"]
    
            costs.append(c)
            if i % 100 ==0:
                print("Costs after iter %i: %f"%(i,c))
        
        params = {
            "w": self.w,
            "b": self.b
            }
        
        return params


# In[32]:


neural_nets = nn(a,c,0.001,1000)
neural_nets.forward_propagate()


# In[22]:


np.shape(neural_nets.x0)[1]


# In[24]:


neural_nets.forward_propagate()


# In[25]:


neural_nets.fwd_propagate()


# In[26]:


neural_nets.gradient_descent()


# In[ ]:





# In[ ]:




