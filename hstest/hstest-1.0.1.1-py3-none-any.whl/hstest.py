# CTGAN 
import warnings
import warnings
from ctgan import CTGANSynthesizer
from pycaret.classification import *
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN

warnings.simplefilter(action='ignore', category=FutureWarning)

with warnings.catch_warnings():
    # ignore all caught warnings
    warnings.filterwarnings("ignore")
    # execute code that will generate warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

#  (1) 정형 데이터일 경우,
# 불균형 확인부 함수 선언


def pycaret_acc(trd,label):
    warnings.filterwarnings('ignore')
    clf = setup(data = trd, target=label,data_split_shuffle=True, silent=True, normalize= True, fix_imbalance = False, session_id=42) 
    best_1 = compare_models(sort = 'Accuracy', n_select = 1, exclude=['xgboost','dummy','svm','ridge'])
        
def origin(x, label):
    # nothing
    return x
    
def imbalance_CTGAN(x, label):
        #print(sum(train_data.Group==0), sum(train_data.Group==1) )
        #print(sum(test_data.Group==0), sum(test_data.Group==1) )
        
        # 라벨에 해당하는 "컬럼" 을 정의하는 문구가 필요함 
        # Group 을 라벨로 대체
        
    
    train_data_0= x[x[label]==x[label].unique()[0]]
    train_data_1= x[x[label]==x[label].unique()[1]]
        ### len(train_data_0)-len(train_data_1)개 생성
    
    maxa = max(len(train_data_0),len(train_data_1))
    mina = min(len(train_data_0),len(train_data_1))
    random_sample= maxa-mina
    
    data = train_data_1
    ctgan = CTGANSynthesizer(epochs=100)
    ctgan.set_random_state(123)
    ctgan.fit(data,[label])
    samples_129_1 = ctgan.sample(random_sample)
    samples_129_1[label] = 1
    train_129 = pd.concat([train_data_1 ,samples_129_1 ], axis = 0 )
    train_data_ctgan =pd.concat([train_data_0 , train_129], axis = 0)
    return train_data_ctgan
    # ADASYN
def imbalance_ADASYN(x, label):
    ada = ADASYN(random_state=42)
    # 너무 적은 데이터 -> 오류
    
    X, y = x.drop(label, axis = 1), x[label]
    X_res, y_res = ada.fit_sample(X, y)
    df_X_res = pd.DataFrame(X_res)
    df_y_res = pd.DataFrame(y_res)
    df_X_res.columns = X.columns
    #df_y_res.columns
    train_data_adasyn = pd.concat([df_X_res, df_y_res[label]] , axis = 1)
    return train_data_adasyn
    # UNDERSAMPLING 
def imbalance_UNDER(x, label):
    
    #print(self.data)
    #print(self.data[self.label].unique()[0])
    #print(self.data[self.label].unique()[1])
    
    train_data_0= x[x[label]==x[label].unique()[0]]
    train_data_1= x[x[label]==x[label].unique()[1]]
    
    if len(train_data_0) > len(train_data_1) :
        train_data_under = pd.concat([train_data_0.sample(len(train_data_1)),train_data_1], axis = 0).reset_index(drop= True)
    else : 
        train_data_under = pd.concat([train_data_1.sample(len(train_data_0)),train_data_0], axis = 0).reset_index(drop= True)
    
    #print(train_data_under)
    return train_data_under
    #SMOTE
def imbalance_SMOTE(x, label):

    smote = SMOTE(random_state=0)
    X_train_over,y_train_over = smote.fit_sample(x.drop(label, axis = 1),x[label])
    train_data_smote = pd.concat([X_train_over, y_train_over], axis = 1) 
    return train_data_smote
    
def ttt(model,data,label):
    
    pycaret_acc(model(data, label), label)
    target_acc = pull()['Accuracy'][0]
    target_model = pull()['Model'][0]
    return target_acc,target_model      

    
    
class Some:
    data = {}
# 입력 함수 선언
    def __init__(self, data):
        self.data = data
        self.label, self.list_im = Some.imbalance_judgment(self.data)
#####################################################################################################
    
# label 결정 함수 선언
    def input_label():
        #for test input
        #label = input("label_input : ")
        label = 'Group'
        if label == "exit" : 
            
            raise Exception('작동 종료')
        else:  
            pass
            return label

#####################################################################################################
    #
# 전처리 함수 선언
    
    # 이상치 대체 함수 선언
    def anomaly_replace(self): 
        anomaly_data = self.data 
        # preprocessing -> anomaly_data 
        
        
        # being preprocessing 
        pre_ano_data = self.data 
        
        # 결측값 대체 함수 선언
        def impute_data(x):
            pass
        # split for impute 
        
        # impute
        
        #    return imputed_data
        
        imputed_data = impute_data(pre_ano_data)
        
        return imputed_data

    #return 전처리된 데이터    


#####################################################################################################
    def imbalance_judgment(self):  
        label = Main.input_label()
        if len(self[label].unique()) <= 1 : 
                # 단일 Label 시 오류 출력
            print("label에 대한 입력이 잘못되었거나 단일 Label 데이터입니다.")
            imbalance_judgment(self)
                # break는 while 이나 for 문에서 사용
        else : 
            # label unique 확인
            list_label = []
            for i in range(len(self[label].unique())):
                list_label.append(self[label].unique()[i])
                # print((list_label)) 
                # label별 데이터 개수 확인
                tmp = []
                for i in list_label :
                    tmp.append(len(self[self[label]==i])) 
                value = int( max(tmp) == min(tmp))
            if max(tmp) == min(tmp) : 
                            # True : 1 
                print("불균형 없음")
                list_im = [origin]#[origin, imbalance_UNDER, imbalance_SMOTE, imbalance_ADASYN, imbalance_CTGAN]
                return  label, list_im        
            else :

                print("불균형 있음")
                            # false : 0 
                            # False ->  불균형이라고 판단함 
                list_im = [origin, imbalance_UNDER, imbalance_SMOTE, imbalance_ADASYN, imbalance_CTGAN]
                return  label, list_im   
#####################################################################################################

# 출력 부분 함수 선언

    def work_last(self):
        #print(Main.imbalance_UNDER(self))
        #print(Main.imbalance_CTGAN(self))
        data = self.data
        label = self.label 
        #print(data)
        #print(imbalance_SMOTE)
        
        #print( ttt( imbalance_SMOTE, data , label))
        tmp = 0
        name = 0 
        i_iter = 0
        list_ls= []
        list_im = self.list_im
        for i in iter(list_im):
            acc, model = ttt(i,data,label)
            idr = str(i.__name__)
            if tmp > acc:
                tmp = tmp
                name = model

                #model = i.target_model
            else : 
                tmp = acc
                name = model
                i_iter = str(i)
            list_ls.append([acc, model, idr])

        print(tmp, name, i_iter)  #1
        df_ls = pd.DataFrame(list_ls)
        print(df_ls)
        number = df_ls.index[  df_ls[0] == max(df_ls[0]) ]
        print(df_ls.iloc[number]) #2
        print("last_comparison_complete\n")
        #print(self.data)

#####################################################################################################
