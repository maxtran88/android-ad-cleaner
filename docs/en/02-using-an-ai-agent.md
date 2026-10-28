# 02 Let an AI Agent Run It for You

Suits: you have a computer and want to hand the whole job to an AI.
Prerequisite: Developer mode and USB debugging are turned on on the phone ([screenshot tutorial](00-enabling-developer-mode.md)), connected to the computer with a data cable. Even if adb and Python are not installed, the AI will install them for you.

## Which tools can be used

Choose an AI tool **that can run commands on your computer**. A web chat window cannot run commands; for that case, see [03-using-a-chat-ai](03-using-a-chat-ai.md).

| Tool | Maker | Can run commands | Notes |
|---|---|---|---|
| WorkBuddy | Tencent | ✅ | Desktop version; let it work in the local working directory |
| Claude Code | Anthropic | ✅ | Runs in a terminal, reads `CLAUDE.md` |
| Codex | OpenAI | ✅ | Terminal or desktop version, reads `AGENTS.md` |
| Trae | ByteDance | ✅ | Use Builder / SOLO mode |
| Cursor | Anysphere | ✅ | Use Agent mode |
| DeepSeek / Doubao / ChatGPT web version | — | ❌ | Use [03-using-a-chat-ai](03-using-a-chat-ai.md) |

## How to start

Send the AI this message:

```text
Please clone https://github.com/rddmwmddr/android-ad-cleaner , read the AGENTS.md in the repo,
then help me remove ads from the phone connected to this computer. Before each change, tell me what you are about to change.
```

The AI will then do these things in order:

1. Clone the repo and read `AGENTS.md`.
2. Check adb and Python, and install anything that is missing.
3. Run `run.py devices` and tell you which phone was recognized and whether a ready-made model recipe exists.
4. Save a snapshot of the state before changes.
5. Run the model recipe, or turn things off page by page following the checklist.
6. List the marketing notification channels, show you the list, and turn them off after you approve.
7. Detect Quick Apps and ask whether you want to suspend ad packages and turn off Quick Apps.
8. Finish up and report what was turned off and what was not.
9. Remind you to turn off Developer mode. If you say "turn it off for me", the AI will turn it off from the computer, and the connection will drop.

## Things the AI will ask you

| AI asks | How you answer |
|---|---|
| Phone is locked, please unlock it | Unlock the phone and keep the screen on |
| Multiple devices recognized, which one to handle | Say the model or serial number |
| Should these marketing notification channels be turned off | Look at the list and speak up about anything you want to keep |
| Should these ad packages be suspended | You decide. Suspension can be restored |
| Should the browser home page be switched to the simple version | You decide |

## While it runs

- Keep the phone's screen on, unlocked, and plugged in.
- Do not touch the phone. The script is tapping the screen; if you touch it, things go wrong.
- For models with a model recipe, the whole run takes 4 to 6 minutes. For models without one, the AI has to search page by page, so it takes longer.

## After it finishes

1. Open pull-down search, the minus-one screen, the app store, and the browser, and confirm they work normally.
2. Ask the AI to save this run's paths as a model recipe, so the same model takes only a few minutes next time.
3. If you are willing to share, submit the model recipe as a PR; see [04-writing-a-recipe-for-a-new-model](04-writing-a-recipe-for-a-new-model.md).

## Useful follow-up commands

```text
Only run the Browser and Themes sections.
Save this phone's paths as a model recipe.
Restore all suspended packages.
List the marketing notifications still on for this phone.
```