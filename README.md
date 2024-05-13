# csv2dat-for-xcpc
这是一个简单的python脚本，可以用于将csv格式的榜单转换为codeforces的contest添加ghost所要求的DAT格式。这份代码之前被应用于从pintia导出榜单至codeforces.

## 前置要求
有一个csv表格，每行一个队伍，内容分别是：编号，队名，学校，A题结果，B题结果，C题结果...

如果您正在使用pintia平台，你可以将成绩单和参赛队伍信息两个表格按某种方式（如以第一队员为主键）拼接，并按格式删去不必要数据项并调整顺序。

请注意，编号应当是唯一的，如果导出的排名存在同排名的情况，请重新标号。

## 使用方法

在程序内配置程序的参数后运行即可。

参考文档：

[About Codeforces and Polygon functionality,ATSTNG,2024.5.12](https://codeforces.com/blog/entry/124035)

修改日志：

2024.5.13：修正罚时的处理逻辑，将贡献的WA提交改为尽可能晚的提交，并增加提示。

2024.5.12：第一个版本完成