"""
1.登录 -> 得到cookie
2.携带cookie 请求我的书架上的url
3.将1，2操作衔接
4.使用session进行请求
"""
import requests

# 会话 服务端与客户端之间的互相交流
session = requests.session()