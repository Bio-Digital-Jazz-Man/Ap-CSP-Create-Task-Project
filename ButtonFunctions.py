"""Screen management helpers for the calculator app."""
from __future__ import annotations

import tkinter as tk
from typing import Dict, List


class ScreenManager:
    """Handles navigation between the keypad and expressions history screens."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.main_frame = tk.Frame(root)
        self.extra_frame = tk.Frame(root)
        self._history: List[str] = []
        self._history_listbox = None
        self._build_extra_frame()

    def show_main(self) -> None:
        self.extra_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def show_extra(self) -> None:
        self.main_frame.pack_forget()
        self.extra_frame.pack(fill="both", expand=True)

    def add_history_entry(self, entry: str) -> None:
        self._history.insert(0, entry)
        if self._history_listbox is not None:
            self._history_listbox.delete(0, tk.END)
            for item in self._history:
                self._history_listbox.insert(tk.END, item)

    def apply_theme(self, theme: Dict[str, str]) -> None:
        bg = theme.get("frame-background", "#ffffff")
        fg = theme.get("display-text-color", "#000000")
        font = (
            theme.get("display-text-font", "Helvetica"),
            theme.get("display-text-size", 16),
        )
        self.main_frame.configure(bg=bg)
        self.extra_frame.configure(bg=bg)
        if self._history_listbox is not None:
            self._history_listbox.configure(bg=theme.get("display-background", bg), fg=fg, font=font)
        if hasattr(self, "_extra_label"):
            self._extra_label.configure(bg=bg, fg=fg, font=font)
        if hasattr(self, "_back_button"):
            self._back_button.configure(font=font)

    def _build_extra_frame(self) -> None:
        self._extra_label = tk.Label(self.extra_frame, text="Saved expressions")
        self._extra_label.pack(pady=12)

        self._history_listbox = tk.Listbox(self.extra_frame, width=40, height=10)
        self._history_listbox.pack(fill="both", expand=True, padx=20, pady=10)

        self._back_button = tk.Button(self.extra_frame, text="Back to calculator", command=self.show_main)
        self._back_button.pack(pady=12)
