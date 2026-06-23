from pathlib import Path

images = list(Path("datasets/Images").glob("*.jpg"))

print("Total Images:", len(images))