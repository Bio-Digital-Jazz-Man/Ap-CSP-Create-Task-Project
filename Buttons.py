"""Keypad UI encapsulation for the calculator."""
from __future__ import annotations

import tkinter as tk
from typing import Callable, Dict, List


class ButtonPanel:
    """Encapsulates the calculator keypad."""

    def __init__(
        self,
        parent: tk.Frame,
        display_var: tk.StringVar,
        theme_manager,
        show_expressions: Callable[[], None],
        record_history: Callable[[str], None],
    ) -> None:
        self.parent = parent
        self.display_var = display_var
        self._theme_manager = theme_manager
        self._show_expressions = show_expressions
        self._record_history = record_history
        self._buttons: List[tk.Button] = []
        self._build_buttons()
        self._theme_manager.register(self.apply_theme)

    def _build_buttons(self) -> None:
        keypad = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("÷", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("×", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
        ]

        for label, row, column in keypad:
            command = self._build_command(label)
            button = tk.Button(self.parent, text=label, command=command)
            button.grid(row=row, column=column, sticky="nsew", padx=4, pady=4)
            self._buttons.append(button)

        clear_button = tk.Button(self.parent, text="AC", command=self._clear)
        clear_button.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
        self._buttons.append(clear_button)

        expr_button = tk.Button(self.parent, text="Expressions", command=self._show_expressions)
        expr_button.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=4, pady=4)
        self._buttons.append(expr_button)

    def _build_command(self, label: str) -> Callable[[], None]:
        if label == "=":
            return self._evaluate
        return lambda s=label: self._append(s)

    def _append(self, char: str) -> None:
        current = self.display_var.get()
        if current == "0" or current == "Error":
            self.display_var.set(char)
        else:
            self.display_var.set(current + char)

    def _clear(self) -> None:
        self.display_var.set("0")

    def _evaluate(self) -> None:
        raw_expression = self.display_var.get()
        expression = raw_expression.replace("×", "*").replace("÷", "/")
        try:
            result = str(eval(expression, {"__builtins__": {}}, {}))
        except Exception:
            self.display_var.set("Error")
            return
        self._record_history(f"{raw_expression} = {result}")
        self.display_var.set(result)

    def apply_theme(self, theme: Dict[str, str]) -> None:
        font = (theme.get("button-text-font", "Helvetica"), theme.get("button-text-size", 20))
        foreground = theme.get("button-text-color", "#000000")
        background = theme.get("button-background", "#d3d3d3")
        for button in self._buttons:
            button.configure(font=font, fg=foreground, bg=background, activebackground=background)
