# Redis 知识库

## Redis 核心概念

### 基础概念
- **Redis (Remote Dictionary Server)**: 开源的内存数据结构存储，用作数据库、缓存和消息代理
- **键值存储 (Key-Value Store)**: 数据以键值对形式存储
- **内存存储**: 数据主要存储在内存中，提供极高的读写性能
- **持久化**: 支持RDB快照和AOF日志两种持久化方式
- **数据结构**: 支持字符串、列表、集合、有序集合、哈希、位图等多种数据结构

### 数据类型
- **String (字符串)**: 最基本的数据类型，可以包含任何数据
- **List (列表)**: 字符串列表，按插入顺序排序
- **Set (集合)**: 无序的字符串集合，不允许重复
- **Sorted Set (有序集合)**: 带分数的字符串集合，按分数排序
- **Hash (哈希)**: 字段-值对的集合
- **Bitmaps (位图)**: 通过位操作存储布尔信息
- **HyperLogLog**: 用于基数统计的概率数据结构
- **Streams (流)**: 用于消息传递的日志数据结构

### 架构特性
- **单线程模型**: 命令执行是单线程的，避免并发问题
- **事件驱动**: 基于事件循环处理网络请求
- **复制**: 主从复制支持数据冗余
- **哨兵模式**: 自动故障转移和高可用性
- **集群模式**: 数据分片和水平扩展

## Redis 基本操作

### 连接和配置
```bash
# 启动Redis服务器
redis-server

# 启动Redis服务器并指定配置文件
redis-server /path/to/redis.conf

# 连接Redis客户端
redis-cli

# 连接远程Redis
redis-cli -h host -p port -a password

# 测试连接
ping

# 选择数据库 (0-15)
select 1

# 查看配置信息
config get *

# 设置配置
config set timeout 300
```

### 键操作
```bash
# 设置键值
set mykey "Hello Redis"

# 获取键值
get mykey

# 检查键是否存在
exists mykey

# 删除键
del mykey

# 设置过期时间
expire mykey 60
setex mykey 60 "value"

# 查看剩余生存时间
ttl mykey

# 移除过期时间
persist mykey

# 重命名键
rename mykey newkey

# 查找键
keys user:*

# 随机返回一个键
randomkey

# 移动键到其他数据库
move mykey 1
```

### 字符串操作
```bash
# 设置字符串
set username "john_doe"
set counter 100

# 获取字符串
get username

# 设置多个值
mset key1 "value1" key2 "value2"

# 获取多个值
mget key1 key2

# 字符串追加
append username "_extra"

# 获取字符串长度
strlen username

# 自增操作
incr counter
incrby counter 5

# 自减操作
decr counter
decrby counter 3

# 设置新值并返回旧值
getset counter 200

# 位操作
setbit mybit 7 1
getbit mybit 7
bitcount mykey
```

### 列表操作
```bash
# 从左侧插入
lpush mylist "item1"
lpush mylist "item2" "item3"

# 从右侧插入
rpush mylist "item4"

# 从左侧弹出
lpop mylist

# 从右侧弹出
rpop mylist

# 获取列表长度
llen mylist

# 获取列表元素
lrange mylist 0 -1
lindex mylist 1

# 设置指定位置元素
lset mylist 0 "new_item"

# 修剪列表
ltrim mylist 0 2

# 阻塞弹出
blpop mylist 10
brpop mylist 10
```

### 集合操作
```bash
# 添加元素
sadd myset "member1"
sadd myset "member2" "member3"

# 获取所有元素
smembers myset

# 检查元素是否存在
sismember myset "member1"

# 移除元素
srem myset "member1"

# 获取集合大小
scard myset

# 随机获取元素
srandmember myset
spop myset

# 集合运算
sadd set1 "a" "b" "c"
sadd set2 "b" "c" "d"

# 交集
sinter set1 set2

# 并集
sunion set1 set2

# 差集
sdiff set1 set2
```

### 有序集合操作
```bash
# 添加元素
zadd leaderboard 100 "player1"
zadd leaderboard 200 "player2" 150 "player3"

# 获取元素分数
zscore leaderboard "player1"

# 获取排名
zrank leaderboard "player1"
zrevrank leaderboard "player1"

# 获取范围内的元素
zrange leaderboard 0 -1 withscores
zrevrange leaderboard 0 -1 withscores

# 按分数范围获取
zrangebyscore leaderboard 100 200 withscores
zrevrangebyscore leaderboard 200 100 withscores

# 增加分数
zincrby leaderboard 50 "player1"

# 获取集合大小
zcard leaderboard

# 统计分数范围内的元素数量
zcount leaderboard 100 200

# 移除元素
zrem leaderboard "player1"
```

### 哈希操作
```bash
# 设置字段值
hset user:1000 name "John Doe"
hset user:1000 email "john@example.com" age 30

# 获取字段值
hget user:1000 name

# 获取所有字段值
hgetall user:1000

# 获取所有字段
hkeys user:1000

# 获取所有值
hvals user:1000

# 检查字段是否存在
hexists user:1000 name

# 删除字段
hdel user:1000 age

# 获取字段数量
hlen user:1000

# 增加数值字段
hincrby user:1000 age 1

# 设置多个字段
hmset user:1001 name "Jane" email "jane@example.com"

# 获取多个字段
hmget user:1001 name email
```

### 发布订阅
```bash
# 订阅频道
subscribe news sports

# 发布消息
publish news "Breaking news!"

# 模式订阅
psubscribe news.*

# 取消订阅
unsubscribe news
punsubscribe news.*
```

## 高级功能

### 事务操作
```bash
# 开始事务
multi

# 添加命令到事务队列
set key1 "value1"
set key2 "value2"
incr counter

# 执行事务
exec

# 取消事务
discard

# 监视键（乐观锁）
watch key1
multi
set key1 "new_value"
exec
```

### Lua脚本
```bash
# 执行Lua脚本
eval "return redis.call('set', KEYS[1], ARGV[1])" 1 mykey "myvalue"

# 加载脚本
script load "return redis.call('get', KEYS[1])"

# 执行已加载的脚本
evalsha sha1_hash 1 mykey

# 检查脚本是否存在
script exists sha1_hash

# 删除所有脚本
script flush
```

### 流水线操作
```bash
# 使用管道批量执行命令
(echo -en "PING\r\nSET key1 value1\r\nGET key1\r\n"; sleep 1) | nc localhost 6379

# 在编程语言中使用管道
# Python示例
import redis
r = redis.Redis()
pipe = r.pipeline()
pipe.set('key1', 'value1')
pipe.get('key1')
result = pipe.execute()
```

## 持久化配置

### RDB持久化
```bash
# 手动保存
save
bgsave

# 配置自动保存
# 在redis.conf中配置
save 900 1      # 900秒内至少有1个键被修改
save 300 10     # 300秒内至少有10个键被修改
save 60 10000   # 60秒内至少有10000个键被修改
```

### AOF持久化
```bash
# 启用AOF
appendonly yes

# AOF同步策略
appendfsync always    # 每次写操作都同步
appendfsync everysec  # 每秒同步一次（推荐）
appendfsync no        # 由操作系统决定

# AOF重写
bgrewriteaof
```

## 复制和高可用

### 主从复制
```bash
# 在从节点配置
slaveof 127.0.0.1 6379

# 查看复制信息
info replication

# 断开复制
slaveof no one
```

### 哨兵模式
```bash
# 启动哨兵
redis-sentinel /path/to/sentinel.conf

# 哨兵配置示例
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1
```

### 集群模式
```bash
# 创建集群
redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 \
127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 \
--cluster-replicas 1

# 集群操作
redis-cli -c -p 7000
cluster info
cluster nodes

# 添加节点
redis-cli --cluster add-node 127.0.0.1:7006 127.0.0.1:7000

# 重新分片
redis-cli --cluster reshard 127.0.0.1:7000
```

## 性能优化

### 内存优化
```bash
# 查看内存使用
info memory

# 内存碎片率
mem_fragmentation_ratio

# 设置最大内存
maxmemory 1gb

# 内存淘汰策略
maxmemory-policy allkeys-lru    # 所有键LRU
maxmemory-policy volatile-lru   # 过期键LRU
maxmemory-policy allkeys-random # 所有键随机
maxmemory-policy volatile-ttl   # 过期时间最短的键
```

### 连接优化
```bash
# 查看连接信息
info clients
client list

# 设置最大连接数
maxclients 10000

# 连接超时
timeout 300

# 限制客户端输出缓冲区
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
```

## 监控和诊断

### 信息统计
```bash
# 查看所有信息
info

# 查看服务器信息
info server

# 查看客户端信息
info clients

# 查看内存信息
info memory

# 查看持久化信息
info persistence

# 查看统计信息
info stats

# 查看复制信息
info replication

# 查看CPU信息
info cpu

# 查看集群信息
info cluster

# 查看键空间信息
info keyspace
```

### 慢查询日志
```bash
# 查看慢查询配置
config get slowlog-*

# 设置慢查询阈值（微秒）
config set slowlog-log-slower-than 10000

# 设置慢查询日志最大长度
config set slowlog-max-len 128

# 查看慢查询日志
slowlog get
slowlog get 10
slowlog len
slowlog reset
```

### 性能测试
```bash
# 基准测试
redis-benchmark -h 127.0.0.1 -p 6379 -c 50 -n 100000

# 测试特定命令
redis-benchmark -t set,get -n 100000 -q

# 测试流水线
redis-benchmark -t set,get -n 100000 -q -P 16
```

## 安全配置

### 认证和访问控制
```bash
# 设置密码
config set requirepass "your_password"

# 客户端认证
auth your_password

# 重命名危险命令
rename-command FLUSHALL ""
rename-command CONFIG ""

# 绑定IP地址
bind 127.0.0.1

# 保护模式
protected-mode yes
```

### 网络安全
```bash
# SSL/TLS配置
tls-port 6379
tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-ca-cert-file /path/to/ca.crt

# 防火墙规则
# 只允许特定IP访问Redis端口
```

## 数据备份和恢复

### 备份策略
```bash
# RDB备份
# 自动根据配置生成快照
# 手动生成快照
bgsave

# AOF备份
# 自动记录所有写操作

# 复制备份
# 使用从节点作为热备份
```

### 恢复操作
```bash
# 从RDB文件恢复
# 将RDB文件放在工作目录，重启Redis

# 从AOF文件恢复
# 启用AOF，Redis启动时会重放AOF日志

# 数据迁移
redis-cli --rdb /path/to/dump.rdb
```

## 常用场景

### 缓存场景
```bash
# 设置缓存
set user:1000:profile "{\"name\":\"John\",\"age\":30}" ex 3600

# 缓存击穿保护
setnx lock:user:1000 1
expire lock:user:1000 5

# 缓存预热
# 启动时加载热点数据到Redis
```

### 会话存储
```bash
# 存储会话
set session:abc123 "{\"user_id\":1000,\"last_active\":\"2023-01-01\"}" ex 1800

# 更新会话
expire session:abc123 1800

# 删除会话
del session:abc123
```

### 消息队列
```bash
# 简单队列
lpush task:queue "task1"
rpop task:queue

# 延迟队列
zadd delayed:queue 1640995200 "delayed_task"
zrangebyscore delayed:queue 0 1640995200

# 发布订阅
publish notifications "New message"
subscribe notifications
```

### 计数器
```bash
# 页面浏览量
incr page:views:homepage

# 用户行为统计
hincrby user:1000:stats page_views 1
hincrby user:1000:stats clicks 1

# 限流器
incr rate_limit:user:1000
expire rate_limit:user:1000 60
```

### 排行榜
```bash
# 游戏分数排行榜
zadd leaderboard 1000 "player1"
zadd leaderboard 1500 "player2"
zrevrange leaderboard 0 9 withscores

# 实时排名
zrank leaderboard "player1"
zrevrank leaderboard "player1"
```

## 工具和资源

### Redis 工具
- **redis-cli**: 命令行客户端
- **redis-benchmark**: 性能测试工具
- **redis-check-aof**: AOF文件检查工具
- **redis-check-rdb**: RDB文件检查工具
- **redis-sentinel**: 哨兵模式
- **redis-server**: 服务器

### 第三方工具
- **RedisInsight**: 官方图形化管理工具
- **Redis Desktop Manager**: 桌面管理工具
- **Redisson**: Java客户端，提供分布式对象和服务
- **Redis-py**: Python客户端
- **Lettuce**: Java异步客户端

### 监控工具
- **Redis Exporter**: Prometheus指标导出器
- **Redis-stat**: 实时监控工具
- **Redis Live**: Web监控界面

### 学习资源
- **官方文档**: https://redis.io/documentation
- **Redis命令参考**: https://redis.io/commands
- **Redis大学**: 官方培训课程
- **Redis Labs博客**: 最佳实践和案例研究

## 最佳实践

### 开发最佳实践
- 合理选择数据结构
- 使用管道批量操作
- 避免大键和大值
- 设置合理的过期时间
- 使用连接池

### 运维最佳实践
- 监控内存使用和碎片率
- 配置合理的持久化策略
- 设置内存淘汰策略
- 定期备份数据
- 使用哨兵或集群保证高可用

### 安全最佳实践
- 启用认证
- 绑定特定IP
- 重命名危险命令
- 使用SSL/TLS加密
- 定期安全审计

### 性能最佳实践
- 优化数据结构选择
- 使用适当的数据编码
- 避免阻塞操作
- 合理配置内存
- 监控慢查询

这个文档为Redis的使用提供了全面的知识
