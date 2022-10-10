import math
from matplotlib import pyplot
from typing import Callable, Dict, List, Union

class Bool_expression: # Булева формула, операндами которой являются нечёткие высказывания
    def __init__(self, Truth = None):
        self.__Truth = Truth
    
    def Calculate_truth(self):
        return None
    
    @property
    def Truth(self) -> Union[float,None]: #-Свойство: Измненение значения truth высказывания
        #if self.__Truth is None:  # Если Input_parameter_value truth для данного элемента ещё не рассчитано
           # Результат = self.Calculate_truth() # Рассчитываем Input_parameter_value truth
            #self.__Truth = Результат # Запоминаем чтобы избежать перерасчётов в дальнейшем
        return self.__Truth # Возвращаем в качестве значения свойства
    
    @Truth.setter
    def Truth(self,input_parameter):
        if(input_parameter is None or (input_parameter <= 1 and input_parameter >= 0)):
            self.__Truth = input_parameter
        else:
           raise ValueError("the value must be in the range from 0 to 1")
    
    
    def __and__(self,other): # Конъюнкиця (&)
        return Bool_expression(self[1]*other[1] if self.Truth is not None and other.Truth is not None else None)
        
    def __or__(self,other): # Дизъюнкция (|)
        return Bool_expression(self[1]*other[0] + other[1] if self.Truth is not None and other.Truth is not None else None)
        
    def __invert__(self): # Отрицание (~)
        return Bool_expression(1 - self[1] if self.Truth is not None else None)
    
    def __rshift__(self, other): # Импликация (>>)
       return ~self | other    # [ other[0]*self[1], self[0]*other[0] + other[1] ] 
    
    def __getitem__(self,item): # Индексатор
        return self.Truth if item == 1 else 1 - self.Truth
    
    def __str__(self):
        return str(self.Truth)
    
class Fuzzy_variable: # Кортеж вида (Name,A), где 
    def __init__(self, Name:str, A: Dict[float,float] = None):
        self.Name = Name  # Name переменной,  
        self.A = A if A is not None else {}      # A - нечёткое множество на универсуме X (все пары вида (x,u(x)))
    
    def __getitem__(self,item) -> Union[float, str]: # Индексатор
        return self.A[item] if item in self.A else "None"
    
    def __str__(self):
        return "{Name} = {function}".format(Name = self.Name, function = self.A)

class Linguistic_variable: # Кортеж вида (бета,T,X,G,M), где 
    def __init__(self, Name:str, Input_parameter_value:float = None, 
                 #X:List[int] = None, 
                 T:List[Fuzzy_variable] = None 
                 #G = None, 
                 #M = None
                 ):
        self.Name = Name    # бета - Name переменной
        self.Input_parameter_value = Input_parameter_value 
        #self.X = X if X is not None else []          # X - область определения Term-множества(универсум нечётких переменных), 
        self.T = T if T is not None else []          # T - множество её значений(Term-множество состоящее из нечётких переменных) 
        #self.G = G          # G - синтаксическая процедура, позволяющая генерировать новые Termы(значения)
        #self.M = M          # M - семантическая процедура, ставящая в соответствие каждому Termу, полученному с помощью G нечёткое множество
        self.Defuzzified_Input_parameter_value = None
    
    def __str__(self):
        #Строка = self.Name + ": " +  str(self.Input_parameter_value) + "\n\t" + "\n\t".join([НПеременная.Name + ": \t" +  str(НПеременная[self.Input_parameter_value]) for НПеременная in self.T])
        return """
{Name}: {Input_parameter_value}
{Fuzzy_variables}""".format(
Name = self.Name, 
Input_parameter_value = self.Input_parameter_value, 
Fuzzy_variables = "\n".join(["{Принадлежность}: \t{НП}".format(
                                НП = str(нп), 
                                Принадлежность = "\t" +  str(нп[self.Input_parameter_value])) for нп in self.T]))
                                
class Fuzzy_statement(Bool_expression): #<Linguistic_variable> IS <нечёткая_переменная(Term) данной лингвистической переменной> 
    def __init__(self, Linguistic_variable:Linguistic_variable, Term:Fuzzy_variable):
        self.Linguistic_variable = Linguistic_variable # Лингвистическая переменная 
        self.Term = Term # Term лингвистической переменной
        super().__init__()
     
    def Calculate_truth(self)-> Union[float, None]:
        return self.Term.A[self.Linguistic_variable.Input_parameter_value] if self.Linguistic_variable.Input_parameter_value is not None else None
    
    @property
    def Uncertainty(self)-> Union[float,None]: #-Свойство-геттер: Uncertainty - S(x) = -x0*log2(x0) -x1*log2(x1)
            return { 
                self[0] is None : None,
                self[0] not in [0,1] : -self[0]*math.log(self[0],2) - self[1]*math.log(self[1],2),
                self[0] in [0,1] : 0 #Учитывая невозможность вычисления логарифма от нуля рассматриваются дополнительно два предельных случая x0=0 и x1=0
                }[True]
    
    def __str__(self):
        return "{Linguistic_variable} {Term} = {Truth}".format(
            Linguistic_variable = self.Linguistic_variable.Name, Term = self.Term.Name, Truth = self.Truth)

class CNF(Bool_expression):
    def __init__(self,List_statements:List[Fuzzy_statement],F:Dict[Fuzzy_statement,float]):
        self.List_statements = List_statements  #список высказываний, которые содержит кнф
        self.F = F  # F - список весовых коэффициентов высказываний, входящих в кнф
        super().__init__()
    
    def Calculate_truth(self) -> Union[float, None]:
        Агр = None
        for i in self.List_statements:
            if Агр is None:
                Агр = Bool_expression(i.Truth)
            else:
                Агр = Агр & i
        return Агр.Truth
    
    def __str__(self):
        return " v ".join(["(" + str(statement) + ")" for statement in self.List_statements]) + " = " + str(self.Truth)
    
class Rule:
    def __init__(self,Antecedent:CNF,Consequent:CNF,Z:float = 1): # Задание правила вида A -> B = Z
        self.Antecedent = Antecedent # A - Antecedent правила (вида кнф)
        self.Consequent = Consequent # B - Consequent правила(вида кнф)
        self.Z = Z # Z - степень нечёткости правила (вещественное число в интервале [0,1])
        self.Not_using = True # Все правила при выводе учитываются только один раз
        
    def __str__(self):
        return "{Antecedent} -> {Consequent} = {Нечёткость}".format(
            Antecedent = f"[{self.Antecedent}]", Consequent = f"[{self.Consequent}]", Нечёткость = self.Z)
    
class Model:
    #------------ Rules вывода ------------
        
    @staticmethod
    def Withdrawal_rule_modus_ponens(Rule:Rule):
        if(Rule.Antecedent[1] is not None and Rule.Antecedent[1] >= (1-Rule.Z) and Rule.Antecedent[1] != 0):
            return 1 - (1 - Rule.Z)/Rule.Antecedent[1]
        else:
           raise Exception("withdrawal is not possible")
    
    
    @staticmethod
    def Withdrawal_rule_absent(Rule:Rule):
        return None
    
    #------------ Распределения truth ------------
    
    @staticmethod
    def Truth_distribution_standart(Rule:Rule) -> Dict[Fuzzy_statement,float]:
       return dict((Fi[0],Fi[1]*Rule.Consequent.Truth if Rule.Consequent.Truth is not None else Fi[1]) for Fi in Rule.Consequent.F.items())
      
    @staticmethod
    def Truth_distribution_students_problem(Rule:Rule) -> Dict[Fuzzy_statement,float]:
       return dict((Fi[0],Fi[1]*Rule.Antecedent[1] * Rule.Z) for Fi in Rule.Consequent.F.items())
    
    
    #------------ Композиции ------------
    
    @staticmethod
    def Composition_disjunction_matric(x:float,ux:float):
        return (Bool_expression(x) | Bool_expression(ux)).Truth if x is not None else ux
    
    @staticmethod
    def Composition_conjunction_matric(x:float,ux:float):
        return (Bool_expression(x) & Bool_expression(ux)).Truth if x is not None else ux
    
    @staticmethod
    def Composition_conjunction_nematric(x:float,ux:float):
        return min(x,ux)
    
    @staticmethod
    def Composition_larsen(x:float,ux:float):
        return x*ux
    
    #------------ Additions ------------
    
    @staticmethod
    def Addition_standart(Statement:Fuzzy_statement, New_Truth:float):
        Statement.Truth = New_Truth
    
    @staticmethod
    def Addition_Cukamoto(Statement:Fuzzy_statement, New_Truth:float): # Сохранить пару вида ci,wj где ci - Truth высказывания wj - предполагаемое Input_parameter_value его лингвистической переменной 
        if hasattr(Statement.a,"CW"):
            Statement.Linguistic_variable.CW.append(next((x,New_Truth) for x in Statement.Term.A.keys() if Statement.Term.A[x] == New_Truth))
        else:
            Statement.Linguistic_variable.CW = dict(next((x,New_Truth) for x in Statement.Term.A.keys() if Statement.Term.A[x] == New_Truth))
    
    #------------ Методы дефаззификации ------------
    
    @staticmethod
    def Accumulation_disjunction_matric(UX:List[float]):
        Sn = Bool_expression(0)
        for u in UX:
            Sn = Sn | Bool_expression(u)
        return Sn.Truth

    @staticmethod
    def Accumulation_disjunction_nematric(UX:List[float]) -> float:
        return max(UX)
    
    #------------ Методы дефаззификации ------------
    @staticmethod
    def defuzzification_method_centration_tightness(Linguistic_variable:Linguistic_variable) -> float:
        function = list(Linguistic_variable.Accumulated_function.items())
        нижняя_сумма = верхняя_сумма = 0
        ux1 = function[0]
        for ux2 in function:
            if ux2 != ux1:
                a = (ux2[1]-ux1[1])/(ux2[0]-ux1[0])
                b=ux1[1]-a*ux1[0]
                нижняя_сумма += (ux2[0]**2 - ux1[0]**2)*a/2 + (ux2[0] - ux1[0])*b
                верхняя_сумма += (ux2[0]**3-ux1[0]**3)*a/3 + (ux2[0]**2 - ux1[0]**2)*b/2
            ux1 = ux2
        
        return верхняя_сумма/нижняя_сумма if нижняя_сумма > 0 else 0
    
    @staticmethod
    def defuzzification_method_centration_tightness_points(Linguistic_variable:Linguistic_variable):
        return sum([x*ux for (x,ux) in Linguistic_variable.Accumulated_function.items()]) / sum(Linguistic_variable.Accumulated_function.values())
    
    @staticmethod
    def Defuzzification_method_center_plat(Linguistic_variable):
        суммарная_площадь = sum(Linguistic_variable.Accumulated_function.values()) 
        текущая_площадь = 0
        центр = 0
        for (x,ux) in Linguistic_variable.Accumulated_function.items():
            if текущая_площадь <= (суммарная_площадь - ux)/2:
                текущая_площадь += ux
                центр = x
                
        return центр
    
    @staticmethod
    def defuzzification_method_centration_tightness_modify(Linguistic_variable:Linguistic_variable):
        return sum([x*ux for (x,ux) in Linguistic_variable.CW])/sum(Linguistic_variable.CW.values())
    
    #-------------------- Стандартные алгоритмы ------------------------------
    @staticmethod
    def Models(name:str):
        return {
            "Students_problem":Model(Composition= Model.Composition_conjunction_matric,Rule_withdrawal =Model.Withdrawal_rule_absent,Rule_distribution_truth=Model.Truth_distribution_students_problem),
            "Students_problem2":Model(Composition= Model.Composition_conjunction_matric,Rule_withdrawal =Model.Withdrawal_rule_modus_ponens,Rule_distribution_truth=Model.Truth_distribution_students_problem),
            "Mamdani_matrix" :Model(),
            "Mamdani_nomatrix": Model(Composition= Model.Composition_conjunction_nematric,Rule_accumulation=Model.Accumulation_disjunction_nematric,Method_defuzzification=Model.defuzzification_method_centration_tightness_points),
            "Cukamoto":Model(Composition=Model.Composition_conjunction_nematric,Addition= Model.Addition_Cukamoto, Rule_accumulation = lambda  ux: None,Method_defuzzification = Model.defuzzification_method_centration_tightness_modify),
            "Larsens":Model(Composition= Model.Composition_larsen, Rule_accumulation = Model.Accumulation_disjunction_nematric, Method_defuzzification= Model.defuzzification_method_centration_tightness_points)
        }[name]
    
    
    def __init__(self,
                 Rule_withdrawal : Callable[[Fuzzy_variable,float], float] = Withdrawal_rule_modus_ponens,
                 Rule_distribution_truth: Callable[[Rule], Dict[Fuzzy_statement,float]] = Truth_distribution_standart,
                 Composition: Callable[[float,float],Union[float,None]] = Composition_disjunction_matric,
                 Addition: Callable[[Fuzzy_statement,float],None] = Addition_standart,
                 Rule_accumulation: Callable[[List[float]],Union[float,None]] = Accumulation_disjunction_matric,
                 Method_defuzzification: Callable[[Linguistic_variable],float] = defuzzification_method_centration_tightness):
        
        self.Rule_withdrawal  = Rule_withdrawal 
        self.Rule_distribution_truth = Rule_distribution_truth 
        self.Composition = Composition
        self.Addition = Addition
        
        self.Rule_accumulation = Rule_accumulation
        self.Method_defuzzification = Method_defuzzification
        
class Fuzzy_output:
    def __init__(self):
            self.Linguistic_variables = []
            self.Fuzzy_variables = []
            self.Statements = []
            self.CNF_List = {}
            self.Rules = []
    
    def Set_input_parameters(self,y:List[Linguistic_variable],x:List[float]):
        for i in range(0,len(y)):
           y[i].Input_parameter_value = x[i]

    def Predict(self,x:List[float]):
        
        List_var1 = self.Linguistic_variables.copy()
        for i in self.Rules: #Формирование списка входных переменных
            for j in i.Consequent.List_statements:
                if j.Linguistic_variable in List_var1:
                    List_var1.remove(j.Linguistic_variable)
                else:
                    j.Linguistic_variable.Defuzzified_Input_parameter = None
                    j.Linguistic_variable.Accumulated_function = None
            
        for i in range(0,len(List_var1)): # Задание значений входных переменных
            for j in [x for x in self.Linguistic_variables if x == List_var1[i]]:
                j.Input_parameter_value = x[i]

        for k in self.Fuzzy_variables:
            k.A = next(val for (key,val) in self.functions.items() if key.Name == k.Name).copy()
        
        for k in self.Rules:
            k.Not_using = True
        
        return self.Withdrawal(Model=Model.Models("Students_problem"),Reading_files = False) # логический вывод и формирование новых дефаззифицированных значений 
        
         
    def Withdrawal (self, Model = Model(),Reading_files = True):
        def Formation_base_references():
            def Read_Table(function, Name_file):
                try:
                 with open(Name_file, encoding = 'utf-8', mode = 'r') as Файл:
                    Шапка = Файл.readline().rstrip("\n")
                    Запись = Файл.readline().rstrip("\n")
                    while Запись:
                        try:
                            function(Запись.split("\t"))
                        except Exception as e:
                            print("Запись {Зп} была пропущена ввиду некорректности: {Ошибка}".format( 
                                                                                                 Ошибка = e, 
                                                                                                 Зп = dict(zip(Шапка.split("\t"),Запись.split("\t")))))
                        finally:
                            Запись = Файл.readline().rstrip("\n")
                except Exception as e:
                    print(f"Файл не найден: {Name_file}")
                
            def Строка_к_вещественному(Строка):
                try:
                    return float(Строка.replace(",","."))
                except:
                    return None 
        
            def Read_лингвистическую_переменную(Запись):
                self.Linguistic_variables.append(
                    Linguistic_variable(Запись[0],Строка_к_вещественному(Запись[1])))    

            def Read_нечёткую_переменную(Запись):
                НП = Fuzzy_variable(Запись[0])
                self.Fuzzy_variables.append(НП)
                self.Linguistic_variables[int(Запись[1])].T.append(НП)
        
            def Read_функцию_принадлежности(Запись):
                self.Fuzzy_variables[int(Запись[0])].A[Строка_к_вещественному(Запись[1])] = Строка_к_вещественному(Запись[2])
                
            def Read_высказывание(Запись):
                self.Statements.append(Fuzzy_statement(self.Linguistic_variables[int(Запись[0])],self.Fuzzy_variables[int(Запись[1])]))
        
            def Read_кнф(Запись):
                try:
                    self.CNF_List[int(Запись[1])].List_statements.append(self.Statements[int(Запись[0])])
                    self.CNF_List[int(Запись[1])].F[self.Statements[int(Запись[0])]] =float(Запись[2])
                except:
                    self.CNF_List[int(Запись[1])] = CNF([self.Statements[int(Запись[0])]],{self.Statements[int(Запись[0])]:float(Запись[2])})
        
            def Read_правила(Запись): 
                self.Rules.append(
                    Rule(self.CNF_List[int(Запись[0])],self.CNF_List[int(Запись[1])],Строка_к_вещественному(Запись[2])))
    
            for Этап in [
                (Read_лингвистическую_переменную ,  "Linguistic_variables.txt"),
                (Read_нечёткую_переменную ,  "Fuzzy_variables.txt"),
                (Read_функцию_принадлежности ,  "Function_application.txt"),
        
                (Read_высказывание ,  "Statements.txt"),
                (Read_кнф ,  "CNF.txt"),
                (Read_правила ,   "Rules.txt")
            ]:
                Read_Table(Этап[0],Этап[1])
        
        def Фаззификация(): # Нахождение значений функции принадлежности задействованых в правилах Termов на основе исходных данных
            for Rule in self.Rules:
                    for Statement in Rule.Antecedent.List_statements:
                        Statement.Truth = Statement.Calculate_truth()#Statement.Truth
                    
        def Агрегирование_подусловий(): # Определение truth условий каждого из правил
            for Rule in self.Rules:
                if Rule.Not_using:
                    
                    Truth = Rule.Antecedent.Calculate_truth()
                    Rule.Antecedent.Truth = Truth

                    Rule.Not_using = Truth is None or (Truth <= 1 and Truth >= 0) 
                    
                    Rule.Активность = (Truth is not None and Truth > 0) or (Model.Rule_withdrawal !=Model.Withdrawal_rule_modus_ponens) 
                
        def Активизация_подзаключений( # Определение truth заключений, подзаключений, а также новых Termов подзаключений
            Rule_withdrawal , 
            Rule_деления_truth, # Способ деления вычисленной по правилу truth между членами кнф 
            Composition,  # Способ композиции новой функции для Termов, Truth которых изменилась 
            Addition # Дополнительные действия если требуются
            ):
            for Rule in self.Rules:
                if Rule.Активность and Rule.Not_using:
                    #if Rule.Consequent.Truth is None: - стоит ли вычислять заново Truth заключения если она уже известна из предыдущих расчётов?
                    try:
                        Rule.Consequent.Truth = Rule_withdrawal (Rule) # Находим Truth заключения        
                        
                        New_Truth = Rule_деления_truth(Rule)  # Нахождение truth и новой функции принадлежности для Termов подзаключений
                        for Statement in Rule.Consequent.List_statements: # Нераспределённую Truth делим поровну между всеми членами кнф 
                            Statement.Term.A = dict((x,Composition(ux,New_Truth[Statement])) for (x,ux) in Statement.Term.A.items())
                            if Statement.Linguistic_variable.Input_parameter_value is not None:
                                Addition(Statement,Statement.Term.A[Statement.Linguistic_variable.Input_parameter_value])
                    except Exception as e:
                        pass#print(e)
                    finally:
                        Rule.Not_using = False
                                    
        def Аккумуляция_заключений(Rule_accumulation): # Объединение всех Termов каждой лингвистической переменной в аккумулированную функцию
            for ЛП in self.Linguistic_variables:
                if ЛП.Input_parameter_value is None:
                    ЛП.Accumulated_function = dict((x,Rule_accumulation([u.A[x] for u in ЛП.T])) for x in ЛП.T[0].A.keys())
        
        def Дефаззификация_выходных_переменных(Метод):
            for ЛП in self.Linguistic_variables:
                if ЛП.Input_parameter_value is None:
                    ЛП.Defuzzified_Input_parameter_value = Метод(ЛП)

        if Reading_files:
            Formation_base_references()
            self.functions = dict((NP,NP.A) for NP in self.Fuzzy_variables.copy())
       
        while True:
            Использованность_правил = [not x.Not_using for x in self.Rules]
            
            Фаззификация()
            Агрегирование_подусловий()
            Активизация_подзаключений(Model.Rule_withdrawal ,Model.Rule_distribution_truth,Model.Composition,Model.Addition)
            Аккумуляция_заключений(Model.Rule_accumulation)
            Дефаззификация_выходных_переменных(Model.Method_defuzzification)
            
            if all([not x.Not_using for x in self.Rules]) or all([a==p for a,p in zip(Использованность_правил,[not x.Not_using for x in self.Rules])]):
               break
        
        вывод = ""
        for ЛП in self.Linguistic_variables:
            try:
                if hasattr(ЛП,"Accumulated_function"): 
                    вывод += str(round(ЛП.Defuzzified_Input_parameter_value,2))
            except:
                print("Error")  
        
        return вывод
   
    def __str__(self):
        return """
---Лингвистические перменные---
{Linguistic_variables}
---Rules---
{Rules}
    """.format(
        Fuzzy_variables = "\n".join([str(Переменная) for Переменная in self.Fuzzy_variables]), 
        Linguistic_variables = "\n".join([str(Переменная) for Переменная in self.Linguistic_variables]),
        Rules = "\n".join([str(Rule) for Rule in self.Rules])) 
    
дз = Fuzzy_output()
print(дз.Withdrawal(Model.Models("Students_problem")))

st2 = ""
for i in range(0,11,1):
    for j in range(0,11,1):
        for k in range(0,11,1):
            st = дз.Predict([float(i),float(j),float(k)]) 
            if st != st2 and st!="0":
                print(f"{i}:{j}:{k} - {st}")
                st2 = st