import jax.numpy as np
from jax.lax import *
from jax import custom_jvp,jvp
from functools import partial
import types,jax

def odeint45(f,y0,t,*args,h0=1e-5,param_T=(0.,0.),event=[],tol=1.48e-8):
    return _odeint45(f,event,h0,param_T,tol,y0,t,*args)


def rk_step(y_prev, t_prev, h,f,*args):
    k1=f(y_prev, t_prev,*args)
    if isinstance(y_prev,dict):
        k2 = f({i:y_prev[i] + h*0.2 * k1[i] for i in k1.keys()}, t_prev + 0.2*h,
           *args)
        k3 = f({i:y_prev[i] + h*(3 *k1[i] + 9 * k2[i]) / 40 for i in k1.keys()},
           t_prev + 3 * h / 10,*args)
        k4 = f({i:y_prev[i] + h*(44 * k1[i] / 45 - 56 * k2[i] / 15 +32*k3[i]/ 9)
            for i in k1.keys()},t_prev + 4 * h / 5,*args)
        k5 = f({i:y_prev[i] + h*(19372 * k1[i] / 6561 - 25360 * k2[i] / 2187 +
            64448 * k3[i] / 6561- 212 * k4[i] / 729) for i in k1.keys()},
           t_prev + 8 * h / 9,*args)
        k6 = f({i:y_prev[i] + h*(9017 * k1[i] / 3168 - 355 * k2[i] / 33 +
            46732 * k3[i] / 5247 +49 * k4[i] / 176 - 5103 * k5[i] / 18656)
            for i in k1.keys()},t_prev + h,*args)
        k7 = f({i:y_prev[i] + h*(35 * k1[i] / 384 + 500 * k3[i] / 1113 +
            125 * k4[i] / 192 -2187 * k5[i] / 6784 + 11 * k6[i] / 84)
            for i in k1.keys()},t_prev + h,*args)

        y = {i:y_prev[i] + h *(35 * k1[i] / 384 + 500 * k3[i] / 1113 +
            125 * k4[i] / 192 -2187 * k5[i] / 6784 + 11 * k6[i] / 84)
            for i in k1.keys()}
        yest = {i:y_prev[i] + h *(5179 * k1[i] / 57600 + 7571* k3[i] / 16695 +
            393 * k4[i] / 640- 92097 * k5[i] / 339200 + 187 * k6[i] / 2100 +
            k7[i] / 40) for i in k1.keys()}
    else:
        k1=f(y_prev, t_prev,*args)
        k2 = f(y_prev + h*0.2 * k1, t_prev + 0.2 * h,*args)
        k3 = f(y_prev + h*(3 * k1 + 9 * k2) / 40,t_prev + 3 * h / 10,*args)
        k4 = f(y_prev + h*(44 * k1 / 45 - 56 * k2 / 15 + 32 * k3 / 9),t_prev +
           4 * h / 5,*args)
        k5 = f(y_prev + h*(19372 * k1 / 6561 - 25360 * k2 / 2187 +
            64448 * k3 / 6561- 212 * k4 / 729),
           t_prev + 8 * h / 9,*args)
        k6 = f(y_prev + h*(9017 * k1 / 3168 - 355 * k2 / 33 + 46732 * k3 / 5247+
            49 * k4 / 176 - 5103 * k5 / 18656),t_prev + h,*args)
        k7 = f(y_prev + h*(35 * k1 / 384 + 500 * k3 / 1113 +
            125 * k4 / 192 -2187 * k5 / 6784 + 11 * k6 / 84),t_prev + h,*args)

        y = y_prev + h *(35 * k1 / 384 + 500 * k3 / 1113 + 125 * k4 / 192
             -2187 * k5 / 6784 + 11 * k6 / 84)
        yest = y_prev + h *(5179 * k1 / 57600 + 7571* k3 / 16695 + 393 * k4 /640
            - 92097 * k5 / 339200 + 187 * k6 / 2100 + k7 / 40)
    t_now = t_prev + h
    return y, yest, t_now


def optimal_step(y,yest,h,tol,errcon=1.89e-4):
    if isinstance(y,dict):
        est=np.linalg.norm(np.array(list(y.values()))-
                           np.array(list(yest.values())))
    else:
        est=np.linalg.norm(y-yest)
    R = (est+1e-16) / h
    err_ratio = R / tol
    delta = (2*err_ratio)**(-0.2)
    h=np.where(est>=errcon,h*delta,1.0*h)
    return h

def envoyer_pdi(t,duree,periode):
    tpdi= cond(t-(t//periode)*periode<duree,lambda t:duree+(t//periode)*periode,
               lambda t:((t//periode)+1)*periode,t)
    return tpdi

def prediction(t,tprev,val_seuil,output,outputprev):
    return t+(t-tprev)*(val_seuil-output)/(output-outputprev)

def interpolation(state):
    y,h,y_prev,t_prev,t_now,output,outputprev=state
    tchoc=(-t_prev*output+t_now*outputprev)/(outputprev-output)
    h=tchoc-t_prev
    ychoc={i:(y_prev[i]-y[i])*tchoc/(t_prev-t_now)+(t_prev*y[i]-t_now*y_prev[i])
             /(t_prev-t_now) for i in y.keys()}
    return ychoc,h,y_prev,t_prev,tchoc,output,outputprev

def GetTimeofNextVarHit(t,tprev,output,y,y_prev,duree,periode):
    tevent=envoyer_pdi(t,duree,periode)
    for i in output.keys():
        temp=prediction(t,tprev,output[i],y[i],y_prev[i])
        tevent=cond(temp>t,lambda tevent:np.minimum(tevent,temp),
                    lambda tevent:tevent,tevent)
    return tevent+1e-12

@partial(custom_jvp,nondiff_argnums=(0,1,2,3,4))
def _odeint45(f,event,h0,param_T,tol,y0,t,*args):

    def scan_fun(state,t):

        def cond_fn(state):
            y_prev,t_prev,h,_=state
            return (t_prev<t) & (h>0)

        def body_fn(state):
            y_prev,t_prev,h,i=state
            y,yest,t_now,inew,hopt,condition=None,None,0.,0,0.,None
            if isinstance(f,(types.FunctionType,
                             jax._src.custom_derivatives.custom_jvp)):
                y,yest,t_now=rk_step(y_prev,t_prev,h,f,*args)
                inew=i
                if event!=[]:
                    for e in event:
                        indice,signe,seuil,indice2,chgt_etat=e
                        output,outputprev=y[indice],y_prev[indice]
                        if signe=='<':
                            condition=np.bitwise_and(output<seuil,
                              np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                        elif signe=='>':
                            condition=np.bitwise_and(output>seuil,
                              np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                        hopt = optimal_step(y, yest, h, tol)
                        y,h,_,_,t_now,_,_=cond(condition,interpolation,
                                            lambda state:state,
                         (y,h,y_prev,t_prev,t_now,output-seuil,outputprev-seuil))
                        y[indice2]=cond(condition,chgt_etat,lambda state:state,
                                        y[indice2])
                elif event==[]:
                    hopt = optimal_step(y, yest, h, tol)
            elif not isinstance(f,(types.FunctionType,
                                   jax._src.custom_derivatives.custom_jvp)):
                f.etat_actuel=i
                y,yest,t_now=rk_step(y_prev,t_prev,h,f.derivative,*args)
                inew=np.argmax(np.array(f.cond_etat(y,t_now)))
                f.etat_suivant=inew
                y = f.init_etat(y)
                output=f.output
                tevent=GetTimeofNextVarHit(t_now,t_prev,output,y,y_prev,
                                           coeff*periode,periode)
                hopt = optimal_step(y,yest, h, tol)
                hopt=np.minimum(tevent-t_now,hopt)
                hopt=np.where(inew!=i,h0,hopt)

            return y,t_now,hopt,inew

        y,t1,h,i = while_loop(cond_fn, body_fn, state)
        return (y,t1,h,i),y

    coeff, periode = param_T
    if isinstance(f,(types.FunctionType,
                     jax._src.custom_derivatives.custom_jvp)):
        i0 = 0
    elif not isinstance(f, (types.FunctionType,
                     jax._src.custom_derivatives.custom_jvp)):
        i0 = f.etat_actuel
    _,ys=scan(scan_fun,(y0,t[0],h0,i0),t[1:])
    if isinstance(ys,dict):
        for i in ys.keys():
            ys[i]=np.insert(ys[i],0,y0[i])
    else:
        ys=np.transpose(np.concatenate((y0[None], ys)))
    return ys


@_odeint45.defjvp
def _odeint45_jvp(f,event,h0,param_T,tol, primals, tangents):
  y0, t, *args = primals
  delta_y0, _, *delta_args = tangents
  nargs = len(args)

  def f_aug(y0,delta_y0, t, *args_and_delta_args):
    args, delta_args = args_and_delta_args[:nargs], args_and_delta_args[nargs:]
    tangent_dot=None
    if isinstance(f,(types.FunctionType,jax._src.custom_derivatives.custom_jvp)):
        primal_dot, tangent_dot = jvp(f, (y0, t, *args), (delta_y0, 0.,
                                                          *delta_args))
    elif not isinstance(f,(types.FunctionType,
                           jax._src.custom_derivatives.custom_jvp)):
        primal_dot, tangent_dot = jvp(f.derivative, (y0, t, *args), (delta_y0,
                                                             0., *delta_args))
    return tangent_dot
  ys,ys_dot = odeint45_etendu(f,f_aug,nargs,event,h0,param_T,tol, y0,delta_y0,
                                        t, *args, *delta_args)
  return ys,ys_dot

def rk_step_der(y_prev, t_prev, delta_y_prev,h,f_aug,*args):
    if isinstance(y_prev,dict):
        k1 = f_aug(y_prev, delta_y_prev, t_prev, *args)
        k2 = f_aug(y_prev,{i:delta_y_prev[i]+ h*0.2 * k1[i] for i in k1.keys()},
               t_prev + 0.2 * h , *args)
        k3 = f_aug(y_prev, {i:delta_y_prev[i] + h * (3 * k1[i] + 9 * k2[i]) / 40
                        for i in k1.keys()},t_prev +3 * h / 10, *args)
        k4 = f_aug(y_prev,{i:delta_y_prev[i] + h*(44 * k1[i] / 45 - 56*k2[i]/15
            +32 *k3[i]/9) for i in k1.keys()}, t_prev + 4 * h / 5,*args)
        k5 = f_aug(y_prev, {i:delta_y_prev[i] + h * (19372 * k1[i] / 6561 -
            25360 * k2[i] / 2187+ 64448 * k3[i] / 6561 - 212 * k4[i] / 729)
            for i in k1.keys()},t_prev + 8 * h / 9, *args)
        k6 = f_aug(y_prev,{i:delta_y_prev[i]+h*(9017*k1[i]/3168-355*k2[i]/33
            +46732 * k3[i] / 5247 + 49 * k4[i] / 176 - 5103 * k5[i] / 18656)
                       for i in k1.keys()},t_prev + h, *args)
        delta_y = {i:delta_y_prev[i] + h *(35 * k1[i] / 384 + 500 * k3[i]/1113+
            125 * k4[i] / 192 - 2187 * k5[i] / 6784 + 11 * k6[i] / 84)
               for i in k1.keys()}
    else:
        k1 = f_aug(y_prev, delta_y_prev, t_prev, *args)
        k2 = f_aug(y_prev, delta_y_prev + h * 0.2 * k1,t_prev + 0.2 * h , *args)
        k3 = f_aug(y_prev, delta_y_prev + h * (3 * k1 + 9 * k2) / 40,t_prev
               +3 * h / 10, *args)
        k4 = f_aug(y_prev,delta_y_prev + h*(44 * k1 / 45 - 56 * k2 /15+32*k3/9),
               t_prev + 4 * h / 5,*args)
        k5 = f_aug(y_prev, delta_y_prev + h * (19372 * k1 / 6561 - 25360*k2/2187
                + 64448 * k3 / 6561 - 212 * k4 / 729),t_prev + 8 * h / 9, *args)
        k6 = f_aug(y_prev,delta_y_prev+h*(9017 * k1 / 3168 -355 *k2/33 +46732*k3
            / 5247 + 49 * k4 / 176 - 5103 * k5 / 18656),t_prev + h, *args)
        delta_y = delta_y_prev + h *(35 * k1 / 384 + 500 * k3 / 1113 +
            125 * k4 / 192 - 2187 * k5 / 6784 + 11 * k6 / 84)
    return delta_y


def odeint45_etendu(f,f_aug,nargs,event,h0,param_T,tol,y0,delta_y0,t,*args):
    args_red = args[:nargs]

    def scan_fun(state, t):

        def cond_fn(state):
            y_prev,delta_y_prev, t_prev, h,_ = state
            return (t_prev < t) & (h > 0)

        def body_fn(state):
            y_prev,delta_y_prev, t_prev, h,i = state
            y,yest,delta_y,t_now,inew,hopt,condition=None,None,None,0.,0,0.,None
            if isinstance(f,(types.FunctionType,
                             jax._src.custom_derivatives.custom_jvp)):
                y, yest, t_now = rk_step(y_prev, t_prev, h, f, *args_red)
                inew=i
                if event!=[]:
                    for e in event:
                        indice,signe,seuil,indice2,chgt_etat=e
                        output,outputprev=y[indice],y_prev[indice]
                        if signe=='<':
                            condition=np.bitwise_and(output<seuil,
                              np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                        elif signe=='>':
                            condition=np.bitwise_and(output>seuil,
                              np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                        hopt = optimal_step(y, yest, h, tol)
                        y,h,_,_,t_now,_,_=cond(condition,interpolation,
                                            lambda state:state,
                         (y,h,y_prev,t_prev,t_now,output-seuil,outputprev-seuil))
                        y[indice2]=cond(condition,chgt_etat,lambda state:state,
                                        y[indice2])
                elif event==[]:
                    hopt = optimal_step(y, yest, h, tol)
            elif not isinstance(f,(types.FunctionType,
                                   jax._src.custom_derivatives.custom_jvp)):
                f.etat_actuel=i
                y,yest,t_now=rk_step(y_prev,t_prev,h,f.derivative,*args_red)
                inew=np.argmax(np.array(f.cond_etat(y,t_now)))
                f.etat_suivant=inew
                y = f.init_etat(y)
                output=f.output
                tevent=GetTimeofNextVarHit(t_now,t_prev,output,y,y_prev,
                                           coeff*periode,periode)
                hopt = optimal_step(y,yest, h, tol)
                hopt=np.minimum(tevent-t_now,hopt)
                hopt=np.where(inew!=i,h0,hopt) # pour accelerer execution

            if isinstance(f,(types.FunctionType,
                             jax._src.custom_derivatives.custom_jvp)):
                delta_y=rk_step_der(y_prev,t_prev,delta_y_prev,h,f_aug,*args)
            elif not isinstance(f,(types.FunctionType,
                                   jax._src.custom_derivatives.custom_jvp)):
                delta_y = rk_step_der(y_prev, t_prev, delta_y_prev, h,
                                     f_aug,*args)

            return y, delta_y,t_now, hopt,inew

        y, delta_y,t1, h,i = while_loop(cond_fn, body_fn, state)
        return (y,delta_y, t1, h,i), (y,delta_y)

    coeff, periode = param_T
    if isinstance(f,(types.FunctionType,
                     jax._src.custom_derivatives.custom_jvp)):
        i0 = 0
    elif not isinstance(f, (types.FunctionType,
                     jax._src.custom_derivatives.custom_jvp)):
        i0 = f.etat_actuel
    _, (ys,delta_ys) = scan(scan_fun, (y0, delta_y0,t[0], h0,i0), t[1:])
    if isinstance(ys,dict):
        for i in ys.keys():
            ys[i]=np.insert(ys[i],0,y0[i])
            delta_ys[i] = np.insert(delta_ys[i], 0, delta_y0[i])
    else:
        ys=np.transpose(np.concatenate((y0[None], ys)))
        delta_ys=np.transpose(np.concatenate((delta_y0[None], delta_ys)))
    return ys,delta_ys