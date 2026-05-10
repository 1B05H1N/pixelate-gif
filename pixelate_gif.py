from pathlib import Path
import argparse
import imageio.v2 as imageio
from PIL import Image
import numpy as np

def pixelate(image: Image.Image, factor: int = 8) -> Image.Image:
    """
    Downscale then upscale an image to create a pixelated effect.
    `factor` controls how blocky it looks (higher == chunkier).
    """
    img_small = image.resize(
        (max(1, image.width // factor), max(1, image.height // factor)),
        resample=Image.NEAREST
    )
    return img_small.resize(
        image.size,
        resample=Image.NEAREST
    )

def pixelate_image(src_path: str | Path, dst_path: str | Path, factor: int = 8):
    with Image.open(src_path) as image:
        pixelated = pixelate(image, factor)
        pixelated.save(dst_path)
    print(f"Saved pixelated image -> {dst_path}")

def pixelate_gif(src_path: str | Path, dst_path: str | Path, factor: int = 8):
    reader = imageio.get_reader(src_path)
    meta   = reader.get_meta_data()
    frames, durations = [], []

    for frame in reader:
        pil_frame = Image.fromarray(frame)
        frames.append(pixelate(pil_frame, factor))
        durations.append(meta.get("duration", 40))

    with imageio.get_writer(dst_path, mode="I", duration=durations, loop=0) as writer:
        for frame in frames:
            writer.append_data(np.asarray(frame))

    print(f"Saved pixelated GIF -> {dst_path}")

def detect_input_type(path: str | Path) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".gif":
        return "gif"
    return "image"

def main():
    parser = argparse.ArgumentParser(description="Pixelate GIFs or images.")
    parser.add_argument("input", help="Input media path")
    parser.add_argument("output", help="Output media path")
    parser.add_argument("--factor", type=int, default=8, help="Pixelation factor (default: 8)")
    parser.add_argument(
        "--input-type",
        choices=["auto", "gif", "image"],
        default="auto",
        help="Input type. Use auto to detect from file extension (default: auto)."
    )
    args = parser.parse_args()
    input_type = args.input_type
    if input_type == "auto":
        input_type = detect_input_type(args.input)

    if input_type == "gif":
        pixelate_gif(args.input, args.output, args.factor)
    else:
        pixelate_image(args.input, args.output, args.factor)

if __name__ == "__main__":
    main() 