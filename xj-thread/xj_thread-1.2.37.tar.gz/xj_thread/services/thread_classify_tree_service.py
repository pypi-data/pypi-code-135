"""
Created on 2022-04-11
@author:刘飞
@description:发布子模块逻辑处理
"""
import logging

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import F
from rest_framework import serializers

from ..models import ThreadAuth
from ..models import ThreadClassify
from ..models import ThreadClassify
from ..models import ThreadExtendField
from ..models import ThreadShow
from ..models import ThreadTag
from ..serializers import ThreadAuthListSerializer
from ..serializers import ThreadTagSerializer
from ..utils.model_handle import format_params_handle

log = logging.getLogger()


class ThreadClassifyTreeServices:
    def __init__(self):
        pass

    @staticmethod
    def get_classify_tree(classify_id=None, classify_value=None):
        """
        类别树。
        """
        # 第一步，把类别列表全部读出来
        classify_set = ThreadClassify.objects.annotate(
            classify_value=F('value'),
            category_value=F('category_id__value'),
            show_value=F('show_id__value'),
        ).order_by('sort').values(
            'id',
            'classify_value',
            'name',
            'show_value',
            'category_value',
            'description',
            'icon',
            'sort',
            'parent_id',
        )
        print("> classify_set:", classify_set)
        classify_list = list(classify_set)
        print("> classify_list:", classify_list)

        # 第二步，遍历列表，把数据存放在dict里
        parent_classify_dict = {}  # 父类别ID索引列表字典
        classify_tree = {}
        for item in classify_list:
            # 查找到树根
            if item['id'] == classify_id or item['classify_value'] == classify_value:
                classify_tree = item

            # 边界检查：如果没有父类别，不需要生成索引列表字典
            if not item['parent_id']:
                continue
            
            pid = str(item['parent_id'])  # 父ID的字符串

            # 边界检查：如果索引未创建，则初始化
            if not parent_classify_dict.get(pid, None):
                parent_classify_dict[pid] = []

            # 根据父类别ID插入列表字典
            parent_classify_dict[pid].append(item)

        print("> ThreadClassifyTreeServices classify_tree:", classify_tree)
        print("> ThreadClassifyTreeServices parent_classify_dict:", parent_classify_dict)

        # 递归树
        def recur_tree(tree_node, parent_dict=None):
            """
            递归树
            @param tree_node 树的每个节点
            @param parent_dict 以每个节点的父ID作为键名的字典
            """
            pid_str = str(tree_node['id'])
            tree_node['children'] = parent_dict.get(pid_str, [])
            for child in tree_node['children']:
                recur_tree(child, parent_dict)
            return tree_node

        if classify_tree:
            classify_tree = recur_tree(tree_node=classify_tree, parent_dict=parent_classify_dict)

        if not parent_classify_dict:
            return [], None

        return classify_tree, None

    @staticmethod
    def get_classify_all_tree(classify_value=None, classify_id=None):
        pass
