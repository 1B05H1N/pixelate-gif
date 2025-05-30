# pixelate-gif

A pure-Python script to pixelate every frame of a GIF. Down-samples each frame to lose detail, then upscales with nearest-neighbor interpolation for a blocky, retro look.

## Features
- Works on any GIF (animated or static)
- Adjustable pixelation factor
- Preserves animation timing and loop count
- No external dependencies beyond Pillow and imageio

## Installation

```bash
pip install pillow imageio
```

## Usage

```bash
python pixelate_gif.py input.gif pixelated.gif --factor 10
```

- `input.gif`: Path to your source GIF
- `pixelated.gif`: Output path
- `--factor`: (Optional) Pixelation factor (default: 8)

## How it works
1. Reads the GIF frame-by-frame
2. Downscales and upscales each frame with nearest-neighbor
3. Re-encodes all frames, preserving timing and loop info

## Tweaks
- Change `factor` for chunkier or finer pixelation
- Use `Image.BILINEAR` for a softer look
- Crop and pixelate only a region for selective effects

## Example

Original GIF | Pixelated GIF
:---:|:---:
![Original nacho-libre.gif](nacho-libre.gif) | ![Pixelated nacho-libre-pixelated.gif](nacho-libre-pixelated.gif)

This shows how the script pixelates every frame while preserving animation and looping.