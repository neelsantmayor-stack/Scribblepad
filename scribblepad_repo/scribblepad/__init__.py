"""scribblepad package — simple Tkinter drawing app as a reusable module.

Expose core functions for reuse: `build_gui` and `run_gui`.
"""
from .gui import build_gui, run_gui

__all__ = ["build_gui", "run_gui"]
