# 设计模式知识库

## 设计模式概述

### 什么是设计模式
- **设计模式**: 在软件设计中反复出现的问题的通用、可重用的解决方案
- **模式要素**: 模式名称、问题、解决方案、效果
- **设计原则**: 指导模式应用的基本原则

### 设计原则
- **单一职责原则 (SRP)**: 一个类应该只有一个引起变化的原因
- **开放封闭原则 (OCP)**: 对扩展开放，对修改关闭
- **里氏替换原则 (LSP)**: 子类必须能够替换它们的基类
- **接口隔离原则 (ISP)**: 使用多个专门的接口比使用单一的总接口要好
- **依赖倒置原则 (DIP)**: 依赖于抽象而不是具体实现
- **迪米特法则 (LoD)**: 一个对象应该对其他对象有最少的了解

## 创建型模式

### 工厂方法模式 (Factory Method)
```python
from abc import ABC, abstractmethod

# 产品接口
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# 具体产品
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "ConcreteProductA operation"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "ConcreteProductB operation"

# 创建者
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass
    
    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: {product.operation()}"

# 具体创建者
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# 使用
creator = ConcreteCreatorA()
print(creator.some_operation())  # Creator: ConcreteProductA operation
```

**适用场景**:
- 不知道需要创建哪种具体对象
- 希望将对象的创建与使用分离
- 希望提供扩展点，允许子类决定创建哪种对象

### 抽象工厂模式 (Abstract Factory)
```python
from abc import ABC, abstractmethod

# 抽象产品A
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

# 抽象产品B
class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass

# 具体产品A1
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "ProductA1"

# 具体产品A2
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "ProductA2"

# 具体产品B1
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "ProductB1"

# 具体产品B2
class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "ProductB2"

# 抽象工厂
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# 具体工厂1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

# 具体工厂2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# 客户端代码
def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")

# 使用
client_code(ConcreteFactory1())
client_code(ConcreteFactory2())
```

**适用场景**:
- 需要创建一系列相关或依赖的对象
- 希望产品族能够独立于使用它们的系统
- 需要确保产品之间的兼容性

### 建造者模式 (Builder)
```python
from abc import ABC, abstractmethod
from typing import Any

# 产品
class Car:
    def __init__(self):
        self.parts = []
    
    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Car parts: {', '.join(self.parts)}")

# 建造者接口
class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    
    @abstractmethod
    def produce_engine(self) -> None:
        pass
    
    @abstractmethod
    def produce_wheels(self) -> None:
        pass
    
    @abstractmethod
    def produce_body(self) -> None:
        pass

# 具体建造者
class CarBuilder(Builder):
    def __init__(self):
        self.reset()
    
    def reset(self) -> None:
        self._car = Car()
    
    @property
    def product(self) -> Car:
        car = self._car
        self.reset()
        return car
    
    def produce_engine(self) -> None:
        self._car.add("V8 Engine")
    
    def produce_wheels(self) -> None:
        self._car.add("4 Wheels")
    
    def produce_body(self) -> None:
        self._car.add("Sedan Body")

# 主管
class Director:
    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
    
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_engine()
        self.builder.produce_wheels()
    
    def build_full_featured_product(self) -> None:
        self.builder.produce_engine()
        self.builder.produce_wheels()
        self.builder.produce_body()

# 使用
director = Director()
builder = CarBuilder()
director.builder = builder

print("Standard basic product:")
director.build_minimal_viable_product()
builder.product.list_parts()

print("\nStandard full featured product:")
director.build_full_featured_product()
builder.product.list_parts()

print("\nCustom product:")
builder.produce_engine()
builder.produce_body()
builder.product.list_parts()
```

**适用场景**:
- 创建复杂对象，构造过程需要多个步骤
- 需要创建不同表示的对象
- 希望将对象的构造过程与表示分离

### 原型模式 (Prototype)
```python
import copy
from abc import ABC, abstractmethod

# 原型接口
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# 具体原型
class ConcretePrototype1(Prototype):
    def __init__(self, value: str):
        self._value = value
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"ConcretePrototype1 with value: {self._value}"

class ConcretePrototype2(Prototype):
    def __init__(self, number: int, data: list):
        self._number = number
        self._data = data
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"ConcretePrototype2 with number: {self._number}, data: {self._data}"

# 使用
prototype1 = ConcretePrototype1("Hello")
clone1 = prototype1.clone()
print(f"Original: {prototype1}")
print(f"Clone: {clone1}")

prototype2 = ConcretePrototype2(42, [1, 2, 3])
clone2 = prototype2.clone()
clone2._data.append(4)
print(f"Original: {prototype2}")
print(f"Clone: {clone2}")
```

**适用场景**:
- 需要创建的对象成本较高
- 避免使用子类来扩展对象创建
- 需要动态加载类

### 单例模式 (Singleton)
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

# 使用
s1 = Singleton()
s2 = Singleton()

print(f"ID of s1: {id(s1)}")
print(f"ID of s2: {id(s2)}")
print(f"Are they the same? {s1 is s2}")

# 线程安全的单例模式
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

# 使用
ts1 = ThreadSafeSingleton()
ts2 = ThreadSafeSingleton()
print(f"Thread-safe singleton: {ts1 is ts2}")
```

**适用场景**:
- 需要确保一个类只有一个实例
- 需要全局访问点
- 控制对共享资源的访问

## 结构型模式

### 适配器模式 (Adapter)
```python
from abc import ABC, abstractmethod

# 目标接口
class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass

# 需要适配的类
class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

# 适配器
class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee
    
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

# 使用
def client_code(target: Target) -> None:
    print(target.request())

adaptee = Adaptee()
print(f"Adaptee: {adaptee.specific_request()}")

adapter = Adapter(adaptee)
client_code(adapter)
```

**适用场景**:
- 需要使用现有的类，但其接口不符合需求
- 想要创建一个可重用的类，与不相关的类协同工作
- 需要使用几个现有的子类，但为每个子类进行子类化不现实

### 桥接模式 (Bridge)
```python
from abc import ABC, abstractmethod

# 实现接口
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

# 具体实现A
class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on platform A."

# 具体实现B
class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on platform B."

# 抽象
class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation
    
    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")

# 扩展抽象
class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")

# 使用
def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation())

implementation_a = ConcreteImplementationA()
abstraction = Abstraction(implementation_a)
client_code(abstraction)

implementation_b = ConcreteImplementationB()
abstraction = ExtendedAbstraction(implementation_b)
client_code(abstraction)
```

**适用场景**:
- 想要避免在抽象和实现之间建立永久绑定
- 抽象和实现都应该可以通过子类化来扩展
- 对实现的修改不应该影响客户端代码
- 需要在多个对象间共享实现

### 组合模式 (Composite)
```python
from abc import ABC, abstractmethod
from typing import List

# 组件接口
class Component(ABC):
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent
    
    def add(self, component) -> None:
        pass
    
    def remove(self, component) -> None:
        pass
    
    def is_composite(self) -> bool:
        return False
    
    @abstractmethod
    def operation(self) -> str:
        pass

# 叶子节点
class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

# 复合组件
class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None
    
    def is_composite(self) -> bool:
        return True
    
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

# 使用
def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}")

def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)
    print(f"RESULT: {component1.operation()}")

# 简单的叶子节点
simple = Leaf()
print("Client: I've got a simple component:")
client_code(simple)
print("\n")

# 复杂的树结构
tree = Composite()

branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

branch2 = Composite()
branch2.add(Leaf())

tree.add(branch1)
tree.add(branch2)

print("Client: Now I've got a composite tree:")
client_code(tree)
print("\n")

print("Client: I don't need to check the components classes even when managing the tree:")
client_code2(tree, simple)
```

**适用场景**:
- 需要表示对象的部分-整体层次结构
- 希望客户端能够忽略组合对象与单个对象的差异
- 结构可以具有任何级别的复杂性，并且是动态的

### 装饰器模式 (Decorator)
```python
from abc import ABC, abstractmethod

# 组件接口
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# 具体组件
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

# 装饰器基类
class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component
    
    @property
    def component(self) -> Component:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()

# 具体装饰器A
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

# 具体装饰器B
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

# 使用
def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}")

simple = ConcreteComponent()
print("Client: I've got a simple component:")
client_code(simple)
print("\n")

decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
print("Client: Now I've got a decorated component:")
client_code(decorator2)
```

**适用场景**:
- 需要在不影响其他对象的情况下，动态、透明地给单个对象添加职责
- 需要撤销职责
- 通过子类化进行扩展不切实际

### 外观模式 (Facade)
```python
# 复杂子系统类
class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"
    
    def operation_n(self) -> str:
        return "Subsystem1: Go!"

class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"
    
    def operation_z(self) -> str:
        return "Subsystem2: Fire!"

# 外观类
class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()
    
    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)

# 使用
subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
print(facade.operation())
```

**适用场景**:
- 需要为复杂的子系统提供简单的接口
- 客户端与子系统的实现之间存在很多依赖关系
- 想要将子系统分层，使用外观模式来定义每层的入口点

### 享元模式 (Flyweight)
```python
from typing import Dict

# 享元
class Flyweight:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state
    
    def operation(self, unique_state: str) -> None:
        s = f"Flyweight: Displaying shared ({self._shared_state}) and unique ({unique_state}) state."
        print(s)

# 享元工厂
class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}
    
    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))
    
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)
        
        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        
        return self._flyweights[key]
    
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        for key in self._flyweights:
            print(key)

# 使用
factory = FlyweightFactory([
    {"brand": "Chevrolet", "model": "Camaro2018", "color": "pink"},
    {"brand": "Mercedes Benz", "model": "C300", "color": "black"},
    {"brand": "Mercedes Benz", "model": "C500", "color": "red"},
    {"brand": "BMW", "model": "M5", "color": "red"},
    {"brand": "BMW", "model": "X6", "color": "white"},
])

factory.list_flyweights()

def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight({"brand": brand, "model": model, "color": color})
    flyweight.operation([plates, owner])

add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
add_car_to_police_database(factory, "CL678IR", "James Doe", "BMW", "X1", "red")
```

**适用场景**:
- 应用程序使用了大量的对象
- 由于大量的对象，造成很大的存储开销
- 对象的大多数状态都可以变为外部状态
- 如果删除对象的外部状态，可以用相对较少的共享对象取代很多组对象

### 代理模式 (Proxy)
```python
from abc import ABC, abstractmethod

# 主题接口
class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

# 真实主题
class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")

# 代理
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
    
    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()
    
    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True
    
    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")

# 使用
def client_code(subject: Subject) -> None:
    subject.request()

print("Client: Executing the client code with a real subject:")
real_subject = RealSubject()
client_code(real_subject)

print("\nClient: Executing the same client code with a proxy:")
proxy = Proxy(real_subject)
client_code(proxy)
```

**适用场景**:
- 延迟初始化（虚拟代理）
- 访问控制（保护代理）
- 本地执行远程服务（远程代理）
- 记录日志请求（日志记录代理）
- 缓存请求结果（缓存代理）

## 行为型模式

### 责任链模式 (Chain of Responsibility)
```python
from abc import ABC, abstractmethod
from typing import Optional

# 处理器接口
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass
    
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

# 基础处理器
class AbstractHandler(Handler):
    _next_handler: Handler = None
    
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# 具体处理器
class MonkeyHandler(AbstractHandler):
    def handle(self, request: any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)

# 使用
def client_code(handler: Handler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")

monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()

monkey.set_next(squirrel).set_next(dog)

print("Chain: Monkey > Squirrel > Dog")
client_code(monkey)

print("\n\nSubchain: Squirrel > Dog")
client_code(squirrel)
```

**适用场景**:
- 有多个对象可以处理请求，但不知道哪个对象会处理
- 想在运行时动态指定处理请求的对象集合
- 想在不明确指定接收者的情况下，向多个对象中的一个提交请求

### 命令模式 (Command)
```python
from abc import ABC, abstractmethod

# 命令接口
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# 简单命令
class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload
    
    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing ({self._payload})")

# 复杂命令
class ComplexCommand(Command):
    def __init__(self, receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b
    
    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

# 接收者
class Receiver:
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")
    
    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")

# 调用者
class Invoker:
    _on_start = None
    _on_finish = None
    
    def set_on_start(self, command: Command):
        self._on_start = command
    
    def set_on_finish(self, command: Command):
        self._on_finish = command
    
    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()
        
        print("Invoker: ...doing something really important...")
        
        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

# 使用
invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(
    receiver, "Send email", "Save report"))

invoker.do_something_important()
```

**适用场景**:
- 需要将操作参数化
- 需要将操作放入队列中、记录操作日志，或者支持可撤销操作
- 需要用不同的请求对客户进行参数化

### 解释器模式 (Interpreter)
```python
from abc import ABC, abstractmethod

# 抽象表达式
class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context: str) -> bool:
        pass

# 终结符表达式
class TerminalExpression(AbstractExpression):
    def __init__(self, data: str):
        self._data = data
    
    def interpret(self, context: str) -> bool:
        return self._data in context

# 非终结符表达式
class OrExpression(AbstractExpression):
    def __init__(self, expr1: AbstractExpression, expr2: AbstractExpression):
        self._expr1 = expr1
        self._expr2 = expr2
    
    def interpret(self, context: str) -> bool:
        return self._expr1.interpret(context) or self._expr2.interpret(context)

class AndExpression(AbstractExpression):
    def __init__(self, expr1: AbstractExpression, expr2: AbstractExpression):
        self._expr1 = expr1
        self._expr2 = expr2
    
    def interpret(self, context: str) -> bool:
        return self._expr1.interpret(context) and self._expr2.interpret(context)

# 使用
def get_male_expression():
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    return OrExpression(robert, john)

def get_married_woman_expression():
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    return AndExpression(julie, married)

# 规则：Robert 和 John 是男性
is_male = get_male_expression()
# 规则：Julie 是已婚女性
is_married_woman = get_married_woman_expression()

print("John is male? " + str(is_male.interpret("John")))
print("Julie is a married women? " + str(is_married_woman.interpret("Married Julie")))
```

**适用场景**:
- 当有一个语言需要解释执行，并且可将该语言中的句子表示为一个抽象语法树时
- 效率不是关键问题

### 迭代器模式 (Iterator)
```python
from collections.abc import Iterator, Iterable
from typing import Any, List

# 具体集合
class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
    
    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)
    
    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)
    
    def add_item(self, item: Any):
        self._collection.append(item)

# 具体迭代器
class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False
    
    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        
        return value

# 使用
collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")

print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()))
```

**适用场景**:
- 需要访问聚合对象的内容而不暴露其内部表示
- 需要支持对聚合对象的多种遍历
- 需要为遍历不同的聚合结构提供一个统一的接口

### 中介者模式 (Mediator)
```python
from abc import ABC, abstractmethod
from typing import List

# 中介者接口
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

# 具体中介者
class ConcreteMediator(Mediator):
    def __init__(self, component1, component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self
    
    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

# 基础组件
class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator
    
    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

# 具体组件
class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")
    
    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")
    
    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")

# 使用
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("\nClient triggers operation D.")
c2.do_d()
```

**适用场景**:
- 一组对象以定义良好但是复杂的方式进行通信
- 一个对象引用其他很多对象并且直接与这些对象通信，导致难以复用该对象
- 想定制一个分布在多个类中的行为，而又不想生成太多的子类

### 备忘录模式 (Memento)
```python
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters

# 备忘录
class Memento:
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]
    
    @property
    def state(self) -> str:
        return self._state
    
    @property
    def date(self) -> str:
        return self._date

# 发起人
class Originator:
    _state = None
    
    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")
    
    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")
    
    def _generate_random_string(self, length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))
    
    def save(self) -> Memento:
        return Memento(self._state)
    
    def restore(self, memento: Memento) -> None:
        self._state = memento.state
        print(f"Originator: My state has changed to: {self._state}")

# 管理者
class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator
    
    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())
    
    def undo(self) -> None:
        if not len(self._mementos):
            return
        
        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.date}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
    
    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.date)

# 使用
originator = Originator("Super-duper-super-puper-super.")
caretaker = Caretaker(originator)

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

print()
caretaker.show_history()

print("\nClient: Now, let's rollback!\n")
caretaker.undo()

print("\nClient: Once more!\n")
caretaker.undo()
```

**适用场景**:
- 需要保存和恢复对象的状态快照
- 需要实现撤销操作
- 直接访问对象的成员变量、获取器或设置器将导致封装被突破

### 观察者模式 (Observer)
```python
from abc import ABC, abstractmethod
from random import randrange
from typing import List

# 主题接口
class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass
    
    @abstractmethod
    def detach(self, observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass

# 具体主题
class ConcreteSubject(Subject):
    _state: int = None
    _observers: List = []
    
    def attach(self, observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)
    
    def detach(self, observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)
        
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

# 观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

# 具体观察者A
class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")

# 具体观察者B
class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

# 使用
subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()
```

**适用场景**:
- 当一个对象状态的改变需要改变其他对象时
- 一个对象需要通知其他对象，但不知道这些对象是谁
- 需要在运行时动态建立对象之间的关系

### 状态模式 (State)
```python
from abc import ABC, abstractmethod

# 上下文
class Context:
    _state = None
    
    def __init__(self, state) -> None:
        self.transition_to(state)
    
    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self
    
    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()

# 状态接口
class State(ABC):
    @property
    def context(self):
        return self._context
    
    @context.setter
    def context(self, context) -> None:
        self._context = context
    
    @abstractmethod
    def handle1(self) -> None:
        pass
    
    @abstractmethod
    def handle2(self) -> None:
        pass

# 具体状态A
class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())
    
    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")

# 具体状态B
class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")
    
    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())

# 使用
context = Context(ConcreteStateA())
context.request1()
context.request2()
```

**适用场景**:
- 一个对象的行为取决于它的状态，并且它必须在运行时根据状态改变它的行为
- 一个操作中含有庞大的多分支的条件语句，且这些分支依赖于该对象的状态

### 策略模式 (Strategy)
```python
from abc import ABC, abstractmethod

# 策略接口
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: list):
        pass

# 具体策略A
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list):
        return sorted(data)

# 具体策略B
class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list):
        return reversed(sorted(data))

# 上下文
class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

# 使用
context = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
context.do_some_business_logic()

print()

print("Client: Strategy is set to reverse sorting.")
context.strategy = ConcreteStrategyB()
context.do_some_business_logic()
```

**适用场景**:
- 许多相关的类仅仅是行为有异
- 需要使用一个算法的不同变体
- 算法使用客户端不应该知道的数据
- 一个类定义了多种行为，并且这些行为在这个类的操作中以多个条件语句的形式出现

### 模板方法模式 (Template Method)
```python
from abc import ABC, abstractmethod

# 抽象类
class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()
    
    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")
    
    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")
    
    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")
    
    @abstractmethod
    def required_operations1(self) -> None:
        pass
    
    @abstractmethod
    def required_operations2(self) -> None:
        pass
    
    def hook1(self) -> None:
        pass
    
    def hook2(self) -> None:
        pass

# 具体类A
class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")
    
    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

# 具体类B
class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")
    
    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")
    
    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")

# 使用
print("Same client code can work with different subclasses:")
concrete_class1 = ConcreteClass1()
concrete_class1.template_method()

print("\n")

concrete_class2 = ConcreteClass2()
concrete_class2.template_method()
```

**适用场景**:
- 一次性实现一个算法的不变部分，并将可变的行为留给子类来实现
- 各子类中公共的行为应被提取出来并集中到一个公共父类中以避免代码重复
- 控制子类扩展

### 访问者模式 (Visitor)
```python
from abc import ABC, abstractmethod
from typing import List

# 元素接口
class Component(ABC):
    @abstractmethod
    def accept(self, visitor) -> None:
        pass

# 具体元素A
class ConcreteComponentA(Component):
    def accept(self, visitor) -> None:
        visitor.visit_concrete_component_a(self)
    
    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"

# 具体元素B
class ConcreteComponentB(Component):
    def accept(self, visitor) -> None:
        visitor.visit_concrete_component_b(self)
    
    def special_method_of_concrete_component_b(self) -> str:
        return "B"

# 访问者接口
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element) -> None:
        pass
    
    @abstractmethod
    def visit_concrete_component_b(self, element) -> None:
        pass

# 具体访问者1
class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")
    
    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")

# 具体访问者2
class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")
    
    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")

# 使用
def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)

components = [ConcreteComponentA(), ConcreteComponentB()]

print("The client code works with all visitors via the base Visitor interface:")
visitor1 = ConcreteVisitor1()
client_code(components, visitor1)

print("It allows the same client code to work with different types of visitors:")
visitor2 = ConcreteVisitor2()
client_code(components, visitor2)
```

**适用场景**:
- 一个对象结构包含很多类对象，它们有不同的接口，而你想对这些对象实施一些依赖于其具体类的操作
- 需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而你想避免让这些操作"污染"这些对象的类
- 定义对象结构的类很少改变，但经常需要在此结构上定义新的操作

## 设计模式总结

### 模式分类
- **创建型模式**: 关注对象的创建过程
- **结构型模式**: 关注类和对象的组合
- **行为型模式**: 关注对象间的职责分配和算法

### 选择模式的考虑因素
- **问题域**: 模式是否适合当前问题
- **灵活性**: 模式是否提供足够的扩展性
- **复杂性**: 模式是否会引入不必要的复杂性
- **性能**: 模式对性能的影响

### 最佳实践
- 理解模式背后的原则，而不是死记硬背
- 根据具体需求选择合适的模式
- 避免过度设计
- 保持代码的简洁性和可读性

这个文档为设计模式的学习和应用提供了全面的知识储备，涵盖了23种经典设计模式的详细说明和实际应用示例。
