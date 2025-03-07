
---

title: ubuntu下使用cron执行定时任务更新代码
date: 2019-07-31 08:44:03
tags: [cron, ]

---

尽管在特定时间运行命令非常有用(`at`命令可以实现)，但是在重复的时间间隔内自动运行程序也非常重要。您必须使用crontab来安排此类重复性作业，例如，如果您希望在每晚的午夜将文件备份到云端。

<!-- more -->

尽管在特定时间运行命令非常有用(`at`命令可以实现)，但是在重复的时间间隔内自动运行程序也非常重要。您必须使用crontab来安排此类重复性作业，例如，如果您希望在每晚的午夜将文件备份到云端。

您可以通过将任务信息放在具有特定格式的文件中并使用crontab命令提交此文件来定时执行该任务。 cron守护程序 -  crond  - 每分钟检查任务信息并在指定时间执行任务。

来自cron任务的任何输出都将邮寄给提交任务的用户。 （在提交的任务信息文件中，您可以为邮寄的输出指定不同的收件人。）

### 谁可以使用cron来制定任务

两个配置文件控制谁可以使用crontab在Linux中调度cron作业：

- /etc/cron.allow包含允许使用crontab命令提交任务的用户的名称。
- /etc/cron.deny包含不允许使用crontab命令提交任务的用户的名称。

### cron添加任务

使用`crontab -e`命令就能打开一个文本编辑器, 你可以在该文本的最后追加一样类似这样的配置:

`5 0 * * * $HOME/myjob`, 以空格为间隔, 每个字段的意义如下:

- 第一位: 分钟
- 第二位: 小时
- 第三位: 日
- 第四位: 月
- 第五位: 星期几
- 后面所有是你要定时执行的任务


上面的命令指的是, 在每天12:05执行myjob文件里的命令。


注意, 编辑完成文件以后, 使用`:wq`命令来保存和退出!

### 注意执行的命令文件必须具有可执行权限

使用这个命令, 使得你的文件具有可执行的权限, 否则你添加的定时任务时不能执行的。
```bash
chmod +x $HOME/myjob
```

### cron查看定时任务

- 查看root用户的所有任务

```
crontab -l
```

- 查看某个用户`testuser`的所有定时任务:

```
crontab -u testuser -l
```

- 查看daily(每日一次)任务logrotate

```
less /etc/cron.daily/logrotate
```

- 同样道理可以查看每小时一次的任务

```
ls -la /etc/cron.hourly/
```

同样还有`ron.weekly`, `cron.monthly`等, 请自行实验!



### cron即时调试

之前我给服务器添加了一个定时任务, 但是很长时间以后才发现, 任务总是执行失败的, 因为我没有调试这个任务。 
所以我建议大家在修改了cron任务的时候, 可以执行这个命令, 即时立刻执行任务:


```bash
run-parts /etc/cron.daily
```

从字面就能理解, 他可以执行daily的任务, 也就是每日一次的任务, 除了daily, 还有hourly/weekly等, 具体你自己去`ls /etc | grep cron`查看。




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](ubuntu下使用cron执行定时任务更新代码.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
