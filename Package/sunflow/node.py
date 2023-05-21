# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个装载函数对象的节点类，主要功能函数对象节点实例化，主要技术property描述符动态属性
"""
模块介绍
-------

这是一个装载函数对象的节点类，主要功能函数对象节点实例化，主要技术property描述符动态属性

设计模式：

    无

关键点：    

    （1）Property描述符动态属性

主要功能：            

    （1）函数节点对象化                                             

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################






####### Node节点对象类 ######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）Property描述符动态属性                                            ###
### 主要功能：                                                            ###
### （1）函数节点对象化                                                    ###
############################################################################



###### Node节点对象类 #####################################################################
##########################################################################################



class Node(object):
    '''
    类介绍：

        这是一个装载函数对象的节点类，主要功能函数对象节点实例化，主要技术property描述符动态属性
    '''


    def __init__(self,func,inputs,outputs,name):
        '''
        属性功能：

            定义一个节点类属性初始化方法

        参数：
            func (object): 函数对象
            inputs (list): 输入列表
            outputs (list): 输出列表
            name (str): 函数名称
        '''

        ### 参数检验
        ### 验证func参数是否为可调用函数对象
        if not callable(func):
            raise ValueError(_node_error_message(msg='func argument must be a function,not {}'.format(type(func).__name__)))
        ### 验证inputs参数是否存在且是否为列表、字典和字符串
        if inputs and not isinstance(inputs,(list,dict,str)):
            raise ValueError(_node_error_message(msg='inputs argument must be one of [String,List,Dict,None],not {}'.format(type(inputs).__name__)))
        ### 验证outputs参数是否存在且是否为列表、字典和字符串
        if outputs and not isinstance(outputs,(list,dict,str)):
            raise ValueError(_node_error_message(msg='outputs argument must be one of [String,List,Dict,None],not {}'.format(type(outputs).__name__)))
        ### 验证name参数是否存在且是否为列表、字典和字符串
        if name and not isinstance(name,(list,dict,str)):
            raise ValueError(_node_error_message(msg='name argument must be one of [String,List,Dict,None],not {}'.format(type(name).__name__)))
        ### 开始加载验证后参数
        self._func = func
        self._inputs = inputs
        self._outputs = outputs
        self._name = name


    def get_func(self):
        '''
        方法功能：

            定义一个获取节点函数的方法

        参数：
            无

        返回：
            node_func (object): 节点函数对象
        '''

        node_func = self._func

        return node_func


    def get_inputs(self):
        '''
        方法功能：

            定义一个获取节点输入参数的方法

        参数：
            无

        返回：
            node_inputs (list): 节点输入列表
        '''

        node_inputs = self._inputs

        return node_inputs


    def get_outputs(self):
        '''
        方法功能：

            定义一个获取节点输出列表的方法

        参数：
            无

        返回：
            node_outputs (list): 节点输出列表
        '''

        node_outputs = self._outputs

        return node_outputs


    @property
    def func(self):
        '''
        方法功能：

            定义一个描述符协议property动态属性获取函数对象方法

        参数：
            无

        返回：
            无
        '''

        return self._func


    @func.setter
    def func(self,func):
        '''
        方法功能：

            定义一个描述符协议property动态属性设置函数对象方法

        参数：
            func (object): 
        '''

        self._func = func


    @property
    def inputs(self):
        '''
        方法功能：

            定义一个描述符协议动态属性获取输入方法

        参数：
            无

        返回：
            _inputs (list): 参数属性输入
        '''

        return self._inputs


    @property
    def outputs(self):
        '''
        方法功能：

            定义一个描述符协议动态属性获取输出方法

        参数：
            无

        返回：
            _outputs (list): 参数属性输出
        '''

        return self._outputs


    @property
    def name(self):
        '''
        方法功能：

            定义一个描述符协议动态属性获取名称方法

        参数：
            无

        返回：
            _name (str): 参数属性名称
        '''

        return self._name


    def run(self,*args,**kwargs):
        '''
        方法功能：

            定义一个节点运行的方法

        参数：
            args (tuple): 输入参数元组
            kwargs (dict): 输入参数字典

        返回：
            run_result (object): 运行结果对象
        '''

        run_result = self.func(*args,**kwargs)
        
        return run_result



####### 辅助函数集合 ###########################################################################################################
###############################################################################################################################



def _node_error_message(msg):
    '''
    函数功能：

        定义一个输出节点错误信息的函数

    参数：
        msg (str): 错误信息

    返回：
        result (str): 组合好的错误信息输出
    '''

    result_a = "Invalid Node defination:{} \n".format(msg)
    result_b = "Format should be: Node(function,inputs,outputs)"
    result = result_a + result_b

    return result



################################################################################################################################
################################################################################################################################


