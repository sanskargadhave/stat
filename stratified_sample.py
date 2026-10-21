import numpy as np
p1=np.random.uniform(1,10,size=20)
p2=np.random.uniform(50,60,size=30)
p3=np.random.uniform(100,110,size=40)
hetrop=np.concatenate([p1,p2,p3])
srswor=np.random.choice(hetrop,size=18)

s1=np.random.choice(p1,size=4,replace=False)
s2=np.random.choice(p2,size=5,replace=False)
s3=np.random.choice(p3,size=8,replace=False)

stratified=np.concatenate([s1,s2,s3])

print("\nHistogeneous population=",hetrop)
print("\nam of hetro population=",np.mean(hetrop))

print("\nsrswor sample=",srswor)
print("\nam of srswor=",np.mean(srswor))

print("\nstratified sample=",stratified)
print("\nam of stratified sample =",np.mean(stratified))