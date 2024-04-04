import math
def solve_Q(zin, rl,f, loaimach):
    Q=None
    if(loaimach==1):
       Q=math.sqrt((zin/rl-1))
    if(loaimach==2):
       Q=math.sqrt((zin/rl-1))
    if(loaimach==3):
       Q=math.sqrt((rl/zin-1))
    if(loaimach==4):
       Q=math.sqrt((rl/zin-1))
    return Q
 
def solve_L(zin, rl, f, loaimach):
   #1-4 tinh L
   #2-3 tinh C
    L=None
    Cs=None
    C=None
    Q=solve_Q(zin, rl,f,loaimach)

    if(loaimach==1):
       L=Q*rl/(2*3.14*f)       
    if(loaimach==2):
       C=solve_C(zin, rl, f, loaimach)
       L=rl**2*C/(1+Q**2)
      
    if(loaimach==3):
       C=solve_C(zin, rl, f, loaimach)
       Cs=((Q*Q+1)/(Q*Q))*C
       L=1/((2*3.14*f)**2*Cs)
    if(loaimach==4):
       L=rl/(Q*2*3.14*f)         
    return L
 
def solve_C(zin, rl, f, loaimach):
    C=None
    L=None
    Q=solve_Q(zin, rl,f,loaimach)
    if(loaimach==1):
       L=solve_L(zin, rl, f, 1)
       C=(L/rl**2)/(Q**2+1)   
    if(loaimach==2):
       C=1/(rl*Q*2*3.14*f)
    if(loaimach==3):
       C=Q/(rl*2*3.14*f)
       
    if(loaimach==4):
       L=solve_L(zin, rl, f, 4)
       C=(L/(rl**2))*(Q**2+1)
    return C