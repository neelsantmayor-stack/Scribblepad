# ScribblePad

ScribblePad is a small, simple Tkinter drawing app — a toy project for learning how to build a GUI in Python.

This repo is structured as a Python package so it can be imported or installed, and also includes an example standalone script.

## Features
- Draw freehand on a canvas using left mouse button
- `scribblepad.gui.build_gui(start_mainloop=False)` returns the created Tk root (for tests)
- `scribblepad.gui.run_gui()` runs the GUI (entry point)

## Quickstart
Install (editable):

```bash
cd scribblepad_repo
pip install -e .
```

Run as module (without installing):

```bash
python -m scribblepad.gui
```


> Note: If you still have `scribblepad.py` at the repository root or elsewhere in Downloads, it is recommended to delete or move it into `examples/` to avoid accidental imports or name collisions. The current example is at `examples/original_scribblepad.py` and the import-safe package is under `scribblepad/`.
Run installed script:

```bash
scribblepad-gui
```

Or run the example script directly:

```bash
python examples/original_scribblepad.py
```

## Tests

```bash
pip install -r requirements.txt
pytest
```

## License
This project is MIT licensed — see the `LICENSE` file.
