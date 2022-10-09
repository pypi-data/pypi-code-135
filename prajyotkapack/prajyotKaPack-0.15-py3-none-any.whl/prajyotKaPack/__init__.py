def ins(a):
    print("hello world ins")
    return


def ws(ws):
    print("hello world ins")
    return


def gp(s):
    print("hello world ins")
    return


def linux():
    print("hello this is function of linux")


dict_hnP1 = {'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
             'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
             'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193,
             'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

dict_gnP1 = dict(
    Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
    Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
    Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
    Drobeta=dict(Mehadia=75, Craiova=120),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99, Bucharest=211),
    Giurgiu=dict(Bucharest=90),
    Hirsova=dict(Eforie=86, Urziceni=98),
    Iasi=dict(Neamt=87, Vaslui=92),
    Lugoj=dict(Mehadia=70, Timisoara=111),
    Mehadia=dict(Lugoj=70, Drobeta=75),
    Neamt=dict(Iasi=87),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
    Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
    Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
    Timisoara=dict(Lugoj=111, Arad=118),
    Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
    Vaslui=dict(Iasi=92, Urziceni=142),
    Zerind=dict(Oradea=71, Arad=75)
)


class aip1:

    def getname():
        return "bfs"

    dict_gn = dict(
        Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
        Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
        Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
        Drobeta=dict(Mehadia=75, Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99, Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86, Urziceni=98),
        Iasi=dict(Neamt=87, Vaslui=92),
        Lugoj=dict(Mehadia=70, Timisoara=111),
        Mehadia=dict(Lugoj=70, Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
        Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
        Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
        Timisoara=dict(Lugoj=111, Arad=118),
        Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
        Vaslui=dict(Iasi=92, Urziceni=142),
        Zerind=dict(Oradea=71, Arad=75)
    )

    dict_hn = {'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
               'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
               'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193,
               'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

    def code():
        dict_gn = dict(
        Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
        Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
        Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
        Drobeta=dict(Mehadia=75, Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99, Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86, Urziceni=98),
        Iasi=dict(Neamt=87, Vaslui=92),
        Lugoj=dict(Mehadia=70, Timisoara=111),
        Mehadia=dict(Lugoj=70, Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
        Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
        Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
        Timisoara=dict(Lugoj=111, Arad=118),
        Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
        Vaslui=dict(Iasi=92, Urziceni=142),
        Zerind=dict(Oradea=71, Arad=75)
        )
        
        dict_hn = {'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
               'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
               'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193,
               'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

        import queue as Q
        #from RMP import dict_hn


        start = 'Arad'
        goal = 'Bucharest'
        result = ''


        def BFS(city, cityq, visitedq):
            global result
            if city == start:
                result = result+' '+city
            for eachcity in dict_gn[city].keys():
                if eachcity == goal:
                    result = result+' '+eachcity
                    return
                if eachcity not in cityq.queue and eachcity not in visitedq.queue:
                    cityq.put(eachcity)
                    result = result+' '+eachcity
            visitedq.put(city)
            BFS(cityq.get(), cityq, visitedq)

        def main():
            cityq = Q.Queue()
            visitedq = Q.Queue()
            BFS(start, cityq, visitedq)
            print("BFS Traversal from ", start, " to ", goal, " is: ")
            print(result)

        main()


class aip2:
    def getname():
        return "A*"


    dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

    dict_gn=dict(
    Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
    Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
    Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
    Drobeta=dict(Mehadia=75,Craiova=120),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99,Bucharest=211),
    Giurgiu=dict(Bucharest=90),
    Hirsova=dict(Eforie=86,Urziceni=98),
    Iasi=dict(Neamt=87,Vaslui=92),
    Lugoj=dict(Mehadia=70,Timisoara=111),
    Mehadia=dict(Lugoj=70,Drobeta=75),
    Neamt=dict(Iasi=87),
    Oradea=dict(Zerind=71,Sibiu=151),
    Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
    Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
    Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
    Timisoara=dict(Lugoj=111,Arad=118),
    Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
    Vaslui=dict(Iasi=92,Urziceni=142),
    Zerind=dict(Oradea=71,Arad=75)
    )

    def code():
        dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

        dict_gn=dict(
        Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
        Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
        Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
        Drobeta=dict(Mehadia=75,Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99,Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86,Urziceni=98),
        Iasi=dict(Neamt=87,Vaslui=92),
        Lugoj=dict(Mehadia=70,Timisoara=111),
        Mehadia=dict(Lugoj=70,Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71,Sibiu=151),   
        Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
        Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
        Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
        Timisoara=dict(Lugoj=111,Arad=118),
        Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
        Vaslui=dict(Iasi=92,Urziceni=142),
        Zerind=dict(Oradea=71,Arad=75)
        )



        import queue as Q
        #from RMP import dict_hn

        start='Arad'
        goal='Bucharest'
        result=''

        def DLS(city, visitedstack, startlimit, endlimit):
            global result
            found=0
            result=result+city+' '
            visitedstack.append(city)
            if city==goal:
                return 1
            if startlimit==endlimit:
                return 0
            for eachcity in dict_gn[city].keys():
                if eachcity not in visitedstack:
                    found=DLS(eachcity, visitedstack, startlimit+1, endlimit)
                    if found:
                        return found

        def IDDFS(city, visitedstack, endlimit):
            global result
            for i in range(0, endlimit):
                print("Searching at Limit: ",i)
                found=DLS(city, visitedstack, 0, i)
                if found:
                    print("Found")
                    break
                else:
                    print("Not Found! ")
                    print(result)
                    print("-----")
                    result=' '
            visitedstack=[]

        def main():
            visitedstack=[]
            IDDFS(start, visitedstack, 9)
            print("IDDFS Traversal from ",start," to ", goal," is: ")
            print(result)


        main() 



class aip3s:
    def getname():
        return "A*"

    dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

    dict_gn = dict(

        Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
        Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
        Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
        Drobeta=dict(Mehadia=75, Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99, Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86, Urziceni=98),
        Iasi=dict(Neamt=87, Vaslui=92),
        Lugoj=dict(Mehadia=70, Timisoara=111),
        Mehadia=dict(Lugoj=70, Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
        Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
        Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
        Timisoara=dict(Lugoj=111, Arad=118),
        Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
        Vaslui=dict(Iasi=92, Urziceni=142),
        Zerind=dict(Oradea=71, Arad=75))

    def code():
        dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
        
        dict_gn = dict(        
        Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
        Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
        Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
        Drobeta=dict(Mehadia=75, Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99, Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86, Urziceni=98),
        Iasi=dict(Neamt=87, Vaslui=92),
        Lugoj=dict(Mehadia=70, Timisoara=111),
        Mehadia=dict(Lugoj=70, Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
        Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
        Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
        Timisoara=dict(Lugoj=111, Arad=118),
        Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
        Vaslui=dict(Iasi=92, Urziceni=142),
        Zerind=dict(Oradea=71, Arad=75)
        )


        import queue as Q
        #from RMP import dict_gn
        #from RMP import dict_hn

        start='Arad'
        goal='Bucharest'
        result3=''

        def get_fn(citystr):
            cities=citystr.split(" , ")
            hn=gn=0
            for ctr in range(0, len(cities)-1):
                gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
            hn=dict_hn[cities[len(cities)-1]]
            return(hn+gn)

        def expand(cityq):
            global result3
            tot, citystr, thiscity=cityq.get()
            if thiscity==goal:
                result3=citystr+" : : "+str(tot)
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
            print(result3)

        main() 

import queue as Q

class aip3:
    dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
    
        #from RMP import dict_gn
        #from RMP import dict_hn
    dict_gn = dict(
        Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
        Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
        Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
        Drobeta=dict(Mehadia=75, Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99, Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86, Urziceni=98),
        Iasi=dict(Neamt=87, Vaslui=92),
        Lugoj=dict(Mehadia=70, Timisoara=111),
        Mehadia=dict(Lugoj=70, Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
        Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
        Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
        Timisoara=dict(Lugoj=111, Arad=118),
        Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
        Vaslui=dict(Iasi=92, Urziceni=142),
        Zerind=dict(Oradea=71, Arad=75)
    )

    start='Arad'
    goal='Bucharest'
    result=''
    
    def get_fn(citystr):
        cities=citystr.split(" , ")
        hn=gn=0
        for ctr in range(0, len(cities)-1):
            gn=gn+aip3.dict_gn[cities[ctr]][cities[ctr+1]]
            hn=aip3.dict_hn[cities[len(cities)-1]]
            return(hn+gn)
    def expand(cityq):
        global result
        tot, citystr, thiscity=cityq.get()
        if thiscity==aip3.goal:
            result=citystr+" : : "+str(tot)
            return
        for cty in aip3.dict_gn[thiscity]:
            cityq.put((aip3.get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
        aip3.expand(cityq)

    def main():
        
        cityq=Q.PriorityQueue()
        thiscity=aip3.start
        cityq.put((aip3.get_fn(aip3.start),aip3.start,thiscity))
        aip3.expand(cityq)
        print("The A* path with the total is: ")
        print(result)

    def output():
        print("The A* path with the total is: Arad , Sibiu , Fagaras , Bucharest : : 140")




import queue as Q
class aip4:
    
    dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
    
        #from RMP import dict_gn
        #from RMP import dict_hn
    dict_gn = dict(
        Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
        Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
        Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
        Drobeta=dict(Mehadia=75, Craiova=120),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99, Bucharest=211),
        Giurgiu=dict(Bucharest=90),
        Hirsova=dict(Eforie=86, Urziceni=98),
        Iasi=dict(Neamt=87, Vaslui=92),
        Lugoj=dict(Mehadia=70, Timisoara=111),
        Mehadia=dict(Lugoj=70, Drobeta=75),
        Neamt=dict(Iasi=87),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
        Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
        Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
        Timisoara=dict(Lugoj=111, Arad=118),
        Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
        Vaslui=dict(Iasi=92, Urziceni=142),
        Zerind=dict(Oradea=71, Arad=75)
    )

    start='Arad'
    goal='Bucharest'
    result=''
    
    def get_fn(citystr):
        cities=citystr.split(',')
        hn=gn=0
        for ctr in range(0,len(cities)-1):
            gn=gn+aip4.dict_gn[cities[ctr]][cities[ctr+1]]
        hn=aip4.dict_hn[cities[len(cities)-1]]
        return(hn+gn)

    def printout(cityq):
        for i in range(0,cityq.qsize()):
            print(cityq.queue[i])

    def expand(cityq):
        global result
        tot,citystr,thiscity=cityq.get()
        nexttot=999
        if not cityq.empty():
            nexttot,nextcitystr,nextthiscity=cityq.queue[0]
        if thiscity==aip4.goal and tot<nexttot:
            result=citystr+'::'+str(tot)
            return
        print("Expanded city------------------------------",thiscity)
        print("Second best f(n)------------------------------",nexttot)
        tempq=Q.PriorityQueue()
        for cty in aip4.dict_gn[thiscity]:
                tempq.put((aip4.get_fn(citystr+','+cty),citystr+','+cty,cty))
        for ctr in range(1,3):
            ctrtot,ctrcitystr,ctrthiscity=tempq.get()
            if ctrtot<nexttot:
                cityq.put((ctrtot,ctrcitystr,ctrthiscity))
            else:
                cityq.put((ctrtot,citystr,thiscity))
                break
        aip4.printout(cityq)
        aip4.expand(cityq)
    def main():
        cityq=Q.PriorityQueue()
        thiscity=aip4.start
        cityq.put((999,"NA","NA"))
        cityq.put((aip4.get_fn(aip4.start),aip4.start,thiscity))
        aip4.expand(cityq)
        print(result)


class aip5:
    def code():
        
        import numpy as np
        import pandas as pd
        import sklearn as sk
        from sklearn.metrics import confusion_matrix
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import classification_report

#func importing dataset
        def importdata():
            balance_data=pd.read_csv("balance-scale.data")

      #print the dataset shape
            print("Dataset Length : ",len(balance_data))
      
      #printing the dataset observations
            print("Dataset : ",balance_data.head())
            return balance_data

#func to split the dataset
        def splitdataset(balance_data):
      #seperating the target variable
            X=balance_data.values[:,1:5]
            Y=balance_data.values[:,0]

      #splitting the dataset into train and test
            X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=100)
            return X,Y,X_train,X_test,y_train,y_test

#function to perform training with entropy
        def train_using_entropy(X_train,X_test,y_train,y_test):
      #decision tree with entropy
              clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)

      #performing training
              clf_entropy.fit(X_train,y_train)
              return clf_entropy

        def prediction(X_test,clf_object):
              y_pred=clf_object.predict(X_test)
              print("Predicted Values : ")
              print(y_pred)
              return y_pred

        def cal_accuracy(y_test,y_pred):
              print("Accuracy : ",accuracy_score(y_test,y_pred)*100)

        def main():
              data=importdata()
              X,Y,X_train,X_test,y_train,y_test=splitdataset(data)
      
              clf_entropy=train_using_entropy(X_train,X_test,y_train,y_test)

              print("Results using entropy : ")
              y_pred_entropy=prediction(X_test,clf_entropy)
              cal_accuracy(y_test,y_pred_entropy)



class aip6:

    #Please Download 
    rwp_examples = dict(
        x1=dict(Alt='Y', Bar='N', Fri='N',Hun='Y',Pat='S',Price='$$$',Rain='N',Res='Y',Type='F',Est='0-10',ans='Y'),
        x2=dict(Alt='Y', Bar='N', Fri='N',Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='T',Est='30-60',ans='N'),
        x3=dict(Alt='N', Bar='Y', Fri='N',Hun='N',Pat='S',Price='$',Rain='N',Res='N',Type='B',Est='0-10',ans='Y'),
        x4=dict(Alt='Y', Bar='N', Fri='Y',Hun='Y',Pat='F',Price='$',Rain='Y',Res='N',Type='T',Est='10-30',ans='Y'),
        x5=dict(Alt='Y', Bar='N', Fri='Y',Hun='N',Pat='F',Price='$$$',Rain='N',Res='Y',Type='F',Est='>60',ans='N'),
        x6=dict(Alt='N', Bar='Y', Fri='N',Hun='Y',Pat='S',Price='$$',Rain='Y',Res='Y',Type='I',Est='0-10',ans='Y'),
        x7=dict(Alt='N', Bar='Y', Fri='N',Hun='N',Pat='N',Price='$',Rain='Y',Res='N',Type='B',Est='0-10',ans='N'),
        x8=dict(Alt='N', Bar='N', Fri='N',Hun='Y',Pat='S',Price='$$',Rain='Y',Res='Y',Type='T',Est='0-10',ans='Y'),
        x9=dict(Alt='N', Bar='Y', Fri='Y',Hun='N',Pat='F',Price='$',Rain='Y',Res='N',Type='B',Est='>60',ans='N'),
        x10=dict(Alt='Y', Bar='Y', Fri='Y',Hun='Y',Pat='F',Price='$$$',Rain='N',Res='Y',Type='I',Est='10-30',ans='N'),
        x11=dict(Alt='N', Bar='N', Fri='N',Hun='N',Pat='N',Price='$',Rain='N',Res='N',Type='T',Est='0-10',ans='N'),
        x12=dict(Alt='Y', Bar='Y', Fri='Y',Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='B',Est='0-10',ans='Y')
        )

#from RWP import rwp_examples
    total_exp = 12
    def tot(attribute, value):
        count = 0
        for key, val in aip6.rwp_examples.items():
            for key1, val1 in val.items():
                if key1 == attribute:
                    if val1 == value:
                        count += 1
        return count
    def getProbab(attribute, attribval, value):
        count = 0
        for key, val in aip6.rwp_examples.items():
            val1 = aip6.rwp_examples[key][attribute]
            val2 = aip6.rwp_examples[key]['ans']
            if val1 == attribval and val2 == value:
                count += 1
        probab = count / aip6.tot('ans', value)
        return probab
    def main():
        PAltYes = aip6.tot('Alt', 'Y') / aip6.total_exp
        PAltNo = aip6.tot('Alt', 'N') / aip6.total_exp    
        PBarYes = aip6.tot('Bar', 'Y') / aip6.total_exp
        PBarNo = aip6.tot('Bar', 'N') / aip6.total_exp    
        PFriYes = aip6.tot('Fri', 'Y') / aip6.total_exp
        PFriNo = aip6.tot('Fri', 'N') / aip6.total_exp    
        PHunYes = aip6.tot('Hun', 'Y') / aip6.total_exp
        PHunNo = aip6.tot('Hun', 'N') / aip6.total_exp    
        PPatSome = aip6.tot('Pat', 'S') / aip6.total_exp
        PPatFull = aip6.tot('Pat', 'F') / aip6.total_exp
        PPatNone = aip6.tot('Pat', 'N') / aip6.total_exp
        PPriceCheap = aip6.tot('Price', '$') / aip6.total_exp
        PPriceAvg = aip6.tot('Price', '$$') / aip6.total_exp
        PPriceExp = aip6.tot('Price', '$$$') / aip6.total_exp    
        PRainYes = aip6.tot('Rain', 'Y') / aip6.total_exp
        PRainNo = aip6.tot('Rain', 'N') / aip6.total_exp    
        PResYes = aip6.tot('Res', 'Y') / aip6.total_exp
        PResNo = aip6.tot('Res', 'N') / aip6.total_exp    
        PTypeFrench = aip6.tot('Type', 'F') / aip6.total_exp
        PTypeItalian = aip6.tot('Type', 'I') / aip6.total_exp
        PTypeBurger = aip6.tot('Type', 'B') / aip6.total_exp
        PTypeThai = aip6.tot('Type', 'T') / aip6.total_exp    
        PEstFew = aip6.tot('Est', '0-10') / aip6.total_exp
        PEstMore = aip6.tot('Est', '10-30') / aip6.total_exp
        PEstStillMore = aip6.tot('Est', '30-60') / aip6.total_exp
        PEstTooMuch = aip6.tot('Est', '>60') / aip6.total_exp
        PAnsYes = aip6.tot('ans', 'Y') / aip6.total_exp
        PAnsNo = aip6.tot('ans', 'N') / aip6.total_exp    
        print('Probability for will wait if there is an Alternate Restaurant Nearby: ')
        print('Yes: Will Wait ', (aip6.getProbab('Alt', 'Y', 'Y') * PAnsYes/PAltYes) * 100, '%')
        print('No: Will Wait ', (aip6.getProbab('Alt', 'Y', 'N') * PAnsNo/PAltYes ) * 100, '%')
        print('Probability for will wait if there No is an Alternate Restaurant Nearby: ')
        print('Yes: Will Wait ', (aip6.getProbab('Alt', 'N', 'Y') * PAnsYes/PAltNo) * 100, '%')
        print('No: Will Wait ', (aip6.getProbab('Alt', 'N', 'N') * PAnsNo/PAltNo) * 100, '%')
        print('Probability for will wait if Estimated Wait time is 0-10 minutes: ')
        print('Yes: Will Wait ', (aip6.getProbab('Est', '0-10', 'Y') * PAnsYes/PEstFew) * 100, '%')
        print('No: Will Wait ', (aip6.getProbab('Est', '0-10', 'N') * PAnsNo/PEstFew) * 100, '%')
        print('Probability for will wait if Estimated Wait time is 10-30 minutes ')
        print('Yes: Will Wait ', (aip6.getProbab('Est', '10-30', 'Y') * PAnsYes/PEstMore) * 100, '%')
        print('No: Will Wait ', (aip6.getProbab('Est', '10-30', 'N') * PAnsNo/PEstMore) * 100, '%')
        print("Probability for Will Wait if the Estimated Wait Time is 30-60 mins: ")
        print("Yes: Will Wait: ",(aip6.getProbab('Est','30-60','Y')*PAnsYes/PEstStillMore)*100,"%")
        print("No: Will Wait: ",(aip6.getProbab('Est','30-60','N')*PAnsNo/PEstStillMore)*100,"%")
        print("Probability for Will Wait if the Estimated Wait Time is >60 mins: ")
        print("Yes: Will Wait: ",(aip6.getProbab('Est','>60','Y')*PAnsYes/PEstTooMuch)*100,"%")
        print("No: Will Wait: ",(aip6.getProbab('Est','>60','N')*PAnsNo/PEstTooMuch)*100,"%")
        print('Probability for will wait if there are Some Patrons ')
        print('Yes: Will Wait ', (aip6.getProbab('Pat', 'S', 'Y') * PAnsYes/PPatSome) * 100, '%')
        print('No: Will Wait ', (aip6.getProbab('Pat', 'S', 'N') * PAnsNo/PPatSome) * 100, '%')
        print("Probability for Will Wait if there are None Patrons: ")
        print("Yes: Will Wait: ",(aip6.getProbab('Pat','N','Y')*PAnsYes/PPatNone)*100,"%")
        print("No: Will Wait: ",(aip6.getProbab('Pat','N','N')*PAnsNo/PPatNone)*100,"%")
        print("Probability for Will Wait if there are Full Patrons: ")
        print("Yes: Will Wait: ",(aip6.getProbab('Pat','F','Y')*PAnsYes/PPatFull)*100,"%")
        print("No: Will Wait: ",(aip6.getProbab('Pat','F','N')*PAnsNo/PPatFull)*100,"%")
        print('Probability for will wait if the place is Thai ')
        print('Yes: Will Wait ', (aip6.getProbab('Type', 'T', 'Y') * PAnsYes/PTypeThai) * 100, '%')
        print('No: Will Wait ', (aip6.getProbab('Type', 'T', 'N') * PAnsNo/PTypeThai) * 100, '%')    

import numpy as np

class NeuralNetwork():
        
    def __init__(self):
        #seeding for random number generation
        np.random.seed()

        #converting weights to a 3 by 1 matrix
        self.synaptic_weights=2*np.random.random((3,1))-1

    #x is output variable
    def sigmoid(self, x):
        #applying the sigmoid function
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        #computing derivative to the sigmoid function
        return x*(1-x)

    def train(self,training_inputs,training_outputs,training_iterations):

        #training the model to make accurate predictions while adjusting
        for iteration in range(training_iterations):
            #siphon the training data via the neuron
            output=self.think(training_inputs)

            error=training_outputs-output

            #performing weight adjustments
            adjustments=np.dot(training_inputs.T,error*self.sigmoid_derivative(output))

            self.synaptic_weights+=adjustments

    def think(self,inputs):
        #passing the inputs via the neuron to get output
        #converting values to floats

        inputs=inputs.astype(float)
        output=self.sigmoid(np.dot(inputs,self.synaptic_weights))

        return output

class aip7:

    def main():
    #initializing the neuron class
        neural_network=NeuralNetwork()

        print("Beginning randomly generated weights: ")
        print(neural_network.synaptic_weights)

    #training data consisting of 4 examples--3 inputs & 1 output
        training_inputs=np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
        training_outputs=np.array([[0,1,1,0]]).T

    #training taking place
        neural_network.train(training_inputs,training_outputs,15000)

        print("Ending weights after training: ")
        print(neural_network.synaptic_weights)

        user_input_one=str(input("User Input One: "))
        user_input_two=str(input("User Input Two: "))
        user_input_three=str(input("User Input Three: "))

        print("Considering new situation: ",user_input_one,user_input_two,user_input_three)
        print("New output data: ")
        print(neural_network.think(np.array([user_input_one,user_input_two,user_input_three])))



