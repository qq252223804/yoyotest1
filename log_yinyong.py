#cording:utf-8
from common.logger import Log

# a=Log()
# print(a.getlog())

# Log().debug("一个debug信息")
# # Log().info('这是一个info日志信息')
#
# Log().warning("一个warning222222信息")


try:
    1 / 0
except:
    # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息
    Log().debug('this is an exception message')
