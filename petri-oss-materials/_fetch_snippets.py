#!/usr/bin/env python3
"""Fetch OSS core snippets into petri-oss-materials/ ONLY."""
from __future__ import annotations
import json, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = {"User-Agent": "Colony-Petri-Materials/1.0 (research)"}

# Curated: ≥11 projects per Petri, mix of README + real source files
ITEMS = [
  # ========== 01-agent (≥11) ==========
  ("NousResearch", "hermes-agent", "README.md", "01-agent", "DeepSeek 官方集成的自进化 agent"),
  ("NousResearch", "hermes-agent", "AGENTS.md", "01-agent", "Hermes agent 约定"),
  ("badlogic", "pi", "README.md", "01-agent", "pi 极简 coding agent harness"),
  ("steipete", "pi-mono", "README.md", "01-agent", "pi monorepo / 反框架"),
  ("OpenHands", "OpenHands", "README.md", "01-agent", "自主软件工程 agent"),
  ("OpenHands", "software-agent-sdk", "README.md", "01-agent", "OpenHands SDK"),
  ("langchain-ai", "langgraph", "README.md", "01-agent", "状态图/checkpoint agent 运行时"),
  ("huggingface", "smolagents", "README.md", "01-agent", "最小 tool-calling 环"),
  ("huggingface", "smolagents", "src/smolagents/agents.py", "01-agent", "agents.py 核心循环源码"),
  ("crewAIInc", "crewAI", "README.md", "01-agent", "角色制多 agent"),
  ("browser-use", "browser-use", "README.md", "01-agent", "浏览器自动化眼手"),
  ("pydantic", "pydantic-ai", "README.md", "01-agent", "类型安全 tool calling"),
  ("openai", "openai-agents-python", "README.md", "01-agent", "官方 Agents SDK / handoff"),
  ("browserbase", "stagehand", "README.md", "01-agent", "自愈式浏览器操作 SDK"),
  # ========== 02-ai-config (≥11) ==========
  ("BerriAI", "litellm", "README.md", "02-ai-config", "自托管万模网关(OpenRouter 魂镜像)"),
  ("OpenRouterTeam", "ai-sdk-provider", "README.md", "02-ai-config", "OpenRouter AI SDK provider"),
  ("songquanpeng", "one-api", "README.md", "02-ai-config", "API 中转聚合"),
  ("QuantumNous", "new-api", "README.md", "02-ai-config", "新一代 API 聚合"),
  ("Portkey-AI", "gateway", "README.md", "02-ai-config", "可观测 AI 网关"),
  ("vllm-project", "vllm", "README.md", "02-ai-config", "本地高吞吐推理"),
  ("ollama", "ollama", "README.md", "02-ai-config", "本地模型一键服务"),
  ("openai", "openai-node", "README.md", "02-ai-config", "OpenAI SDK 形状事实源"),
  ("anthropics", "anthropic-sdk-typescript", "README.md", "02-ai-config", "Anthropic Messages API 形状"),
  ("open-webui", "open-webui", "README.md", "02-ai-config", "多模型 WebUI/连接器"),
  ("Helicone", "helicone", "README.md", "02-ai-config", "LLM 可观测与代理"),
  ("lobehub", "lobe-chat", "README.md", "02-ai-config", "多供应商聊天前端+插件协议"),
  # ========== 03-bridge (≥11) ==========
  ("AliceLJY", "telegram-ai-bridge", "README.md", "03-bridge", "A2A-TG 信封+防环"),
  ("songsid", "AgEnD", "README.md", "03-bridge", "多 CLI 舰队 daemon"),
  ("diegofal", "aibot-framework", "README.md", "03-bridge", "A2A v0.3 + 多通道 bot"),
  ("a2aproject", "A2A", "README.md", "03-bridge", "A2A 官方协议"),
  ("modelcontextprotocol", "python-sdk", "README.md", "03-bridge", "MCP Python SDK"),
  ("modelcontextprotocol", "typescript-sdk", "README.md", "03-bridge", "MCP TypeScript SDK"),
  ("grammyjs", "grammY", "README.md", "03-bridge", "现代 Telegram bot 框架"),
  ("telegraf", "telegraf", "README.md", "03-bridge", "经典 Telegram bot"),
  ("matrix-org", "matrix-js-sdk", "README.md", "03-bridge", "Matrix 去中心 IM"),
  ("discordjs", "discord.js", "README.md", "03-bridge", "Discord 网关 bot"),
  ("team-attention", "agent-council", "README.md", "03-bridge", "多 agent 议会/协作"),
  ("yogirk", "agent-council", "README.md", "03-bridge", "多 agent council 变体"),
  # ========== 04-porter (≥11) ==========
  ("logseq", "logseq", "README.md", "04-porter", "双链 outliner PKM"),
  ("silverbulletmd", "silverbullet", "README.md", "04-porter", "浏览器端 markdown OS"),
  ("foambubble", "foam", "README.md", "04-porter", "VS Code 双链笔记"),
  ("TriliumNext", "Notes", "README.md", "04-porter", "层级知识库"),
  ("outline", "outline", "README.md", "04-porter", "团队知识库"),
  ("AppFlowy-IO", "AppFlowy", "README.md", "04-porter", "Notion 开源替代"),
  ("jsgrrchg", "NeverWrite", "README.md", "04-porter", "vault + agent 审阅"),
  ("usememos", "memos", "README.md", "04-porter", "轻量笔记流"),
  ("siyuan-note", "siyuan", "README.md", "04-porter", "块级笔记(思源)"),
  ("anyproto", "anytype-ts", "README.md", "04-porter", "对象型 PKM"),
  ("standardnotes", "app", "README.md", "04-porter", "加密本地笔记"),
  # ========== 05-ui-shell (≥11) ==========
  ("penpot", "penpot", "README.md", "05-ui-shell", "开源 Figma"),
  ("tldraw", "tldraw", "README.md", "05-ui-shell", "无限画布 SDK"),
  ("excalidraw", "excalidraw", "README.md", "05-ui-shell", "手绘白板"),
  ("GrapesJS", "grapesjs", "README.md", "05-ui-shell", "可视化页面构建"),
  ("prevwong", "craft.js", "README.md", "05-ui-shell", "可拖拽编辑器内核"),
  ("webstudio-is", "webstudio", "README.md", "05-ui-shell", "开源可视化建站"),
  ("radix-ui", "primitives", "README.md", "05-ui-shell", "无样式可访问原语"),
  ("shadcn-ui", "ui", "README.md", "05-ui-shell", "可复制组件系统"),
  ("BuilderIO", "mitosis", "README.md", "05-ui-shell", "跨框架组件"),
  ("clauderic", "dnd-kit", "README.md", "05-ui-shell", "拖拽交互原语"),
  ("facebook", "react", "README.md", "05-ui-shell", "组件模型事实源(对照)"),
  # ========== 06-code (≥11) ==========
  ("continuedev", "continue", "README.md", "06-code", "开源 AI IDE 助手"),
  ("Aider-AI", "aider", "README.md", "06-code", "git 感知编码 agent"),
  ("Aider-AI", "aider", "aider/repomap.py", "06-code", "repo map 源码"),
  ("Aider-AI", "aider", "aider/coders/base_coder.py", "06-code", "coder 基类"),
  ("TabbyML", "tabby", "README.md", "06-code", "自托管补全服务"),
  ("anomalyco", "opencode", "README.md", "06-code", "终端 AI 编程"),
  ("voideditor", "void", "README.md", "06-code", "开源 Cursor 向 IDE"),
  ("tree-sitter", "tree-sitter", "README.md", "06-code", "语法树精准定位"),
  ("jesseduffield", "lazygit", "README.md", "06-code", "git TUI"),
  ("microsoft", "monaco-editor", "README.md", "06-code", "浏览器代码编辑器"),
  ("coder", "code-server", "README.md", "06-code", "浏览器 VS Code"),
  ("gitui-org", "gitui", "README.md", "06-code", "Rust git TUI"),
  # ========== 07-workflow (≥11) ==========
  ("n8n-io", "n8n", "README.md", "07-workflow", "可视化自动化"),
  ("Comfy-Org", "ComfyUI", "README.md", "07-workflow", "节点图生成工作流"),
  ("Comfy-Org", "ComfyUI", "execution.py", "07-workflow", "节点执行引擎源码"),
  ("langflow-ai", "langflow", "README.md", "07-workflow", "LLM 可视化流"),
  ("FlowiseAI", "Flowise", "README.md", "07-workflow", "低代码 LLM 流"),
  ("windmill-labs", "windmill", "README.md", "07-workflow", "脚本工作流平台"),
  ("activepieces", "activepieces", "README.md", "07-workflow", "开源 Zapier"),
  ("node-red", "node-red", "README.md", "07-workflow", "事件流编程"),
  ("PrefectHQ", "prefect", "README.md", "07-workflow", "数据工作流"),
  ("huginn", "huginn", "README.md", "07-workflow", "自托管自动化 agent"),
  ("temporalio", "sdk-typescript", "README.md", "07-workflow", "持久工作流 SDK"),
  # ========== 08-plugin (≥11) ==========
  ("violentmonkey", "violentmonkey", "README.md", "08-plugin", "开源篡改猴"),
  ("violentmonkey", "violentmonkey", "src/injected/content/inject.js", "08-plugin", "内容脚本注入"),
  ("greasemonkey", "greasemonkey", "README.md", "08-plugin", "userscript 鼻祖"),
  ("scriptscat", "scriptcat", "README.md", "08-plugin", "脚本猫"),
  ("quoid", "userscripts", "README.md", "08-plugin", "Safari userscripts"),
  ("wxt-dev", "wxt", "README.md", "08-plugin", "现代浏览器扩展框架"),
  ("PlasmoHQ", "plasmo", "README.md", "08-plugin", "扩展 DX 框架"),
  ("crxjs", "chrome-extension-tools", "README.md", "08-plugin", "CRX Vite 工具"),
  ("mozilla", "web-ext", "README.md", "08-plugin", "Firefox 扩展工具"),
  ("GoogleChrome", "chrome-extensions-samples", "README.md", "08-plugin", "官方扩展样例"),
  ("lobehub", "lobe-chat-plugins", "README.md", "08-plugin", "聊天插件协议"),
]

def get_json(url: str):
  req = urllib.request.Request(url, headers=UA)
  with urllib.request.urlopen(req, timeout=45) as r:
    return json.loads(r.read().decode("utf-8", "replace"))

def get_bytes(url: str) -> bytes:
  req = urllib.request.Request(url, headers=UA)
  with urllib.request.urlopen(req, timeout=45) as r:
    return r.read()

def repo_meta(owner, repo):
  try:
    m = get_json(f"https://api.github.com/repos/{owner}/{repo}")
    return m.get("default_branch") or "main", m.get("stargazers_count"), m.get("description") or "", m.get("license", {}) or {}
  except Exception as e:
    return None, None, str(e), {}

def fetch_file(owner, repo, path, branch):
  raw = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
  try:
    return get_bytes(raw), raw
  except Exception:
    api = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    data = get_json(api)
    if isinstance(data, dict) and data.get("download_url"):
      return get_bytes(data["download_url"]), data["download_url"]
    raise

def truncate(b: bytes, limit=100_000) -> bytes:
  if len(b) <= limit:
    return b
  return b[:limit] + f"\n\n/* TRUNCATED: kept {limit}/{len(b)} bytes */\n".encode()

def safe_name(owner, repo, path):
  return f"{owner}__{repo}__{path.replace('/', '__')}"

def main():
  catalog = []
  ok = fail = 0
  for owner, repo, path, folder, note in ITEMS:
    branch, stars, desc, lic = repo_meta(owner, repo)
    time.sleep(0.12)
    snip_dir = ROOT / folder / "snippets"
    snip_dir.mkdir(parents=True, exist_ok=True)
    fname = safe_name(owner, repo, path)
    # keep extension
    ext = Path(path).suffix or ".txt"
    dest = snip_dir / (fname if fname.endswith(ext) else fname + ext)
    status, err, url, size = "ok", "", "", 0
    if not branch:
      status, err = "repo-miss", desc
      fail += 1
      dest.write_text(f"# FETCH FAILED\n\nrepo miss: {owner}/{repo}\n{err}\n", encoding="utf-8")
    else:
      try:
        data, url = fetch_file(owner, repo, path, branch)
        data = truncate(data)
        if dest.suffix in {".py", ".js", ".ts", ".tsx", ".cljs"}:
          header = (
            f"/* MATERIAL source=https://github.com/{owner}/{repo}/blob/{branch}/{path}\n"
            f" * stars={stars} note={note}\n"
            f" * Colony petri-oss-materials research snapshot; upstream license applies\n"
            f" */\n\n"
          ).encode()
        else:
          header = (
            f"<!-- MATERIAL source=https://github.com/{owner}/{repo}/blob/{branch}/{path} "
            f"stars={stars} note={note} -->\n\n"
          ).encode()
        dest.write_bytes(header + data)
        size = dest.stat().st_size
        ok += 1
      except Exception as e:
        status, err = "fetch-fail", str(e)
        fail += 1
        dest.write_text(f"# FETCH FAILED\n\n{owner}/{repo}/{path}\n{err}\nnote: {note}\n", encoding="utf-8")
    lic_name = (lic or {}).get("spdx_id") or (lic or {}).get("name") or "?"
    catalog.append({
      "folder": folder, "owner": owner, "repo": repo, "path": path, "note": note,
      "stars": stars, "branch": branch, "license": lic_name, "desc": desc if status != "repo-miss" else "",
      "status": status, "error": err, "bytes": size, "file": str(dest.relative_to(ROOT)),
      "html_url": f"https://github.com/{owner}/{repo}",
    })
    print(f"[{status}] {folder} {owner}/{repo} ★{stars} -> {dest.name}")

  (ROOT / "_fetch_catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
  print(f"DONE ok={ok} fail={fail}")

if __name__ == "__main__":
  main()
