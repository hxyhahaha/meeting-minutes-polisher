# Meeting Minutes Polisher

`Meeting Minutes Polisher`是一个面向会议语音转文字场景的Codex workflow/skill，用于把用户连续输入的多段原始转写整理成完整、书面、结构化的中文会议纪要，并在末尾生成简洁清晰的要点总结，同时导出Word文件。

它适合以下场景：

- 上市公司路演、反路演、专家访谈、业绩交流会、电话会
- 用户手动粘贴的多段音频转文字内容
- 需要尽量还原现场表达逻辑，而不是做大幅删减式摘要
- 需要最终交付成可直接使用的会议纪要和`.docx`文件

## 这个项目是什么

这个项目是一个workflow/skill定义，不是独立的AI应用，也不自带模型服务。

它主要包含三部分：

- 纪要整理规则：定义如何保留信息、修正文法、标注Q&A、生成小标题、避免乱改术语
- 风格规范：约束格式、数据处理、专有名词校对、自检要求
- Word导出脚本：把最终纪要与要点总结导出为`.docx`
- 可选API运行脚本：在不使用Codex时，通过使用者自己的API key调用兼容接口

## 这个项目不包含什么

本项目：

- 不包含任何OpenAI API key
- 不包含任何其他模型厂商的密钥
- 不提供模型额度
- 不直接托管AI推理能力

如果你从GitHub下载本项目，你拿到的是workflow本身，而不是一个自带AI调用权限的成品服务。

## API与隐私说明

为了避免暴露作者的API或账户能力，本仓库不会提供任何私有密钥、令牌或账号凭据。

使用者需要自行准备可用的AI运行环境，例如：

- 支持skills的Codex环境
- 自己接入的OpenAI API或其他模型API
- 自己实现的兼容工作流运行方式

请不要把下面这些内容提交到GitHub：

- `.env`
- `*.pem`
- `*.key`
- 平台账号密钥
- 本地导出的私有会议纪要原文
- 任何带客户、专家、公司敏感信息的源转写

## 核心能力

这个workflow默认要求：

- 用户输入公司名称
- 用户连续输入一段或多段会议转写文本
- AI在用户明确表示“开始整理”之前先持续接收，不提前输出
- 最终生成完整会议纪要、要点总结和Word文件

整理时的核心约束包括：

- 不擅自删减内容
- 不遗漏重要逻辑、数字、时间、规模、条件和结论
- 不擅自错误修改品牌名、产品名、项目名和专业名词
- 不出现莫名其妙的空格
- 数字之间不要有逗号，例如使用`1000000`而不是`1,000,000`
- 去掉发言人标识
- 当话题切换时补充小标题
- 当出现Q&A时，在每组问答前总结主题，并分别加上`Q：`和`A：`

## 输出结果

默认输出包括三部分：

1. 完整会议纪要
2. 几大点涵盖几小点的要点总结
3. `.docx`文件

Word文件默认命名为：

`{公司名称}会议纪要.docx`

## 目录结构

```text
skills/meeting-minutes-polisher/
├── SKILL.md
├── agents/openai.yaml
├── references/style-guide.md
└── scripts/
    ├── export_minutes_to_docx.py
    └── run_with_openai_responses.py
```

## 使用方式

### 方式一：在Codex环境中作为skill使用

这适用于已经在Codex中安装了skill的情况。仓库本身不提供模型额度，实际推理能力由Codex环境提供。

具体步骤：

1. 把`skills/meeting-minutes-polisher/`安装到你的Codex skills目录。
2. 重启Codex，让skill被重新加载。
3. 在新对话里直接调用`$meeting-minutes-polisher`。

示例：

```text
请使用$meeting-minutes-polisher处理下面这份会议转写。
公司名称：某某公司
先收着，后面我还会继续贴。
```

然后持续粘贴多段转写内容。

如果还没贴完，可以继续发送：

```text
继续
```

或者：

```text
还有下一段，先不要整理。
```

等全部内容输入完毕后，再发送：

```text
可以了，开始整理并生成Word文件。
```

Codex模式下的特点：

- 适合持续多轮输入
- 不需要你在仓库里保存任何API key
- 使用的是你自己的Codex运行环境

### 方式二：使用者自备API key运行

这适用于不在Codex里运行、但希望复用这套workflow规则的情况。

仓库中提供了一个示例脚本：

`skills/meeting-minutes-polisher/scripts/run_with_openai_responses.py`

它会：

- 读取本workflow的`SKILL.md`和`style-guide.md`
- 读取你提供的会议转写文本
- 调用兼容的Responses API
- 输出完整纪要
- 可选保存`.txt`和`.docx`

#### 第一步：准备你自己的API key

不要把真实key写进仓库。建议只在本地环境变量中设置。

可以参考仓库里的`.env.example`，但不要把真实`.env`提交到GitHub。

macOS或Linux示例：

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_MODEL="gpt-5"
export OPENAI_BASE_URL="https://api.openai.com/v1"
```

#### 第二步：准备会议转写文本

把转写保存为本地文本文件，例如：

`transcript.txt`

#### 第三步：运行脚本

```bash
python3 skills/meeting-minutes-polisher/scripts/run_with_openai_responses.py \
  --company "某某公司" \
  --transcript transcript.txt \
  --output-text outputs/某某公司会议纪要.txt \
  --output-docx outputs/某某公司会议纪要.docx
```

如果只想在终端看到结果，不保存文件，也可以只传`--company`和`--transcript`。

#### 这类API运行方式的特点

- 必须由使用者自己提供API key
- 仓库不会包含作者的任何key
- 可以接入OpenAI API，也可以接入兼容的base URL
- 多段转写需要使用者先自行合并为一个文本文件，或者自行扩展脚本

### 方式三：迁移为其他平台的工作流

如果你不使用Codex，也可以把这套规则迁移到：

- 自己的Prompt工程
- 内部知识助手
- 网页工具
- 桌面应用
- 其他支持大模型调用的自动化系统

但迁移后，模型调用、会话记忆、多段输入拼接与文件导出能力都需要你自己提供。

## 发布到GitHub时只上传workflow

如果你准备公开仓库，建议只上传下面这些文件：

- `README.md`
- `.gitignore`
- `.env.example`
- `skills/meeting-minutes-polisher/SKILL.md`
- `skills/meeting-minutes-polisher/agents/openai.yaml`
- `skills/meeting-minutes-polisher/references/style-guide.md`
- `skills/meeting-minutes-polisher/scripts/export_minutes_to_docx.py`
- `skills/meeting-minutes-polisher/scripts/run_with_openai_responses.py`

建议的Git命令思路也是只添加这些workflow文件，而不是直接上传整个工作目录。

## 自检机制

本workflow要求AI在交付前主动检查：

- 是否整合了用户发送的全部片段
- 是否有任何重要信息被遗漏
- 是否为了简洁而擅自删除内容
- 是否错误改写了专有名词或专业术语
- 是否误改了数字、日期、比例、产能、金额等数据
- 是否出现了多余空格
- 是否把数字写成带逗号的格式

如果某个专有名词无法确认，默认要求使用更保守的写法，而不是强行“纠正”成一个可能错误的词。

## 适合公开仓库，但不适合公开的数据

适合公开：

- workflow规则
- 格式规范
- Word导出脚本
- 示例提示词

不建议公开：

- 客户会议原文
- 专家访谈实录
- 内部会议纪要
- 带公司敏感信息的完整转写
- 任何私有API配置
- 你自己已经写过的任何公司会议纪要、整理稿、Word成品、PDF原文或提取文本
- 任何真实API key或带真实key的环境变量文件

## 许可证与使用建议

如果你准备公开发布，建议你自行补充许可证，并在仓库首页说明：

- 该项目提供的是workflow设计，不提供模型访问权限
- 使用者需自行准备合规的数据来源与模型环境
- 使用者应自行承担会议原文上传、处理和分享时的合规责任

## 备注

如果你准备把这个项目正式发布到GitHub，建议至少保留以下文件：

- `README.md`
- `skills/meeting-minutes-polisher/SKILL.md`
- `skills/meeting-minutes-polisher/references/style-guide.md`
- `skills/meeting-minutes-polisher/scripts/export_minutes_to_docx.py`

公开上传时，建议只上传workflow本身，不上传任何真实公司材料。当前项目中的公司会议纪要、整理稿、转写文本、PDF和Word成品都不应进入公开仓库。

## 相关说明

关于OpenAI API接入，这个仓库遵循两个基本原则：

- API key必须由使用者自己提供，不会由仓库提供
- API key应通过环境变量加载，而不是写入代码或提交到GitHub

这与OpenAI官方文档的建议一致：API key应作为密钥保存，并通过环境变量提供给应用；官方Quickstart也展示了通过`OPENAI_API_KEY`环境变量使用API的方式。[OpenAI Quickstart](https://platform.openai.com/docs/quickstart/make-your-first-api-request) 同时，OpenAI API参考文档明确说明API使用Bearer方式认证，且不应暴露在客户端代码中。[OpenAI API Reference](https://platform.openai.com/docs/api-reference/backward-compatibility?lang=ruby)

本仓库提供的`run_with_openai_responses.py`示例脚本默认通过`Authorization: Bearer ...`发送请求，并把`store`设置为`false`，以减少不必要的响应存储。这一点是基于OpenAI关于`/v1/responses`数据控制说明做出的保守设置。[Data controls](https://platform.openai.com/docs/models/default-usage-policies-by-endpoint)
