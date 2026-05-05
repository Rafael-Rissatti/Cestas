import os
from PIL import Image

def optimize_images():
    base_dir = "E:\\Python\\Cestas\\Cestas"
    categories = ["Cafe_da_Manha", "Cerveja"]
    root_images = ["c1.jpeg", "c2.jpeg", "c3.jpeg", "c4.jpeg", "c5.jpeg", "c6.jpeg", "c7.jpeg", "c8.jpeg", "fundo1.png", "fundo2.png"]
    
    thumb_size = (400, 400)
    
    # Process categories
    for cat in categories:
        cat_path = os.path.join(base_dir, cat)
        thumb_path = os.path.join(cat_path, "thumbs")
        
        if not os.path.exists(thumb_path):
            os.makedirs(thumb_path)
            
        for filename in os.listdir(cat_path):
            if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
                img_path = os.path.join(cat_path, filename)
                
                # Convert original to WebP (optimized)
                name, _ = os.path.splitext(filename)
                webp_name = name + ".webp"
                webp_path = os.path.join(cat_path, webp_name)
                
                with Image.open(img_path) as img:
                    # Save optimized original
                    img.save(webp_path, "WEBP", quality=85)
                    print(f"Optimized: {webp_path}")
                    
                    # Create thumbnail
                    img.thumbnail(thumb_size)
                    thumb_webp_path = os.path.join(thumb_path, webp_name)
                    img.save(thumb_webp_path, "WEBP", quality=80)
                    print(f"Thumbnail: {thumb_webp_path}")

    # Process root images
    for filename in root_images:
        img_path = os.path.join(base_dir, filename)
        if os.path.exists(img_path):
            name, _ = os.path.splitext(filename)
            webp_path = os.path.join(base_dir, name + ".webp")
            with Image.open(img_path) as img:
                img.save(webp_path, "WEBP", quality=85)
                print(f"Root Optimized: {webp_path}")

if __name__ == "__main__":
    optimize_images()
