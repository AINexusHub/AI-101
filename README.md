# AI-101

AI编程学习与实践项目

## 项目描述

这是一个专注于AI编程学习和实践的Python项目，使用PDM进行现代Python包管理。项目旨在展示AI开发的最佳实践，包括机器学习、数据处理和AI算法实现。

## 项目结构

```
AI-101/
├── README.md           # 项目索引文档 (当前文件)
├── ai_101/            # AI应用代码目录
│   ├── function_call.ipynb
│   ├── multi_round_chat.ipynb
│   ├── rag.ipynb
│   └── tools/
├── knowledge_prepare/  # 知识准备文档
│   ├── kubernetes.md  # Kubernetes知识库
│   ├── readme.md      # SaaS平台知识储备
│   └── language_learning.md
|   └── .....
└── tests/             # 测试目录
```

## 文档索引

### 核心文档
- **[Kubernetes知识库](knowledge_prepare/kubernetes.md)** - 完整的Kubernetes部署、运维和最佳实践指南
- **[SaaS平台知识储备](knowledge_prepare/readme.md)** - SaaS平台架构、多租户设计和运维知识
- **[语言学习指南](knowledge_prepare/language_learning.md)** - 编程语言学习资源

### AI应用示例
- **[函数调用示例](ai_101/function_call.ipynb)** - AI函数调用实践
- **[多轮对话示例](ai_101/multi_round_chat.ipynb)** - 多轮对话AI应用
- **[RAG应用示例](ai_101/rag.ipynb)** - 检索增强生成应用

## 功能特性

- 使用PDM进行AI项目依赖管理
- AI 应用开发
- 支持测试驱动的AI开发
- 云原生和Kubernetes部署知识

## 安装

1. 确保已安装PDM：
   ```bash
   pdm --version
   ```

   如果没有安装，请参考 [这个文档](https://pdm-project.org/en/latest/#installation)

2. 克隆项目并安装依赖：
   ```bash
   git clone git@github.com:AINexusHub/AI-101.git
   cd AI-101
   pdm install
   ```

3. 设置.env 文件
```
DEEPSEEK_API_KEY=sk-xx
```

## 许可证

MIT License
