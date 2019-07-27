new_global = 1
def A():
    print("entering inside A   ")
    print("calling API B from A")
    new_global = 0
    #line2
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    B()

def B():
    print("entering inside B")
    print("calling API C")
    print("testing change in B")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    C()

def C():
    print("entering inside C")
    print("calling API D")
    #line33
    #line4
    #line5
    #line6
    #line7
    #line8
    D()

def D():
    print("entering inside D")
    #line3
    #line4
    #line5
    #line6
    #line777
    #line8

def E():
    print("entering inside E")
    new_global = 0
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    F()

def F():
    print("entering inside F")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line888
    G()
def G():
    print("entering inside G")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    H()

def H():
    print("entering inside H")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    I()
def I():
    print("entering inside I")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    J()

def J():
    print("entering inside J")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8

def K():
    print("entering inside K")
    print("testing change in K")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    L()

def L():
    print("entering inside L")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    M()

def M():
    print("entering inside M")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    N()

def N():
    print("entering inside N")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    O()

def O():
    print("entering inside O")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8

def P():
    print("entering inside D")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    Q()

def Q():
    print("entering inside Q")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    R()

def R():
    print("entering inside R")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    S()

def S():
    print("entering inside S")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8
    T()
def T():
    print("entering inside T")
    #line3
    #line4
    #line5
    #line6
    #line7
    #line8


def main():
    print("inside project main ")
    A()
if __name__ == '__main__':
    main()