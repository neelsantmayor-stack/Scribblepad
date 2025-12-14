import pytest

try:
    import tkinter as tk
except Exception:
    tk = None


def test_build_gui_no_mainloop():
    """Test we can build the GUI without running the mainloop and then destroy it.

    This validates importability and that a GUI can be built programmatically.
    """
    from scribblepad.gui import build_gui

    if tk is None:
        pytest.skip("tkinter not available")

    root = build_gui(start_mainloop=False)
    assert root is not None
    # clean up
    root.destroy()
