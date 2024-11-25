from PIL import Image
import os

def resize_images(input_directory, output_directory, target_size):
    """
    Resizes all images in the input directory and saves them in the output directory.
    
    """
    # Check if input directory exists
    if not os.path.exists(input_directory):
        print(f"Error: Input directory does not exist: {input_directory}")
        return

    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        filepath = os.path.join(input_directory, filename)
        
        # Check if it's a file and an image
        if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                with Image.open(filepath) as img:
                    # Resize the image
                    img_resized = img.resize(target_size, Image.ANTIALIAS)
                    
                    # Save the resized image to the output directory
                    output_path = os.path.join(output_directory, filename)
                    img_resized.save(output_path)
                    print(f"Resized and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


input_dir = "/Users/tusharsharma/Desktop/input_images"  
output_dir = "/Users/tusharsharma/Desktop/output_images"  
resize_dimensions = (300, 300)  

resize_images(input_dir, output_dir, resize_dimensions)
