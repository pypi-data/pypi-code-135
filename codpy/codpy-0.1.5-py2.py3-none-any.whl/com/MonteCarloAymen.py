import abc
from cmath import isinf
import numpy as np
# from regex import F
from codpy_tools import *
from mapping import *
import openturns as opt
from scipy.optimize import linear_sum_assignment
import ot
from scipy.stats import qmc

class StochasticProcess(abc.ABC):
    @abc.abstractmethod
    def get_process(self,**kwargs):
        pass


class path_generator(abc.ABC):
    def __init__(self,**kwargs):
        pass
    def get_param(**kwargs): return kwargs.get('path_generator')
    @abc.abstractmethod
    def generate(self,N,payoff,**kwargs):
        pass

    def get_process(**kwargs) : return path_generator.get_param(**kwargs).get('process')
    def get_D(**kwargs) : return path_generator.get_process(**kwargs).get_process(**kwargs).factors()



class payoff(abc.ABC):
    @abc.abstractmethod
    def f(self,x):
        pass
    @abc.abstractmethod
    def get_times(self,**kwargs):
        pass

class pricer(abc.ABC):
    @abc.abstractmethod
    def price(self,**kwargs):pass
    def nabla(self,**kwargs):return FD.nabla(fun = self.price, **kwargs)
    def hessian(self,**kwargs):return FD.hessian(fun = self.price, **kwargs)

    def nablas(self, values,**kwargs): 
        out = get_matrix(FD.nablas(values = values,fun = self.price, **kwargs))
        return out

    def hessians(self, values,**kwargs): 
        out = FD.hessians(fun = self.price,values = values,**kwargs)
        return out
    def prices(self,set_fun, values,**kwargs): 
        copy_kwargs = copy.deepcopy(kwargs)
        def helper(v): 
            k = set_fun(v,**copy_kwargs)
            return self.price(**k) 
        if isinstance(values,list): out = [helper(v) for v in get_matrix(values)]
        elif isinstance(values,np.ndarray): out = [helper(values[n]) for n in range(0,values.shape[0]) ]
        elif isinstance(values,pd.DataFrame): return self.prices(set_fun, values.values,**copy_kwargs)
        out = np.array(out)

        return out
    def pnls(self,set_fun, x,z,**kwargs): 
        left = self.prices(set_fun, x,**kwargs)
        right = self.prices(set_fun, z,**kwargs)
        pnls = right[:min(len(left),len(right))] - left[:min(len(left),len(right))]

        # from QL_tools import BasketOptionClosedFormula
        # spot = BasketOptionClosedFormula.get_spot_basket(x= z[:,1:],**kwargs)
        # spot,toto,p = lexicographical_permutation(spot,pnls.copy())
        # plt.plot(spot,toto)
        # plt.show()

        # grad = op.nabla(x=x[:,:,0], y=x[:,:,0], z=x[:,:,0], fx=pnls, rescale = True,**kwargs)

        return pnls

class MonteCarloPricer(pricer):

    def get_params(**kwargs) :  return kwargs.get('MonteCarloPricer',{})
    def get_N(**kwargs): return MonteCarloPricer.get_params(**kwargs)['N']

    def price(self,payoff,generator,**kwargs):
        N = MonteCarloPricer.get_N(**kwargs)
        x=generator.generate(N=N,payoff=payoff,**kwargs)
        if isinstance(generator,historical_path_generator): y=payoff.f(x[:,1:,:])
        else:  y=payoff.f(x)
        return np.mean(y)

def optimal_reorder(X,**kwargs):
    from scipy import stats
    type_of_x = kwargs['type']
    Y = X.copy() 
    if type_of_x == 'low':
        # sequence=opt.SobolSequence(X.shape[1]-1) 
        # sequence=opt.HaltonSequence(X.shape[1]-1)
        sequence=opt.FaureSequence(X.shape[1]-1)
        # sequence=opt.ReverseHaltonSequence(X.shape[1]-1)
        # sequence=opt.HaselgroveSequence(X.shape[1]-1) 
        uniformSequence = np.array(sequence.generate(X.shape[2])).T

        # N = X.shape[2]
        # uniformSequence = np.array([i/N +1/(2*N) for i in range(N)]).reshape((N,1)).T
        # np.random.shuffle(uniformSequence)
    else:
        uniformSequence=np.random.rand(X.shape[0],X.shape[1]-1,X.shape[2])
        np.random.shuffle(uniformSequence)
    Y[0,1:,:]=uniformSequence
    C = ot.dist(X[0,1:,:].T, Y[0,1:,:].T)
    permutation = linear_sum_assignment(C, maximize=False)
    new_Y = Y[0,1:,:].T[permutation[1]]
    Y[0,1:,:]=new_Y.T
    return Y


class historical_path_generator(path_generator):

    def generate_from_samples(self,samples,sample_times,**kwargs):
        def generate_from_samples_dataframe(samples,sample_times,**kwargs):
            pd_samples = np.ndarray((1,samples.shape[1],samples.shape[0]))
            pd_samples[0,0,:] = samples.Date
            pd_samples[0,1:,:] = samples.loc[:,samples.columns != "Date"].T
            out = generate_from_samples_np(pd_samples,sample_times,**kwargs)
            return out
        def generate_from_samples_np(samples,sample_times,**kwargs):
            from QL_tools import option_param_getter
            getter = kwargs.get('getter',option_param_getter())
            seed=kwargs.get("seed",np.random.randint(low = 0,high = 1e+8))
            seed = 4
            grid_projection = kwargs.get("grid_projection",True)
            np.random.seed(seed)
            mapping = kwargs.get("map",None)
            N = option_param_getter.get_N(**kwargs)
            D = samples.shape[1]-1
            mapped_samples=np.zeros((samples.shape[0],samples.shape[1],samples.shape[2]-1))
            if mapping is not None: 
                time_list = list(set(samples[:,0,:].flatten()))
                time_list.sort()
                mapped_samples[:,0,:] = samples[:,0,1:]
                mapped_samples[:,1:,:] = mapping(samples[:,1:,:],**kwargs, times = time_list)[:,:,1:]
                mean = 0
                
            payoff_times=get_float(sample_times)
            projected_samples = optimal_reorder(mapped_samples,**kwargs)
            # random_samples = np.zeros((N,D+1,len(payoff_times)))
            # random_samples[:,0,:] = np.array(payoff_times)
            # random_samples[:,1:,:] = np.random.rand(N,D,len(payoff_times))            
            
            # Modified random samples: We generate N samples for each asset
            random_samples = np.zeros((N,D+1))
            random_samples[:,0] = list(range(1, N+1))
            random_samples[:,1:] = np.random.rand(N,D)      
            # if (grid_projection):
            #     random_samples[:,1:,:] = alg.grid_projection(random_samples[:,1:,:])

            x = format_32(projected_samples)
            z = random_samples
            fx = format_32(mapped_samples)

            f_z = np.zeros((z.shape[0],fx.shape[1]))
            f_z[:,:] = op.projection(x = x[:,:],y = x[:,:],z = z[:,:], fx = fx[:,:],**kwargs)
            # f_z[:,1:] = op.projection(x = x[:,1:],y = x[:,1:],z = z[:,1:], fx = fx[:,1:],**kwargs)
            f_z[:,0] = z[:,0]

            # f_z = format_23(f_z,random_samples.shape)
            # if mapping is not None: 
            #     time_start = get_float(kwargs.get('time_start',getter.get_today_date(**kwargs)))
            #     time_start = payoff_times[0]
            #     payoff_times.insert(0,time_start)
            #     f_z[:,1:,:] = inverse(mapping)(f_z[:,1:,:],**kwargs, times = payoff_times,mean=mean, initial_values = getter.get_spot(**kwargs))
            return f_z,fx
            
        import pandas 
        generate_from_samples_switchDict = { pandas.core.frame.DataFrame: generate_from_samples_dataframe }
        type_debug = type(samples)
        method = generate_from_samples_switchDict.get(type_debug,generate_from_samples_np)
        return method(samples,sample_times,**kwargs)

    def generate(self,N,payoff,time_list=None,**kwargs):
        historical_generator = kwargs.get("historical_generator",None)
        samples = historical_generator.generate(**kwargs)
        if time_list is None: time_list = payoff.get_times(**kwargs)
        return self.generate_from_samples(samples=samples,sample_times=time_list,**kwargs)



class Recurrent_historical_path_generator(historical_path_generator):
    def generate_from_samples(self,samples,sample_times,**kwargs):
        h=kwargs.get('h',5)
        p=kwargs.get('p',0)
        samples,fx=preprocess(samples,h,p)
        # samples = split(samples,h)
        return super().generate_from_samples(samples,sample_times,**kwargs)

def remove_mean(A):
    mean = np.mean(A[:,1,:])
    A[:,1,:] = A[:,1,:] - mean
    return A,mean

def split(A,h):
    out=np.zeros((int(A.shape[2]/h),A.shape[1],h))
    for i in range(int(A.shape[2]/h)):
        out[i,:,:]=A[0,:,i*h:(i+1)*h]
    return out

def preprocess(A,h,p):
    
    D = A.shape[1]
    New_N = A.shape[0]*(A.shape[2]-h-p)+1
    out_x = np.zeros((New_N,D,h))
    out_fx = np.zeros((New_N,D,p))

    for i in range(D):
        out_x[:,i,:],out_fx[:,i,:]=ts_format(A[0,i,:],h,p)
    
    return out_x,out_fx

