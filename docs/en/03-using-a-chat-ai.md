# 03 Let a Chat AI Walk You Through It

Suits: you only have a phone, no computer.
How it works: a chat AI cannot operate your phone; it reads the checklist and tells you step by step where to tap. You reply when you have tapped, or send it a screenshot.

## Three steps to start

1. Open any one of DeepSeek, Doubao, or ChatGPT. DeepSeek needs "Web search" turned on; Doubao and ChatGPT can read links by default.
2. Copy the whole boxed text from [prompts/聊天AI提示词.md](../../prompts/聊天AI提示词.md) and send it to the AI.
3. Answer the AI's questions: brand, model, and system version.

Find the model and system version here:

| Brand | Path |
|---|---|
| OPPO / OnePlus / realme | Settings → About phone |
| Xiaomi / Redmi | Settings → My device |
| vivo / iQOO | Settings → System management & upgrade → Version info |
| Honor / Huawei | Settings → About phone |

## What the conversation looks like

```text
AI: What brand and model is your phone? What system version is it on?
You: OPPO Find N6, ColorOS 16
AI: Step 1: Open "Settings" → "Privacy" → "Device identifiers & ads" → "Ad tracking".
    On this page each app has a switch; turn them all off. Reply "Done" when finished.
You: Done
AI: Step 2: Swipe right from the left edge of the home screen to open the minus-one screen…
```

## If the AI cannot read the link

1. Open [docs/checklists/](checklists/), find your brand.
2. Open the checklist file, select all, and copy it.
3. Paste it to the AI and say "Follow this checklist and walk me through it."

## Compared with method 1

| | Method 1: AI agent | Method 2: Chat AI |
|---|---|---|
| Needs a computer | Yes | No |
| Who taps the screen | The script | You |
| Time taken | 4 to 6 minutes (with a model recipe) | 30 to 60 minutes |
| Can suspend ad packages | Yes | No (needs adb) |
| Can turn off marketing notifications in bulk | Yes | No, one by one |
