# Docker 知识库

## Docker 核心概念

### 基础概念
- **容器 (Container)**: 轻量级、可执行的软件包，包含运行应用所需的一切
- **镜像 (Image)**: 容器的模板，包含应用代码、运行时、库、环境变量和配置文件
- **Dockerfile**: 构建镜像的文本文件，包含构建指令
- **Docker Hub**: 公共镜像仓库
- **Docker Registry**: 镜像存储和分发服务
- **Docker Compose**: 多容器应用定义和运行工具

### 容器生命周期
- **创建 (Create)**: 从镜像创建容器
- **启动 (Start)**: 启动已创建的容器
- **运行 (Run)**: 创建并启动容器
- **停止 (Stop)**: 停止运行中的容器
- **重启 (Restart)**: 重启容器
- **暂停 (Pause)**: 暂停容器进程
- **恢复 (Unpause)**: 恢复暂停的容器
- **删除 (Remove)**: 删除容器

## Docker 基本操作

### 镜像管理
```bash
# 拉取镜像
docker pull ubuntu:20.04

# 查看本地镜像
docker images

# 构建镜像
docker build -t myapp:latest .

# 删除镜像
docker rmi myapp:latest

# 推送镜像到仓库
docker push myregistry/myapp:latest
```

### 容器操作
```bash
# 运行容器
docker run -d --name mycontainer nginx:latest

# 运行交互式容器
docker run -it ubuntu:20.04 /bin/bash

# 查看运行中的容器
docker ps

# 查看所有容器
docker ps -a

# 停止容器
docker stop mycontainer

# 启动已停止的容器
docker start mycontainer

# 重启容器
docker restart mycontainer

# 删除容器
docker rm mycontainer

# 强制删除运行中的容器
docker rm -f mycontainer
```

### 容器网络
```bash
# 查看网络
docker network ls

# 创建网络
docker network create mynetwork

# 连接容器到网络
docker network connect mynetwork mycontainer

# 断开网络连接
docker network disconnect mynetwork mycontainer
```

### 数据管理
```bash
# 创建数据卷
docker volume create myvolume

# 查看数据卷
docker volume ls

# 使用数据卷
docker run -v myvolume:/data ubuntu:20.04

# 绑定挂载主机目录
docker run -v /host/path:/container/path ubuntu:20.04
```

## Dockerfile 编写

### 基础指令
```dockerfile
# 基础镜像
FROM ubuntu:20.04

# 维护者信息
LABEL maintainer="your-email@example.com"

# 设置工作目录
WORKDIR /app

# 复制文件
COPY . .

# 安装依赖
RUN apt-get update && apt-get install -y python3

# 暴露端口
EXPOSE 8080

# 环境变量
ENV NODE_ENV=production

# 启动命令
CMD ["python3", "app.py"]
```

### 最佳实践
- 使用多阶段构建减少镜像大小
- 合理使用 `.dockerignore` 文件
- 按依赖频率排序指令
- 使用非root用户运行应用
- 最小化镜像层数

## Docker Compose

### 基本配置
```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - frontend

  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
    networks:
      - frontend
      - backend

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - backend

volumes:
  db_data:

networks:
  frontend:
  backend:
```

### Compose 操作
```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看服务状态
docker-compose ps

# 查看服务日志
docker-compose logs

# 构建服务镜像
docker-compose build

# 执行命令
docker-compose exec web bash
```

## 容器编排

### Docker Swarm
```bash
# 初始化Swarm集群
docker swarm init

# 加入节点
docker swarm join --token <token> <manager-ip>:2377

# 部署服务
docker service create --name web nginx:latest

# 扩展服务
docker service scale web=3

# 更新服务
docker service update --image nginx:1.21 web
```

### 服务发现和负载均衡
- **内置负载均衡**: Docker Swarm模式自动提供
- **服务发现**: 通过服务名进行DNS解析
- **健康检查**: 容器健康状态监控

## 监控和日志

### 容器监控
```bash
# 查看容器资源使用
docker stats

# 查看容器详细信息
docker inspect mycontainer

# 查看容器进程
docker top mycontainer
```

### 日志管理
```bash
# 查看容器日志
docker logs mycontainer

# 实时查看日志
docker logs -f mycontainer

# 查看指定时间范围的日志
docker logs --since 1h mycontainer

# 导出日志到文件
docker logs mycontainer > container.log
```

## 安全最佳实践

### 镜像安全
- 使用官方基础镜像
- 定期更新镜像和依赖
- 扫描镜像漏洞
- 最小化镜像大小

### 容器安全
- 使用非root用户运行
- 限制容器权限
- 配置安全策略
- 网络隔离

### 运行时安全
- 限制资源使用
- 配置安全上下文
- 监控异常行为
- 定期安全审计

## 故障排除

### 常见问题
- 容器启动失败
- 网络连接问题
- 存储卷挂载失败
- 资源不足

### 调试工具
```bash
# 进入容器调试
docker exec -it mycontainer bash

# 查看容器事件
docker events

# 检查容器配置
docker inspect mycontainer

# 端口映射检查
docker port mycontainer

# 网络连接测试
docker exec mycontainer ping othercontainer
```

### 性能优化
- 合理配置资源限制
- 优化镜像构建
- 使用缓存策略
- 监控资源使用

## 工具和资源

### Docker 工具
- **Docker Desktop**: 桌面版Docker环境
- **Docker CLI**: 命令行工具
- **Docker Compose**: 多容器编排
- **Docker Swarm**: 原生集群管理

### 第三方工具
- **Portainer**: Docker图形化管理界面
- **Watchtower**: 自动更新容器
- **Trivy**: 镜像安全扫描
- **Dive**: 镜像分析工具

### 学习资源
- **官方文档**: https://docs.docker.com/
- **Docker Hub**: https://hub.docker.com/
- **Docker Samples**: 官方示例项目
- **Docker Community**: 社区论坛和博客

## 最佳实践

### 开发最佳实践
- 使用多阶段构建
- 合理使用缓存
- 环境变量配置
- 健康检查配置

### 生产最佳实践
- 使用编排工具
- 配置监控告警
- 备份和恢复策略
- 安全扫描和审计

### 性能最佳实践
- 优化镜像大小
- 合理资源限制
- 网络优化
- 存储优化

这个文档为Docker的使用提供了全面的知识储备，涵盖了从基础概念到生产部署的各个方面。
