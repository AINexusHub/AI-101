# PostgreSQL 知识库

## PostgreSQL 核心概念

### 数据库基础概念
- **数据库 (Database)**: 数据的逻辑容器，包含表、视图、函数等对象
- **模式 (Schema)**: 数据库内的命名空间，用于组织数据库对象
- **表 (Table)**: 数据的二维结构，由行和列组成
- **行 (Row/Record)**: 表中的一条记录
- **列 (Column/Field)**: 表中的字段，定义数据类型
- **主键 (Primary Key)**: 唯一标识表中每行的字段
- **外键 (Foreign Key)**: 建立表间关系的字段
- **索引 (Index)**: 提高查询性能的数据结构
- **序列 (Sequence)**: 生成唯一数字序列的对象

### 数据类型
- **数值类型**: INTEGER, BIGINT, DECIMAL, NUMERIC, REAL, DOUBLE PRECISION
- **字符串类型**: CHAR, VARCHAR, TEXT
- **日期时间类型**: DATE, TIME, TIMESTAMP, INTERVAL
- **布尔类型**: BOOLEAN
- **数组类型**: 支持任意数据类型的数组
- **JSON类型**: JSON, JSONB (二进制JSON)
- **几何类型**: POINT, LINE, CIRCLE, POLYGON
- **网络地址类型**: INET, CIDR, MACADDR
- **UUID类型**: 全局唯一标识符

### 高级特性
- **事务支持**: ACID特性保证数据一致性
- **MVCC (多版本并发控制)**: 无锁读取，提高并发性能
- **存储过程**: 使用PL/pgSQL等语言编写
- **触发器**: 数据变更时自动执行的操作
- **视图**: 虚拟表，基于查询结果
- **物化视图**: 缓存查询结果的视图
- **分区表**: 水平分割大表数据
- **全文搜索**: 内置全文搜索功能
- **地理空间支持**: PostGIS扩展

## PostgreSQL 基本操作

### 数据库操作
```sql
-- 创建数据库
CREATE DATABASE mydb;

-- 连接到数据库
\c mydb

-- 查看所有数据库
\l

-- 删除数据库
DROP DATABASE mydb;

-- 查看数据库信息
SELECT datname, encoding, datcollate FROM pg_database;
```

### 模式操作
```sql
-- 创建模式
CREATE SCHEMA myschema;

-- 设置搜索路径
SET search_path TO myschema, public;

-- 查看所有模式
\dn

-- 删除模式
DROP SCHEMA myschema CASCADE;
```

### 表操作
```sql
-- 创建表
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 查看表结构
\d users

-- 修改表
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN email TYPE VARCHAR(150);
ALTER TABLE users DROP COLUMN phone;

-- 删除表
DROP TABLE users;

-- 重命名表
ALTER TABLE users RENAME TO customers;
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
('charlie', 'charlie@example.com', 'hash3')
RETURNING id;

-- 查询数据
SELECT * FROM users;
SELECT id, username, email FROM users;
SELECT * FROM users WHERE id = 1;
SELECT * FROM users WHERE username LIKE 'j%';
SELECT * FROM users ORDER BY created_at DESC;
SELECT COUNT(*) FROM users;

-- 更新数据
UPDATE users SET email = 'new_email@example.com' WHERE id = 1;
UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE id = 1;

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

-- 创建部分索引
CREATE INDEX idx_active_users ON users(username) WHERE active = true;

-- 创建表达式索引
CREATE INDEX idx_lower_username ON users(LOWER(username));

-- 查看索引
\di

-- 删除索引
DROP INDEX idx_username;
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
GROUP BY u.id, u.username;

-- 右连接
SELECT p.title, u.username
FROM posts p
RIGHT JOIN users u ON p.user_id = u.id;

-- 全外连接
SELECT u.username, p.title
FROM users u
FULL OUTER JOIN posts p ON u.id = p.user_id;

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

-- 相关子查询
SELECT username,
       (SELECT COUNT(*) FROM posts WHERE user_id = users.id AND created_at > CURRENT_DATE - INTERVAL '7 days') as recent_posts
FROM users;
```

### 窗口函数
```sql
-- 排名函数
SELECT 
    username,
    post_count,
    RANK() OVER (ORDER BY post_count DESC) as rank,
    DENSE_RANK() OVER (ORDER BY post_count DESC) as dense_rank,
    ROW_NUMBER() OVER (ORDER BY post_count DESC) as row_num
FROM (
    SELECT u.username, COUNT(p.id) as post_count
    FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
    GROUP BY u.id, u.username
) user_stats;

-- 聚合窗口函数
SELECT 
    username,
    post_count,
    AVG(post_count) OVER () as avg_posts,
    SUM(post_count) OVER (ORDER BY created_at) as running_total
FROM user_post_stats;
```

### 聚合函数
```sql
-- 基本聚合
SELECT 
    COUNT(*) as total_users,
    AVG(EXTRACT(YEAR FROM AGE(created_at))) as avg_account_age_years,
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

-- 分组集
SELECT 
    COALESCE(TO_CHAR(created_at, 'YYYY-MM'), 'Total') as month,
    COUNT(*) as signups
FROM users
GROUP BY ROLLUP (TO_CHAR(created_at, 'YYYY-MM'));

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
BEGIN;

-- 或者使用更明确的语法
START TRANSACTION;

-- 执行多个操作
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- 提交事务
COMMIT;

-- 回滚事务
ROLLBACK;

-- 保存点
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
SAVEPOINT sp1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- 如果需要回滚到保存点
ROLLBACK TO SAVEPOINT sp1;
COMMIT;
```

### 事务隔离级别
```sql
-- 查看当前隔离级别
SHOW transaction_isolation;

-- 设置隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- 可用的隔离级别
-- READ UNCOMMITTED (PostgreSQL中实际为READ COMMITTED)
-- READ COMMITTED (默认)
-- REPEATABLE READ
-- SERIALIZABLE
```

## 存储过程和函数

### 函数
```sql
-- 创建函数
CREATE OR REPLACE FUNCTION get_user_post_count(user_id INTEGER)
RETURNS INTEGER AS $$
DECLARE
    post_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO post_count 
    FROM posts 
    WHERE user_id = user_id;
    
    RETURN post_count;
END;
$$ LANGUAGE plpgsql;

-- 使用函数
SELECT username, get_user_post_count(id) as post_count FROM users;

-- 删除函数
DROP FUNCTION get_user_post_count(INTEGER);
```

### 存储过程 (PostgreSQL 11+)
```sql
-- 创建存储过程
CREATE OR REPLACE PROCEDURE transfer_funds(
    from_account INTEGER,
    to_account INTEGER,
    amount DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- 验证余额
    IF (SELECT balance FROM accounts WHERE id = from_account) < amount THEN
        RAISE EXCEPTION 'Insufficient funds';
    END IF;
    
    -- 执行转账
    UPDATE accounts SET balance = balance - amount WHERE id = from_account;
    UPDATE accounts SET balance = balance + amount WHERE id = to_account;
    
    -- 记录交易
    INSERT INTO transactions (from_account, to_account, amount, created_at)
    VALUES (from_account, to_account, amount, CURRENT_TIMESTAMP);
END;
$$;

-- 调用存储过程
CALL transfer_funds(1, 2, 100.00);
```

### 触发器函数
```sql
-- 创建触发器函数
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 创建触发器
CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
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

-- 更新视图定义
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

### 物化视图
```sql
-- 创建物化视图
CREATE MATERIALIZED VIEW user_stats AS
SELECT 
    u.id,
    u.username,
    COUNT(p.id) as post_count,
    COUNT(DISTINCT c.id) as comment_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
LEFT JOIN comments c ON u.id = c.user_id
GROUP BY u.id, u.username;

-- 刷新物化视图
REFRESH MATERIALIZED VIEW user_stats;

-- 并发刷新（PostgreSQL 9.4+）
REFRESH MATERIALIZED VIEW CONCURRENTLY user_stats;

-- 删除物化视图
DROP MATERIALIZED VIEW user_stats;
```

## JSON 操作

### JSON 数据类型
```sql
-- 创建包含JSON列的表
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    attributes JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入JSON数据
INSERT INTO products (name, attributes) VALUES
('Laptop', '{"brand": "Dell", "specs": {"cpu": "i7", "ram": "16GB"}, "price": 999.99}'),
('Phone', '{"brand": "Apple", "specs": {"storage": "128GB", "color": "black"}, "price": 899.99}');

-- 查询JSON数据
SELECT name, attributes->>'brand' as brand
FROM products;

-- JSON路径查询
SELECT name, attributes#>'{specs,cpu}' as cpu
FROM products;

-- JSON条件查询
SELECT name, attributes->>'price' as price
FROM products
WHERE (attributes->>'price')::DECIMAL > 900;

-- JSON数组操作
SELECT name, jsonb_array_length(attributes->'tags') as tag_count
FROM products
WHERE attributes ? 'tags';
```

## 分区表

### 范围分区
```sql
-- 创建主表
CREATE TABLE sales (
    id SERIAL,
    sale_date DATE NOT NULL,
    product_id INTEGER,
    amount DECIMAL(10,2)
) PARTITION BY RANGE (sale_date);

-- 创建分区
CREATE TABLE sales_2023_q1 PARTITION OF sales
    FOR VALUES FROM ('2023-01-01') TO ('2023-04-01');

CREATE TABLE sales_2023_q2 PARTITION OF sales
    FOR VALUES FROM ('2023-04-01') TO ('2023-07-01');

CREATE TABLE sales_2023_q3 PARTITION OF sales
    FOR VALUES FROM ('2023-07-01') TO ('2023-10-01');

CREATE TABLE sales_2023_q4 PARTITION OF sales
    FOR VALUES FROM ('2023-10-01') TO ('2024-01-01');
```

### 列表分区
```sql
-- 按地区分区
CREATE TABLE customers (
    id SERIAL,
    name VARCHAR(100),
    region VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY LIST (region);

-- 创建分区
CREATE TABLE customers_north PARTITION OF customers
    FOR VALUES IN ('north', 'northeast');

CREATE TABLE customers_south PARTITION OF customers
    FOR VALUES IN ('south', 'southeast');

CREATE TABLE customers_west PARTITION OF customers
    FOR VALUES IN ('west', 'northwest');
```

## 用户和权限管理

### 用户和角色管理
```sql
-- 创建角色
CREATE ROLE app_user WITH LOGIN PASSWORD 'secure_password';
CREATE ROLE read_only WITH LOGIN PASSWORD 'readonly_pass';

-- 修改角色
ALTER ROLE app_user WITH PASSWORD 'new_password';
ALTER ROLE app_user VALID UNTIL '2024-12-31';

-- 删除角色
DROP ROLE app_user;

-- 查看角色
\du
```

### 权限管理
```sql
-- 授予权限
GRANT CONNECT ON DATABASE mydb TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;

-- 授予序列权限
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- 授予特定表权限
GRANT SELECT ON users TO read_only;

-- 撤销权限
REVOKE DELETE ON users FROM app_user;

-- 查看权限
\dp
\z users

-- 默认权限
ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;
```

## 备份和恢复

### 逻辑备份
```bash
# 备份整个数据库
pg_dump -U postgres -d mydb -f mydb_backup.sql

# 备份特定模式
pg_dump -U postgres -d mydb -n public -f public_schema.sql

# 只备份结构
pg_dump -U postgres -d mydb --schema-only -f mydb_structure.sql

# 只备份数据
pg_dump -U postgres -d mydb --data-only -f mydb_data.sql

# 自定义格式备份（压缩）
pg_dump -U postgres -d mydb -Fc -f mydb_backup.dump

# 并行备份
pg_dump -U postgres -d mydb -j 4 -Fd -f mydb_backup_dir/
```

### 恢复数据
```bash
# 恢复SQL备份
psql -U postgres -d mydb -f mydb_backup.sql

# 恢复自定义格式备份
pg_restore -U postgres -d mydb mydb_backup.dump

# 恢复并行备份
pg_restore -U postgres -d mydb -j 4 -Fd mydb_backup_dir/

# 仅
