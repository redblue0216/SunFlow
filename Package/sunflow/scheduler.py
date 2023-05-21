# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个调度管理类，主要功能组合节点，形成执行流程；主要技术内部方法和魔法方法
"""
模块介绍
-------

这是一个调度管理类，主要功能组合节点，形成执行流程；主要技术内部方法和魔法方法

设计模式：

    无

关键点：    

    （1）属性功能

主要功能：            

    （1）功能节点管理                                      

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import collections



####### Scheduler流程管理类 #################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）属性功能                                                         ###
### 主要功能：                                                            ###
### （1）功能节点管理                                                     ###
############################################################################



###### Pipeline流程管道类 #####################################################################
##############################################################################################



class Pipeline(object):
    '''
    类介绍：

        这是一个流程管理类，主要功能组合节点，形成执行流程；主要技术内部方法和魔法方法
    '''


    def __init__(self,nodes):
        '''
        属性功能：

            定义一个流程管道类属性初始化方法

        参数：
            nodes (list): 节点对象列表(有序)
            _nodes_by_name (list): 节点名称列表(有序)
            _nodes_by_input (orderdict): 节点输入列表(有序)
            _nodes_by_output (orderdict): 节点输出列表(有序)
        '''

        ### 验证输入参数
        if nodes is None:
            raise ValueError("nodes argument of pipeline is None.It must be an iterable of nodes and/or pipeline instead.")
        if nodes and not isinstance(nodes,(list)):
            raise ValueError("nodes argument of pipeline is not list.It must be an list of nodes and/or pipeline instead.")
        ### 装载节点列表
        nodes = list(nodes)
        self.nodes = nodes
        ### 解析装载的节点生成相应的信息数据列表
        ### _nodes_by_name
        _nodes_by_name_list = [tmp_node.name for tmp_node in nodes]
        ### _nodes_by_input,_nodes_by_output
        _nodes_by_inputs_orderdict = collections.OrderedDict()
        _nodes_by_outputs_orderdict = collections.OrderedDict()
        for tmp_node in nodes:
            _nodes_by_inputs_orderdict[tmp_node.name] = tmp_node.inputs
            _nodes_by_outputs_orderdict[tmp_node.name] = tmp_node.outputs
        ### 装载名称、输入和输出列表
        self._nodes_by_name = _nodes_by_name_list
        self._nodes_by_inputs = _nodes_by_inputs_orderdict
        self._nodes_by_outputs = _nodes_by_outputs_orderdict


    def __add__(self,other):
        '''
        方法功能：

            定义一个加号运算符的魔法方法

        参数：
            other (object): 另一个流程管道对象

        返回：
            new_pipeline (object): 新组合的流程管道对象
        '''

        ### 验证参数对象
        if not isinstance(other,Pipeline):
            return NotImplemented
        ### 拼接两个流程管道对象
        new_nodes = list(self.nodes + other.nodes)
        new_pipeline = Pipeline(nodes = new_nodes)

        return new_pipeline


    def names(self):
        '''
        方法功能：

            定义一个列举流程管道中节点名称的方法

        参数：
            无

        返回：
            names (list): 节点名称列表
        '''

        return self._nodes_by_name


    def inputs(self):
        '''
        方法功能：

            定义一个列举流程管道中输入参数的方法

        参数：
            无

        返回：
            inputs (orderdict): 输入参数有序字典
        '''

        return self._nodes_by_inputs


    def outputs(self):
        '''
        方法功能：

            定义一格列举流程管道中输出参数的方法

        参数：
            无

        返回：
            outputs (orderdict): 输出参数有序字典
        '''

        return self._nodes_by_outputs



##############################################################################################################################################
##############################################################################################################################################


