# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个流程调度运行类，主要功能使用数据缓存和挂载对象运行流程管道对象，主要技术操作实例化
"""
模块介绍
-------

这是一个流程调度运行类，主要功能使用数据缓存和挂载对象运行流程管道对象，主要技术操作实例化

设计模式：

    无

关键点：    

    （1）数据缓存和hook技术

主要功能：            

    （1）流程调度运行器                                    

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractclassmethod
from sunflow.node import Node
from sunflow.scheduler import Pipeline
from sunflow.io import LocalDataCatalog
from sunflow.hook import HookManager



####### Scheduler流程运行类 #################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）数据缓存和hook技术                                                ###
### 主要功能：                                                            ###
### （1）流程管道运行器                                                    ###
############################################################################



###### Runner流程调度运行抽象类 #####################################################################
###################################################################################################



class BaseRunner(metaclass=ABCMeta):
    '''
    类介绍：

        这是一个流程调度运行器抽象类，主要功能使用数据缓存和挂载对象运行流程调度对象，主要技术操作实例化
    '''


    def __init__(self,scheduler,catalog,hook_manager):
        '''
        属性功能：

            定义一个流程调度运行类属性初始化方法

        参数：
            scheduler (object): 流程调度对象
            catalog (object): 目录对象
            hook_manager (object): 挂载对象
        '''

        self.scheduler = scheduler
        self.catalog = catalog
        self.hook_manager = hook_manager


    @abstractclassmethod
    def execute(self,is_release):
        '''
        方法功能：

            定义一个执行流程调度的抽象方法。

        参数：
            is_release (bool): 执行完节点是否清空缓存

        返回：
            无
        '''

        pass



###### SequentialRunner顺序运行实现类 #####################################################################
##########################################################################################################



class SequentialRunner(BaseRunner):
    '''
    类介绍：

        这是一个流程管道运行器具体实现类，主要功能使用数据缓存和挂载对象运行流程管道对象，主要技术操作实例化
    '''


    def __init__(self,scheduler,catalog,hook_manager):
        '''
        属性功能：

            定义一个流程管道运行类属性初始化方法，继承自BaseRunner

        参数：
            scheduler (object): 流程调度对象
            catalog (object): 目录对象
            hook_manager (object): 挂载对象
            done_nodes (object): 已完成节点集合
            remaining_nodes (object): 剩余节点集合
        '''

        super().__init__(scheduler=scheduler,catalog=catalog,hook_manager=hook_manager)
        self.done_nodes = set()
        self.remaining_nodes = set()


    def execute(self,is_release=True):
        '''
        方法功能：

            定义一个执行流程管道的具体实现方法，需要使用scheduler对象、catalog对象和hook_manager对象

        参数：
            is_release (bool): 执行完节点是否清空缓存

        返回：
            result (str): 运行结果信息
        '''

        ### 获取scheduler加载的节点列表
        nodes = self.scheduler.nodes
        ### 在__init__中已预先创建done_nodes和remaining_dones
        ### 开始循环执行scheduler节点
        for exec_index,node in enumerate(nodes):
            print('==========>>>>>> starting execute {} node'.format(exec_index))
            try:
                ### step-1-收集参数
                ### 获取输入列表
                required_inputs_list = node.get_inputs()
                ### 根据输入列表从缓存中获取对应输入参数数据,并整合成输入数据字典
                # required_input_data_dict = {}
                # for required_input in required_inputs_list:
                #     required_data = self.catalog.load(data_name=required_input)
                #     required_input_data_dict[required_input] = required_data
                hook_manager = HookManager()
                ### 以下涉及到数据目录datacatalog的相关hook功能操作，暂时只支持本地操作
                ### 获取数据目录类型
                data_catalog_type = type(self.catalog).__name__
                if data_catalog_type == 'LocalDataCatalog':
                    collected_data_dict = hook_manager.hook.collect_parameter_data_before_node_run_locally(catalog=self.catalog,inputs=required_inputs_list)
                ### step-2-运行函数
                required_input_data_dict = collected_data_dict[0]
                node_output_data = node.run(**required_input_data_dict)
                ### step-3-缓存结果
                ### 获取输出名称列表
                # node_output_list = node.get_outputs()
                # self.catalog.save(data_name=node_output_list[0],data_obj=node_output_data) ### 此处默认输出为一个对象，因此只使用输出列表的0索引
                node_output_name = node.get_outputs()
                ### 以下涉及到数据目录datacatalog的相关hook功能操作，暂时只支持本地操作
                ### 获取数据目录类型
                data_catalog_type = type(self.catalog).__name__
                if data_catalog_type == 'LocalDataCatalog':
                    hook_manager.hook.store_cache_data_after_node_run_locally(catalog=self.catalog,outputs=node_output_name,data_objects=[node_output_data])### 此处默认输出为一个对象，因此只使用输出列表的0索引;并且数据对象使用列表装载
                ### 调整节点运行状态集合done_nodes和remaining_done
                self.done_nodes.add(node)
                print('==========>>>>>> execute {} node well done!'.format(exec_index))
            except Exception:
                self.remaining_nodes = set(nodes) - set(self.done_nodes)
                raise
            ### 清空使用过的输入参数数据缓存
            if is_release == True:
                for release_input in required_inputs_list:
                    self.catalog.release(data_name=release_input)



##############################################################################################################################################################
##############################################################################################################################################################


