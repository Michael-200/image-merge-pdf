from PIL import Image
import os

def images_to_pdf(input_folder, output_pdf="output.pdf"):
    # Supported image extensions by Pillow
    supported_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")

    # Collect image files
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_ext)]

    if not image_files:
        raise ValueError("No supported image files found in the folder.")

    # Sort for consistent ordering (optional)
    image_files.sort()

    rgb_images = []
    for file in image_files:
        try:
            img = Image.open(os.path.join(input_folder, file)).convert("RGB")
            rgb_images.append(img)
        except Exception as e:
            print(f"Skipping {file}: {e}")

    if not rgb_images:
        raise ValueError("No valid images could be processed.")

    # Save as PDF
    rgb_images[0].save(output_pdf, save_all=True, append_images=rgb_images[1:])
    print(f"PDF created successfully: {output_pdf}")


if __name__ == "__main__":
    # Example: convert all images in the "images" folder into SilverBullet.pdf
    images_to_pdf("images", "file.pdf")
