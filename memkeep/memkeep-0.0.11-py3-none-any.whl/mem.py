import os



def newpath(name):
    os.mkdir(f'{name}/')

def mempath(memp):
    memp.mempr = f'{memp}/'

mempr = 'NO_PATH/'

def save(name, value):  # memkeep.mem.save("OBJname", "Content")
    f = open(mempr + str(name) + ".txt", 'w')
    f.write(str(value))
    f.close()
    
def get(name):          # memkeep.mem.get("OBJ")
    f = open(mempr + str(name) + ".txt", 'r')
    return f.read()
    
def clearmem():         # memkeep.mem.clearmem()
    for i in os.listdir(mempr):
        os.remove(mempr + str(i))

def remove(*names):     # memkeep.mem.remove("OBJ1", "OBJ2", "OBJ3")
    for i in names:
        os.remove(mempr + str(i) + ".txt")
        

def list(tf):
        c = 0
        for i in os.listdir(mempr):
            c += 1
            if tf:
                print(str(c) + " > " + str(i).replace(".txt", ""))
            else:   
                print(str(i).replace(".txt", ""))
                

def exists(name): # memkeep.mem.exists("OBJ")
    list = []
    for i in os.listdir(mempr):
        list.append(str(i).replace(".txt", "").replace("array_", ""))
    if str(name).replace("array_", "").replace(".txt", "") in list:
        return True
    else:
        return False
        
class array():
    def make(name):
        os.mkdir(f'{mempr}array_' + str(name))
        f = open(f'{mempr}array_' + str(name) + "/count.txt", 'w')
        f.write('0')
        f.close()
    
    def add(name, *adds): # memkeep.mem.arrayadd("Obj1", "Thing2")
        for i in adds:
            f = open(f'{mempr}array_' + str(name) + "/count.txt", 'r')
            count = int(f.read())
            count += 1
            f.close()
            f = open(f'{mempr}array_' + str(name) + "/count.txt", 'w')
            f.write(str(count))
            f.close()
            f = open(f'{mempr}' + str(name) + "/" + str(count) + ".txt", 'w')
            f.write(str(i))
            f.close()
        

    
    def clear(name): # memkeep.mem.arrayclear("OBJ")
        for i in os.listdir(f'{mempr}array_' + str(name)):
            if not i == "count.txt":
                os.remove(f'{mempr}array_' + str(name) + "/" + str(i))
                f = open(f'{mempr}array_' + str(name) + "/count.txt", 'w')
                f.write("0")
                f.close()
        
    def isempty(name):
        f = open(f'{mempr}array_{str(name)}/count.txt', 'r')
        o = f.read()
        f.close()
        if o == "0":
            return True
        else: 
            return False
    
    def size(name):
        f = open(f'{mempr}array_{str(name)}/count.txt', 'r')
        i = int(f.read())
        f.close()
        return i
    
    def get(name):
        list = []
        for i in os.listdir(f'{mempr}array_{str(name)}'):
            f = open(f'{mempr}array_{str(name)}/{str(i)}', 'r')
            if not i == "count.txt":
                list.append(f.read())
        f.close()
        return list
        
    class item():
        def get(name, item):
            f = open(f'{mempr}array_{str(name)}/{str(item)}.txt', 'r')
            i = f.read()
            f.close()
            return i
        
        def remove(name, item):
            os.remove(f'{mempr}array_{str(name)}/{str(item)}.txt')
            f = open(f'{mempr}array_{str(name)}/count.txt', 'r')
            c = f.read()
            f.close()
            f = open(f'{mempr}array_{str(name)}/count.txt', 'w')
            f.write(str(int(c) - 1))
            f.close()
            o = int(c) - 1
            i = 0
            for x in range(o):
                i += 1
                os.rename(f'{mempr}array_{str(name)}/{str(i + 1)}.txt', f'{mempr}array_{str(name)}/{str(i)}.txt')
                
        def change(name, item, value):
            f = open(f'{mempr}array_{str(name)}/{str(item)}.txt', 'w')
            f.write(str(value))
            f.close()
            
    def remove(name):
        for i in os.listdir(f'{mempr}array_{str(name)}'):
            os.remove(f'{mempr}array_{str(name)}/{str(i)}')
        os.rmdir(f'{mempr}array_{str(name)}')
        
    def addlist(name, list_):
        f = open(f'{mempr}array_{str(name)}/count.txt', 'r')
        o = int(f.read())
        f.close()
        for i in list_:
            o += 1
            f = open(f'{mempr}array_{str(name)}/{str(o)}.txt', 'w')
            f.write(str(i))
            f.close()
        f = open(f'{mempr}array_{str(name)}/count.txt', 'w')
        f.write(str(o))
        f.close()
        
    
            
        
    
         