# 语言学习资源

## Java

### 基础语法
- **官方教程**: https://docs.oracle.com/javase/tutorial/
- **在线学习**: https://www.runoob.com/java/java-tutorial.html
- **Java 8+ 新特性**: Lambda表达式、Stream API、Optional

### Spring Boot 框架
- **官方文档**: https://spring.io/projects/spring-boot
- **核心模块**:
  - Spring Data JPA: 数据持久化
  - Spring Integration: 企业集成模式
  - Spring REST Docs: API文档生成
  - Spring Security: 安全框架
  - Spring Cloud: 微服务架构

### 第三方库
- **Maven仓库**: https://mvnrepository.com/
- **常用库**:
  - Lombok: 代码简化
  - MapStruct: 对象映射
  - Jackson: JSON处理
  - Logback: 日志框架

### 微服务相关
- **Spring Cloud**: 服务发现、配置中心、网关
- **分布式事务**: Seata
- **链路追踪**: Sleuth + Zipkin

## Go

### 基础语法
- **官方文档**: https://go.dev/
- **在线教程**: https://tour.golang.org/
- **并发编程**: Goroutine, Channel

### 数据库框架
- **GORM**: https://gorm.io/index.html
- **SQL驱动**: database/sql
- **ORM选择**: GORM, XORM, Ent

### Web 框架
- **Gin**: https://gin-gonic.com/
- **Echo**: 高性能Web框架
- **Fiber**: Express风格的Go框架

### 第三方库
- **包管理**: Go Modules
- **依赖查找**: https://pkg.go.dev/
- **常用库**:
  - Viper: 配置管理
  - Zap: 高性能日志
  - Testify: 测试框架

### 微服务相关
- **gRPC**: 高性能RPC框架
- **Protocol Buffers**: 序列化协议
- **服务发现**: Consul, etcd

## Node.js

### Web 框架
- **Express**: https://expressjs.com/
- **NestJS**: 企业级框架
- **Fastify**: 高性能框架

### 基础语法
- **官方文档**: https://nodejs.org/en/docs/
- **在线教程**: https://www.runoob.com/nodejs/nodejs-tutorial.html
- **ES6+ 特性**: Promise, async/await, 模块系统

### 数据库框架
- **TypeORM**: https://typeorm.io/docs/getting-started
- **Prisma**: 现代ORM
- **Sequelize**: 传统ORM

### 第三方库
- **NPM仓库**: https://www.npmjs.com/
- **常用库**:
  - Axios: HTTP客户端
  - Winston: 日志框架
  - Joi: 数据验证
  - Socket.io: WebSocket

### 微服务相关
- **NestJS微服务**: 内置微服务支持
- **消息队列**: Bull, Agenda
- **API网关**: Express Gateway

## Python

### 基础语法
- **官方文档**: https://docs.python.org/3/
- **在线教程**: https://docs.python.org/3/tutorial/
- **Python 3.8+ 新特性**: 类型提示、异步编程

### Web 框架
- **Flask**: https://flask.palletsprojects.com/en/stable/quickstart/
- **FastAPI**: 现代高性能API框架
- **Django**: 全功能Web框架

### 数据库
- **SQLAlchemy**: https://docs.sqlalchemy.org/en/20/orm/quickstart.html
- **Django ORM**: Django内置ORM
- **异步ORM**: Tortoise-ORM, SQLModel

### 第三方库
- **PyPI**: https://pypi.org/
- **常用库**:
  - Requests: HTTP客户端
  - Pydantic: 数据验证
  - Celery: 分布式任务队列
  - Pandas: 数据分析

### 微服务相关
- **FastAPI微服务**: 异步微服务框架
- **消息队列**: Celery + Redis/RabbitMQ
- **API文档**: OpenAPI/Swagger

## 云原生语言特性

### 容器化支持
- **多阶段构建**: 所有语言都支持
- **最小化镜像**: Alpine Linux基础镜像
- **健康检查**: 应用健康检查端点

### 配置管理
- **环境变量**: 12-factor应用原则
- **配置中心**: 支持动态配置更新
- **密钥管理**: 安全的密钥存储

### 监控和日志
- **结构化日志**: JSON格式日志输出
- **指标暴露**: Prometheus指标端点
- **健康检查**: 就绪性和存活性检查

