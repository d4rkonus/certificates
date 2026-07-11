#!/usr/bin/env python3
"""Simple desktop countdown timer app."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox


class CountdownApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Contador hacia atras")
        self.root.resizable(False, False)
        self.remaining_seconds = 0
        self.running = False
        self.timer_job: str | None = None

        self.minutes_var = tk.StringVar(value="5")
        self.seconds_var = tk.StringVar(value="0")
        self.status_var = tk.StringVar(value="Listo")

        self._build_ui()
        self._update_display(0)

    def _build_ui(self) -> None:
        container = tk.Frame(self.root, padx=16, pady=16)
        container.grid(row=0, column=0)

        tk.Label(container, text="Minutos:").grid(row=0, column=0, sticky="e")
        tk.Entry(container, width=6, textvariable=self.minutes_var).grid(
            row=0, column=1, padx=(6, 12), sticky="w"
        )

        tk.Label(container, text="Segundos:").grid(row=0, column=2, sticky="e")
        tk.Entry(container, width=6, textvariable=self.seconds_var).grid(
            row=0, column=3, padx=(6, 0), sticky="w"
        )

        self.display_label = tk.Label(
            container,
            text="00:00",
            font=("Helvetica", 34, "bold"),
            pady=16,
            width=8,
        )
        self.display_label.grid(row=1, column=0, columnspan=4)

        button_row = tk.Frame(container)
        button_row.grid(row=2, column=0, columnspan=4, pady=(4, 8))

        tk.Button(button_row, text="Iniciar", width=10, command=self.start).grid(
            row=0, column=0, padx=4
        )
        tk.Button(button_row, text="Pausar", width=10, command=self.pause).grid(
            row=0, column=1, padx=4
        )
        tk.Button(button_row, text="Reiniciar", width=10, command=self.reset).grid(
            row=0, column=2, padx=4
        )

        tk.Label(container, textvariable=self.status_var, fg="#444").grid(
            row=3, column=0, columnspan=4
        )

    def _update_display(self, seconds: int) -> None:
        minutes = seconds // 60
        secs = seconds % 60
        self.display_label.config(text=f"{minutes:02d}:{secs:02d}")

    def _get_input_seconds(self) -> int | None:
        try:
            minutes = int(self.minutes_var.get())
            seconds = int(self.seconds_var.get())
        except ValueError:
            messagebox.showerror("Entrada invalida", "Usa numeros enteros.")
            return None

        if minutes < 0 or seconds < 0 or seconds > 59:
            messagebox.showerror(
                "Entrada invalida",
                "Minutos debe ser >= 0 y segundos entre 0 y 59.",
            )
            return None

        total = minutes * 60 + seconds
        if total <= 0:
            messagebox.showerror(
                "Entrada invalida",
                "La cuenta regresiva debe ser mayor que cero.",
            )
            return None
        return total

    def start(self) -> None:
        if self.running:
            return

        if self.remaining_seconds <= 0:
            initial = self._get_input_seconds()
            if initial is None:
                return
            self.remaining_seconds = initial

        self.running = True
        self.status_var.set("Contando...")
        self._tick()

    def pause(self) -> None:
        self.running = False
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.status_var.set("Pausado")

    def reset(self) -> None:
        self.pause()
        self.remaining_seconds = 0
        self._update_display(0)
        self.status_var.set("Listo")

    def _tick(self) -> None:
        self._update_display(self.remaining_seconds)

        if not self.running:
            return
        if self.remaining_seconds <= 0:
            self.running = False
            self.status_var.set("Tiempo terminado")
            self.root.bell()
            messagebox.showinfo("Fin", "La cuenta regresiva ha terminado.")
            return

        self.remaining_seconds -= 1
        self.timer_job = self.root.after(1000, self._tick)


def main() -> None:
    root = tk.Tk()
    app = CountdownApp(root)
    root.protocol("WM_DELETE_WINDOW", app.pause)
    root.mainloop()


if __name__ == "__main__":
    main()
