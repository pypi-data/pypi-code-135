#----------------------------------------------summary statistics--------------------------------------------------------------

def mean_var_exvx(X,P):
    import numpy as np
    import pandas as pd
    import math 
    x=np.array(X)
    p=np.array(P)
    mean=sum(x*p)
    x2=sum(x*x*p)
    var=x2-(mean*mean)
    sd=math.sqrt(var)
    data={' X':x,  '  P(X=x)':p,'  X*P':x*p,'  X^2*P':x*x*p   }
    dff=pd.DataFrame(data)
    dff.index=rowname=range(len(x))
    print(dff)
    print(" ")
    print("From table we sum (x*p) and (x^2*p) columns")
    print(" ")
    print(f" E(X)=Σ(x*p)={round(mean,4)} ")
    print("")
    print(f" E(X^2)=Σ(x^2*p)={round(x2,4)}")
    print("")
    print(f" V(x)=E(x)-(E(x))^2={round(mean,4)}-({round(x2,4)})^2={round(var,4)}")
    print("")
    print(f" Sd(x)=sqrt(v(x))=sqrt({round(var,4)})={round(sd,4)}")
    print("")
    print(" So Expectd value, Variance and standard deviation of probability distribution is,")
    print("")
    print(f"  E(X)={round(mean,4)} ,  V(x)={round(var,4)}  ,  Sd(x)={round(sd,4)}")
    
    
def Summary_stats_groupdata(L,U,f,q,d,p):
    import numpy as np
    import pandas as pd
    import math 
    l=np.array(L)
    u=np.array(U)
    f=np.array(F)
    x=(l+u)/2
    n=sum(f);FX=sum(f*x);FX2=sum(f*x*x);xbar=(FX)/n
    v=(FX2-(FX)**2/n)/n;sv=(FX2-(FX)**2/n)/(n-1)
    cv=(math.sqrt(v)/xbar)*100;cf=np.cumsum(f)
    
    
    
    q1=(round((q*(n)/4),2))
    q11=float(q1)
    for i in range(len(cf)):
        if q11<=cf[i]:
         break; 
    if i==0:
        CFq=0
    else:
        CFq=cf[i-1]
    Lq=l[i];cq=u[1]-l[1];Fq=f[i]
    Q=Lq+((q*n/4)-CFq)*(cq/Fq)
    
    
    
    
    d1=(round((d*(n)/10),2))
    d11=float(d1)
    for j in range(len(cf)):
        if d11<=cf[j]:
         break; 
    if j==0:
        CFd=0
    else:
        CFd=cf[j-1]
    Ld=l[j];cd=u[1]-l[1];Fd=f[j]
    D=Ld+((d*n/10)-CFd)*(cd/Fd)
    
    
    
    p1=(round((p*(n)/100),2))
    p11=float(p1)
    for k in range(len(cf)):
        if p11<=cf[k]:
         break; 
    if k==0:
        CFp=0
    else:
        CFp=cf[k-1]
    Lp=l[k];cp=u[1]-l[1];Fp=f[k]
    P=Lp+((p*n/100)-CFp)*(cp/Fp)
    
    

    

    for m in range(len(f)):
     if f[m]==max(f):
         break;
        
    print(len(f)-1)
    if m==0:
        Low=l[m];f1=f[m];fo=0;f2=f[m+1];C=u[m]-l[m]
    elif m==len(f)-1:
        Low=l[m];f1=f[m];fo=f[m-1];f2=0;C=u[m]-l[m]
    else:
        Low=l[m];f1=f[m];fo=f[m-1];f2=f[m+1];C=u[m]-l[m]
        
    mode=Low+((f1-fo)/(2*f1-fo-f2))*C
    
    
    
    
    rowname=range(len(u))
    data={' X':x,  '  f':f, 'f*x':f*x, 'f*x^2':f*x*x, 'cf':cf }
    dff=pd.DataFrame(data)
    dff.index=rowname


    rowname=range(len(x))
    data={'Lower limit':l,'Upper limit':u,'    f':f,' Mid point(x)':x, 'f*x':f*x, 'f*x^2':f*x*x, 'cf':cf }
    dff=pd.DataFrame(data)
    dff.index=rowname
    print(dff)
    print(" ")
    print(f"From table we have Σf*x={round(FX,4)}  and Σf*x^2={round(FX2,4)} and n={n}")
    print("*******************************************************************")
    print(" ")
    print(f"xbar=(Σ(fx)/n)=({round(FX,4)}/{n})={round(xbar,4)}")
    print(" ")
    print(f"σ^2_x=Var(x)=( Σfx^2-(Σfx)^2/n )/(n)=( {FX2}-({FX})^2/{n} )/({n})={round(v,4)}") 
    print(" ")
    print(f"σ_x=SD(x)=sqrt(σ^2_x)=sqrt({round(v,4)})={round(math.sqrt(v),4)}")
    print(" ")
    print(f"S^2_x=Var(x)=( Σfx^2-(Σfx)^2/n )/(n-1)=( {FX2}-({FX})^2/{n} )/({n-1})={round(sv,4)}") 
    print(" ")
    print(f"Sx=sd(x)=sqrt(S^2x)=sqrt({round(sv,4)})={round(math.sqrt(sv),4)}")
    print(" ")
    print(f"Coefficient of variation:")
    print(f"CV=(sd/mean)*100=({round(math.sqrt(v),4)}/{round(xbar,4)})*100={round(cv,4)}%")
    print(" ")
    print("*************************Quartile**********************************")
    print(" ")
    print(f"Q{q} classs with ({q}*(n)/4)th obs in cf column")
    print(f"Q{q} classs with ({q}*({n})/4)={q1}th obs in cf column")
    print(f"class {l[i]}-{u[i]} have cf just ≥{q11} ")
    print(f"lower limit of quartile class is L={Lq},Width of class c={cq}")
    print(f"cf of class previous to quartile class CF={CFq},freq of class is F={Fq}")
    print(f"Q{q}=L+(({q}*n/4)-cf)*(c/f)")
    print(f"Q{q}={Lq}+(({q}*{n}/4)-{CFq})*({cq}/{Fq})")
    print(f"Q{q}={round(Q,4)}")
    print(" ")
    print("*************************Decile**********************************")
    print(" ")
    print(f"D{d} classs with ({d}*(n)/10)th obs in cf column")
    print(f"D{d} classs with ({d}*({n})/10)={d1}th obs in cf column")
    print(f"class {l[j]}-{u[j]} have cf just ≥{d11} ")
    print(f"lower limit of Decile class is L={Ld},Width of class c={cd}")
    print(f"cf of class previous to Decile class CF={CFd},freq of class is F={Fd}")
    print(f"D{d}=L+(({d}*n/10)-cf)*(c/f)")
    print(f"D{d}={Ld}+(({d}*{n}/10)-{CFd})*({cd}/{Fd})")
    print(f"D{d}={round(D,4)}")
    print(" ")
    print("************************Percetile*********************************")
    print(" ")
    print(f"P{p} classs with ({p}*(n)/100)th obs in cf column")
    print(f"P{p} classs with ({p}*({n})/100)={p1}th obs in cf column")
    print(f"class {l[k]}-{u[k]} have cf just ≥{p11} ")
    print(f"lower limit of percentile class is L={Lp},Width of class c={cp}")
    print(f"cf of class previous to percentile class CF={CFp},freq of class is F={Fp}")
    print(f"P{p}=L+(({p}*n/100)-cf)*(c/f)")
    print(f"P{p}={Lp}+(({p}*{n}/100)-{CFp})*({cp}/{Fp})")
    print(f"P{p}={round(P,4)}")
    print(" ")
    print("************************Percetile*********************************")
    print(" ")
    print(f"Mode is calculate as below, ")
    print(f"Modal class is {l[m]}-{u[m]}")
    print(f"Lower boudary point L={Low}")
    print(f"Frequency of modal class is f1={f1}")
    print(f"Frequency of preceding class f0={fo}")
    print(f"Frequency of succeding class f2={f2}")
    print(f"Class length of modal class C={C}")
    print(" ")
    print(f"mode=L+(f1-fo)/(2*f1-fo-f2)*c")
    print(f"mode={Low}+( ({f1}-{fo})/({2}*{f1}-{fo}-{f2}) )*{C}")
    print(f"mode={mode}")
    
def mean_sd_xy(X,Y):
    import numpy as np
    import pandas as pd
    import math 
    x=np.array(X)
    y=np.array(Y)
    nx=len(x);ny=len(y)    
    sx=sum(x);sx2=sum(x*x);ax=sx/nx;
    vx=(sx2-(sx**2/nx))/nx; svx=(sx2-(sx**2/nx))/(nx-1)
    
    sy=sum(y);sy2=sum(y*y);ny=len(y);ay=sy/ny;
    vy=(sy2-(sy**2/ny))/ny; svy=(sy2-(sy**2/ny))/(ny-1)
    xrowname=range(len(x))
    yrowname=range(len(y))
    
    
    dffx=pd.DataFrame({' X':x,  '  X^2':x*x})
    dffy=pd.DataFrame({' Y':y,  '  Y^2':y*y})
    dffx.index=xrowname
    dffy.index=yrowname
    print(dffx)
    print("")
    print(dffy)
    print(" ")
    print(f"From table we have Σxi={round(sx,4)}  and Σxi^2={round(sx2,4)} and n={nx}")
    print(f"                   Σyi={round(sy,4)}  and Σyi^2={round(sy2,4)} and n={ny}")
    print("******************************************************************* ")
    print(" ")
    print(f"xbar=(Σ(x)/n)=({sum(x)}/{nx})={round(ax,4)}")
    print(" ")
    print(f"S^2x=( Σx^2-(Σx)^2/n )/(n-1)=( {sx2}-({sx})^2/{nx} )/({nx-1})={round(svx,4)}") 
    print(" ")
    print(f"Sx=sd(x)=sqrt(S^2x)=sqrt({round(svx,4)})={round(math.sqrt(svx),4)}")
    print(" ")
    print(" *****************************************************************")
    print(" ")
    print(f"ybar=(Σ(y)/n)=({sum(y)}/{ny})={round(ay,4)}")
    print(" ")
    print(f"S^2y=( Σy^2-(Σy)^2/n )/(n-1)=( {sy2}-({sy})^2/{ny} )/({ny-1})={round(svy,4)}") 
    print(" ")
    print(f"Sy=sd(y)=sqrt(S^2y)=sqrt({round(svy,4)})={round(math.sqrt(svy),4)}")
    print(" ")
    
def Summary_stats_raw_data(X,q,d,p):
    import numpy as np
    import pandas as pd
    import math 
    x=np.array(X)
    sx=sum(x);sx2=sum(x*x);n=len(x);a=sx/n;
    v=(sx2-(sx**2/n))/n; sv=(sx2-(sx**2/n))/(n-1)
    cv=(math.sqrt(v)/a)*100
    xx=np.sort(x)
    
    q1=(round((q*(n+1)/4),2))
    q11=float(q1)
    Q1=xx[math.floor(q1-1)]+math.modf(q11)[0]*(xx[math.ceil(q1-1)]-xx[math.floor(q1-1)])
    
    
    d1=(round((d*(n+1)/10),2))
    d11=float(d1)
    D1=xx[math.floor(d1-1)]+math.modf(d11)[0]*(xx[math.ceil(d1-1)]-xx[math.floor(d1-1)])
    
    p1=(round((p*(n+1)/100),2))
    p11=float(p1)
    P1=xx[math.floor(p1-1)]+math.modf(p11)[0]*(xx[math.ceil(p1-1)]-xx[math.floor(p1-1)])
    

    rowname=range(len(x))
    data={' X':x,  '  X^2':x*x}
    dff=pd.DataFrame(data)
    dff.index=rowname
    print(dff)
    print(" ")
    print(f"From table we have Σxi={round(sx,4)}  and Σxi^2={round(sx2,4)} and n={n}")
    print("******************************************************************* ")
    print(" ")
    print(f"xbar=(Σ(x)/n)=({sum(x)}/{n})={round(a,4)}")
    print(" ")
    print(f"σ^2_x=Var(x)=( Σx^2-(Σx)^2/n )/(n)=( {sx2}-({sx})^2/{n} )/({n})={round(v,4)}") 
    print(" ")
    print(f"σ_x=SD(x)=sqrt(σ^2_x)=sqrt({round(v,4)})={round(math.sqrt(v),4)}")
    print(" ")
    print(f"S^2x=( Σx^2-(Σx)^2/n )/(n-1)=( {sx2}-({sx})^2/{n} )/({n-1})={round(sv,4)}") 
    print(" ")
    print(f"Sx=sd(x)=sqrt(S^2x)=sqrt({round(sv,4)})={round(math.sqrt(sv),4)}")
    print(" ")
    print(f"Coefficient of variation:")
    print(f"CV=(sd/mean)*100=({round(math.sqrt(v),4)}/{round(a,4)})*100={round(cv,4)}")
    print(" ")
    print("****************************************************************** ")
    print(f"Firsy arrange data in ascending order as follows, ")
    print(f"{xx}")
    print(" ")
    print(f"Q{q}=({q}*(n+1)/4)th obs")
    print(f"  =({q}*({n}+1)/4)th obs")
    print(f"  ={q1}th obs")
    print(f"  ={math.floor(q1)}th+{round(math. modf(q11)[0],4)}*({math.ceil(q1)}th-{math.floor(q1)}th)")
    print(f"  ={xx[math.floor(q1-1)]}+{round(math. modf(q11)[0],4)}*({xx[math.ceil(q1-1)]}-{xx[math.floor(q1-1)]})")
    print(f"  ={Q1}")
    print(" ")
    print("(Inter quartile Range)IQR=Q3-Q1={Q3}-{Q1}=")
    print(" ")
    print(f"D{d}=({d}*(n+1)/10)th obs")
    print(f"  =({d}*({n}+1)/10)th obs")
    print(f"  ={d1}th obs")
    print(f"  ={math.floor(d1)}th+{round(math. modf(d11)[0],4)}*({math.ceil(d1)}th-{math.floor(d1)}th)")
    print(f"  ={xx[math.floor(d1-1)]}+{round(math. modf(d11)[0],4)}*({xx[math.ceil(d1-1)]}-{xx[math.floor(d1-1)]})")
    print(f"  ={D1}")
    print(" ")
    print(f"P{p}=({p}*(n+1)/100)th obs")
    print(f"  =({p}*({n}+1)/100)th obs")
    print(f"  ={p1}th obs")
    print(f"  ={math.floor(p1)}th+{round(math. modf(p11)[0],4)}*({math.ceil(p1)}th-{math.floor(p1)}th)")
    print(f"  ={xx[math.floor(p1-1)]}+{round(math. modf(p11)[0],4)}*({xx[math.ceil(p1-1)]}-{xx[math.floor(p1-1)]})")
    print(f"  ={P1}")
    print(" ")

def Summary_statisitcs_ungrouped_data(X,F,q,d,p):
    import numpy as np
    import pandas as pd
    import math
    x=np.array(X)
    f=np.array(F)
    n=sum(f);FX=sum(f*x);FX2=sum(f*x*x);xbar=(FX)/n
    v=(FX2-(FX)**2/n)/n
    sv=(FX2-(FX)**2/n)/(n-1)
    cv=(math.sqrt(v)/xbar)*100
    
    cf=np.cumsum(f)
    q1=(round((q*(n+1)/4),2))
    q11=float(q1)
    i = 0
    while cf[i]<=q11:
     i += 1
    
    d1=(round((d*(n+1)/10),2))
    d11=float(d1)
    j = 0
    while cf[j]<=d11:
     j += 1 
    
    p1=(round((p*(n+1)/100),2))
    p11=float(p1)
    k = 0
    while cf[k]<=p11:
     k += 1 
        
    
    rowname=range(len(x))
    data={' X':x,  '  f':f, 'f*x':f*x, 'f*x^2':f*x*x, 'cf':cf }
    dff=pd.DataFrame(data)
    dff.index=rowname
    print(dff)
    print(" ")
    print(f"From table we have Σf*x={round(FX,4)}  and Σf*x^2={round(FX2,4)} and n={n}")
    print("******************************************************************* ")
    print(" ")
    print(f"xbar=(Σ(fx)/n)=({round(FX,4)}/{n})={round(xbar,4)}")
    print(" ")
    print(f"σ^2_x=Var(x)=( Σfx^2-(Σfx)^2/n )/(n)=( {FX2}-({FX})^2/{n} )/({n})={round(v,4)}") 
    print(" ")
    print(f"σ_x=SD(x)=sqrt(σ^2_x)=sqrt({round(v,4)})={round(math.sqrt(v),4)}")
    print(" ")
    print(f"S^2_x=Var(x)=( Σfx^2-(Σfx)^2/n )/(n-1)=( {FX2}-({FX})^2/{n} )/({n-1})={round(sv,4)}") 
    print(" ")
    print(f"Sx=sd(x)=sqrt(S^2x)=sqrt({round(sv,4)})={round(math.sqrt(sv),4)}")
    print(" ")
    print(f"Coefficient of variation:")
    print(f"CV=(sd/mean)*100=({round(math.sqrt(v),4)}/{round(xbar,4)})*100={round(cv,4)}%")
    print(" ")
    print("****************************************************************** ")
    print(" ")
    print(f"Q{q}=({q}*(n+1)/4)th obs")
    print(f"Q{q}=({q}*({n}+1)/4)={q1}th obs")
    print(f"Q{q}=value of x for which cf is just ≥ {q1}")
    print(f"Q{q}={x[i]}")
    print(" ")
    print(f"D{d}=({d}*(n+1)/10)th obs")
    print(f"D{d}=({d}*({n}+1)/10)={d1}th obs")
    print(f"D{d}=value of x for which cf is just ≥ {d1}")
    print(f"D{d}={x[j]}")
    print(" ")
    print(f"P{p}=({p}*(n+1)/100)th obs")
    print(f"P{p}=({p}*({n}+1)/100)={p1}th obs")
    print(f"P{p}=value of x for which cf is just ≥ {p1}")
    print(f"P{p}={x[k]}")
    


#--------------------------------Sample size--------------------------------------------------------------------------------------
def Sample_size_mean(sigma,ME,l):
    import math 
    import scipy.stats
    import math
    a=(100-l)/100
    Z=abs(round(scipy.stats.norm.ppf(a/2),4))
    n=round((Z*sigma/ME)*((Z*sigma/ME)),4)
    no=math.ceil(n)
    print(f"here we have given following information")
    print(f"Sigma={sigma}; M.E={ME}; Confidence level={l}%")
    print(" ")
    print(f"Formula for minimum sample size is,")
    print("n>=((z*sigma)/(E))^2")
    print(f"n>=(({Z}*{sigma})/({ME}))^2     Note: Excel command for z_c is  =NORMSINV({a/2})")
    print(f"n>={n}")
    print("")
    print(f"Round n to interger so n={no}")
    print("")
    print(f"So minimum sample size is n={no}")


def Sample_size_proportion(p,ME,l):
    import math 
    import scipy.stats
    import math
    a=(100-l)/100
    Z=abs(round(scipy.stats.norm.ppf(a/2),4))
    n=round(p*(1-p)*(Z/ME)*(Z/ME),4)
    no=math.ceil(n)
    print(f"here we have given following information")
    print(f"p={p}; M.E={ME}; Confidence level={l}%")
    print(" ")
    print(f"Formula for minimum sample size required to estimate proportion p={p} ")
    print(f"With required margin of error (M.E)={ME} is,")
    print("n>=p*(1-p)*(Z/E)^2")
    print(f"n>={p}*(1-{p})*({Z}/{ME})^2     Note: Excel command for z_c is  =NORMSINV({a/2})")
    print(f"n>={n}")
    print("")
    print(f"Round n to interger so n={no}")
    print("")
    print(f"So minimum sample size to estimate proportion p={p} ")
    print(f"With required margin of error (M.E)={ME} is n={no}")
    


#-------CORRELATION----------------------------------------------------------------------------------------------------------------------------------------

def correlation(X,Y,a):
    import math 
    import scipy.stats
    import pandas as pd
    import numpy as np
    x=np.array(X)
    y=np.array(Y)
    n=len(x)
    df=n-2
    sumx=sum(x)  
    sumy=sum(y)
    sumx2=sum(x*x)
    sumy2=sum(y*y)
    sumxy=sum(x*y)
    xbar=sum(x)/n
    ybar=sum(y)/n
    ssxx=sum((x-xbar)*(x-xbar))
    ssyy=sum((y-ybar)*(y-ybar))
    ssxy=sum((x-xbar)*(y-ybar))
    r=(ssxy/math.sqrt(ssxx*ssyy))
    t_cal=round(r*math.sqrt((n-2)/(1-r*r)),4)
    tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
    p=round(scipy.stats.t.sf(abs(t_cal),df)*2,4)

    print(f"here we have given following information")
    data={'X':x,'Y':y,'x^2':x*x,'y^2':y*y,'x*y':x*y}
    dff= pd.DataFrame(data)
    print(dff)
    print(" ")
    print(f"from table we calculate sum for each columns")
    print(" ")
    print(f"Σx={round(sumx,4)}; Σy={round(sumy,4)}; Σx^2={round(sumx2,4)}; Σy^2={round(sumy2,4)}; Σx*y={round(sumxy,4)}")
    print(" ")
    print("************calcuation of mean and sum of sqaure***************")
    print(f"xbar=(Σx/n)=({round(sumx,4)}/{n})={round(xbar,4)}")
    print(f"ybar=(Σy/n)=({round(sumy,4)}/{n})={round(ybar,4)}")
    print(f"SSxx=Σx^2-(Σx)^2/n={round(sumx2,4)}-({round(sumx,4)})^2/{n}={round(ssxx,4)}")
    print(f"SSyy=Σy^2-(Σy)^2/n={round(sumy2,4)}-({round(sumy,4)})^2/{n}={round(ssyy,4)}")
    print(f"SSxy=Σxy-(Σy)(Σx)/n={round(sumxy,4)}-({round(sumx,4)}*{round(sumy,4)})/{n}={round(ssxy,4)}")
    print(" ")
    print("************calcuation of correlation*************************")
    print(f"r=SSxy/sqrt(SSxx*SSyy)=({round(ssxy,4)}/sqrt({round(ssxx,4)}*{round(ssyy,4)}))={round(r,4)}")
    print(" ")
    print("************Correlation Test*********************")
    print(f"here we have given following information")
    print(f"r={round(r,4)}; n={n}; alpha={a}; df=n-2={n}-2={df}")
    print(" ")
    print("Null and alternative:")
    print("Ho: r=0 (correlation is insignificant)")
    print("H1: r≠0 (correlation is significant)")
    print(" ")
    print("Test statistics:")
    print("t_cal=(r*math.sqrt((n-2)/(1-r^2))")
    print(f"t_cal=t_cal=({round(r,4)}*math.sqrt(({n}-2)/(1-{round(r,4)}*{round(r,4)}))={t_cal}")
    print(" ")
    print("Cirtical value and Pvalue:")
    print(f"t_c={tc} is critical value with df=n-1={n}-2={df} ")
    print(f"P={p} is p value of test statistic  ")
    print(f"Note: Excel command for t_c is  =TINV({a},{df})")
    print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},2)")
    print(" ")
    print("Decision:")
    print("1]Based on cirtical value approch-")
    if p>a:
            print(f"here t_cal <= t_c so do not reject null hypothesis")
    else: 
            print(f"here t_cal > t_c so reject null hypothesis")
            
    print("")
    
    print("2]Based on P- value approch-")
    if p>a:
            print(f"here Pvalue >= alpha so do not reject null hypothesis")
    else: 
            print(f"here Pvalue < alpha  so reject null hypothesis")
    print("")
    print("Conclusion:")
    if p>a:
            print("Ho: r=0 (correlation is insignificant)")
    
    else:
            print("H1: r≠0 (correlation is significant)")
    

#----------------Z_TEST----------------------------------------------------------------------------------------------------------------------------
def Two_sample_ztest_two_tail(x1bar,sigma1,n1,x2bar,sigma2,n2,a):
  import math
  import scipy.stats
  z_cal=round((x1bar-x2bar)/(math.sqrt(sigma1*sigma1/n1+sigma2*sigma2/n2)),4)
  z=abs(round(scipy.stats.norm.ppf(a/2),4))
  p=round(2*(1-scipy.stats.norm.cdf(abs(z_cal))),4)
  print(f"here we have given following information")
  print(f"x1bar={x1bar},sigma1={sigma1},n1={n1},x2bar={x2bar},sigma2={sigma2},n2={n2},alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1=mue2")
  print(f"H1:mue1≠mue2")
  print(" ")
  print("Test statistics:")
  print("z_cal=(x1bar-x2bar)/(sqrt(sigma1^2/n1+sigma2^2/n2))")
  print(f"z_cal=({x1bar}-{x2bar})/(sqrt({round(sigma1*sigma1,4)}/{n1} + {round(sigma2*sigma2,4)}/{n2}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =abs(NORMSINV({a/2}))")
  print(f"      and for Pvalue is  =2*(1-NORMSDIST(abs({z_cal})))")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here |z_cal| <= z_c so do not reject null hypothesis")
  else: 
        print(f"here |z_cal| > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1=mue2")
  else:
        print(f"Ho:mue1≠mue2")
  
  
def  Two_sample_ztest_right_tail(x1bar,sigma1,n1,x2bar,sigma2,n2,a):
  import math
  import scipy.stats
  z_cal=round((x1bar-x2bar)/(math.sqrt(sigma1*sigma1/n1+sigma2*sigma2/n2)),4)
  z=abs(round(scipy.stats.norm.ppf(a),4))
  p=round(1-scipy.stats.norm.cdf((z_cal)),4)
  print(f"here we have given following information")
  print(f"x1bar={x1bar},sigma1={sigma1},n1={n1},x2bar={x2bar},sigma2={sigma2},n2={n2},alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1=mue2")
  print(f"H1:mue1>mue2")
  print(" ")
  print("Test statistics:")
  print("z_cal=(x1bar-x2bar)/(sqrt(sigma1^2/n1+sigma2^2/n2))")
  print(f"z_cal=({x1bar}-{x2bar})/(sqrt({round(sigma1*sigma1,4)}/{n1} + {round(sigma2*sigma2,4)}/{n2}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =-NORMSINV({a})")
  print(f"      and for Pvalue is  =1-NORMSDIST({z_cal})")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here z_cal <= z_c so do not reject null hypothesis")
  else: 
        print(f"here z_cal > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1=mue2")
  else:
        print(f"Ho:mue1>mue2")
  
def Two_sample_ztest_left_tail(x1bar,sigma1,n1,x2bar,sigma2,n2,a):
  import math
  import scipy.stats
  z_cal=round((x1bar-x2bar)/(math.sqrt(sigma1*sigma1/n1+sigma2*sigma2/n2)),4)
  z=abs(round(scipy.stats.norm.ppf(a),4))
  p=round(1-scipy.stats.norm.cdf((z_cal)),4)
  print(f"here we have given following information")
  print(f"x1bar={x1bar},sigma1={sigma1},n1={n1},x2bar={x2bar},sigma2={sigma2},n2={n2},alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1=mue2")
  print(f"H1:mue1<mue2")
  print(" ")
  print("Test statistics:")
  print("z_cal=(x1bar-x2bar)/(sqrt(sigma1^2/n1+sigma2^2/n2))")
  print(f"z_cal=({x1bar}-{x2bar})/(sqrt({round(sigma1*sigma1,4)}/{n1} + {round(sigma2*sigma2,4)}/{n2}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={-z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =NORMSINV({a})")
  print(f"      and for Pvalue is  =NORMSDIST({z_cal})")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here z_cal >= z_c so do not reject null hypothesis")
  else: 
        print(f"here z_cal < z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1=mue2")
  else:
        print(f"H1:mue1<mue2")

def  One_sample_ztest_two_tail(mue,xbar,sd,n,a):
 import math
 import scipy.stats
 z_cal=round((xbar-mue)/(sd/math.sqrt(n)),4)
 z=abs(round(scipy.stats.norm.ppf(a/2),4))
 p=round(2*(1-scipy.stats.norm.cdf(abs(z_cal))),4)
 print(f"here we have given following information")
 print(f"xbar={xbar}; sd={sd}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print(f"Ho:mue={mue}")
 print(f"H1:mue≠{mue}")
 print(" ")
 print("Test statistics:")
 print("z_cal=(xbar-mue)/(sd/sqrt(n))")
 print(f"z_cal=({xbar}-{mue})/({sd}/sqrt({n}))={z_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"z_c={z} is critical value ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for z_c is  =abs(NORMSINV({a/2}))")
 print(f"      and for Pvalue is  =2*(1-NORMSDIST(abs({z_cal})))")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here |z_cal| <= z_c so do not reject null hypothesis")
 else: 
        print(f"here |z_cal| > z_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"mue={mue}")
 else:
        print(f"mue≠{mue}")


def  One_sample_ztest_right_tail(mue,xbar,sd,n,a):
 import math
 import scipy.stats
 z_cal=round((xbar-mue)/(sd/math.sqrt(n)),4)
 z=abs(round(scipy.stats.norm.ppf(a),4))
 p=round((1-scipy.stats.norm.cdf((z_cal))),4)
 print(f"here we have given following information")
 print(f"xbar={xbar}; sd={sd}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print(f"Ho:mue={mue}")
 print(f"H1:mue>{mue}")
 print(" ")
 print("Test statistics:")
 print("z_cal=(xbar-mue)/(sd/sqrt(n))")
 print(f"z_cal=({xbar}-{mue})/({sd}/sqrt({n}))={z_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"z_c={z} is critical value ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for z_c is  =NORMSINV({a})")
 print(f"      and for Pvalue is  =1-NORMSDIST({z_cal})")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here z_cal <= z_c so do not reject null hypothesis")
 else: 
        print(f"here z_cal > z_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"mue={mue}")
 else:
        print(f"mue>{mue}")
 
 
def One_sample_ztest_left_tail(mue,xbar,sd,n,a):
 import math
 import scipy.stats
 z_cal=round((xbar-mue)/(sd/math.sqrt(n)),4)
 z=abs(round(scipy.stats.norm.ppf(a),4))
 p=round(scipy.stats.norm.cdf((z_cal)),4)
 print(f"here we have given following information")
 print(f"xbar={xbar}; sd={sd}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print(f"Ho:mue={mue}")
 print(f"H1:mue<{mue}")
 print(" ")
 print("Test statistics:")
 print("z_cal=(xbar-mue)/(sd/sqrt(n))")
 print(f"z_cal=({xbar}-{mue})/({sd}/sqrt({n}))={z_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"z_c={-z} is critical value ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for z_c is  =NORMSINV({a})")
 print(f"      and for Pvalue is  =NORMSDIST({z_cal})")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here z_cal >= z_c so do not reject null hypothesis")
 else: 
        print(f"here z_cal < z_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"mue={mue}")
 else:
        print(f"mue<{mue}")


#------------------T TEST--------------------------------------------------------------------------------------------------------------------------------

def Paired_ttest_two_tail(X,Y,a):
  import math 
  import statistics
  import scipy.stats
  import numpy as np
  import pandas as pd  
  n=len(X)
  df=n-1
  D=np.array(X)-np.array(Y)
  D=[float(item) for item in D]
  xbar_d=round(statistics.mean(D),4)
  S_d=round(statistics.stdev(D),4)
  t_cal=round((xbar_d)/(S_d/math.sqrt(n)),4)
  tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
  p=round(scipy.stats.t.sf(abs(t_cal),df)*2,4)
  print(f"here we have given following information")
  print(f"Depenent samples and, alpha={a}")
  print(f"x={X}")
  print(f"Y={Y}")  
  print("Di=Xi-Yi")
  print(f"Di={D}")
  print("We calculate mean and sd from Di")
  print(f"xbar_d=({D[0]}+....+{D[-1]})/{n}={xbar_d}")
  print(f"S_d=sqrt(({D[0]}-({xbar_d}))^2+...+({D[-1]}-({xbar_d}))^2)/({n-1}))={S_d}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1-mue2=0")
  print(f"H1:mue1-mue2≠0")
  print(" ")
  print("Test statistics:")
  print("t_cal=(xbar_d)/(S_d/sqrt(n))")
  print(f"t_cal=({xbar_d})/({S_d}/sqrt({n}))={t_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"t_c={tc} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for t_c is  =TINV({a},{df})")
  print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},2)")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here |t_cal| <= t_c so do not reject null hypothesis")
  else: 
        print(f"here |t_cal| > t_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1-mue2=0")
  else:
        print(f"H1:mue1-mue2≠0")

 
def  Paired_ttest_right_tail(X,Y,a):
  import math 
  import statistics
  import scipy.stats
  import numpy as np
  import pandas as pd
  n=len(X)
  df=n-1
  D=np.array(Y)-np.array(X)
  D=[float(item) for item in D]
  xbar_d=round(statistics.mean(D),4)
  S_d=round(statistics.stdev(D),4)
  t_cal=round((xbar_d)/(S_d/math.sqrt(n)),4)
  tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
  p=round(1-scipy.stats.t.sf(abs(t_cal),df),4)
  print(f"here we have given following information")
  print(f"Depenent samples and, alpha={a}")
  print(f"x={X}")
  print(f"Y={Y}")  
  print("Di=Yi-Xi")
  print(f"Di={D}")
  print("We calculate mean and sd from Di")
  print(f"xbar_d=({D[0]}+....+{D[-1]})/{n}={xbar_d}")
  print(f"S_d=sqrt(({D[0]}-({xbar_d}))^2+...+({D[-1]}-({xbar_d}))^2)/({n-1}))={S_d}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1-mue2=0")
  print(f"H1:mue1-mue2>0")
  print(" ")
  print("Test statistics:")
  print("t_cal=(xbar_d)/(S_d/sqrt(n))")
  print(f"t_cal=({xbar_d})/({S_d}/sqrt({n}))={t_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"t_c={tc} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for t_c is  =TINV({a},{df})")
  print(f"      and for Pvalue is  =1-TDIST(abs({t_cal}),{df},1)")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here t_cal<= z_c so do not reject null hypothesis")
  else: 
        print(f"here t_cal > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1-mue2=0")
  else:
        print(f"H1:mue1-mue2>0")
  
  
def Paired_ttest_left_tail(X,Y,a):
  import math 
  import statistics
  import scipy.stats
  import numpy as np
  import pandas as pd
  n=len(X)
  df=n-1
  D=np.array(Y)-np.array(X)
  D=[float(item) for item in D]
  xbar_d=round(statistics.mean(D),4)
  S_d=round(statistics.stdev(D),4)
  t_cal=round((xbar_d)/(S_d/math.sqrt(n)),4)
  tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
  p=round(scipy.stats.t.sf(abs(t_cal),df),4)
  print(f"here we have given following information")
  print(f"Depenent samples and, alpha={a}")
  print(f"x={X}")
  print(f"Y={Y}")  
  print("Di=Yi-Xi")
  print(f"Di={D}")
  print("We calculate mean and sd from Di")
  print(f"xbar_d=({D[0]}+....+{D[-1]})/{n}={xbar_d}")
  print(f"S_d=sqrt(({D[0]}-({xbar_d}))^2+...+({D[-1]}-({xbar_d}))^2)/({n-1}))={S_d}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1-mue2=0")
  print(f"H1:mue1-mue2<0")
  print(" ")
  print("Test statistics:")
  print("t_cal=(xbar_d)/(S_d/sqrt(n))")
  print(f"t_cal=({xbar_d})/({S_d}/sqrt({n}))={t_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"t_c={-tc} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for t_c is  =-TINV({a},{df})")
  print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},1)")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here t_cal >= t_c so do not reject null hypothesis")
  else: 
        print(f"here t_cal < t_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1-mue2=0")
  else:
        print(f"H1:mue1-mue2<0")
  

def Two_sample_ttest_two_tail(x1bar,s1,n1,x2bar,s2,n2,a):
  import math 
  import scipy.stats 
  sp2=round(((n1-1)*s1*s1+(n2-1)*s2*s2)/(n1+n2-2),4)    
  SE=round(math.sqrt(sp2*(1/n1+1/n2)),4)
  t_cal=round((x1bar-x2bar)/SE,4)
  df=n1+n2-2    
  t_c=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
  p=round(scipy.stats.t.sf(abs(t_cal),df)*2,4)
  print(f"here we have given following information")
  print(f"x1bar={x1bar},s1={s1},n1={n1},x2bar={x2bar},s2={s2},n2={n2},alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1=mue2")
  print(f"H1:mue1≠mue2")
  print(" ")
  print("Test statistics:")
  print("")
  print(f"sp^2=((n1-1)*s1^2+(n2-1)*s2^2)/(n1+n2-2)")
  print(f"sp^2=({n1-1}*{s1}^2+{n2-1}*{s2}^2)/({n1}+{n2}-2)={sp2}")
  print("")
  print(f"SE=sqrt(sp^2*(1/n1+1/n2))=sqrt({sp2}*(1/{n1}+1/{n2}))={SE} ")
  print("")
  print(f"Test statistics is given as")
  print(f"t_cal=(x1bar-x2bar)/SE=({x1bar}-{x2bar})/{SE}={t_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"t_c={t_c} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for t_c is  =TINV({a},{df})")
  print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},2)")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here |t_cal| <= t_c so do not reject null hypothesis")
  else: 
        print(f"here |t_cal| > t_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:mue1=mue2")
  else:
        print(f"Ho:mue1≠mue2")
  
  
def Two_sample_ttest_right_tail(x1bar,s1,n1,x2bar,s2,n2,a):
  import math 
  import scipy.stats
  sp2=round(((n1-1)*s1*s1+(n2-1)*s2*s2)/(n1+n2-2),4)    
  SE=round(math.sqrt(sp2*(1/n1+1/n2)),4)
  t_cal=round((x1bar-x2bar)/SE,4)
  df=n1+n2-2    
  tc=abs(round(scipy.stats.t.ppf(q=a,df=df),4))
  p=round(1-(scipy.stats.t.sf(abs(t_cal),df)),4)
  print(f"here we have given following information")
  print(f"x1bar={x1bar},s1={s1},n1={n1},x2bar={x2bar},s2={s2},n2={n2},alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1-mue2=0")
  print(f"H1:mue1-mue2>0")
  print(" ")
  print("Test statistics:")
  print("")
  print(f"sp^2=((n1-1)*s1^2+(n2-1)*s2^2)/(n1+n2-2)")
  print(f"sp^2=({n1-1}*{s1}^2+{n2-1}*{s2}^2)/({n1}+{n2}-2)={sp2}")
  print("")
  print(f"SE=sqrt(sp^2*(1/n1+1/n2))=sqrt({sp2}*(1/{n1}+1/{n2}))={SE} ")
  print("")
  print(f"Test statistics is given as")
  print(f"t_cal=(x1bar-x2bar)/SE=({x1bar}-{x2bar})/{SE}={t_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"t_c={tc} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for t_c is  =TINV({a*2},{df})")
  print(f"      and for Pvalue is  =1-TDIST(abs({t_cal}),{df},1)")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here t_cal < t_c so do not reject null hypothesis")
  else: 
        print(f"here t_cal >= t_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"mue1-mue2=0")
  else:
        print(f"mue1-mue2>0")
  
  
def Two_sample_ttest_left_tail(x1bar,s1,n1,x2bar,s2,n2,a):
  import math 
  import scipy.stats
  sp2=round(((n1-1)*s1*s1+(n2-1)*s2*s2)/(n1+n2-2),4)    
  SE=round(math.sqrt(sp2*(1/n1+1/n2)),4)
  t_cal=round((x1bar-x2bar)/SE,4)
  df=n1+n2-2    
  tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
  p=round((scipy.stats.t.sf(abs(t_cal),df)),4)
  print(f"here we have given following information")
  print(f"x1bar={x1bar},s1={s1},n1={n1},x2bar={x2bar},s2={s2},n2={n2},alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:mue1-mue2=0")
  print(f"H1:mue1-mue2<0")
  print(" ")
  print("Test statistics:")
  print("")
  print(f"sp^2=((n1-1)*s1^2+(n2-1)*s2^2)/(n1+n2-2)")
  print(f"sp^2=({n1-1}*{s1}^2+{n2-1}*{s2}^2)/({n1}+{n2}-2)={sp2}")
  print("")
  print(f"SE=sqrt(sp^2*(1/n1+1/n2))=sqrt({sp2}*(1/{n1}+1/{n2}))={SE} ")
  print("")
  print(f"Test statistics is given as")
  print(f"t_cal=(x1bar-x2bar)/SE=({x1bar}-{x2bar})/{SE}={t_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"t_c={-tc} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for t_c is  =-TINV({a*2},{df})")
  print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},1)")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here t_cal >= t_c so do not reject null hypothesis")
  else: 
        print(f"here t_cal < t_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"mue1-mue2=0")
  else:
        print(f"mue1-mue2<0")
  
  

def One_sample_ttest_two_tail(mue,xbar,s,n,a):
 import math 
 import scipy.stats
 df=n-1    
 t_cal=round((xbar-mue)/(s/math.sqrt(n)),4)
 tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
 p=round(scipy.stats.t.sf(abs(t_cal),df)*2,4)
 print(f"here we have given following information")
 print(f"xbar={xbar}; s={s}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print(f"Ho:mue={mue}")
 print(f"H1:mue≠{mue}")
 print(" ")
 print("Test statistics:")
 print("t_cal=(xbar-mue)/(s/sqrt(n))")
 print(f"t_cal=({xbar}-{mue})/({s}/sqrt({n}))={t_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"t_c={tc} is critical value with df=n-1={n}-1={df} ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for t_c is  =TINV({a},{df})")
 print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},2)")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here |t_cal| <= t_c so do not reject null hypothesis")
 else: 
        print(f"here |t_cal| > t_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"mue={mue}")
 else:
        print(f"mue≠{mue}")
 
 
def One_sample_ttest_right_tail(mue,xbar,s,n,a):
 import math 
 import scipy.stats
 df=n-1    
 t_cal=round((xbar-mue)/(s/math.sqrt(n)),4)
 tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
 p=round(scipy.stats.t.sf(abs(t_cal),df),4)
 print(f"here we have given following information")
 print(f"xbar={xbar}; s={s}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print(f"Ho:mue={mue}")
 print(f"H1:mue>{mue}")
 print(" ")
 print("Test statistics:")
 print("t_cal=(xbar-mue)/(s/sqrt(n))")
 print(f"t_cal=({xbar}-{mue})/({s}/sqrt({n}))={t_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"t_c={tc} is critical value with df=n-1={n}-1={df} ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for t_c is  =TINV({a*2},{df})")
 print(f"      and for Pvalue is  =1-TDIST(abs({t_cal}),{df},1)")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here t_cal <= t_c so do not reject null hypothesis")
 else: 
        print(f"here t_cal > t_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"mue={mue}")
 else:
        print(f"mue>{mue}")
 
 
def One_sample_ttest_left_tail(mue,xbar,s,n,a):
 import math 
 import scipy.stats
 df=n-1    
 t_cal=round((xbar-mue)/(s/math.sqrt(n)),4)
 tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
 p=round((1-scipy.stats.t.sf(abs(t_cal),df)),4)
 print(f"here we have given following information")
 print(f"xbar={xbar}; s={s}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print(f"Ho:mue={mue}")
 print(f"H1:mue<{mue}")
 print(" ")
 print("Test statistics:")
 print("t_cal=(xbar-mue)/(s/sqrt(n))")
 print(f"t_cal=({xbar}-{mue})/({s}/sqrt({n}))={t_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"t_c={-tc} is critical value with df=n-1={n}-1={df} ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for t_c is  =-TINV({a*2},{df})")
 print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},1)")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here t_cal >= t_c so do not reject null hypothesis")
 else: 
        print(f"here t_cal < t_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"mue={mue}")
 else:
        print(f"mue<{mue}")
 

#----------------Proportion_Z_TEST-----------------------------------------------------------------------------------------------------------------------

def Two_sample_proportion_test_two_tail(x1,n1,x2,n2,a):
  import math 
  import scipy.stats
  pbar=round((x1+x2)/(n1+n2),4)    
  p1_cap=round(x1/n1,6)
  p2_cap=round(x2/n2,6)
  z_cal=round((p1_cap-p2_cap)/(math.sqrt(pbar*(1-pbar)*(1/n1+1/n2))),4)
  z=abs(round(scipy.stats.norm.ppf(a/2),4))
  p=round(2*(1-scipy.stats.norm.cdf(abs(z_cal))),4)
  print(f"here we have given following information")
  print(f"x1={x1}; n1={n1}; x2={x2}; n2={n2}; Alpha={a}")
  print(" ")
  print(f"So we get sample proportions,") 
  print(f"   p1_cap=(x1/n1)=({x1}/{n1})={p1_cap}")
  print(f"   p2_cap=(x2/n2)=({x2}/{n2})={p2_cap}")
  print(f"   pbar=(x1+x2)/(n1+n2)=({x1}+{x2})/({n1}+{n2})={pbar}")
  print("")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:P1=p2")
  print(f"H1:P1≠p2")
  print(" ")
  print("Test statistics:")
  print("z_cal=(p1_cap-p2_cap)/(sqrt(pbar*(1-pbar)*(1/n1+1/n2))")
  print(f"z_cal=({p1_cap}-{p2_cap})/(sqrt({pbar}*(1-{pbar})*(1/{n1}+1/{n2}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =NORMSINV({a/2})")
  print(f"      and for Pvalue is  =2*(1-NORMSDIST(abs({z_cal})))")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here |z_cal| <= z_c so do not reject null hypothesis")
  else: 
        print(f"here |z_cal| > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:P1=p2")
  else:
        print(f"Ho:P1≠p2")
  
  

def Two_sample_proportion_test_right_tail(x1,n1,x2,n2,a):
  import math 
  import scipy.stats 
  pbar=round((x1+x2)/(n1+n2),4)    
  p1_cap=round(x1/n1,6)
  p2_cap=round(x2/n2,6)
  z_cal=round((p1_cap-p2_cap)/(math.sqrt(pbar*(1-pbar)*(1/n1+1/n2))),4)
  z=abs(round(scipy.stats.norm.ppf(a),4))
  p=round(1-scipy.stats.norm.cdf(abs(z_cal)),4)
  print(f"here we have given following information")
  print(f"x1={x1}; n1={n1}; x2={x2}; n2={n2}; Alpha={a}")
  print(" ")
  print(f"So we get sample proportions,") 
  print(f"   p1_cap=(x1/n1)=({x1}/{n1})={p1_cap}")
  print(f"   p2_cap=(x2/n2)=({x2}/{n2})={p2_cap}")
  print(f"   pbar=(x1+x2)/(n1+n2)=({x1}+{x2})/({n1}+{n2})={pbar}")
  print("")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:P1=p2")
  print(f"H1:P1>p2")
  print(" ")
  print("Test statistics:")
  print("z_cal=(p1_cap-p2_cap)/(sqrt(pbar*(1-pbar)*(1/n1+1/n2))")
  print(f"z_cal=({p1_cap}-{p2_cap})/(sqrt({pbar}*(1-{pbar})*(1/{n1}+1/{n2}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =NORMSINV({a})")
  print(f"      and for Pvalue is  =1-NORMSDIST({z_cal})")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here z_cal <= z_c so do not reject null hypothesis")
  else: 
        print(f"here z_cal > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:P1=p2")
  else:
        print(f"Ho:P1>p2")
  
  
 
def Two_sample_proportion_test_left_tail(x1,n1,x2,n2,a):
  import math 
  import scipy.stats
  pbar=round((x1+x2)/(n1+n2),4)    
  p1_cap=round(x1/n1,6)
  p2_cap=round(x2/n2,6)
  z_cal=round((p1_cap-p2_cap)/(math.sqrt(pbar*(1-pbar)*(1/n1+1/n2))),4)
  z=abs(round(scipy.stats.norm.ppf(a),4))
  p=round(scipy.stats.norm.cdf(abs(z_cal)),4)
  print(f"here we have given following information")
  print(f"x1={x1}; n1={n1}; x2={x2}; n2={n2}; Alpha={a}")
  print(" ")
  print(f"So we get sample proportions,") 
  print(f"   p1_cap=(x1/n1)=({x1}/{n1})={p1_cap}")
  print(f"   p2_cap=(x2/n2)=({x2}/{n2})={p2_cap}")
  print(f"   pbar=(x1+x2)/(n1+n2)=({x1}+{x2})/({n1}+{n2})={pbar}")
  print("")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:P1=p2")
  print(f"H1:P1<p2")
  print(" ")
  print("Test statistics:")
  print("z_cal=(p1_cap-p2_cap)/(sqrt(pbar*(1-pbar)*(1/n1+1/n2))")
  print(f"z_cal=({p1_cap}-{p2_cap})/(sqrt({pbar}*(1-{pbar})*(1/{n1}+1/{n2}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={-z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =NORMSINV({a})")
  print(f"      and for Pvalue is  =NORMSDIST({z_cal})")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here z_cal >= z_c so do not reject null hypothesis")
  else: 
        print(f"here z_cal < z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:P1=p2")
  else:
        print(f"Ho:P1<p2")
  

def One_sample_proportion_test_two_tail(x,n,po,a):
  import math 
  import scipy.stats
  p_cap=round(x/n,6)
  z_cal=round((p_cap-po)/(math.sqrt(po*(1-po)/n)),4)
  z=abs(round(scipy.stats.norm.ppf(a/2),4))
  p=round(2*(1-scipy.stats.norm.cdf(abs(z_cal))),4)
  print(f"here we have given following information")
  print(f"x={x}; n={n}; sample proprtion p_cap=(x/n)=({x}/{n})={p_cap}; Alpha={a}")
  print("")
  print("Null and alternative:")
  print(f"Ho:Po={po}")
  print(f"H1:Po≠{po}")
  print(" ")
  print("Test statistics:")
  print("z_cal=(p_cap-po)/(sqrt(po*(1-po)/n))")
  print(f"z_cal=({p_cap}-{po})/(sqrt({po}*(1-{po})/{n}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =NORMSINV({a/2})")
  print(f"      and for Pvalue is  =2*(1-NORMSDIST(abs({z_cal})))")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here |z_cal| <= z_c so do not reject null hypothesis")
  else: 
        print(f"here |z_cal| > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:Po={po}")
  else:
        print(f"Ho:Po≠{po}")
  


def One_sample_proportion_test_right_tail(x,n,po,a):
  import math 
  import scipy.stats
  p_cap=round(x/n,6)
  z_cal=round((p_cap-po)/(math.sqrt(po*(1-po)/n)),4)
  z=abs(round(scipy.stats.norm.ppf(a),4))
  p=round(1-scipy.stats.norm.cdf((z_cal)),4)
  print(f"here we have given following information")
  print(f"x={x}; n={n}; sample proprtion p_cap=(x/n)=({x}/{n})={p_cap}; Alpha={a}")
  print("")
  print("Null and alternative:")
  print(f"Ho:Po={po}")
  print(f"H1:Po>{po}")
  print(" ")
  print("Test statistics:")
  print("z_cal=(p_cap-po)/(sqrt(po*(1-po)/n))")
  print(f"z_cal=({p_cap}-{po})/(sqrt({po}*(1-{po})/{n}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c={z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =NORMSINV({a})")
  print(f"      and for Pvalue is  =1-NORMSDIST({z_cal})")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here z_cal <= z_c so do not reject null hypothesis")
  else: 
        print(f"here z_cal > z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:Po={po}")
  else:
        print(f"Ho:Po>{po}")
  
  
def One_sample_proportion_test_left_tail(x,n,po,a):
  import math 
  import scipy.stats
  p_cap=round(x/n,6)
  z_cal=round((p_cap-po)/(math.sqrt(po*(1-po)/n)),4)
  z=abs(round(scipy.stats.norm.ppf(a),4))
  p=round(scipy.stats.norm.cdf((z_cal)),4)
  print(f"here we have given following information")
  print(f"x={x}; n={n}; sample proprtion p_cap=(x/n)=({x}/{n})={p_cap}; Alpha={a}")
  print("")
  print("Null and alternative:")
  print(f"Ho:Po={po}")
  print(f"H1:Po<{po}")
  print(" ")
  print("Test statistics:")
  print("z_cal=(p_cap-po)/(sqrt(po*(1-po)/n))")
  print(f"z_cal=({p_cap}-{po})/(sqrt({po}*(1-{po})/{n}))={z_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"z_c= {-z} is critical value ")
  print(f"P={p} is p value of test statistic  ")
  print(f"Note: Excel command for z_c is  =-NORMSINV({a})")
  print(f"      and for Pvalue is  =NORMSDIST({z_cal})")
  print(" ")
  print("Decision:")
  print("1]Based on cirtical value approch-")
  if p>a:
        print(f"here z_cal >= z_c so do not reject null hypothesis")
  else: 
        print(f"here z_cal < z_c so reject null hypothesis")
        
  print("")
 
  print("2]Based on P- value approch-")
  if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
  else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
  print("")
  print("Conclusion:")
  if p>a:
        print(f"Ho:Po={po}")
  else:
        print(f"Ho:Po<{po}")
  

#--------------------Correlation-----------------------------------------------------------------------------------------------------------------

def correlation_test_two_tail(r,n,a):
 import math
 import scipy.stats
 df=n-2
 t_cal=round(r*math.sqrt((n-2)/(1-r*r)),4)
 tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
 p=round(scipy.stats.t.sf(abs(t_cal),df)*2,4)
 print(f"here we have given following information")
 print(f"r={r}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print("Ho: r=0 (correlation is insignificant)")
 print("H1: r≠0 (correlation is significant)")
 print(" ")
 print("Test statistics:")
 print("t_cal=(r*sqrt((n-2)/(1-r^2))")
 print(f"t_cal=({r}*sqrt(({n}-2)/(1-({r})^2))={t_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"t_c={tc} is critical value with df=n-1={n}-2={df} ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for t_c is  =TINV({a},{df})")
 print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},2)")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here |t_cal| <= t_c so do not reject null hypothesis")
 else: 
        print(f"here |t_cal| > t_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P-value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print("Ho: r=0 (correlation is insignificant)")
 
 else:
        print("H1: r≠0 (correlation is significant)")

def correlation_test_left_tail(r,n,a):
 import math
 import scipy.stats
 df=n-2
 t_cal=round(r*math.sqrt((n-2)/(1-r*r)),4)
 tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
 p=round((scipy.stats.t.sf(abs(t_cal),df)),4)
 print(f"here we have given following information")
 print(f"r={r}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print("Ho: r=0 (correlation is insignificant)")
 print("H1: r<0 (negative correlation is significant)")
 print(" ")
 print("Test statistics:")
 print("t_cal=(r*sqrt((n-2)/(1-r^2))")
 print(f"t_cal=({r}*sqrt(({n}-2)/(1-({r})^2))={t_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"t_c={-tc} is critical value with df=n-1={n}-1={df} ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for t_c is  =-TINV({a*2},{df})")
 print(f"      and for Pvalue is  =TDIST(abs({t_cal}),{df},1)")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here t_cal >= t_c so do not reject null hypothesis")
 else: 
        print(f"here t_cal < t_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P-value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"r=0")
 else:
        print(f"r<0")
 

def correlation_test_right_tail(r,n,a):
 import math 
 import scipy.stats
 df=n-2
 t_cal=round(r*math.sqrt((n-2)/(1-r*r)),4)
 tc=abs(round(scipy.stats.t.ppf(q=a,df=df),2))
 p=round((1-scipy.stats.t.sf(abs(t_cal),df)),4)
 print(f"here we have given following information")
 print(f"r={r}; n={n}; alpha={a}")
 print(" ")
 print("Null and alternative:")
 print("Ho: r=0 (correlation is insignificant)")
 print("H1: r>0 (positive correlation is significant)")
 print(" ")
 print("Test statistics:")
 print("t_cal=(r*sqrt((n-2)/(1-r^2))")
 print(f"t_cal=({r}*sqrt(({n}-2)/(1-({r})^2))={t_cal}")
 print(" ")
 print("Cirtical value and Pvalue:")
 print(f"t_c={tc} is critical value with df=n-1={n}-1={df} ")
 print(f"P={p} is p value of test statistic  ")
 print(f"Note: Excel command for t_c is  =TINV({a*2},{df})")
 print(f"      and for Pvalue is  =1-TDIST(abs({t_cal}),{df},1)")
 print(" ")
 print("Decision:")
 print("1]Based on cirtical value approch-")
 if p>a:
        print(f"here t_cal <= t_c so do not reject null hypothesis")
 else: 
        print(f"here t_cal > t_c so reject null hypothesis")
        
 print("")
 
 print("2]Based on P- value approch-")
 if p>a:
        print(f"here Pvalue >= alpha so do not reject null hypothesis")
 else: 
        print(f"here Pvalue < alpha  so reject null hypothesis")
 print("")
 print("Conclusion:")
 if p>a:
        print(f"r=0")
 else:
        print(f"r>0")


#----------------Variance test----------------------------------------------------------------------------------------------------------------


def One_sample_var_two_tail(pvar,svar,n,a):
  import math
  from scipy.stats.distributions import chi2
  df=n-1    
  x2_cal=round(((n-1)*svar/pvar),4)
  x2_L=round(chi2.ppf(a/2, df),4)
  x2_U=round(chi2.ppf(1-a/2, df),4)
  print(f"here we have given following information")
  print(f"Sigma^2={pvar}; S^2={svar}; n={n}; alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:Sigma^2={pvar}")
  print(f"H1:Sigma^2≠{pvar}")
  print(" ")
  print("Test statistics:")
  print("t_cal=((n-1)*s^2/sigma^2)")
  print(f"t_cal=(({n}-1)*{svar}/{pvar})={x2_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"for given alpha={a}, df={n}-1={df}")
  print(f"(Lower chisqure critical value) x2_L={x2_L}      excel command =CHIINV(1-{a}/2,{df})")
  print(f"(Upper chisqure critical value) x2_U={x2_U}      excel command =CHIINV({a}/2,{df})")
  print(" ")
  print("Decision:")
  print("Based on cirtical value approch-")
  if ((x2_cal>=x2_L)&(x2_cal<=x2_U)):
         print(f"here x2_cal={x2_cal} lies in the range (x2_L={x2_L}, x2_U={x2_U}) so do not reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma^2={pvar}")
        
  else: 
         print(f"here x2_cal={x2_cal} do not lies in the range (x2_L={x2_L}, x2_U={x2_U}) so reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma^2≠{pvar}")
        
 
  
def One_sample_var_right_tail(pvar,svar,n,a):
  import math
  from scipy.stats.distributions import chi2
  df=n-1    
  x2_cal=round(((n-1)*svar/pvar),4)
  x2_U=round(chi2.ppf(1-a, df),4)
  print(f"here we have given following information")
  print(f"Sigma^2={pvar}; S^2={svar}; n={n}; alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:Sigma^2={pvar}")
  print(f"H1:Sigma^2>{pvar}")
  print(" ")
  print("Test statistics:")
  print("t_cal=((n-1)*s^2/sigma^2)")
  print(f"t_cal=(({n}-1)*{svar}/{pvar})={x2_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"for given alpha={a}, df={n}-1={df}")
  print(f"x2_U={x2_U}      excel command  =CHIINV({a},{df})")
  print(" ")
  print("Decision:")
  print("Based on cirtical value approch-")
  if (x2_cal>x2_U):
         print(f"here x2_cal={x2_cal} > x2_U={x2_U} so  reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma^2>{pvar}")
  else: 
         print(f"here x2_cal={x2_cal} < x2_U={x2_U} so do not reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma^2={pvar}")


def One_sample_var_left_tail(pvar,svar,n,a):
  import math
  from scipy.stats.distributions import chi2
  df=n-1    
  x2_cal=round(((n-1)*svar/pvar),4)
  x2_L=round(chi2.ppf(a, df),4)
  print(f"here we have given following information")
  print(f"Sigma^2={pvar}; S^2={svar}; n={n}; alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:Sigma^2={pvar}")
  print(f"H1:Sigma^2<{pvar}")
  print(" ")
  print("Test statistics:")
  print("t_cal=((n-1)*s^2/sigma^2)")
  print(f"t_cal=(({n}-1)*{svar}/{pvar})={x2_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"for given alpha={a},df={df}-1={df}")
  print(f"x2_L={x2_L}      excel command  =CHIINV(1-{a},{df})")
  print(" ")
  print("Decision:")
  print("Based on cirtical value approch-")
  if (x2_cal<x2_L):
         print(f"here x2_cal={x2_cal} < x2_L={x2_L} so  reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma^2<{pvar}")
  else: 
         print(f"here x2_cal={x2_cal} > x2_L={x2_L} so do not reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma^2={pvar}")

    


def Two_sample_var_two_tail(svar1,svar2,n1,n2,a):
  import math
  from scipy import stats 
  df_1=n1-1
  df_2=n2-1
  F_cal=round((svar1/svar2),4)
  F_L=round(stats.f.ppf(q=a/2,dfn=df_1,dfd=df_2),4)
  F_U=round(stats.f.ppf(q=1-a/2,dfn=df_1,dfd=df_2),4)
  print(f"here we have given following information")
  print(f"S1^2={svar1};n1={n1}; S2^2={svar2}; n2={n2},; alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:Sigma1^2=Sigma2^2")
  print(f"H1:Sigma1^2≠Sigma2^2")
  print(" ")
  print("Test statistics:")
  print(f"F_cal=(S1^2/S2^2)=({svar1}/{svar2})={F_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"for given alpha={a},df1={n1}-1={df_1},df2={n2}-1={df_2}")
  print(f"F_L={F_L}      excel command  =FINV(1-{a}/2,{df_1},{df_2})")
  print(f"F_U={F_U}      excel command  =FINV({a}/2,{df_1},{df_2})")
  print(" ")
  print("Decision:")
  print("Based on cirtical value approch-")
  if ((F_cal>=F_L)&(F_cal<=F_U)):
         print(f"here F_cal={F_cal} lies in the range (F_L={F_L}, F_U={F_U}) so do not reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma1^2=Sigma2^2")
        
  else: 
         print(f"here F_cal={F_cal} do not lies in the range (F_L={F_L}, F_U={F_U}) so reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"H1:Sigma1^2≠Sigma2^2")
         

def Two_sample_var_right_tail(svar1,svar2,n1,n2,a):
  import math
  from scipy import stats
  df_1=n1-1
  df_2=n2-1
  F_cal=round((svar1/svar2),4)
  F_U=round(stats.f.ppf(q=1-a,dfn=df_1,dfd=df_2),4)
  print(f"here we have given following information")
  print(f"S1^2={svar1}; n1={n1}; S2^2={svar2}; n2={n2},; alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:Sigma1^2=Sigma2^2")
  print(f"H1:Sigma1^2>Sigma2^2")
  print(" ")
  print("Test statistics:")
  print(f"F_cal=(S1^2/S2^2)=({svar1}/{svar2})={F_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"for given alpha={a},  df1={n1}-1={df_1},  df2={n2}-1={df_2}")
  print(f"F_U={F_U}      excel command  =FINV({a},{df_1},{df_2})")
  print(" ")
  print("Decision:")
  print("Based on cirtical value approch-")
  if (F_cal<=F_U):
         print(f"here F_cal={F_cal} <= F_U={F_U} so do not reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma1^2=Sigma2^2")
         
  else: 
         print(f"here F_cal={F_cal} > F_U={F_U} so  reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"H1:Sigma1^2>Sigma2^2")
        

def Two_sample_var_left_tail(svar1,svar2,n1,n2,a):
  import math
  from scipy import stats
  df_1=n1-1
  df_2=n2-1
  F_cal=round((svar1/svar2),4)
  F_L=round(stats.f.ppf(q=a,dfn=df_1,dfd=df_2),4)
  print(f"here we have given following information")
  print(f"S1^2={svar1};n1={n1}; S2^2={svar2}; n2={n2},; alpha={a}")
  print(" ")
  print("Null and alternative:")
  print(f"Ho:Sigma1^2=Sigma2^2")
  print(f"H1:Sigma1^2<Sigma2^2")
  print(" ")
  print("Test statistics:")
  print(f"F_cal=(S1^2/S2^2)=({svar1}/{svar2})={F_cal}")
  print(" ")
  print("Cirtical value and Pvalue:")
  print(f"for given alpha={a},  df1={n1}-1={df_1},  df2={n2}-1={df_2}")
  print(f"F_L={F_L}      excel command  =FINV(1-{a},{df_1},{df_2})")
  print(" ")
  print("Decision:")
  print("Based on cirtical value approch-")
  if (F_cal>=F_L):
         print(f"here F_cal={F_cal} >= F_L={F_L} so do not reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"Ho:Sigma1^2=Sigma2^2")
        
  else: 
         print(f"here F_cal={F_cal} < F_L={F_L} so  reject null hypothesis")
         print(" ")
         print("Conclusion:")
         print(f"H1:Sigma1^2<Sigma2^2")
        

 
#------------------------CONFIDENCE INTERVAL--------------------------------------------------------------------------------------------------------------

def Confidence_interval_one_sample_proportion(x,n,l):
    import math
    import scipy.stats
    z=abs(round(scipy.stats.norm.ppf((100-l)/200),2))
    p_cap=round(x/n,2)
    ll=round(p_cap-z*math.sqrt(p_cap*(1-p_cap)/n),4)
    ul=round(p_cap+z*math.sqrt(p_cap*(1-p_cap)/n),4)
    ME=round(z*math.sqrt(p_cap*(1-p_cap)/n),4)
    print(f"here we have given following information")
    print(f"x={x}; n={n}; sample proprtion p_cap=x/n=({x}/{n})={p_cap}; confidence level={l}%")
    print("")
    print(f"for given confidence level we get cirtical value z_c={z}")
    print(f"Critical Value is obtain from excel with command=NORMSINV({((100-l)/100)/2})")
    print("")
    print(f"{l}% confidence interval for one sample porportion is given by ")
    print(f"CI=p_cap ± z*sqrt(p_cap*(1-p_cap)/n)")
    print(f"CI={p_cap} ± {z}*sqrt({p_cap}*(1-{p_cap})/{n})")
    print(f"CI={p_cap} ± {ME}")
    print(f"Lower limit={p_cap}-{ME}={ll}")
    print(f"Upper limit={p_cap}+{ME}={ul}")
    print("")
    print(f"So {l}% Confidence interval for one sample proportion is ( {ll} < P < {ul} )")
  
def Confidence_interval_two_sample_proportion(x1,n1,x2,n2,l):
    import math
    import scipy.stats
    z=abs(round(scipy.stats.norm.ppf((100-l)/200),2))
    p1_cap=round(x1/n1,4)
    p2_cap=round(x2/n2,4)
    pd=round(p1_cap-p2_cap,4)
    ll=round((p1_cap-p2_cap)-z*math.sqrt((p1_cap*(1-p1_cap)/n1)+(p2_cap*(1-p2_cap)/n2)),4)
    ul=round((p1_cap-p2_cap)+z*math.sqrt((p1_cap*(1-p1_cap)/n1)+(p2_cap*(1-p2_cap)/n2)),4)
    ME=round(z*math.sqrt((p1_cap*(1-p1_cap)/n1)+(p2_cap*(1-p2_cap)/n2)),4)
    print(f"here we have given following information")
    print(f"x1={x1}; n={n1}; sample proprtion p1_cap=x1/n1=({x1}/{n1})={p1_cap}")
    print(f"x2={x2}; n={n2}; sample proprtion p2_cap=x2/n2=({x2}/{n2})={p2_cap}") 
    print(f"confidence level={l}%")
    print("")
    print(f"for given confidence level we get cirtical value z_c={z}")
    print(f"Critical Value is obtain from excel with command=NORMSINV({((100-l)/100)/2})")
    print("")
    print(f"{l}% confidence interval for one sample porportion is given by ")
    print(f"CI=(p1_cap-p2cap) ± z*sqrt((p1_cap*(1-p1_cap)/n1)+(p2_cap*(1-p2_cap)/n2))")
    print(f"CI=({p1_cap}-{p2_cap}) ± {z}*sqrt(({p1_cap}*(1-{p1_cap})/{n1})+({p2_cap}*(1-{p2_cap})/{n2}))")
    print(f"CI={pd} ± {ME}")
    print(f"Lower limit={pd}-{ME}={ll}")
    print(f"Upper limit={pd}+{ME}={ul}")
    print("")
    print(f"So {l}% Confidence interval for differnce in proportion is ( {ll} < pd < {ul} )")
    
def Confidence_interval_var_ratio(s1,n1,s2,n2,l):
    import math
    from scipy.stats import f
    a=(100-l)/100    
    df_1=n1-1
    df_2=n2-1
    F_L=round(f.ppf(q=a/2,dfn=df_2,dfd=df_1),4)
    F_U=round(f.ppf(q=1-a/2,dfn=df_2,dfd=df_1),4)
    LL=round(((s1*s1)/(s2*s2))*F_L,4)
    UL=round(((s1*s1)/(s2*s2))*F_U,4)
    print(f"here we have given following information")
    print(f"S1={s1};n1={n1}; S2={s2}; n2={n2},; confidence level={l}")
    print(" ")
    print(f"for given confidence {l}% required Cirtical value obtain as below")
    print(f"F_L={F_L}      excel command  =FINV(1-{a}/2,{df_2},{df_1})")
    print(f"F_U={F_U}      excel command  =FINV({a}/2,{df_2},{df_1})")
    print(" ")
    print(" confidence interval for Ratio of variance is given by,")
    print(f"Lower limit=((s1^2/s2^2)*F_L)=(({s1}^2/{s2}^2)*{F_L})={LL}")
    print(f"Upper limit=((s1^2/s2^2)*F_U)=(({s1}^2/{s2}^2)*{F_U})={UL}")
    print(" ")
    print(f"{l}% Confidence intrerval for Ratio of var's is ")
    print(f" {LL} <(sigma1^2/sigma2^2)< {UL}") 

def Confidence_interval_mean_unknown_var(xbar,s,n,l):
    import math
    import scipy.stats
    df=n-1
    tc=abs(round(scipy.stats.t.ppf(q=(100-l)/200,df=df),2))
    ll=round(xbar-tc*(s/math.sqrt(n)),4)
    Ul=round(xbar+tc*(s/math.sqrt(n)),4)
    ME=round(tc*math.sqrt(s/n),4)
    print(f"here we have given following information")
    print(f"xbar={xbar};s={s};n={n};confidence level={l}%")
    print("")
    print(f"for given confidence level we get cirtical value t_c={tc}")
    print(f"Critical Value is obtain from excel with command=TINV({(100-l)/100},{df})")
    print("")
    print(f"{l}% confidence interval for mean when population sd not known is given by ")
    print("CI=xbar ± t*(s/sqrt(n))")
    print(f"CI={xbar} ± {tc}*({s}/sqrt({n}))")
    print(f"CI={xbar} ± {ME}")
    print(f"Lower limit={xbar}-{ME}={ll}")
    print(f"Upper limit={xbar}+{ME}={Ul}")
    print("")
    print(f"So {l}% Confidence interval for mean when var unkown is ( {ll} < xbar < {Ul} )")


def Confidence_interval_diff_mean_unknown_var(x1bar,x2bar,s1,s2,n1,n2,l):
    import math
    import scipy.stats
    df=n1+n2-2
    t=abs(round(scipy.stats.t.ppf(q=(100-l)/200,df=df),4))
    sp=round(math.sqrt(((n1-1)*s1*s1+(n2-1)*s2*s2)/df),4)
    se=round(sp*math.sqrt(1/n1+1/n2),4)
    ll=round((x1bar-x2bar)-t*se,3)
    Ul=round((x1bar-x2bar)+t*se,3)
    ME=round(t*se,4)
    print(f"here we have given following information")
    print(f"x1bar={x1bar}; n1={n1};s1={s1};x2bar={x2bar};n2={n2};s2={s2};confidence level={l}%")
    print("")
    print("pooled sd and standard error is calculated as")
    print("sp=sqrt(((n1-1)*s1^2+(n2-1)*s2^2)/(n1+n2-2))")
    print(f"  =sqrt((({n1}-1)*{s1}^2+({n2}-1)*{s2}^2)/{df})={sp}")
    print("se=sp*sqrt(1/n1+1/n2)")
    print(f"  ={sp}*sqrt(1/{n1}+1/{n2})={se}")
    print("")
    print(f"for given confidence level we get cirtical value t_c={t}")
    print(f"Critical Value is obtain from excel with command=TINV({((100-l)/100)},{df})")
    print("")
    print(f"{l}% confidence interval for difference mean when population sd unknown is given by ")
    print("CI=(x1bar-x2bar) ± t*se")
    print(f"CI={x1bar-x2bar} ± {t}*se")
    print(f"CI={x1bar-x2bar} ± {ME}")
    print(f"Lower limit={x1bar-x2bar}-{ME}={ll}")
    print(f"Upper limit={x1bar-x2bar}+{ME}={Ul}")
    print("")
    print(f"So {l}% Confidence interval for mean difference when var's unknown is ( {ll} < x1bar-x2bar < {Ul} )")
    

def Confidence_interval_var(s2,n,l):
    import math
    from scipy.stats import chi2
    a=(100-l)/100    
    df=n-1   
    x2_L=round(chi2.ppf(1-a/2, df),4)
    x2_U=round(chi2.ppf(a/2, df),4)
    LL=round(((n-1)*s2/x2_L),4)
    UL=round(((n-1)*s2/x2_U),4)
    print(f"here we have given following information")
    print(f"S^2={s2}; n={n}; confidence level={l}")
    print(" ")
    print(f"for given confidence {l}% required Cirtical value obtain as below")
    print(f"x2_Lower={x2_L}      excel command   =CHIINV({a}/2,{df})")
    print(f"x2_Upper={x2_U}      excel command   =CHIINV(1-{a}/2,{df})")
    print(" ")
    print(" confidence interval for variance is given by,")
    print(f"Lower limit=((n-1)*s^2/x2_Lower)=(({n}-1)*{s2}/{x2_L})={LL}")
    print(f"Upper limit=((n-1)*s^2/x2_Upper)=(({n}-1)*{s2}/{x2_U})={UL}")
    
def Confidence_interval_mean_known_var(xbar,sigma,n,l):
    import math
    import scipy.stats
    Z=abs(round(scipy.stats.norm.ppf((100-l)/(2*100)),4))
    ll=round(xbar-Z*(sigma/math.sqrt(n)),4)
    Ul=round(xbar+Z*(sigma/math.sqrt(n)),4)
    ME=round(Z*(sigma/math.sqrt(n)),4)
    print(f"here we have given following information")
    print(f"xbar={xbar}; n={n}; population sd(sigma)={sigma}; confidence level={l}%")
    print("")
    print(f"for given confidence level we get cirtical value z_c={Z}")
    print(f"Critical Value is obtain from excel with command=NORMSINV({((100-l)/100)/2})")
    print("")
    print(f"{l}% confidence interval for mean when population sd known is given by ")
    print("CI=xbar ± z*(sigma/sqrt(n))")
    print(f"CI={xbar} ± {Z}*({sigma}/sqrt({n}))")
    print(f"CI={xbar} ± {ME}")
    print(f"Lower limit={xbar}-{ME}={ll}")
    print(f"Upper limit={xbar}+{ME}={Ul}")
    print("")
    print(f"So {l}% Confidence interval for mean when sigma known is ( {ll} < xbar < {Ul} )")
    
def Confidence_interval_diff_mean_known_var(x1bar,x2bar,sigma1,sigma2,n1,n2,l):
    import math
    import scipy.stats
    Z=abs(round(scipy.stats.norm.ppf((100-l)/(2*100)),4))
    ll=round((x1bar-x2bar)-Z*math.sqrt((sigma1*sigma1/n1)+(sigma2*sigma2/n2)),3)
    Ul=round((x1bar-x2bar)+Z*math.sqrt((sigma1*sigma1/n1)+(sigma2*sigma2/n2)),3)
    ME=round(Z*math.sqrt((sigma1*sigma1/n1)+(sigma2*sigma2/n2)),6)
    print(f"here we have given following information")
    print(f"x1bar={x1bar}; n1={n1};sigma1={sigma1};x2bar={x2bar};n2={n2};sigma2={sigma2};confidence level={l}%")
    print("")
    print(f"for given confidence level we get cirtical value z_c={Z}")
    print(f"Critical Value is obtain from excel with command=NORMSINV({((100-l)/100)/2})")
    print("")
    print(f"{l}% confidence interval for mean when population sd known is given by ")
    print("CI=(x1bar-x2bar) ± Z*math.sqrt((sigma1^2/n1)+(sigma2^2/n2))")
    print(f"CI=({x1bar}-{x2bar}) ± {Z}*math.sqrt(({sigma1}^2/{n1})+({sigma2}^2/{n2}))")
    print(f"CI={x1bar-x2bar} ± {ME}")
    print(f"Lower limit={x1bar-x2bar}-{ME}={ll}")
    print(f"Upper limit={x1bar-x2bar}+{ME}={Ul}")
    print("")
    print(f"So {l}% Confidence interval for mean difference when var's known is ( {ll} < x1bar-x2bar < {Ul} )")
  

#----------------------------CHISQURE TEST-------------------------------------------------------------------------------------------------------------

def Chisqure_test_independentness(Rowname,Colname,X,a,ho,h1):
    import pandas as pd
    import numpy as np
    from scipy  import stats
    x=np.array(X)
    rowname=np.array(Rowname)
    colname=np.array(Colname)
    of=pd.DataFrame(x)
    of.index=rowname
    of.columns=colname
    r=of.shape[0]
    c=of.shape[1]
    d=of.to_numpy()
    G=float(np.sum(d))
    SR=d.sum(axis=1)
    R= np.reshape(SR, -1)
    SC=d.sum(axis=0)
    C= np.reshape(SC, -1)
    of.loc['Col_Total',:]= of.sum(axis=0)
    of.loc[:,'Row_Total'] = of.sum(axis=1)
    ef= [[0 for i in range(c)] for j in range(r)]
    for i in range(0,r):
        for j in range(0,c):
                ef[i][j]=float(R[i]*C[j]/G)
    eef=pd.DataFrame(ef)
    eef.index=rowname
    eef.columns=colname 
    chisq=sum(map(sum,((d-ef)**2)/ef))
    df=(r-1)*(c-1)
    x2_cr=round(stats.chi2.ppf(1-a, df),4)
    p=stats.distributions.chi2.sf(chisq , df)
    
    print("##Null and alternative:")
    print(f"ho: {ho}")
    print(f"h1: {h1}")
    print(" ")
    print("Observed frequencies(oi):")
    print(of)
    print(" ")
    print("Expected frequencies(ei): ")
    print(eef)
    print(" ")
    print("Calculation of Expected frequencies(ei) :")    
    print("formula is e(i,j)=(ri*cj)/N")
    print(" ")
    for i in range(0,r):
        for j in range(0,c):                
                print("e("+str(i)+","+str(j)+")=("+str(R[i])+"*"+str(C[j])+")/"+str(G)+"="+str(round(ef[i][j],4)))   
                
    print(" ")
    print("##Test statistics:")
    print(f"x2_cal=Σ(oi-ei)^2/ei=({np.round(d[0][0],3)}-{np.round(ef[0][0],3)})^2/{np.round(ef[0][0],3)}+....+({np.round(d[r-1][c-1],3)}-{np.round(ef[r-1][c-1],3)})^2/{np.round(ef[r-1][c-1],3)}={round(chisq,4)}")
    
    print(" ")
    print("##Cirtical value and Pvalue:")
    print(" ")
    print(f"degrees of freedom=df=(r-1)*(c-1)=({r}-1)*({c}-1)={df}")
    print(f"x2_cr={x2_cr}   obtain with excel command  =CHIINV({a},{df})  ")
    print(f"Pvalue={round(p,5)}      obtain with excel command=CHIDST({round(chisq,4)},{df}) ")   
    print(" ")
    print("##Decision:")
    print(" ")
    print("Based on cirtical value approch-")
    if (chisq>x2_cr):
            print(f"here x2_cal > x2_cr={x2_cr} so  reject null hypothesis")
            print(" ")
            
    else: 
            print(f"here x2_cal < x2_cr={x2_cr} so do not reject null hypothesis")
            print(" ")
            
            
    print("Based on Pvalue value approch-")
    if (p>=a):
            print(f"here Pvalue > a={a} so do not reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H0: {ho}")
            
    else: 
            print(f"here Pvalue < alpha={a} so  reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H1: {h1}")
            

def Chisqure_test_equality_of_proportion(O,Rowname,a,Ho,H1):
    import math 
    from scipy  import stats
    import pandas as pd
    import numpy as np
    o=np.array(O)
    rowname=np.array(Rowname)
    n=sum(o)
    l=len(o)
    df=l-1
    pi=(1/l)
    e=np.repeat(n*pi,l, axis=0)
    x=((o-e)**2)/e
    chisq=sum(x)
    x2_cr=round(stats.chi2.ppf(1-a, df),4)
    p=stats.distributions.chi2.sf(chisq , df)
    print("##Null and alternative hypothesis:")
    print(f"Ho:  {Ho}")
    print(f"H1:  {H1}")
    print(" ")
    print(f"n=sum(oi)={n}")
    print(f"Ei=n*pi=n*(1/k)={n}*(1/{l})={round(n*pi,4)}")
    print(" ")
    print(f"************************TABLE************************************")
    data={'obs freq(oi)':np.round_(o,4),'Exp freq(Ei=n*pi)':np.round_(e,4),'(oi-ei)^2/ei':np.round_(x,4)}
    dff= pd.DataFrame(data)
    dff.index=rowname
    print(dff)
    print(" ")
    print("##Test statistic:")
    print(" ")
    print(f"x2_cal=Σ(oi-ei)^2/ei=({np.round(o[0],3)}-{np.round(e[0],3)})^2/{np.round(e[0],3)}+....+({np.round(o[l-1],3)}-{np.round(e[l-1],3)})^2/{np.round(e[l-1],3)}={round(chisq,4)}")

    print(" ")
    print("##Cirtical value and Pvalue:")
    print(" ")
    print(f"x2_cr={x2_cr}   obtain with excel command  =CHIINV({a},{df})  ")
    print(f"Pvalue={round(p,4)}      obtain with excel command=CHIDST({round(chisq,4)},{df}) ")   
    print(" ")
    print("##Decision:")
    print(" ")
    print("Based on cirtical value approch-")
    if (chisq>x2_cr):
            print(f"here x2_cal > x2_cr={x2_cr} so  reject null hypothesis")
            print(" ")
            
    else: 
            print(f"here x2_cal < x2_cr={x2_cr} so do not reject null hypothesis")
            print(" ")
            
            
    print("Based on Pvalue value approch-")
    if (p>=a):
            print(f"here Pvalue > a={a} so do not reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H0: {Ho}")
            
    else: 
            print(f"here Pvalue < alpha={a} so  reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H1: {H1}")
            
def Chisqure_test_fitting_of_poisson(X,O,a,Ho,H1):
    import math 
    from scipy  import stats
    import pandas as pd
    import numpy as np
    x=np.array(X)
    o=np.array(O)    
    n=sum(o)
    l=len(o)
    df=l-2
    Xbar=round(sum(X*o)/sum(o),4)
    p=stats.poisson.pmf(X, mu=Xbar)
    e=n*p
    x=((o-e)**2)/e
    chisq=sum(x)
    x2_cr=round(stats.chi2.ppf(1-a, df),4)
    p=stats.distributions.chi2.sf(chisq , df)
    print("##Null and alternative hypothesis:")
    print(f"Ho:  {Ho}")
    print(f"H1:  {H1}")
    print(" ")
    print("first we find xbar which is estimator for lamda (poisson parameter)")
    print(f"lamda=xbar=Σ(x*o)/Σ(o)={sum(X*o)}/{sum(o)}={Xbar}") 
    print("Formula for expected freq Ei=n*pi")
    print(f"Where  n=sum(oi)={n}  and pi are pi poisson probabilities with lamda={Xbar} as follow, ")
    for i in X:
        print("p(x="+str(i)+")=( exp(-lamda)*lamda^"+str(i)+" )/"+str(i)+"!="+str(round(stats.poisson.pmf(i, mu=2),4)))
    print(" ")
    
    print(f"************************TABLE************************************")
    data={'X':X,'obs freq F (oi)':np.round_(o,4),'Exp freq(Ei=n*pi)':np.round_(e,4),'(oi-ei)^2/ei':np.round_(x,4)}
    dff= pd.DataFrame(data)
    print(dff)
    print(" ")
    print("##Test statistic:")
    print(" ")
    print(f"x2_cal=Σ(oi-ei)^2/ei=({np.round(o[0],3)}-{np.round(e[0],3)})^2/{np.round(e[0],3)}+....+({np.round(o[l-1],3)}-{np.round(e[l-1],3)})^2/{np.round(e[l-1],3)}={round(chisq,4)}")

    print(" ")
    print("##Cirtical value and Pvalue:")
    print(" ")
    print(f"x2_cr={x2_cr}   obtain with excel command  =CHIINV({a},{df})  ")
    print(f"Pvalue={round(p,4)}      obtain with excel command=CHIDST({round(chisq,4)},{df}) ")   
    print(" ")
    print("##Decision:")
    print(" ")
    print("Based on cirtical value approch-")
    if (chisq>x2_cr):
            print(f"here x2_cal > x2_cr={x2_cr} so  reject null hypothesis")
            print(" ")
            
    else: 
            print(f"here x2_cal < x2_cr={x2_cr} so do not reject null hypothesis")
            print(" ")
            
            
    print("Based on Pvalue value approch-")
    if (p>=a):
            print(f"here Pvalue > a={a} so do not reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H0: {Ho}")
            
    else: 
            print(f"here Pvalue < alpha={a} so  reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H1: {H1}")
            
def Chisqure_test_Observed_Expected_equality_test(O,E,a,Ho,H1,Rowname):
    import math 
    from scipy  import stats
    import pandas as pd
    import numpy as np
    o=np.array(O)
    e=np.array(E)
    rowname=np.array(Rowname)
    n=sum(o)
    l=len(o)
    df=l-1
    x=((o-e)**2)/e
    chisq=sum(x)
    x2_cr=round(stats.chi2.ppf(1-a, df),4)
    p=stats.distributions.chi2.sf(chisq , df)
    print("##Null and alternative hypothesis:")
    print(f"Ho:  {Ho}")
    print(f"H1:  {H1}")
    print(" ")
    print(f"n=sum(oi)={n}")
    print("Ei=n*pi")
    print(" ")
    print(f"************************TABLE************************************")
    data={'obs freq(oi)':np.round_(o,4),'Exp freq(Ei)':np.round_(e,4),'(oi-ei)^2/ei':np.round_(x,4)}
    dff= pd.DataFrame(data)
    dff.index=rowname
    print(dff)
    
    print(" ")
    print("##Test statistic:")
    print(" ")
    print(f"x2_cal=Σ(oi-ei)^2/ei=({np.round(o[0],3)}-{np.round(e[0],3)})^2/{np.round(e[0],3)}+....+({np.round(o[l-1],3)}-{np.round(e[l-1],3)})^2/{np.round(e[l-1],3)}={round(chisq,4)}")

    print(" ")
    print("##Cirtical value and Pvalue:")
    print(" ")
    print(f"x2_cr={x2_cr}   obtain with excel command  =CHIINV({a},{df})  ")
    print(f"Pvalue={round(p,4)}      obtain with excel command=CHIDST({round(chisq,4)},{df}) ")   
    print(" ")
    print("##Decision:")
    print(" ")
    print("Based on cirtical value approch-")
    if (chisq>x2_cr):
            print(f"here x2_cal > x2_cr={x2_cr} so  reject null hypothesis")
            print(" ")
            
    else: 
            print(f"here x2_cal < x2_cr={x2_cr} so do not reject null hypothesis")
            print(" ")
            
            
    print("Based on Pvalue value approch-")
    if (p>=a):
            print(f"here Pvalue > a={a} so do not reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H0: {Ho}")
            
    else: 
            print(f"here Pvalue < alpha={a} so  reject null hypothesis")
            print(" ")
            print("##Conclusion:")
            print(f"H1: {H1}")


#----------------------------Regression ---------------------------------------------------------------------------

 
def Regression_stepbystep(X,Y,xo,l):
     import math 
     from scipy  import stats
     import pandas as pd
     import numpy as np
     x=np.array(X)
     y=np.array(Y)
     n=len(x)
     sumx=sum(x)  
     sumy=sum(y)
     sumx2=sum(x*x)
     sumy2=sum(y*y)
     sumxy=sum(x*y)
     xbar=sum(x)/n
     ybar=sum(y)/n
     ssxx=sum((x-xbar)*(x-xbar))
     ssyy=sum((y-ybar)*(y-ybar))
     ssxy=sum((x-xbar)*(y-ybar))
     r=(ssxy/math.sqrt(ssxx*ssyy))
     Slope=(ssxy/ssxx)
     Intercept=(ybar-Slope*xbar)
     yo=Intercept+Slope*xo
     SST=ssyy
     SSR=Slope*ssxy
     SSE=ssyy-SSR
     MSR=SSR
     MSE=SSE/(n-2)
     sigma=math.sqrt(MSE)
     F=MSR/MSE
     FC=round(stats.f.ppf(q=1-0.05,dfn=1,dfd=n-2),4)
     R_2=round(SSR/SST,4)
     Adj_R_2=round(1-((1-R_2)*(n-1)/(n-1-1)),4)
     t_c=abs(round(stats.t.ppf(q=(100-l)/200,df=n-1-1),6))
     LL=yo-t_c*sigma*math.sqrt(1+1/n+(xo-xbar)*(xo-xbar)/ssxx )
     UL=yo+t_c*sigma*math.sqrt(1+1/n+(xo-xbar)*(xo-xbar)/ssxx )
     LLc=yo-t_c*sigma*math.sqrt(1/n+(xo-xbar)*(xo-xbar)/ssxx )
     ULc=yo+t_c*sigma*math.sqrt(1/n+(xo-xbar)*(xo-xbar)/ssxx )
    
     print(f"here we have given following information")
     data={'X':x,'Y':y,'x^2':x*x,'y^2':y*y,'x*y':x*y}
     df= pd.DataFrame(data)
     dff={'SV':['SSR','SSE','SST'],'df':['1',n-2,n-1,],'SS':[SSR,SSE,SST],'MSS':[MSR,MSE,'.'],'F statitics':[F,'.','.'],'F critical':[FC,'.','.',]}
     dff= pd.DataFrame(dff)
     print(df)
     print(" ")
     print(f"from table we calculate sum for each columns")
     print(" ")
     print(f"Σx={round(sumx,4)}; Σy={round(sumy,4)}; Σx^2={round(sumx2,4)}; Σy^2={round(sumy2,4)}; Σx*y={round(sumxy,4)}")
     print(" ")
     print("************calcuation of mean and sum of sqaure***************")
     print(f"xbar=(Σx/n)=({round(sumx,4)}/{n})={round(xbar,4)}")
     print(f"ybar=(Σy/n)=({round(sumy,4)}/{n})={round(ybar,4)}")
     print(f"SSxx=Σx^2-(Σx)^2/n={round(sumx2,4)}-({round(sumx,4)})^2/{n}={round(ssxx,4)}")
     print(f"SSyy=Σy^2-(Σy)^2/n={round(sumy2,4)}-({round(sumy,4)})^2/{n}={round(ssyy,4)}")
     print(f"SSxy=Σxy-(Σy)(Σx)/n={round(sumxy,4)}-({round(sumx,4)}*{round(sumy,4)})/{n}={round(ssxy,4)}")
     print(" ")
     print("************calcuation of correlation*************************")
     print(f"r=SSxy/sqrt(SSxx*SSyy)=({round(ssxy,4)}/sqrt({round(ssxx,4)}*{round(ssyy,4)}))={round(r,4)}")
     print(" ")
     print("************calcuation of Regression coeffcient ***************")
     print(f"slope=b1=(SSxy/SSxx)=({round(ssxy,4)}/{round(ssxx,4)})={round(Slope,4)}")
     print(f"intercept=bo=ybar-b1*xbar={round(ybar,4)}-{round(Slope,4)}*{round(xbar,4)}= {round(Intercept,4)}")
     print(" ")
     print("************Regression line is*********************************")
     print(f"Y= {round(Intercept,4)}+{round(Slope,4)}*x")
     print(" ")
     print(f"****************predicted value for x={xo} is *******************")
     print(f"Y= {round(Intercept,4)}+{round(Slope,4)}*{xo}={round(yo,4)}")
     print(" ")
     print(f"****************Calculation of ANOVA****************************")
     print(f"Sum of squres :")
     print(f"SST=ssyy={round(SST,4)};   SSR=slope*ssxy={round(SSR,4)};  SSE=SST-SSR={round(SST,4)}-{round(SSR)}={round(SSE,4)}")
     print(" ")
     print(f"Degress of fredom :")
     print(f" Df for SSR=k=1; Df for SSE=n-k-1={n-2};  Df for SST=n-1={n-1};")
     print(" ")
     print(f"Mean sum of squres :")
     print(f"MSR=(SSR/k)=({round(SSR)}/1)={round(MSR,4)};  MSE=(SSE/(n-k))=({round(SSE,4)}/({n}-2))={round(MSE,4)}")
     print(" ")
     print(f"Calculation of F statistics :")
     print(f"F statistics is F=({round(MSR,4)}/{round(MSE,4)})={round(F,4)}")
     print(" ")
     print(f"***************(Analysis of variance) ANOVA****************************")
     print(dff)
     print(" ")
     print(f"**************Conclusion****************************************")
     if (F<=FC):
             print(f"Decision: here F_cal <= F_cr so do not reject null hypothesis")
             print("Conclusion:")
             print(f"Coeffcien are significantly differ from zero")
            
     else: 
             print(f"Decision: here F_cal > F_cr so  reject null hypothesis")
             print("Conclusion: Coeffcien does not significantly differ from zero")
            
     print(" ")        
     print(f"***********R squre(Coeffcient of determination)****************************")
     print(f"R^2=(SSR/TSS)=({round(SSR,4)}/{round(SST,4)})={R_2}")
     print(f"Interpretation: {(R_2*100)}% variation of dependent variable is explaned by independent variable")
     print(" ")
     print(f"********************Adj R squre(Adjusted R^2)*********************")
     print(f"Adj_R^2=1-((1-R^2)*(n-1)/(n-k-1))=1-({(1-R_2)}*{(n-1)}/{(n-1-1)})={Adj_R_2}")
     print(f"Interpretation: {(Adj_R_2*100)}% variation of dependent variable is explaned by independent variable")
     print(" ")
     print(f"********************Prediction interval*********************")
     print(f"Here we have,  n={n}, Confidence level={l}, df={n-1-1}")
     print(f"for given confidence level {l}% and df={n-1-1} t_ c value is tc={t_c} ")
     print(" ")
     print(f"LL=ycap-t_c*sigma*sqrt(1+1/n+(xo-Xbar)^2/SSXX )")
     print(f"LL={round(yo,4)}-{t_c}*{round(sigma,4)}*sqrt(1+1/{n}+({xo}-{round(xbar,4)})^2/{round(ssxx,4)})={LL}")
     print(" ")
     print(f"UL=ycap+t_c*sigma*sqrt(1+1/n+(xo-Xbar)^2/SSXX )")
     print(f"UL={round(yo,4)}+{t_c}*{round(sigma,4)}*sqrt(1+1/{n}+({xo}-{round(xbar,4)})^2/{round(ssxx,4)})={UL}")
     print(" ")
     print(f"So {l}% prediction interval is ({round(LL,4)} , {round(UL,4)})")
     print(" ")
     print(" ")
     print(f"********************Confidence  interval for mean response*****************")
     print(f"Here we have,  n={n}, Confidence level={l}, df={n-1-1}")
     print(f"for given confidence level {l}% and df={n-1-1} t_ c value is tc={t_c} ")
     print(" ")
     print(f"LL=ycap-t_c*sigma*sqrt(1/n+(xo-Xbar)^2/SSXX )")
     print(f"LL={round(yo,4)}-{t_c}*{round(sigma,4)}*sqrt(1/{n}+({xo}-{round(xbar,4)})^2/{round(ssxx,4)})={LLc}")
     print(" ")
     print(f"UL=ycap+t_c*sigma*sqrt(1/n+(xo-Xbar)^2/SSXX )")
     print(f"UL={round(yo,4)}+{t_c}*{round(sigma,4)}*sqrt(1/{n}+({xo}-{round(xbar,4)})^2/{round(ssxx,4)})={ULc}")
     print(" ")
     print(f"So {l}% Confidence  interval for mean response is ({round(LLc,4)} , {round(ULc,4)})")

 
def Regression_given_xyx2y2xxn(x,y,x2,y2,xy,n):
    import numpy as np 
    import math
    import pandas as pd
    b1=(n*xy-x*y)/(n*x2-x**2)
    b0=(y-b1*x)/n

    print(f"Regression line:")
    print(" ")
    print("slope coefficient is  ")
    print(f"b1=(n∑xy-∑x*∑y)/(n*∑x^2-(∑x)^2)")
    print(f"b1=({n}*{xy}-{x}*{y})/({n}*{x2}-{x}^2) ")
    print(f"b1={round(b1,4)}")
    print(" ")
    print("Intercept coefficient is  ")
    print(f"b0=({y}-{round(b1,4)}*{x})/{n} ")
    print(f"b0= {round(b0,4)}")
    print("")
    print(f"So regression line is ycap={round(b0,4)}+{round(b1,4)}*x")
    

def Regression_mean_sd(r,xbar,ybar,sdx,sdy,xo):
     import math 
     from scipy  import stats
     import pandas as pd
     import numpy as np
     Slope=(r*sdy/sdx)
     Intercept=(ybar-Slope*xbar)
     yo=Intercept+Slope*xo
     print("We have given following information, ")
     print(f"r={r}; xbar={xbar}; ybar={ybar}; sdx={sdx}; sdy={sdy}")
     print("************calcuation of Regression coeffcient ***************")
     print(f"slope=b1=(r*sdy/sdx)=({r}*{sdy}/{sdx})={round(Slope,4)}")
     print(f"intercept=bo=ybar-b1*xbar={ybar}-{round(Slope,4)}*{xbar}={Intercept}")
     print(" ")
     print("************Regression line is*********************************")
     print(f"Y= {round(Intercept,4)}+{round(Slope,4)}*x")
     print(" ")
     print(f"****************predicted value for x={xo} is *******************")
     print(f"Y= {round(Intercept,4)}+{round(Slope,4)}*{xo}={round(yo,4)}")
     print(" ")
 

#-----------------------------Regression_Confidence_Interval-----------------------------------------------------------------------------------


def Regression_CI_given_MSE(b1,MSE,SSXX,n,k,l):
    import math
    import scipy.stats
    df=n-k-1
    a=round((100-l)/100,4)
    tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),4))
    SE=round(math.sqrt(MSE/SSXX),6)
    ME=round(tc*SE,4)
    ll=round(b1-ME,4)
    ul=round(b1+ME,4)
    print("here we have given following information")
    print(f"slope(b1)={b1}; MSE={MSE}; SSXX={SSXX};df=n-k-1=({n}-{k}-{1})={df}; level={l}%")
    print("")
    print(f"Standard error for slope is SE=sqrt(MSE/SSXX)=sqrt({MSE}/{SSXX})={SE}")
    print(" ")
    print(f"for given confidence level we get cirtical value t_c={tc}")
    print(f"Critical Value is obtain from excel with command=TINV({a},{df})")
    print("")
    print("")
    print(f"{l}% Confidence interval for regression paramter is given by")
    print("CI=b1 ± t_c*SE")
    print(f"CI={b1} ± {tc}*{SE}")
    print(f"CI={b1} ± {ME}")
    print(f"Lower limit={b1}-{ME}={ll}")
    print(f"Upper limit={b1}+{ME}={ul}")
    print("")
    print(f"So {l}% Confidence interval for regression paramter is given by ( {ll} < b1 < {ul} )")


def Regression_CI_given_SE(b1,SE,n,k,l):
    import math
    import scipy.stats
    df=n-k-1
    a=round((100-l)/100,4)
    tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),4))
    ME=round(tc*SE,4)
    ll=round(b1-ME,4)
    ul=round(b1+ME,4)
    print("here we have given following information")
    print(f"slope(b1)={b1}; S.E={SE}; df=n-k-1=({n}-{k}-{1})={df}; level={l}%")
    print(f"for given confidence level we get cirtical value t_c={tc}")
    print(f"Critical Value is obtain from excel with command=TINV({a},{df})")
    print("")
    print(f"{l}% Confidence interval for regression paramter is given by")
    print("CI=b1 ± t_c*SE")
    print(f"CI={b1} ± {tc}*{SE}")
    print(f"CI={b1} ± {ME}")
    print(f"Lower limit={b1}-{ME}={ll}")
    print(f"Upper limit={b1}+{ME}={ul}")
    print("")
    print(f"So {l}% Confidence interval for regression paramter is given by ( {ll} < b1 < {ul} )")

def Regression_CI_given_SSE(b1,SSE,SSXX,n,k,l):
    import math
    import scipy.stats
    df=n-k-1
    a=round((100-l)/100,4)
    tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
    MSE=round((SSE/df),6)
    SE=round(math.sqrt(MSE/SSXX),6)
    ME=round(tc*SE,4)
    ll=round(b1-ME,4)
    ul=round(b1+ME,4)
    print("here we have given following information")
    print(f"slope(b1)={b1}; MSE={MSE}; SSXX={SSXX};df=n-k-1=({n}-{k}-{1})={df}; level={l}%")
    print("")
    print(f"Standard error for slope is")
    print(f"MSE=sqrt(SSE/df)=sqrt({SSE}/{df})={MSE}")
    print(f"SE=sqrt(MSE/SSXX)=sqrt({MSE}/{SSXX})={SE}")
    print(" ")
    print(f"for given confidence level we get cirtical value t_c={tc}")
    print(f"Critical Value is obtain from excel with command=TINV({a},{df})")
    print("")
    print("")
    print(f"{l}% Confidence interval for regression paramter is given by")
    print("CI=b1 ± t_c*SE")
    print(f"CI={b1} ± {tc}*{SE}")
    print(f"CI={b1} ± {ME}")
    print(f"Lower limit={b1}-{ME}={ll}")
    print(f"Upper limit={b1}+{ME}={ul}")
    print("")
    print(f"So {l}% Confidence interval for regression paramter is given by ( {ll} < b1 < {ul} )")


 

#-----------------------------Regression_Testing-----------------------------------------------------------------------------------

def Regression_test_given_MSE(b1,MSE,SSXX,n,k,a):
     import math 
     import scipy.stats
     df=n-k-1
     SE=round(math.sqrt(MSE/SSXX),6)
     t_cal=round((b1/SE),4)
     tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
     p=round((1-scipy.stats.t.cdf(abs(t_cal),df))*2,4)
    
     print(f"************Two sample t test for slope(b1) is************  ")
     print("")
     print(f"here we have given following information")
     print(f"slope(b1)={b1}; MSE={MSE};SSxx={SSXX}; df=n-k-1=({n}-{k}-{1})={df}; Alpha={a}")
     print("")
     print("We calculate standard error of slope from given information")
     print(f"SE=sqrt(MSE/SSXX)=sqrt({MSE}/{SSXX})={SE}")
     print("")
     print(f"Null and alternative:")
     print(f"Ho:  b1=0  &  H1: b1≠0")
     print("")
     print(f"Test statistics:")
     print(f"t_cal=(b1/SE)=({b1}/{SE})={t_cal}")
     print("")
     print(f"Cirtical value & P_value:")
     print(f"t_c={tc}     Note here Critical Value is obtain from excel with command=TINV({a},{df})")
     print(f"P_value={p}  Note pvalue is obtain from excel with command=TDIST(abs({t_cal}),{df},2)")
     print("")
     print("Decision:")
     if p>a:
             print(f"here |t_cal| <= t_c so do not reject null hypothesis")
     else: 
             print(f"here |t_cal| > t_c so reject null hypothesis")
     print("")
     print("Conclusion:")
     if p>a:
             print("b1=0 that is Slope coeffcient b1 is not important")
     else:
          print("b1≠0 that is Slope coeffcient b1 is important")


def Regression_test_given_SSE(b1,SSE,SSxx,n,k,a):
     import math 
     import scipy.stats
     df=n-k-1
     sigma=round(math.sqrt(SSE/(n-k-1)),6)
     SE=round((sigma/math.sqrt(SSxx)),6)
     t_cal=round((b1/SE),4)
     tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
     p=round((1-scipy.stats.t.cdf(abs(t_cal),df))*2,4)
     
     print(f"************Two sample t test for slope(b1) is************  ")
     print("")
     print(f"here we have given following information")
     print(f"slope(b1)={b1}; SSE={SSE};SSxx={SSxx}; df=n-k-1=({n}-{k}-{1})={df}; Alpha={a}")
     print("")
     print("We calculate standard error of slope from given information")
     print(f"Sigma=sqrt(SSE/(n-k-1))=sqrt({SSE}/({n}-{k}-1))={sigma}")
     print(f"SE=(sigma/sqrt(SSxx))=({sigma}/sqrt({SSxx}))={SE}")
     print("")
     print(f"Null and alternative:")
     print(f"Ho:  b1=0  &  H1: b1≠0")
     print("")
     print(f"Test statistics:")
     print(f"t_cal=(b1/SE)=({b1}/{SE})={t_cal}")
     print("")
     print(f"Cirtical value & P_value:")
     print(f"t_c={tc}     Note here Critical Value is obtain from excel with command=TINV({a},{df})")
     print(f"P_value={p}  Note pvalue is obtain from excel with command=TDIST(abs({t_cal}),{df},2)")
     print("")
     print("Decision:")
     if p>a:
             print(f"here |t_cal| <= t_c so do not reject null hypothesis")
     else: 
             print(f"here |t_cal| > t_c so reject null hypothesis")
     print("")
     print("Conclusion:")
     if p>a:
             print("b1=0 that is Slope coeffcient b1 is not important")
     else:
         print("b1≠0 that is Slope coeffcient b1 is important")


def Regression_test_given_SE(b1,SE,n,k,a):
     import math 
     import scipy.stats
     df=n-k-1
     t_cal=round((b1/SE),4)
     tc=abs(round(scipy.stats.t.ppf(q=a/2,df=df),2))
     p=round((1-scipy.stats.t.cdf(abs(t_cal),df))*2,4)
     
     print(f"************Two sample t test for slope(b1) is************  ")
     print("")
     print(f"here we have given following information")
     print(f"slope(b1)={b1}; S.E={SE}; df=n-k-1=({n}-{k}-{1})={df}; Alpha={a}")
     print("")
     print(f"Null and alternative:")
     print(f"Ho:  b1=0  &  H1: b1≠0")
     print("")
     print(f"Test statistics:")
     print(f"t_cal=(b1/S.E)=({b1}/{SE})={t_cal}")
     print("")
     print(f"Cirtical value & P_value:")
     print(f"t_c={tc}     Note here Critical Value is obtain from excel with command=TINV({a},{df})")
     print(f"P_value={p}  Note pvalue is obtain from excel with command=TDIST(abs({t_cal}),{df},2)")
     print("")
     print("Decision:")
     if p>a:
             print(f"here |t_cal| <= t_c so do not reject null hypothesis")
     else: 
             print(f"here |t_cal| > t_c so reject null hypothesis")
     print("")
     print("Conclusion:")
     if p>a:
             print("b1=0 that is Slope coeffcient b1 is not important")
     else:
         print("b1≠0 that is Slope coeffcient b1 is important")

