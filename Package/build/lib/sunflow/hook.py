# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个钩子挂载管理类，主要功能管理挂载钩子函数，主要技术静态方法
"""
模块介绍
-------

这是一个钩子挂载管理类，主要功能管理挂载钩子函数，主要技术静态方法

设计模式：

    无

关键点：    

    （1）hook技术

主要功能：            

    （1）插件管理                             

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import pluggy
import collections



####### hook挂载管理类 ######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）hook技术                                                         ###
### 主要功能：                                                            ###
### （1）插件管理                                                         ###
############################################################################



###### hook-markers工具类 ###########################################################################
####################################################################################################



HOOK_NAMESPACE = 'sunflow'
hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)



###### hook-specs接口类 ###########################################################################
###################################################################################################



### 本地数据目录接口
class LocalDatacatalogSpecs(object):
    '''
    类介绍：

        这是一个本地数据目录接口类
    '''

    @hook_spec
    def collect_parameter_data_before_node_run_locally(self,catalog,inputs):
        ''' 
        方法功能：

            定义一个运行前收集参数的方法

        参数：
            catalog (object): 数据目录对象
            inputs (list): 输入参数列表

        返回：
            data_dict (dict): 数据字典
        '''

        pass


    @hook_spec
    def store_cache_data_after_node_run_locally(self,catalog,outputs,data_objects):
        '''
        方法功能：

            定义一个运行后保存缓存数据的方法

        参数：
            catalog (object): 数据目录对象
            outputs (list): 输出参数列表
            data_objects (list): 数据对象列表

        返回：
            result (str): 运行结果信息
        '''

        pass



###### hook-impl实现类 #############################################################################
###################################################################################################



### 本地数据目录插件
class LocalDataCatalogPlugin(object):
    '''
    类介绍：

        这是一个本地数据目录插件类，主要功能数据缓存保存、加载操作
    '''

    @hook_impl
    def collect_parameter_data_before_node_run_locally(self,catalog,inputs):
        ''' 
        方法功能：

            定义一个运行前收集参数的方法

        参数：
            catalog (object): 数据目录对象
            inputs (list): 输入参数列表

        返回：
            data_dict (dict): 数据字典
        '''

        data_dict = collections.OrderedDict()
        for tmp_input in inputs:
            tmp_data = catalog.cache_data[tmp_input]
            data_dict[tmp_input] = tmp_data

        return data_dict


    @hook_impl
    def store_cache_data_after_node_run_locally(self,catalog,outputs,data_objects):
        '''
        方法功能：

            定义一个运行后保存缓存数据的方法

        参数：
            catalog (object): 数据目录对象
            outputs (list): 输出参数列表
            data_objects (list): 数据对象列表

        返回：
            result (str): 运行结果信息
        '''

        for tmp_output in zip(outputs,data_objects):
            tmp_name = tmp_output[0]
            tmp_data = tmp_output[1]
            catalog.cache_data[tmp_name] = tmp_data
        result = 'store cache data well done!'
        print(result)

        return result            

            

####### hook挂载管理类 ##############################################################################
####################################################################################################



class HookManager(object):
    '''
    类介绍：

        这是一个钩子挂载管理类，主要功能管理挂载钩子函数，主要技术静态方法
    '''


    def __init__(self):
        '''
        属性功能：

            定义一个属性功能初始化方法

        参数：
            hook_manager_instance (object): 钩子挂载管理对象实例
        '''

        self.hook_manager_instance = self.get_hook_manager_instance()
        self.hook = self.hook_manager_instance.hook


    def create_hook_manager(self):
        '''
        方法功能：

            定义一个创建挂载管理器的方法

        参数：
            无

        返回：
            hook_manager (object): hook管理器对象
        '''

        hook_manager = pluggy.PluginManager(HOOK_NAMESPACE)

        return hook_manager


    def register_plugins(self,hook_manager):
        '''
        方法功能：

            定义一个注册插件对象的方法

        参数：
            hook_manager (object): hook管理器对象

        返回：
            hook_manager (object): 已注册了插件对象的hook管理器对象
        '''

        ### 此处的插件暂时只支持本地数据目录的功能，后续会添加其他实用功能
        ### 添加挂载接口
        hook_manager.add_hookspecs(LocalDatacatalogSpecs)
        ### 注册挂载实现
        hook_manager.register(LocalDataCatalogPlugin()) ### 必须加()开启对象的callable

        return hook_manager


    def get_hook_manager_instance(self):
        '''
        方法功能：

            定义一个获取挂载管理器实例的方法

        参数：
            无

        返回：
            hook_manager (object): 已匹配好相关插件对象的hook管理器对象
        '''

        void_hook_manager = self.create_hook_manager()
        registed_hook_manager = self.register_plugins(hook_manager = void_hook_manager)

        return registed_hook_manager

        

#####################################################################################################################
#####################################################################################################################


