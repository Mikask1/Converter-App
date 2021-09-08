def merge_pdf():
    input_file = inputFile()
    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    for pdf in input_file:
        merger.append(pdf)

    merger.write("../result.pdf")
    merger.close()


def horizontal():
    input_file = inputFile()
    from PIL import Image

    images = [Image.open(img) for img in input_file]
    avg_height = sum(i.height for i in images) // len(images)

    result_img = Image.new(images[0].mode, (sum(i.width for i in images), avg_height))
    x = 1
    for img in images:
        width_ratio = int((avg_height / img.height) * img.width)
        resized_image = img.resize((width_ratio, avg_height))
        result_img.paste(resized_image, (x, 0))
        x += resized_image.width
    result_img.save('../result.png')


def vertical():
    input_file = inputFile()
    from PIL import Image

    images = [Image.open(img) for img in input_file]
    avg_width = sum(i.width for i in images) // len(images)

    result_img = Image.new(images[0].mode, (avg_width, sum(i.height for i in images)))
    y = 0
    for img in images:
        height_ratio = int((avg_width / img.width) * img.height)
        resized_image = img.resize((avg_width, height_ratio))
        result_img.paste(resized_image, (0, y))
        y += resized_image.height
    result_img.save('../result.png')


def convert_images_to_pdf():
    input_file = inputFile()
    from PIL import Image

    images = [Image.open(i) for i in input_file]
    converted = [img.convert('RGB') for img in images]

    if len(converted) == 1:
        converted[0].save('../result.pdf')
    else:
        converted[0].save('../result.pdf', save_all=True, append_images=converted[1:])


def convert_images_to_png():
    input_file = inputFile()

    from PIL import Image
    from pathlib import Path

    # Searches the extension
    for i in range(len(input_file)):
        extension = Path(input_file[i]).suffix
        if extension == '.pdf':
            from pdf2image import convert_from_path
            poppler_path = r'C:\poppler-21.03.0\Library\bin'

            images = convert_from_path(input_file[i], poppler_path=poppler_path)
            converted = images[0].convert('RGB')

            result = '../result' + str(i + 1) + '.png'
            converted.save(result)
        else:
            images = Image.open(input_file[i])
            converted = images.convert('RGB')
            result = '../result' + str(i + 1) + '.png'
            converted.save(result)


def convert_images_to_jpg():
    input_file = inputFile()
    from PIL import Image
    from pathlib import Path

    for i in range(len(input_file)):
        extension = Path(input_file[i]).suffix
        if extension == '.pdf':
            from pdf2image import convert_from_path
            poppler_path = r'C:\poppler-21.03.0\Library\bin'

            images = convert_from_path(input_file[i], poppler_path=poppler_path)
            converted = images[0].convert('RGB')

            result = '../result' + str(i + 1) + '.jpg'
            converted.save(result)
        else:
            images = Image.open(input_file[i])
            converted = images.convert('RGB')
            result = '../result' + str(i + 1) + '.jpg'
            converted.save(result)


def pdf_to_docx():
    input_file = inputFile()
    from pdf2docx import Converter
    for i in range(len(input_file)):
        pdf = input_file[i]
        result = '../result' + str(i + 1) + '.docx'

        cv = Converter(pdf)
        cv.convert(result)  # all pages by default | start = , end = | pages = [0,1,5,7]
        cv.close()


def inputFile():
    import tkinter.filedialog as fd
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    input_file = fd.askopenfilenames(parent=root, title='Choose image to detect')
    return input_file
