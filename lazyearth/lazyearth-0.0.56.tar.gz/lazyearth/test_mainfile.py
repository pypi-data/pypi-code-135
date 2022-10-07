# from lazyearth.mainfile import objearth

# # from configparser import ConfigParser

# # file = 'lazyearth.ini'
# # config = ConfigParser()
# # config.read(file)

# # fractionconstant = float(config['Plot']['fractionnumber'])
# # print(fractionconstant)

# # Nodata = int(config['Data']['Nodata'])
# # print(Nodata)

# # Cloud = (config['Cloud']['Fashcloud'])
# # print(Cloud)


class employee:
    def __init__(self,name,job,salary):
        self.name   = name
        self.job    = job
        self.salary = salary
    def detail(self):
        print("Name   : ",self.name)
        print("Job    : ",self.job)
        print("Salary : ",self.salary)