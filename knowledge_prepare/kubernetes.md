# Kubernetes 知识库

## Kubernetes (K8s) 核心知识

### 基础概念
- **Pod**: 最小部署单元，包含一个或多个容器
- **Deployment**: 管理Pod的副本和更新策略
- **Service**: 提供稳定的网络访问端点
- **ConfigMap & Secret**: 配置管理和敏感信息存储
- **Namespace**: 资源隔离和逻辑分区
- **StatefulSet**: 有状态应用
- **Ingress**: 外部访问入口管理

### 部署策略
- **滚动更新 (Rolling Update)**: 零停机部署
- **蓝绿部署 (Blue-Green)**: 快速回滚
- **金丝雀发布 (Canary)**: 渐进式发布
- **A/B测试**: 功能验证

### 资源管理
- **Resource Quotas**: 资源配额限制
- **Limit Ranges**: 资源限制范围
- **Horizontal Pod Autoscaler (HPA)**: 自动扩缩容
- **Vertical Pod Autoscaler (VPA)**: 垂直资源调整

## 容器化技术
- **Docker**: 容器运行时
- **容器镜像管理**: 私有仓库、镜像安全扫描
- **多阶段构建**: 优化镜像大小
- **容器安全**: 最小权限原则

## 网络与存储
- **CNI插件**: Calico
- **服务网格**: Istio
- **持久化存储**: PV, PVC, StorageClass

## 监控与日志
- **监控方案**: Prometheus + Grafana
- **日志收集**: EFK/ELK Stack (Elasticsearch, Fluentd, Kibana)
- **告警管理**: Alertmanager

## CI/CD 流水线
- **GitOps**: ArgoCD, FluxCD
- **流水线工具**: Jenkins, GitLab CI, GitHub Actions
- **镜像构建**: Kaniko, BuildKit
- **安全扫描**: Trivy, Clair

## 工具和资源

### Kubernetes 工具
- **kubectl**: Kubernetes命令行工具
- **k9s**: 终端UI管理工具
- **Helm**: 包管理工具

### 学习资源
- **官方文档**: https://kubernetes.io/docs/

## 最佳实践

### 部署最佳实践
- 使用声明式配置
- 实施GitOps工作流
- 自动化测试和验证
- 渐进式发布策略

### 安全最佳实践
- 最小权限原则
- 定期安全扫描
- 网络策略隔离
- 密钥管理

### 性能优化
- 资源请求和限制设置
- 合理的副本数配置
- 缓存策略优化
- 数据库连接池管理

## 故障排除

### 常见问题
- Pod启动失败
- 服务无法访问
- 资源不足
- 网络连接问题

### 调试工具
- `kubectl describe`
- `kubectl logs`
- `kubectl exec`
- `kubectl port-forward`

这个文档为基于Kubernetes的部署提供了全面的知识储备，涵盖了从基础设施到应用架构的各个方面。
