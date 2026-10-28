"""CLI language support (Chinese / English / Vietnamese).

Locale files live at the repo root: ``locales/{lang}.json`` with flat
dotted keys (``cli.devices.header``). Chinese (``zh``) is the default and
the fallback for any missing key. This module never deletes or replaces
the Chinese originals: every ``t()`` call site passes the original Chinese
text as ``default=``, so before the staged keys are merged into
``locales/`` the output stays exactly as it was.

Language selection, in priority order:
  1. ``--lang zh|en|vi`` on the command line (handled by
     :func:`extract_lang_args`, which also strips it from argv so existing
     commands keep working unchanged),
  2. the ``AAC_LANG`` environment variable,
  3. the ``LANG``/``LANGUAGE`` environment variable (``en_US.UTF-8``,
     ``vi_VN``, ``zh_CN`` ... -- only the language prefix is used),
  4. ``zh``.

Phone-screen matching strings are NEVER routed through this module: the
phone UI is Chinese, so strings used to find or match on-screen text must
stay exactly as they are. Only strings printed or shown to the user go
through :func:`t`.
"""
import json
import os

SUPPORTED = ("zh", "en", "vi")
_LOCALES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "locales")

_cache = {}
_lang = "zh"


def _normalize(value):
    """'en_US.UTF-8' -> 'en', 'vi' -> 'vi', anything else unsupported -> 'zh'."""
    if not value:
        return None
    prefix = value.strip().lower().replace("-", "_").split("_")[0].split(".")[0]
    return prefix if prefix in SUPPORTED else None


def resolve_lang(explicit=None):
    """Best language without changing global state."""
    for candidate in (explicit, os.environ.get("AAC_LANG"), os.environ.get("LANG"),
                      os.environ.get("LANGUAGE")):
        lang = _normalize(candidate)
        if lang:
            return lang
    return "zh"


def set_lang(lang):
    """Set the current language (falls back to zh) and export it so that
    child processes (run.py shells out to fast.py / chan_fast.py) inherit it."""
    global _lang
    _lang = _normalize(lang) or "zh"
    os.environ["AAC_LANG"] = _lang
    return _lang


def current_lang():
    return _lang


def extract_lang_args(argv):
    """Pull ``--lang <lang>`` / ``--lang=<lang>`` out of argv.

    Returns ``(lang_or_None, cleaned_argv)``. Unknown values fall back to
    zh via :func:`set_lang`. Callers must use the cleaned argv afterwards.
    """
    cleaned, lang = [], None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--lang" and i + 1 < len(argv):
            lang = argv[i + 1]
            i += 2
        elif arg.startswith("--lang="):
            lang = arg.split("=", 1)[1]
            i += 1
        else:
            cleaned.append(arg)
            i += 1
    if lang is not None:
        set_lang(lang)
    return lang, cleaned


def _load(lang):
    if lang not in _cache:
        data = {}
        try:
            with open(os.path.join(_LOCALES_DIR, lang + ".json"), encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            data = {}
        _cache[lang] = data
    return _cache[lang]


def _lookup(data, key):
    if key in data:
        return data[key]
    node = data
    for part in key.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node if isinstance(node, str) else None


def t(key, default=None, lang=None, **kwargs):
    """Translate ``key``; fall back to the zh locale, then to ``default``
    (call sites always pass the original Chinese text), then to ``key``."""
    use = lang or _lang
    text = _lookup(_load(use), key)
    if text is None and use != "zh":
        text = _lookup(_load("zh"), key)
    if text is None:
        text = default if default is not None else key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError, ValueError):
            pass
    return text


# Environment language applies from import time, so module-level errors
# (e.g. run.py's adb check) already respect AAC_LANG / LANG. An explicit
# --lang flag, handled in main(), overrides this afterwards.
_lang = resolve_lang()
