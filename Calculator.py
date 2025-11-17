"""Main entry point for the Tkinter calculator."""
from __future__ import annotations

import tkinter as tk
from pathlib import Path

from ButtonFunctions import ScreenManager
from Buttons import ButtonPanel
from theme_manager import ThemeManager


class CalculatorApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.screen_manager = ScreenManager(self.root)
        self._configure_main_grid()

        self.display_var = tk.StringVar(value="0")
        self.display_entry = tk.Entry(
            self.screen_manager.main_frame,
            textvariable=self.display_var,
            justify="right",
            relief="flat",
        )
        self.display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

        self.theme_manager = ThemeManager(self.root, Path(__file__).with_name("themes.json"))
        self.theme_manager.register(self._apply_theme_to_display)
        self.theme_manager.register(self.screen_manager.apply_theme)

        self.button_panel = ButtonPanel(
            parent=self.screen_manager.main_frame,
            display_var=self.display_var,
            theme_manager=self.theme_manager,
            show_expressions=self.screen_manager.show_extra,
            record_history=self.screen_manager.add_history_entry,
        )

        self._theme_choice = tk.StringVar(value=self.theme_manager.current_theme)
        self._build_menu()

        self.theme_manager.apply(self.theme_manager.current_theme)
        self.screen_manager.show_main()

    def _configure_main_grid(self) -> None:
        for row in range(6):
            self.screen_manager.main_frame.rowconfigure(row, weight=1)
        for column in range(4):
            self.screen_manager.main_frame.columnconfigure(column, weight=1)

    def _apply_theme_to_display(self, theme) -> None:
        font = (theme.get("display-text-font", "Helvetica"), theme.get("display-text-size", 32))
        self.display_entry.configure(
            font=font,
            fg=theme.get("display-text-color", "#000000"),
            bg=theme.get("display-background", "#ffffff"),
            insertbackground=theme.get("display-text-color", "#000000"),
        )

    def _build_menu(self) -> None:
        menubar = tk.Menu(self.root)
        view_menu = tk.Menu(menubar, tearoff=False)
        view_menu.add_command(label="Calculator", command=self.screen_manager.show_main)
        view_menu.add_command(label="Expressions", command=self.screen_manager.show_extra)

        theme_menu = tk.Menu(view_menu, tearoff=False)
        for name in self.theme_manager.names:
            theme_menu.add_radiobutton(
                label=name.title(),
                value=name,
                variable=self._theme_choice,
                command=lambda n=name: self.theme_manager.apply(n),
            )
        view_menu.add_cascade(label="Theme", menu=theme_menu)
        menubar.add_cascade(label="View", menu=view_menu)
        self.root.config(menu=menubar)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    CalculatorApp().run()
