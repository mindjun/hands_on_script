# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:13:27 2017

@author: yimeng.zhang
"""

# 导入需要的库
import numpy as np
import scipy.stats as st
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,robust_scale
from sklearn.cross_validation import train_test_split, cross_val_score, KFold,ShuffleSplit
from sklearn.ensemble import BaggingRegressor
from sklearn.feature_selection import VarianceThreshold,SelectKBest,chi2
#from minepy import MINE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel


from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.neural_network import MLPClassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from xgboost.sklearn import XGBClassifier
import xgboost as xgb
from xgboost import XGBClassifier
from imblearn.over_sampling import RandomOverSampler,SMOTE
'''
1. 数据载入
    导入数据
    切分训练集和测试集

2. 数据预处理
    (opt) 标准化 StandardScaler 
    missing值填补 （在数据库中完成）
    
3. 特征工程

3. 模型训练
    逻辑回归模型
    ADABOOST

4. 效果评估
    测试集混合矩阵
    cross-validation
    
'''
np.set_printoptions(precision=3)
standard_method = ''
model = ''
random_seed = 1
# 导入数据并分为训练集和测试集
df = pd.read_excel(io=r'E:\Desktop\工作\23 P2P商户评级\二期\样本v0.3\data-12重点坏商户和好商户.xlsx')
#print(df.columns)
x = df.iloc[:,2:]
y = df.iloc[:,1]
#print(y)
print('total sample:',x.shape[0])
cv = ShuffleSplit(x.shape[0],n_iter=10,test_size=0.2,random_state=random_seed) # 划分方式

#print(y)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=random_seed)
#print(y_train)
#print(y_test)
print(y_train.value_counts())
#ros = RandomOverSampler(ratio={0:302, 1:150}, random_state=0)
#X_train_resampled, y_train_resampled = ros.fit_sample(X_train, y_train)
#print(pd.Series(y_train_resampled).value_counts())

sm = SMOTE(ratio={0:302, 1:150}, random_state=0)
X_train_resampled, y_train_resampled = sm.fit_sample(X_train, y_train)
print(pd.Series(y_train_resampled).value_counts())

# 标准化 
if standard_method == 'zscore':
    sc = StandardScaler()
    #sc.fit(X_train)
    X_all_std = sc.fit_transform(x)
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.fit_transform(X_test)
    print('标准化方法','z-score')
    #print(X_test_std)

elif standard_method == 'maxmin':
    sc = MinMaxScaler()
    X_all_std = sc.fit_transform(x)
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.fit_transform(X_test)
    print('标准化方法','maxmin')
    
elif standard_method == 'robust_scale':
    #sc = robust_scale(X, axis=0, with_centering=True, with_scaling=True, quantile_range=(25.0, 75.0), copy=True)
    X_all_std = robust_scale(X=x, axis=0, with_centering=True, with_scaling=True, quantile_range=(25.0, 75.0), copy=True)
    X_train_std = robust_scale(X=X_train, axis=0, with_centering=True, with_scaling=True, quantile_range=(25.0, 75.0), copy=True)
    X_test_std = robust_scale(X=X_test, axis=0, with_centering=True, with_scaling=True, quantile_range=(25.0, 75.0), copy=True)
    print('标准化方法','robust_scale')
    
else:
    print('no standardize')


# 特征工程
# 选择K个最好的特征，返回选择特征后的数据
#selectk = SelectKBest(chi2,k=60)
#X_train_std = selectk.fit_transform(X_train_std, y_train)
#print(X_train_std.shape)

# 逻辑回归拟合
# 模型1 - 未标准化
#lr_model = LogisticRegression()
##lr_model.fit(X_train, y_train)
if model == 'LR':
    # 模型2 - 标准化
    lr_model_std = LogisticRegression()
    lr_model_std.fit(X_train_std, y_train)
    
    #X_all_std = selectk.transform(X_all_std)
          
    # score 标准化
    # 准确率： 整体的正确率
    print('逻辑回归模型')
    scores_std = cross_val_score(lr_model_std, X_all_std, y, cv=10, scoring='accuracy')  
    print('准确率：',np.mean(scores_std), scores_std)  
    '''
    精确率（precision）P=TP/(TP+FP)
    '''
    precisions_std = cross_val_score(lr_model_std, X_all_std, y, cv=10, scoring='precision')  
    print('精确率：', np.mean(precisions_std), precisions_std) 
    '''
    召回率（recall）R=TP/(TP+FN) 
    '''
    recalls_std = cross_val_score(lr_model_std, X_all_std, y, cv=10, scoring='recall')  
    print('召回率：', np.mean(recalls_std), recalls_std)  
    
  
    # 测试集效果检验，输出混淆矩阵
    y_predict = lr_model_std.predict(X_test_std)
    y_prob = lr_model_std.predict_proba(X_test_std)
    #print(y_test, y_prob)
    print(confusion_matrix(y_test, y_predict))


elif model == 'e-tree':
    clf = ExtraTreesClassifier()
    clf = clf.fit(X_train_std, y_train)
    #特征重要性(数值越高特征越重要)
    #print(clf.feature_importances_)
    e_tree_fea = SelectFromModel(clf, threshold='1.25*mean',prefit=True)
    x_tree = e_tree_fea.transform(X_train_std)
    clf = ExtraTreesClassifier()    
    clf = clf.fit(x_tree,y_train)
    X_all_std = e_tree_fea.transform(X_all_std)
    print('x-tree模型')
    scores_std = cross_val_score(clf, X_all_std, y, cv=10, scoring='accuracy')  
    print('准确率：',np.mean(scores_std), scores_std)  
    
    precisions_std = cross_val_score(clf, X_all_std, y, cv=10, scoring='precision')  
    print('精确率：', np.mean(precisions_std), precisions_std) 
    '''
    召回率（recall）R=TP/(TP+FN) 
    '''
    recalls_std = cross_val_score(clf, X_all_std, y, cv=10, scoring='recall')  
    print('召回率：', np.mean(recalls_std), recalls_std)  

    
elif model == 'mix':
    classifiers = {
    'KN': KNeighborsClassifier(3),
    'SVC': SVC(kernel="linear", C=0.025),
    'DT': DecisionTreeClassifier(max_depth=5),
    'RF': RandomForestClassifier(n_estimators=30, max_depth=10, max_features=1),  # clf.feature_importances_
    'ET': ExtraTreesClassifier(n_estimators=30, max_depth=None),  # clf.feature_importances_
    'AB': AdaBoostClassifier(base_estimator=GradientBoostingClassifier(), algorithm='SAMME.R', n_estimators=150),
    'GB': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0), # clf.feature_importances_
    'GNB': GaussianNB(),
    #'LD': LinearDiscriminantAnalysis(),
    'LR': LogisticRegression(),
    'XG': XGBClassifier()
    }

    
    for name, clf in classifiers.items():
        scores = cross_val_score(clf, X=x, y=y, cv=cv, scoring='accuracy')
        print('accu',name,'\t--> ',scores.mean(),scores)
#        scores = cross_val_score(clf, X_all_std, y, cv=cv, scoring='precision')
#        print('precision',name,'\t--> ',scores.mean(),scores)
#        scores = cross_val_score(clf, X_all_std, y, cv=cv, scoring='recall')
#        print('recall',name,'\t--> ',scores.mean(),scores)
  
else:
    pass
#     
ada_model_std = XGBClassifier() 
#scores = cross_val_score(ada_model_std, X=x, y=y, cv=cv, scoring='accuracy')
#print('accu','XGB','\t--> ',scores.mean(),scores)
#one_to_left = st.beta(10, 1) 
#from_zero_positive = st.expon(0, 50)
#params = {  
#    "n_estimators": st.randint(3, 40),
#    "max_depth": st.randint(3, 40),
#    "learning_rate": st.uniform(0.05, 0.4),
#    "colsample_bytree": one_to_left,
#    "subsample": one_to_left,
#    "gamma": st.uniform(0, 10),
#    'reg_alpha': from_zero_positive,
#    "min_child_weight": from_zero_positive,
#}
#
#
#gs = RandomizedSearchCV(ada_model_std, params, n_jobs=1)  
#gs.fit(X_train, y_train)
#print(gs.best_estimator_)
#
print('训练集大小',X_train.shape)
print('测试集大小',X_test.shape)
print('重复抽样后训练集大小',X_train_resampled.shape)

ada_model_std.fit(X_train_resampled, y_train_resampled)
##print(ada_model_std.get_params)


y_predict = ada_model_std.predict(X_test.as_matrix())
#y_prob = ada_model_std.predict_proba(X_test)
#print(y_predict,y_prob)
print(confusion_matrix(y_test, y_predict))
print(ada_model_std.score(X=X_test.as_matrix(),y=y_test))


#for i in y_test:
#    print(i)

# feature selection 
#feature_imp = ada_model_std.feature_importances_
#for i in feature_imp:
#    print(i)
#ada_model_feature_selection = SelectFromModel(ada_model_std, threshold=10e-6,prefit=True)
#x_all_feature_selection = ada_model_feature_selection.transform(x)
#X_train_feature_selection =  ada_model_feature_selection.transform(X_train)
#X_test_feature_selection = ada_model_feature_selection.transform(X_test)
#
#ada_model2 = AdaBoostClassifier(n_estimators=150)
#ada_model2.fit(X_train_feature_selection, y_train)
#print('特征筛选后训练集大小',X_train_feature_selection.shape)
#print('特征筛选后测试集大小',X_test_feature_selection.shape)
#print(x_all_feature_selection.shape)
#scores2 = cross_val_score(ada_model2, X=x_all_feature_selection, y=y, cv=cv, scoring='accuracy')
#print('accu ADABOOST 特征筛选后模型','\t--> ',scores2.mean(),scores2)
#y_predict2 = ada_model2.predict(X_test_feature_selection)
#y_prob2 = ada_model2.predict_proba(X_test_feature_selection)
##print(y_test, y_prob)
#print(confusion_matrix(y_test, y_predict2))
#print(ada_model2.score(X=X_test_feature_selection,y=y_test))

#ada_model2.fit(X_train_feature_selection,y_)


#print(X_all_std.shape)
#print(x_feature_selection.shape)
#
#ada_model_std2 = AdaBoostClassifier(n_estimators=150)
#ada_model_std2.fit(X_train_std_feature_selection, y_train)        
#scores2 = cross_val_score(ada_model_std2, x_all_std_feature_selection, y, cv=10, scoring='accuracy')       
#print('accu','adaboost','\t--> ',scores2.mean(),scores2)

# 对2 家商户进行测试
#df2 = pd.read_excel(io=r'E:\Desktop\工作\23 P2P商户评级\二期\样本v0.3\data-去除好坏商户3个月为0.xlsx')
##print(df.columns)
#x2 = df2.iloc[:,2:]
#y2 = df2.iloc[:,1]
##print(y)
#print(x2.shape)
#print('total test sample:',x2.shape[0])
#y_predict2 = ada_model_std.predict(x2)
#y_prob2 = ada_model_std.predict_proba(x2)
## print('y-predict2',y_predict2,y_prob2)
#print(confusion_matrix(y2,y_predict2))