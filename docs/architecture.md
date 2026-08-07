Anime-AI-Companion 架构理解文档
版本：Day2 前置完成
目标：理解一个基于 LLM 的 AI 应用完整架构
1. 项目定位
Anime-AI-Companion 是什么？
Anime-AI-Companion 是一个基于大语言模型（LLM）的角色陪伴系统。
目标：
通过：
角色设定
人格 Prompt
用户历史记忆
LLM生成能力
让普通的大语言模型变成一个具有稳定人格、能够长期交流的 AI 角色。
简单理解：
普通 GPT：
用户
 ↓
GPT
 ↓
回答
Anime-AI-Companion：
用户
 ↓
角色系统
 ↓
人格系统
 ↓
记忆系统
 ↓
Prompt构建
 ↓
LLM
 ↓
角色回复
2. AI应用整体架构理解
五层架构
用户层

↓

Controller/API层

↓

Service业务层

↓

AI应用层

↓

外部资源层
第一层：用户层（User）
负责：
用户与系统交互。
例如：
用户输入：
今天好累
用户不关心：
GPT在哪里
Prompt怎么生成
数据库怎么查
用户只希望：
得到角色回复。
第二层：Controller/API层
对应项目：
backend/api/
文件：
chat.py
character.py
职责：
接收请求
例如：
用户：
POST /chat

{
 message:"今天好累"
}
Controller接收。
调用Service
Controller不负责：
判断角色
拼Prompt
调数据库
调LLM
它只负责：
接收
 ↓
转发
 ↓
返回
类似：
前台客服。
第三层：Service业务层
对应：
backend/services/
包括：
character.py

memory.py

personality.py
这是整个项目的业务核心。
3.1 character.py
职责：
管理角色信息。
例如：
读取：
character.json
里面：
{
"name":"星野",
"age":18,
"background":"..."
}
作用：
告诉系统：
“我要让哪个角色回复”
3.2 personality.py
职责：
生成角色人格 Prompt。
为什么需要它？
因为：
LLM本身没有人格。
GPT不知道：
“你是谁”
“你应该怎么说话”
所以需要：
System Prompt。
例如：
你现在扮演星野。

性格：
温柔
活泼

回复方式：
简短
亲近用户
这个文件负责生成类似内容。
3.3 memory.py
职责：
管理用户历史信息。
例如：
用户：
我喜欢猫
保存。
以后：
用户：
你记得我的喜好吗？
系统查询：
数据库:

user:
喜欢猫
然后加入Prompt。
第四层：Prompt Builder
虽然当前项目没有独立文件，
但是未来应该存在。
职责：
把所有信息组合。
输入：
character：
星野角色设定
personality：
温柔人格
memory：
用户喜欢猫
用户消息：
今天好累
组合：
System:

你是星野...
你性格...
用户喜欢猫...


User:

今天好累
形成完整LLM请求。
第五层：AI Layer
对应：
backend/core/ai.py
职责：
调用LLM。
例如：
Prompt Builder

↓

ai.py

↓

GPT API

↓

返回结果
重点：
ai.py不是负责思考。
它只是：
“负责连接模型”。
类似：
插座。
3. LLM是什么？
LLM：
Large Language Model
大型语言模型。
例如：
GPT
Claude
Gemini
Qwen
它本质：
一个非常强的文本生成模型。
它负责：
根据输入生成文本。
例如：
输入：
你是一个温柔的动漫角色
用户说：
今天好累
输出：
辛苦啦，要不要休息一下？
但是：
LLM不知道：
用户是谁
角色是谁
上一次聊天内容
所以需要：
外部系统提供。
4. 为什么需要这些模块？
问题1：
为什么memory不能放LLM里面？
答案：
因为LLM通常是外部服务。
例如：
GPT服务器。
它不会保存你的用户数据库。
所以：
memory
负责保存

LLM
负责生成
二者职责不同。
问题2：
为什么Prompt不能写死在ai.py？
错误：
ai.py:

prompt="你是星野"
调用GPT
问题：
换角色怎么办？
增加用户怎么办？
正确：
character.py
+
personality.py
+
memory.py

↓

Prompt Builder

↓

ai.py
这样：
角色可以动态变化。
问题3：
为什么API不能直接调用GPT？
错误：
用户

↓

API

↓

GPT
结果：
变成普通聊天机器人。
没有：
人格
记忆
角色
正确：
用户

↓

API

↓

Service

↓

Prompt

↓

AI Layer

↓

LLM
5. Controller-Service-Repository架构理解
这是企业后端常见架构。
Controller
负责：
接收请求。
比如：
用户发送消息
Service
负责：
业务逻辑。
例如：
聊天流程：
获取角色

获取人格

查询记忆

生成Prompt
Repository
负责：
数据访问。
例如：
数据库：
用户历史聊天

角色数据

配置文件
Service：
“不直接操作数据库”
而是：
调用Repository。
原因：
解耦。
6. 当前项目对应关系
Controller

↓

api/chat.py


Service

↓

services/


Repository

↓

未来新增


AI Layer

↓

core/ai.py


External Resource

↓

GPT/Claude/Gemini
数据库
文件系统
7. 一次完整请求流程
用户：
今天好累
流程：
Step 1
API收到：
message="今天好累"
↓
Step 2
Service处理
调用：
character.py
获取：
星野
调用：
personality.py
获取：
温柔人格
调用：
memory.py
获取：
用户喜欢猫
↓
Step 3
Prompt Builder
生成：
System:

你是星野...
用户喜欢猫...


User:

今天好累
↓
Step 4
ai.py
调用：
GPT API
↓
Step 5
GPT返回：
辛苦啦，要不要休息一下？
↓
API返回用户。