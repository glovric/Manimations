# Manimations

## Prerequisites

- **[uv](https://docs.astral.sh/uv/)** - Python package installer
- **[MiKTeX](https://miktex.org/download)** - Latex distribution

## Setup

### Install dependencies

```bash
uv sync
```

### Activate virtual environment

```bash
.venv/Scripts/activate
```

### Render video

```bash
# SceneName is class SceneName in .py file
manim -pql scene.py SceneName
```

## Manim options

### Quality

```bash
# Low quality (480p)
manim -pql scene.py Scene

# Medium quality (720p)
manim -pqm scene.py Scene

# High quality (1080p)
manim -pqh scene.py Scene

# 4K quality
manim -pqk scene.py Scene
```

### Preview and output

```bash
# Preview the rendered video
manim -pql scene.py Scene

# Render without opening the video
manim -ql scene.py Scene
```