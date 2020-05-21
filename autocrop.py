#!/usr/bin/env python
import glob
from PIL import Image
import json
import os
import click


@click.command()
@click.option("--regions-config", default="regions.json", show_default=True, type=click.Path(exists=True), help="JSON template file")
@click.option("--output-dir", default="output", show_default=True, type=click.Path(), help="Output directory")
@click.argument("image_paths", nargs=-1, type=click.Path(exists=True))
def crop(output_dir, regions_config, image_paths):
    os.makedirs(output_dir, exist_ok=True)
    with open(regions_config) as json_config_file:
        region_config = json.load(json_config_file)
    
    regions = region_config["regions"]
    print(f"{len(regions)} to cut from each image")
 
    if not image_paths:
        raise click.UsageError("No image paths provided")
    image_paths = list(sorted(image_paths))
    total_images = len(image_paths)
    print(f"{total_images} images to cut")

    for region in regions:
        print("Max width:", region["start_x"] + region["width"])
        print("Max height:", region["start_y"] + region["height"])
        print()

    for c, image_path in enumerate(image_paths):
        print(f"[{c + 1}/{total_images}] Cutting {image_path}")
        img = Image.open(image_path)
        print("Image size:", img.size)
        for i, region in enumerate(regions):
            base_name, extension = os.path.splitext(os.path.basename(image_path))
            image_region_name = base_name + f"_{i + 1}" + extension
            print(f"    Cutting into {image_region_name}")
            cut_box = (
                    region["start_x"],
                    region["start_y"],
                    region["start_x"] + region["width"],
                    region["start_y"] + region["height"]
                    )
            cropped_region = img.crop(cut_box)
            image_region_path = os.path.join(output_dir, image_region_name)
            cropped_region.save(image_region_path)


if __name__ == "__main__":
    crop()

