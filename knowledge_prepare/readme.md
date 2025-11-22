# SaaS平台知识储备

## 基础设施相关

- [Docker知识库](./docker.md)
- [Kubernetes知识库](./kubernetes.md)
- [MySQL知识库](./mysql.md)
- [PostgreSQL知识库](./postgres.md)
- [Redis知识库](./redis.md)

## SaaS平台架构

### 多租户架构
- **数据库级别**: 共享数据库、共享模式、独立数据库
- **应用级别**: 租户标识、数据隔离、资源隔离
- **计费模型**: 按使用量、按功能、混合计费

### 微服务架构
- **服务拆分原则**: 单一职责、松耦合
- **API网关**: Kong, Ambassador, Traefik
- **服务发现**: Consul, Eureka
- **配置中心**: Apollo, Nacos

### 数据管理
- **数据分片策略**: 基于租户ID、基于地理位置
- **缓存策略**: Redis集群、多级缓存
- **消息队列**: Kafka, RabbitMQ, NATS
- **数据备份与恢复**: 跨区域备份、时间点恢复

### 安全架构
- **身份认证**: OAuth2, JWT, OpenID Connect
- **权限管理**: RBAC, ABAC
- **网络安全**: 网络策略、服务网格安全
- **数据加密**: 传输加密、静态加密

## 运维与监控

### 可观测性
- **指标 (Metrics)**: 应用性能、业务指标
- **日志 (Logs)**: 结构化日志、日志聚合
- **追踪 (Traces)**: 分布式追踪、调用链分析

### 高可用性
- **多区域部署**: 跨可用区、跨地域
- **故障转移**: 自动故障检测和恢复
- **负载均衡**: 服务级别、全局负载均衡

### 成本优化
- **资源利用率监控**: 自动扩缩容策略
- **预留实例**: 长期资源预留
- **Spot实例**: 成本敏感型工作负载

## 语言算法类
- [language_learning.md](./language_learning.md)
- [数据结构和算法知识库](./data_structures_algorithms.md)
- [设计模式知识库](./design_patterns.md)
