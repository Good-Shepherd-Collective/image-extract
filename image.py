import fitz  
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each page of the PDF
    for i in range(len(doc)):
        page = doc.load_page(i)
        
        # Extract images
        image_list = page.get_images(full=True)
        
        # Save each image
        for image_index, img in enumerate(image_list, start=1):
            # Get the XREF of the image
            xref = img[0]
            
            # Extract the image bytes
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Construct the image file name
            image_filename = f"page_{i+1}_image_{image_index}.png"
            image_filepath = os.path.join(output_folder, image_filename)
            
            # Save the image
            with open(image_filepath, "wb") as image_file:
                image_file.write(image_bytes)
            
            print(f"Saved {image_filepath}")

    print("Image extraction completed.")

# Example usage
pdf_path = "Indigenous-Erasure.pdf" #Change this file name of your pdf
output_folder = "Indigenous-Erasure-Images" #Change this to the folder name you want the images saved to
extract_images_from_pdf(pdf_path, output_folder)
