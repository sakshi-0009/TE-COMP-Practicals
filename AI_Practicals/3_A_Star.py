# Implement A star Algorithm for any game search problem.

dict_hn={
    'A':1,
    'B':2,
    'C':3,
    'D':1,
    'E':2,
    'F':3,
    'G':0,
    'H':1,
    'I':2,
    'J':3,
}
dict_gn=dict(
    A=dict(B=3,C=4,D=2),
    B=dict(E=1,F=2),
    C=dict(J=3),
    D=dict(H=1,I=3),
    E=dict(G=5),
    F=dict(G=2),
    H=dict(G=5),
    I=dict(G=1),
    J=dict(G=2),
)

import queue as Q 
start='A'
goal='G' 
result='' 

def get_fn(citystr):
    cities=citystr.split(" , ") 
    hn=gn=0 
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
        hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def expand(cityq): 
    global result
    tot, citystr, thiscity=cityq.get()
    if thiscity==goal:
        result=citystr+"  : "+str(tot)
        return 
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq) 
    print("The A* path with the total is: ") 
    print(result)
main()