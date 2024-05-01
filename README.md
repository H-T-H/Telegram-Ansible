# Telegram-ansible
在Telegram控制ansible

**烂尾中，以后可能再写**

# 前言
你是否遭遇过，有个自动化的任务没有执行，但是你手边没有电脑？

反正我遭遇了，这个机器人是给我自己写的。

只需将hosts.ini和playbook.yaml导入至机器人，即可在任意Telegram客户端上运行ansible的自动化任务。




# 如何安装

## (1)使用 Docker 部署
### 自行构建
1. 在[BotFather](https://t.me/BotFather)获取Telegram Bot API
2. 在[Getmyid_bot](https://t.me/getmyid_bot)获取Telegram user id
3. 克隆项目
```
git clone https://github.com/H-T-H/Telegram-Ansible.git
```
4. 进入项目目录
```
cd Telegram-Ansible
```
5. 构建镜像
```
docker build -t telegram_ansible_bot .
```
6. 运行镜像
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram 机器人 API} -e USER_ID={Telegram 账号的USER ID} telegram_ansible_bot
```





# 使用方法
1. **/show_playbook**， 会返回playbook.yaml文件内容
2. **/edit_playbook**， 编辑playbook.yaml文件内容
3. **/show_hosts**，    会返回hosts.ini文件内容
4. **/edit_playbook**， 编辑hosts.ini文件内容
5. **/just_shell**，    还没写好，暂时没用
6. **/run**，           运行playbook
7. **/cancel**，        取消当前事件，比如取消编辑文件


# 临时要用，写的比较粗糙，以下是TODO list
1. 用户验证
2. 多playbook
3. 密钥登录
4. just_shell命令，用于对一个主机组运行一行shell命令
