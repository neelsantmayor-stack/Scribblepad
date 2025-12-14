"""ScribblePad Tkinter GUI module.

Functions:
- build_gui(start_mainloop=True): constructs the GUI and optionally starts mainloop.
- run_gui(): convenience wrapper which runs the GUI.

This design keeps GUI construction separate from invoking mainloop so tests can
create widget trees without blocking or opening a window in headless tests.
"""
from __future__ import annotations

import tkinter as tk
from typing import Optional


def _on_press(event: tk.Event, canvas: tk.Canvas):
    canvas._last_x, canvas._last_y = event.x, event.y


def _on_drag(event: tk.Event, canvas: tk.Canvas):
    x0, y0 = getattr(canvas, "_last_x", event.x), getattr(canvas, "_last_y", event.y)
    canvas.create_line((x0, y0, event.x, event.y), fill="yellow", width=5)
    canvas._last_x, canvas._last_y = event.x, event.y


def build_gui(start_mainloop: bool = True, geometry: str = "400x400") -> Optional[tk.Tk]:
    """Build the Tk GUI for ScribblePad and optionally run the mainloop.

    Args:
        start_mainloop: When True, call `root.mainloop()` and return None; otherwise return the `tk.Tk` instance.
        geometry: Optional geometry string passed to `root.geometry()`.

    Returns:
        tk.Tk or None depending on `start_mainloop`.
    """
    root = tk.Tk()
    root.geometry(geometry)
    root.title("Scribble Pad")

    canvas = tk.Canvas(root, bg="brown")
    canvas.pack(anchor="nw", fill="both", expand=1)

    canvas.bind("<Button-1>", lambda e: _on_press(e, canvas))
    canvas.bind("<B1-Motion>", lambda e: _on_drag(e, canvas))

    if start_mainloop:
        root.mainloop()
        return None

    return root


def run_gui() -> None:
    """Convenience wrapper that builds and runs the GUI."""
    build_gui(start_mainloop=True)


if __name__ == "__main__":
    run_gui()
