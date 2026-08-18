# Anime AI Companion · 星野

一个可本地运行的 AI 动漫陪伴项目：角色人格、短期聊天上下文、长期记忆与用户资料会在一次完整的聊天流程中协作。项目采用 FastAPI、SQLite 和原生响应式网页，适合用于展示 Python 后端、LLM 工程化和产品落地能力。

## 已实现

- 角色配置：`prompts/character.json` 可独立修改角色名称、性格与说话风格。
- 对话闭环：网页输入 → FastAPI → Prompt 组装 → DeepSeek → 网页展示。
- 双层记忆：最近 20 条消息作为短期上下文；用户表达的名称、喜好与重要句子会进入长期记忆。
- 用户隔离：请求携带 `user_id`，不同用户的聊天历史、资料和长期记忆互不混用。
- 可维护性：启动时兼容升级已有 SQLite 数据库；LLM 配置/网络异常以 503 明确返回；接口带有 Pydantic 校验与测试覆盖。

## 本地启动

在项目根目录执行（PowerShell）：

```powershell
Copy-Item .env.example .env
# 编辑 .env，填入自己的 DEEPSEEK_API_KEY
.\venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
$env:PYTHONPATH = "backend"
uvicorn main:app --app-dir backend --reload
```

打开 [http://127.0.0.1:8000](http://127.0.0.1:8000) 即可聊天；接口文档在 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)。

> `.env` 中的密钥不会被提交。可通过 `DEEPSEEK_MODEL`、`DEEPSEEK_BASE_URL` 和 `LLM_TIMEOUT_SECONDS` 调整模型、兼容端点和超时。

## API

`POST /chat/`

```json
{
  "user_id": 1,
  "message": "我叫小明，我喜欢看动漫"
}
```

成功返回：

```json
{
  "user_id": 1,
  "user": "我叫小明，我喜欢看动漫",
  "character": "星野",
  "reply": "……"
}
```

## 测试

```powershell
cd backend
$env:PYTHONPATH = "."
pytest -q
```

## 项目结构

```text
backend/
  api/          # HTTP 路由与输入输出契约
  core/         # 配置、依赖注入与 LLM 客户端
  services/     # 聊天编排、人格、Prompt、记忆
  models/       # SQLAlchemy 数据模型
  database/     # SQLite 初始化与兼容升级
frontend/       # 原生 HTML/CSS/JS 聊天页面
prompts/        # 可配置角色卡
data/           # 本地 SQLite 数据库（开发环境的本地状态）
```

## 设计说明

聊天请求在生成回答前先保存用户输入，并提取稳定资料与长期记忆；模型返回后再保存角色回复。这样即使重新启动服务，历史和资料仍能保留。原始对话文本与密钥均存于本机，部署到公网前应补充身份认证、速率限制和数据库备份策略。
