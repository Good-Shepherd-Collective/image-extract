# image-extract

Download the repo. Make sure you have Python installed on your system. Download the pdf in the root folder of this project. Change the `pdf_path` and `output_folder` variables in the `image.py` code. Set up the virtual enviroment, install the one dependency and run. 

Set up virtual enviroment
```bash
virtualenv env
```

Install python library 
```bash
pip install pymupdf
```
Change these for your .pdf file and image folder

```bash Example usage
pdf_path = "Indigenous-Erasure.pdf"
output_folder = "Indigenous-Erasure-Images"
extract_images_from_pdf(pdf_path, output_folder)
```
