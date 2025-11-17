"""Theme management utilities for the calculator application."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Dict, List

_DEFAULT_THEME = {
    "button-background": "#d3d3d3",
    "button-forground": "#000000",
    "frame-background": "#ffffff",
    "button-text-font": "Helvetica",
    "button-text-size": 20,
    "button-text-color": "#000000",
    "display-text-size": 32,
    "display-text-font": "Helvetica",
    "display-text-color": "#000000",
    "display-background": "#ffffff",
}


class ThemeManager:
    """Loads themes from disk and notifies subscribers when they change."""

    def __init__(self, root, config_path: Path | str):
        self._root = root
        self._config_path = Path(config_path)
        self._themes: Dict[str, Dict[str, str]] = {"default": dict(_DEFAULT_THEME)}
        self._subscribers: List[Callable[[Dict[str, str]], None]] = []
        self._current_theme = "default"
        self._load_from_disk()

    @property
    def names(self) -> List[str]:
        return list(self._themes.keys())

    @property
    def current_theme(self) -> str:
        return self._current_theme

    def register(self, callback: Callable[[Dict[str, str]], None]) -> None:
        self._subscribers.append(callback)

    def apply(self, name: str) -> None:
        theme = self._themes.get(name, self._themes["default"])
        self._current_theme = name if name in self._themes else "default"
        self._root.configure(bg=theme.get("frame-background", _DEFAULT_THEME["frame-background"]))
        for callback in self._subscribers:
            callback(theme)

    def _load_from_disk(self) -> None:
        if not self._config_path.exists():
            return
        try:
            with self._config_path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError):
            return
        if not isinstance(data, dict):
            return
        for name, theme in data.items():
            if isinstance(theme, dict):
                merged = dict(_DEFAULT_THEME)
                merged.update(theme)
                self._themes[name] = merged
