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


class aip3output:
    
    dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
        
    

    import queue as Q

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
            gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
        hn=dict_hn[cities[len(cities)-1]]
        return(hn+gn)

    def expand(cityq):
        global result
        tot, citystr, thiscity=cityq.get()
        if thiscity==goal:
            result=citystr+" : : "+str(tot)
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

    main()







