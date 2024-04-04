import math

class Pi_solve:
    def __init__(self, zin, rc,rl, f,loaimach):
        self.zin = zin  #input impedance of
        self.rc=rc
        self.rl=rl
        self.f=f
        self.loaimach=loaimach
        
        self.w=2*3.14*self.f

    def Xparallel_Source(self):
        return self.zin/self.solve_Q1()
    def Xserial_Source(self):
        return self.rc*self.solve_Q1()
    def Xparallel_Load(self):
        return self.rl/self.solve_Q2()
    def Xserial_Load(self):
        return self.rc*self.solve_Q2()
    
    def solve_L1(self):
        L1=None
        if(self.loaimach==1):
            #L1=Paralell1
            L1=self.Xparallel_Source()/self.w
        if(self.loaimach==2):
            #L1=Serail1
            L1=self.Xserial_Source()/self.w

        return L1
    
    def solve_L2(self):

        L2=None
        if(self.loaimach==1):
            #L2=Parallel2
            L2=self.Xserial_Load()/self.w
        if(self.loaimach==2):
            #L2=Serial2
            L2=self.Xserial_Load()/self.w
        return L2
    
    def solve_C1(self):
        C1=None
        if(self.loaimach==1):
            #C1=S1
            C1=1/(self.w*self.Xserial_Source())
        if(self.loaimach==2):
            #C1=P1
            C1=1/(self.w*self.Xparallel_Source())
        return C1
    def solve_C2(self):
        C2=None
        if(self.loaimach==1):
            #C2=S2
            C2=1/(self.w*self.Xserial_Load())

        if(self.loaimach==2):
            #C2=P2
            C2=1/(self.w*self.Xparallel_Load())

        return C2
    
    
    
    
    
    def solve_Q1(self):
        return math.sqrt((self.zin/self.rc)-1)
    def solve_Q2(self):
        return math.sqrt((self.rl/self.rc)-1)
