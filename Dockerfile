# 使用 Python 3.9 作为基础镜像
FROM python:3.9-alpine3.18

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . /app/

# 安装依赖
RUN apk update && apk add sshpass && pip install --no-cache-dir -r requirements.txt
    
# 定义环境变量

ENV TELEGRAM_BOT_API_KEY=""
ENV USER_ID=""
# 执行 Python 脚本
CMD ["sh", "-c", "python main.py ${TELEGRAM_BOT_API_KEY} ${USER_ID}"]
