import os
import shutil

def automate_images():
    # Define the source directory (where your files are now)
    # '.' means the current folder where this script is saved
    source_dir = '.' 
    
    # Define the destination directory
    target_dir = './Organized_Images'

    # Create the folder if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created folder: {target_dir}")

    print("Scanning for .jpg files...")
    
    count = 0
    # List all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file ends with .jpg or .jpeg
        if filename.lower().endswith(('.jpg', '.jpeg')):
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)
            
            # Move the file
            shutil.move(source_path, target_path)
            print(f"Moved: {filename}")
            count += 1

    print(f"\nAutomation Complete! {count} images moved to {target_dir}.")

if __name__ == "__main__":
    automate_images()