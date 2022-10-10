import jax.numpy as np
from jax.lax import cond
from jax import custom_jvp
import jax
from functools import partial

def t_is_inf_aT(t,aT,T):
    return t-(t//T)*T<aT

def t_is_sup_aT(t,aT,T):
    return t-(t//T)*T>=aT

def fonction(res):
    return lambda _: res

def vect_temporel(debut,fin,pas):
    return np.linspace(debut,fin,int((fin-debut)/pas))

def indice_t(t,pas,debut=0.):
    return ((t-debut)/pas).astype(int)

def init_val(condition,s,ind,valeur):
    ind=ind[0:-1]
    s[ind]=cond(condition,lambda s:valeur,lambda s:s,s[ind])
    return s

###################################################### external functions
@partial(custom_jvp,nondiff_argnums=(1,2))
def compute_external(inputs,len_output,Extfunc):
    output_type=jax.ShapeDtypeStruct((len_output,),'float64')
    def compute_intermediary_function(inputs):
        outputs=Extfunc.compute(inputs)
        return np.array(outputs)
    outputs=jax.pure_callback(compute_intermediary_function,output_type,inputs)
    return outputs

def jacobien(len_output,Extfunc,primals,tangents):
    inputs,=primals
    dinputs,=tangents
    output_type=jax.ShapeDtypeStruct((len_output,),'float64')
    def compute_intermediary_function(inputs):
        outputs=Extfunc.compute(inputs)
        return np.array(outputs)
    def jacobian_intermediary_function(inputs):
        gradients=Extfunc.jacobian(inputs)
        return np.array(gradients)
    outputs=jax.pure_callback(compute_intermediary_function,output_type,inputs)
    gradient_type=jax.ShapeDtypeStruct((len_output,len(inputs)),'float64')
    gradients=jax.pure_callback(jacobian_intermediary_function,gradient_type,
                                inputs)
    return outputs,np.dot(gradients,dinputs)

compute_external.defjvp(jacobien)
#####################################################