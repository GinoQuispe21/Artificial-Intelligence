import numpy as np
import copy
import random
class it:
    def __init__(self,id = 0, v = 0,w = 0):
        self.id = id
        self.v = v
        self.w = w

class hill_climbing:
    def __init__(self, cap, items):
        self.cap = cap
        self.items = items
    def hill_climbing_algorithm(self):
        maxv = 0
        best = []
        for i,_ in enumerate(self.items):
            w = 0
            v = 0
            end = False
            init = copy.deepcopy(self.items)
            random.shuffle(init)
            start = init.pop(i)
            sol = []
            sol.append(start)
            w += start.w
            v += start.v
            print("INICIO: %i %i"%(start.v,start.w))
            while not end:
                bestit = sol[-1]
                auxw = 9999
                auxv = 0
                for item in init:
                    if (item.w + w) <= self.cap and (item.v + v) > auxv and (item.w + w) < auxw:
                        auxv = item.v
                        bestit = item
                if bestit != sol[-1]:
                    w += bestit.w
                    v += bestit.v
                    init.remove(bestit)
                    sol.append(bestit)
                else:
                    if v > maxv:
                        best = copy.deepcopy(sol)
                        maxv = v
                    print("Máximo hasta ahora: %i"%(maxv))
                    print("Valor: %i, Peso: %i de %i\n"%(v,w,self.cap))
                    end = True
                    
        print("\nMEJOR SOLUCION: ")
        print("Valor: %i, Peso: %i de %i-"%(sum([x.v for x in best]),sum([x.w for x in best]),self.cap))
        for item in best:
            print('\t',item.id, item.v,item.w)

values = [it(1,8,5),it(2,7,6),it(3,12,10),it(4,6,4),it(5,2,1),it(6,3,1)]

Example1 = hill_climbing(16, values)

Example1.hill_climbing_algorithm()

