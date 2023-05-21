# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个数据目录对象类，主要功能缓存数据，主要技术orderdict
"""
模块介绍
-------

这是一个数据目录对象类，主要功能缓存数据，主要技术orderdict

设计模式：

    无

关键点：    

    （1）orderdict

主要功能：            

    （1）数据缓存                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractclassmethod
import collections



####### 数据目录对象类 ######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）orderdict                                                        ###
### 主要功能：                                                            ###
### （1）数据缓存                                                         ###
############################################################################



###### 数据目录对象基类 #############################################################################
###################################################################################################



class BaseDataCatalog(metaclass=ABCMeta):
    '''
    类介绍：

        这是一个数据目录对象基类，主要功能缓存数据，主要技术orderdict
    '''


    def __init__(self):
        '''
        属性功能：

            定义一个数据目录对象类属性初始化方法

        参数：
            cache_data_info (orderdict): 缓存数据信息有序字典
        '''

        self.cache_data_info = collections.OrderedDict()


    @abstractclassmethod
    def save(self,data_name,data_obj):
        '''
        方法功能：

            定义一个保存数据的方法

        参数：
            data_name (str): 数据集名称
            data_obj (object): 数据集对象

        返回：
            result (str): 运行结果信息
        '''

        pass

    
    @abstractclassmethod
    def load(self,data_name):
        '''
        方法功能：

            定义一个加载数据的方法

        参数：
            data_name (str): 数据集名称

        返回：
            data_obj (object): 数据集对象
        '''

        pass

    
    @abstractclassmethod
    def release(self,data_name):
        '''
        方法功能：

            定义一个释放数据空间的方法

        参数：
            data_name (str): 数据集名称

        返回：
            result (str): 运行结果信息
        '''

        pass



###### 本地数据目录对象类 ###########################################################################
###################################################################################################



class LocalDataCatalog(BaseDataCatalog):
    '''
    类介绍：

        这是一个数据目录对象类，主要功能缓存数据，主要技术orderdict
    '''


    def __init__(self):
        '''
        属性功能：

            定义一个数据目录对象类属性初始化方法

        参数：
            cache_data_info (orderdict): 缓存数据信息有序字典
            cache_data (orderdict): 数据缓存有序字典
        '''

        super().__init__()
        self.cache_data = collections.OrderedDict()


    def save(self,data_name,data_obj):
        '''
        方法功能：

            定义一个保存数据的方法

        参数：
            data_name (str): 数据集名称
            data_obj (object): 数据集对象

        返回：
            result (str): 运行结果信息
        '''

        self.cache_data[data_name] = data_obj
        result = '{} dataset save well done!'.format(data_name)
        print(result)

        return result


    def load(self,data_name):
        '''
        方法功能：

            定义一个加载数据的方法

        参数：
            data_name (str): 数据集名称

        返回：
            data_obj (object): 数据集对象
        '''

        data_obj = self.cache_data[data_name]
        result = '{} dataset load well done!'.format(data_name)
        print(result)

        return data_obj


    def release(self,data_name):
        '''
        方法功能：

            定义一个释放数据空间的方法

        参数：
            data_name (str): 数据集名称

        返回：
            result (str): 运行结果信息
        '''

        del self.cache_data[data_name]
        result = '{} dataset release well done!'.format(data_name)
        print(result)

        return result



############################################################################################################################
############################################################################################################################


