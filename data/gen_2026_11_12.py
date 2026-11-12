import numpy as np, pandas as pd
rng=np.random.default_rng(1112)
dates=pd.bdate_range("2024-11-11","2026-11-10")
n=len(dates)
mkt=rng.normal(0.10/252,0.17/np.sqrt(252),n)
mkt[300:330]+= -0.006
tick={"KSTL":(1.35,0.25,0.18),"BRWN":(0.6,0.15,0.08),"VRDA":(1.1,0.30,0.22),"OAKM":(0.85,0.18,0.10),"NIMB":(1.6,0.40,0.15)}
P={}
P["MKT_IDX"]=4800*np.cumprod(1+mkt)
for t,(b,iv,alpha) in tick.items():
    r=alpha/252+b*(mkt-0.10/252)+0.10/252*b*0+rng.normal(0,iv/np.sqrt(252),n)
    P[t]=np.round({"KSTL":62,"BRWN":38,"VRDA":115,"OAKM":54,"NIMB":21}[t]*np.cumprod(1+r),2)
P["MKT_IDX"]=np.round(P["MKT_IDX"],2)
rf=np.round(np.clip(4.55-np.linspace(0,1.0,n)+rng.normal(0,0.02,n),0,None),2)
df=pd.DataFrame(P,index=dates); df["RF_ANNUAL_PCT"]=rf
df.index.name="date"; df.to_csv("halyard_prices.csv")
