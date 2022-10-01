import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

def get_info(file_name=None,models=None,split=None, FP=None):
    dataset = file_name.split('/')[-2]
    path = os.path.join(os.path.join(file_name.split(dataset)[0],dataset),'result_save')
    des_model = [model for model in models if model in ['KNN','SVM','RF','XGB','DNN']]
    graph_model = [model for model in models if model not in ['KNN','SVM','RF','XGB','DNN']]
    info =pd.DataFrame()
    for model in des_model:
        model_dir = os.path.join(path,model)
        for des in FP:
            for sp in split:
                file = os.path.join(model_dir,'_'.join([sp,model,des,'best.csv']))
                df = pd.read_csv(file)
                data= df.groupby('type')['se','precision','auc_roc'].mean()
                data=data.reset_index()
                data['model']=model
                data['des'] = des
                data['split'] = sp
                info = pd.concat([info,data],ignore_index=True)
    for model in graph_model:
        model_dir = os.path.join(path,model)

        for sp in split:
            file = os.path.join(model_dir,'_'.join([sp,model,'best.csv']))
            df = pd.read_csv(file)
            data= df.groupby('type')['se','precision','auc_roc'].mean()
            data = data.reset_index()
            data['model']=model
            data['des'] = model
            data['split'] = sp
            info = pd.concat([info,data],ignore_index=True)
    info =info.sort_values('auc_roc',ascending=False)
    info_save = file_name.replace('.csv','_auc.csv')
    info.to_csv(info_save,index=False)

# def show_model(file_name=None,models=None,split=None, FP=None):
#     dataset = file_name.split('/')[-2]
#     model_path = os.path.join(os.path.join(file_name.split(dataset)[0], dataset), 'model_save')
#     para_path = os.path.join(os.path.join(file_name.split(dataset)[0], dataset), 'model_save')
#     des_model = [model for model in models if model in ['KNN', 'SVM', 'RF', 'XGB', 'DNN']]
#     graph_model = [model for model in models if model not in ['KNN', 'SVM', 'RF', 'XGB', 'DNN']]
#     for model in des_model:
#         if model =='DNN':
#             pass
#         else:
#             for sp in split:
#                 for des in FP:
#                     param_file = '_'.join([sp,model,des,'para.csv'])
def para(file_name):
    info_save = file_name.replace('.csv', '_auc.csv')
    data = pd.read_csv(info_save)

    data=data[data['type']=='te']
    data = data.sort_values('auc_roc', ascending=False)
    data['a_sord'] = [i for i in range(len(data))]
    data['f1-score'] = data.apply(lambda x:(2*(x['precision']*x['se'])/(x['precision']+x['se'])),axis=1)
    data=data.sort_values('f1-score',ascending=False)
    data['i_sord'] = [i for i in range(len(data))]
    data['value'] = data.apply(lambda x:x['a_sord']+x['i_sord'],axis=1)
    data = data.sort_values('value')
    data=data[[ 'auc_roc', 'model', 'des', 'split', 'f1-score']]
    print(data)


para('/data/jianping/bokey/OCAICM/dataset/chembl31_1663577628.6572962/chembl31_1663577628.6572962.csv')