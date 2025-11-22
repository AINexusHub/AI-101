# MySQL 知识库

## MySQL 核心概念

### 数据库基础概念
- **数据库 (Database)**: 数据的有组织集合
- **表 (Table)**: 数据的二维结构，由行和列组成
- **行 (Row/Record)**: 表中的一条记录
- **列 (Column/Field)**: 表中的字段，定义数据类型
- **主键 (Primary Key)**: 唯一标识表中每行的字段
- **外键 (Foreign Key)**: 建立表间关系的字段
- **索引 (Index)**: 提高查询性能的数据结构

### 数据类型
- **数值类型**: INT, DECIMAL, FLOAT, DOUBLE
- **字符串类型**: CHAR, VARCHAR, TEXT, BLOB
- **日期时间类型**: DATE, TIME, DATETIME, TIMESTAMP
- **JSON类型**: JSON文档存储

### 存储引擎
- **InnoDB**: 支持事务、行级锁、外键约束（默认）
- **MyISAM**: 不支持事务，表级锁，查询性能好
- **MEMORY**: 内存表，数据存储在内存中
- **ARCHIVE**: 归档存储，压缩率高

## MySQL 基本操作

### 数据库操作
```sql
-- 创建数据库
CREATE DATABASE mydb;

-- 选择数据库
USE mydb;

-- 查看所有数据库
SHOW DATABASES;

-- 删除数据库
DROP DATABASE mydb;

-- 查看数据库字符集
SHOW CREATE DATABASE mydb;
```

### 表操作
```sql
-- 创建表
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 查看表结构
DESCRIBE users;
SHOW CREATE TABLE users;

-- 修改表
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users MODIFY COLUMN email VARCHAR(150);
ALTER TABLE users DROP COLUMN phone;

-- 删除表
DROP TABLE users;

-- 重命名表
RENAME TABLE users TO customers;
```

### 数据操作 (CRUD)
```sql
-- 插入数据
INSERT INTO users (username, email, password) 
VALUES ('john_doe', 'john@example.com', 'hashed_password');

-- 批量插入
INSERT INTO users (username, email, password) VALUES
('alice', 'alice@example.com', 'hash1'),
('bob', 'bob@example.com', 'hash2'),
('charlie', 'charlie@example.com', 'hash3');

-- 查询数据
SELECT * FROM users;
SELECT id, username, email FROM users;
SELECT * FROM users WHERE id = 1;
SELECT * FROM users WHERE username LIKE 'j%';
SELECT * FROM users ORDER BY created_at DESC;
SELECT COUNT(*) FROM users;

-- 更新数据
UPDATE users SET email = 'new_email@example.com' WHERE id = 1;
UPDATE users SET updated_at = NOW() WHERE id = 1;

-- 删除数据
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE username = 'john_doe';
```

### 索引操作
```sql
-- 创建索引
CREATE INDEX idx_username ON users(username);
CREATE UNIQUE INDEX idx_email ON users(email);
CREATE INDEX idx_created_at ON users(created_at);

-- 查看索引
SHOW INDEX FROM users;

-- 删除索引
DROP INDEX idx_username ON users;
```

## 高级查询

### 连接查询
```sql
-- 内连接
SELECT u.username, p.title, p.content
FROM users u
INNER JOIN posts p ON u.id = p.user_id;

-- 左连接
SELECT u.username, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id;

-- 右连接
SELECT p.title, u.username
FROM posts p
RIGHT JOIN users u ON p.user_id = u.id;

-- 自连接
SELECT e1.name as employee, e2.name as manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

### 子查询
```sql
-- 标量子查询
SELECT username, 
       (SELECT COUNT(*) FROM posts WHERE user_id = users.id) as post_count
FROM users;

-- IN 子查询
SELECT * FROM users 
WHERE id IN (SELECT DISTINCT user_id FROM posts);

-- EXISTS 子查询
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM posts p WHERE p.user_id = u.id);
```

### 聚合函数
```sql
-- 基本聚合
SELECT 
    COUNT(*) as total_users,
    AVG(age) as avg_age,
    MAX(created_at) as latest_user,
    MIN(created_at) as earliest_user
FROM users;

-- 分组聚合
SELECT 
    DATE(created_at) as signup_date,
    COUNT(*) as daily_signups
FROM users
GROUP BY DATE(created_at)
ORDER BY signup_date DESC;

-- HAVING 子句
SELECT 
    user_id,
    COUNT(*) as post_count
FROM posts
GROUP BY user_id
HAVING COUNT(*) > 5;
```

## 事务管理

### 事务基础
```sql
-- 开始事务
START TRANSACTION;

-- 执行多个操作
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- 提交事务
COMMIT;

-- 回滚事务
ROLLBACK;
```

### 事务隔离级别
```sql
-- 查看当前隔离级别
SELECT @@transaction_isolation;

-- 设置隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

## 存储过程和函数

### 存储过程
```sql
-- 创建存储过程
DELIMITER //
CREATE PROCEDURE GetUserPosts(IN user_id INT)
BEGIN
    SELECT p.*, u.username
    FROM posts p
    JOIN users u ON p.user_id = u.id
    WHERE p.user_id = user_id;
END //
DELIMITER ;

-- 调用存储过程
CALL GetUserPosts(1);

-- 删除存储过程
DROP PROCEDURE GetUserPosts;
```

### 函数
```sql
-- 创建函数
DELIMITER //
CREATE FUNCTION GetPostCount(user_id INT) 
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE post_count INT;
    SELECT COUNT(*) INTO post_count FROM posts WHERE user_id = user_id;
    RETURN post_count;
END //
DELIMITER ;

-- 使用函数
SELECT username, GetPostCount(id) as post_count FROM users;

-- 删除函数
DROP FUNCTION GetPostCount;
```

## 视图

### 视图操作
```sql
-- 创建视图
CREATE VIEW user_post_summary AS
SELECT 
    u.id,
    u.username,
    u.email,
    COUNT(p.id) as post_count,
    MAX(p.created_at) as latest_post
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id, u.username, u.email;

-- 查询视图
SELECT * FROM user_post_summary;

-- 更新视图
CREATE OR REPLACE VIEW user_post_summary AS
SELECT 
    u.id,
    u.username,
    u.email,
    COUNT(p.id) as post_count,
    MAX(p.created_at) as latest_post,
    u.created_at as member_since
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id, u.username, u.email, u.created_at;

-- 删除视图
DROP VIEW user_post_summary;
```

## 触发器

### 触发器操作
```sql
-- 创建触发器
DELIMITER //
CREATE TRIGGER update_user_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END //
DELIMITER ;

-- 创建审计触发器
DELIMITER //
CREATE TRIGGER audit_user_changes
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_audit_log (user_id, old_email, new_email, changed_at)
    VALUES (OLD.id, OLD.email, NEW.email, NOW());
END //
DELIMITER ;

-- 删除触发器
DROP TRIGGER update_user_timestamp;
```

## 用户和权限管理

### 用户管理
```sql
-- 创建用户
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'secure_password';
CREATE USER 'app_user'@'%' IDENTIFIED BY 'secure_password';

-- 修改用户密码
ALTER USER 'app_user'@'localhost' IDENTIFIED BY 'new_password';

-- 删除用户
DROP USER 'app_user'@'localhost';

-- 查看用户
SELECT user, host FROM mysql.user;
```

### 权限管理
```sql
-- 授予权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_user'@'localhost';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin_user'@'localhost';

-- 授予特定表权限
GRANT SELECT, INSERT ON mydb.users TO 'readonly_user'@'localhost';

-- 撤销权限
REVOKE DELETE ON mydb.* FROM 'app_user'@'localhost';

-- 查看权限
SHOW GRANTS FOR 'app_user'@'localhost';

-- 刷新权限
FLUSH PRIVILEGES;
```

## 备份和恢复

### 逻辑备份
```bash
# 备份整个数据库
mysqldump -u root -p mydb > mydb_backup.sql

# 备份特定表
mysqldump -u root -p mydb users posts > tables_backup.sql

# 只备份结构
mysqldump -u root -p --no-data mydb > mydb_structure.sql

# 只备份数据
mysqldump -u root -p --no-create-info mydb > mydb_data.sql

# 压缩备份
mysqldump -u root -p mydb | gzip > mydb_backup.sql.gz
```

### 恢复数据
```bash
# 恢复整个数据库
mysql -u root -p mydb < mydb_backup.sql

# 恢复压缩备份
gunzip < mydb_backup.sql.gz | mysql -u root -p mydb
```

### 物理备份
```bash
# 使用Percona XtraBackup（需要安装）
xtrabackup --backup --target-dir=/backup/mysql/
xtrabackup --prepare --target-dir=/backup/mysql/
```

## 性能优化

### 查询优化
```sql
-- 使用EXPLAIN分析查询
EXPLAIN SELECT * FROM users WHERE username = 'john_doe';

-- 强制使用索引
SELECT * FROM users FORCE INDEX (idx_username) WHERE username = 'john_doe';

-- 避免SELECT *
SELECT id, username, email FROM users WHERE id = 1;

-- 使用LIMIT限制结果集
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10;
```

### 索引优化
```sql
-- 复合索引
CREATE INDEX idx_user_status ON users(status, created_at);

-- 覆盖索引
CREATE INDEX idx_user_cover ON users(id, username, email);

-- 前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));

-- 查看索引使用情况
SHOW INDEX FROM users;
```

### 配置优化
```sql
-- 查看配置变量
SHOW VARIABLES LIKE '%buffer%';
SHOW VARIABLES LIKE '%cache%';
SHOW VARIABLES LIKE '%innodb%';

-- 临时修改配置
SET GLOBAL innodb_buffer_pool_size = 1073741824; -- 1GB
SET GLOBAL query_cache_size = 67108864; -- 64MB

-- 查看状态变量
SHOW STATUS LIKE 'Innodb_buffer_pool%';
SHOW STATUS LIKE 'Qcache%';
```

## 监控和诊断

### 性能监控
```sql
-- 查看进程列表
SHOW PROCESSLIST;

-- 查看锁信息
SHOW ENGINE INNODB STATUS;

-- 查看表状态
SHOW TABLE STATUS LIKE 'users';

-- 查看慢查询日志配置
SHOW VARIABLES LIKE 'slow_query_log%';
SHOW VARIABLES LIKE 'long_query_time';
```

### 诊断工具
```sql
-- 查看连接信息
SELECT * FROM information_schema.processlist;

-- 查看表空间使用
SELECT 
    table_schema as database_name,
    table_name,
    round(((data_length + index_length) / 1024 / 1024), 2) as size_mb
FROM information_schema.tables
ORDER BY (data_length + index_length) DESC;

-- 查看索引统计
SELECT 
    table_name,
    index_name,
    stat_value * @@innodb_page_size as index_size
FROM mysql.innodb_index_stats
WHERE database_name = 'mydb';
```

## 安全最佳实践

### 数据库安全
- **强密码策略**: 使用复杂密码，定期更换
- **最小权限原则**: 只授予必要的权限
- **网络隔离**: 限制数据库访问来源
- **加密连接**: 使用SSL/TLS加密数据传输
- **定期审计**: 监控异常访问行为

### 数据安全
```sql
-- 启用SSL连接
GRANT USAGE ON *.* TO 'user'@'%' REQUIRE SSL;

-- 数据加密
CREATE TABLE sensitive_data (
    id INT PRIMARY KEY,
    encrypted_data VARBINARY(255)
);

-- 审计日志
CREATE TABLE security_audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    action VARCHAR(50),
    table_name VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 故障排除

### 常见问题
- **连接问题**: 检查网络、防火墙、用户权限
- **性能问题**: 分析慢查询、检查索引使用
- **锁问题**: 查看锁等待、死锁检测
- **空间问题**: 监控磁盘空间、表空间使用

### 调试工具
```sql
-- 查看错误日志
SHOW VARIABLES LIKE 'log_error';

-- 查看二进制日志
SHOW BINARY LOGS;
SHOW BINLOG EVENTS IN 'mysql-bin.000001';

-- 查看复制状态
SHOW SLAVE STATUS;

-- 查看系统变量
SHOW VARIABLES;
SHOW STATUS;
```

### 性能诊断
```sql
-- 分析慢查询
SELECT * FROM mysql.slow_log ORDER BY start_time DESC LIMIT 10;

-- 查看锁等待
SELECT * FROM information_schema.innodb_locks;
SELECT * FROM information_schema.innodb_lock_waits;

-- 查看表碎片
SELECT 
    table_name,
    data_free / 1024 / 1024 as fragmentation_mb
FROM information_schema.tables
WHERE table_schema = 'mydb' AND data_free > 0;
```

## 工具和资源

### MySQL 工具
- **mysql**: 命令行客户端
- **mysqldump**: 逻辑备份工具
- **mysqladmin**: 管理工具
- **mysqlcheck**: 表检查和修复工具
- **mysqlimport**: 数据导入工具

### 第三方工具
- **phpMyAdmin**: Web管理界面
- **MySQL Workbench**: 官方图形化管理工具
- **Percona Toolkit**: 高级管理工具集
- **ProxySQL**: 高性能代理

### 学习资源
- **官方文档**: https://dev.mysql.com/doc/
- **MySQL 8.0参考手册**: 完整的功能说明
- **Percona博客**: 性能优化和最佳实践
- **MySQL社区**: 问题解答和经验分享

## 最佳实践

### 开发最佳实践
- 使用合适的数据类型
- 规范化数据库设计
- 合理使用索引
- 编写高效的SQL查询
- 使用事务保证数据一致性

### 运维最佳实践
- 定期备份和恢复测试
- 监控性能指标
- 定期维护（优化表、重建索引）
- 安全配置和审计
- 容量规划和扩展

### 性能最佳实践
- 优化查询性能
- 合理配置缓存
- 使用连接池
- 读写分离
- 分库分表（大数据量场景）

这个文档为MySQL的使用提供了全面的知识储备，涵盖了从基础概念到高级优化的各个方面。
