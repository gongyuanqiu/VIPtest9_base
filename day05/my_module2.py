# 异常
# try:
#     print(1/0)
# except:
#     print("有错误")
# #捕获异常描述信息
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError) as s:
#     print(s)
# # 捕获所有异常
# try:
#     print(1/0)
# except Exception as a:
#     print(a)

#异常的else
try:
    print(1/1)
except Exception as a:
    print(a)
else:
    print("没有异常执行")

#异常的finally