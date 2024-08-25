from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from colorama import Fore, Style
import pyautogui
import PyPDF2
from PIL import Image
import datetime
from Managing_accounts import Manage_account


# Creating report PDF file
def create_pdf(pdf_file_path):
    c = canvas.Canvas(pdf_file_path, pagesize=letter)

    # Set background color
    c.setFillColorRGB(0.8, 0.9, 1)  # Light blue color
    c.rect(0, 0, letter[0], letter[1], fill=True, stroke=False)

    # Set font and size for the heading
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(colors.darkblue)  # Dark blue color
    c.drawCentredString(letter[0] / 2, 650, "Today's Report")

    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Draw the date
    c.setFont("Helvetica", 24)

    # Draw the first string (current_date)
    c.setFillColorRGB(255, 0, 0)  # Orange color
    c.drawCentredString(letter[0] / 2, letter[1] - 280, "Date: {}".format(current_date))

    # Draw a decorative line
    c.setStrokeColor(colors.red)  # Red color
    c.setLineWidth(4)
    c.line(100, 600, 500, 600)

    # Set font and size for the content
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.black)  # Black color

    # Save the PDF file
    c.save()
    print(Fore.BLUE + Style.BRIGHT + f"PDF file '{pdf_file_path}' has been created." + Style.RESET_ALL)


#Adding Screenshot to pdf
def add_screenshot_to_pdf(pdf_file_path):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

    # Open the existing PDF
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Convert the screenshot to PDF
        screenshot_image = Image.open(screenshot_path)
        screenshot_image_path = "screenshot.pdf"
        screenshot_image.save(screenshot_image_path, "PDF")

        # Merge the PDF and the screenshot image
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        with open(screenshot_image_path, "rb") as screenshot_pdf:
            screenshot_pdf_reader = PyPDF2.PdfReader(screenshot_pdf)
            pdf_writer.add_page(screenshot_pdf_reader.pages[0])

        # Save the modified PDF
        modified_pdf_path = f"E:\\Report Files\\modified_report_file.pdf"
        with open(pdf_file_path, "wb") as modified_pdf:
            pdf_writer.write(modified_pdf)

    print(f"Screenshot added to '{pdf_file_path}'. Modified PDF saved as '{modified_pdf_path}'.")

def add_account_page_to_pdf(existing_pdf_path, account_number, rep=1, strng=None, hed="Runtime of Program:- "):
    """
    account_number=None: Account's points have been collected completely
    rep=1: Opening account for the first time
    rep=2: Failed to read points
    rep=0: Opening account again for points collection after cooldown
    """
    output_pdf_path = existing_pdf_path
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # if account_number=="D":
    #     # Set background color
    #     c.setFillColorRGB(0 / 255, 0 / 255, 102 / 255)  # RGB color values for background (Indigo)
    #     c.rect(0, 0, letter[0], letter[1], fill=True)
    #
    #     # Set font and font size for the heading
    #     c.setFont("Helvetica-Bold", 36)  # Font and size for the heading
    #     # Set text color
    #     c.setFillColorRGB(255 / 255, 215 / 255, 0 / 255)  # RGB color values for text (Gold)
    #     heading = hed  # assuming hed is defined elsewhere
    #     c.drawCentredString(letter[0] / 2, letter[1] - 100, heading)
    #
    #     # Set font size for the text
    #     c.setFont("Helvetica", 24)
    #     # Set text color
    #     c.setFillColorRGB(192 / 255, 192 / 255, 192 / 255)  # RGB color values for text (Light Gray)
    #     # Draw the second string (strng)
    #     c.drawCentredString(letter[0] / 2, letter[1] - 170, strng)  # assuming strng is defined elsewhere
    #
    #     c.save()

    if account_number:
        account_name_image_path = Manage_account("ANIP")
        # Extract the account name from the path
        pro_name = account_name_image_path[account_number - 1].split("\\")
        pro_name = pro_name[2].split(".")

        if rep == 1:
            # Create a new canvas for the page
            c = canvas.Canvas("temp.pdf", pagesize=letter)
            # Set background color
            c.setFillColorRGB(153, 76, 0)  # RGB color values for background (Orange)
            c.rect(0, 0, letter[0], letter[1], fill=True)

            # Set font and font size for the heading and text
            c.setFont("Helvetica-Bold", 36)  # Font and size for the heading

            # Draw the heading
            # Set text color
            c.setFillColorRGB(0, 0, 255)  # RGB color values for text (Blue)
            heading = "Report of Account Number: {}".format(account_number)
            c.drawCentredString(letter[0] / 2, letter[1] - 150, heading)

            # Draw the date
            c.setFont("Helvetica", 20)

            # Draw the first string (current_date)
            c.drawCentredString(letter[0] / 2, letter[1] - 200, "Date: {}".format(current_date))

            # Draw the second string (pro_name)
            c.drawCentredString(letter[0] / 2, letter[1] - 220, "Profile Name: {}".format(pro_name[0]))
            # Save the canvas to the PDF file
            c.save()
            # Open the existing PDF and the new page as PDF objects
            existing_pdf = PyPDF2.PdfReader(open(existing_pdf_path, "rb"))
            new_page = PyPDF2.PdfReader(open("temp.pdf", "rb")).pages[0]

            # Create a PDF writer object to write the merged content
            pdf_writer = PyPDF2.PdfWriter()

            # Add existing pages to the writer
            for page_num in range(len(existing_pdf.pages)):
                page = existing_pdf.pages[page_num]
                pdf_writer.add_page(page)

            # Add the new page to the writer
            pdf_writer.add_page(new_page)

            # Write the merged content to the output PDF file
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

        elif rep == 2:
            # Create a new canvas for the page
            c = canvas.Canvas("temp.pdf", pagesize=letter)
            # Set background color
            c.setFillColorRGB(0.2, 0.6, 0.8)  # RGB color values for background (light blue)
            c.rect(0, 0, letter[0], letter[1], fill=True)

            # Set font and font size for the heading and text
            c.setFont("Helvetica-Bold", 36)  # Font and size for the heading

            # Draw the heading
            # Set text color
            c.setFillColorRGB(255, 255, 0)  # RGB color values for text (yellow)
            heading = "Starting Account Number: {}".format(account_number)
            c.drawCentredString(letter[0] / 2, letter[1] - 150, heading)

            # Draw the date
            c.setFont("Helvetica", 24)

            # Draw the second string (pro_name)
            c.drawCentredString(letter[0] / 2, letter[1] - 220, "Profile Name: {}".format(pro_name[0]))
            # Save the canvas to the PDF file
            c.save()
            # Open the existing PDF and the new page as PDF objects
            existing_pdf = PyPDF2.PdfReader(open(existing_pdf_path, "rb"))
            new_page = PyPDF2.PdfReader(open("temp.pdf", "rb")).pages[0]

            # Create a PDF writer object to write the merged content
            pdf_writer = PyPDF2.PdfWriter()

            # Add existing pages to the writer
            for page_num in range(len(existing_pdf.pages)):
                page = existing_pdf.pages[page_num]
                pdf_writer.add_page(page)

            # Add the new page to the writer
            pdf_writer.add_page(new_page)

            # Write the merged content to the output PDF file
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

        elif rep == 0:
            # Create a new canvas for the page
            c = canvas.Canvas("temp.pdf", pagesize=letter)
            # Set background color
            c.setFillColorRGB(0.2, 0.6, 0.8)  # RGB color values for background (light blue)
            c.rect(0, 0, letter[0], letter[1], fill=True)

            # Set font and font size for the heading and text
            c.setFont("Helvetica-Bold", 36)  # Font and size for the heading

            # Draw the heading
            # Set text color
            c.setFillColorRGB(255, 0, 0)  # RGB color values for text (Red)
            heading = "Starting Account Number: {}".format(account_number)
            c.drawCentredString(letter[0] / 2, letter[1] - 150, heading)

            # Draw the date
            c.setFont("Helvetica", 24)

            # Draw the second string (pro_name)
            c.drawCentredString(letter[0] / 2, letter[1] - 220, "Profile Name: {}".format(pro_name[0]))
            # Save the canvas to the PDF file
            c.save()
            # Open the existing PDF and the new page as PDF objects
            existing_pdf = PyPDF2.PdfReader(open(existing_pdf_path, "rb"))
            new_page = PyPDF2.PdfReader(open("temp.pdf", "rb")).pages[0]

            # Create a PDF writer object to write the merged content
            pdf_writer = PyPDF2.PdfWriter()

            # Add existing pages to the writer
            for page_num in range(len(existing_pdf.pages)):
                page = existing_pdf.pages[page_num]
                pdf_writer.add_page(page)

            # Add the new page to the writer
            pdf_writer.add_page(new_page)

            # Write the merged content to the output PDF file
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

    elif account_number==None:
        if rep == 0:
            # Create a new canvas for the page
            c = canvas.Canvas("temp.pdf", pagesize=letter)
            # Set background color
            c.setFillColorRGB(24 / 255, 24 / 255, 50 / 255)  # RGB color values for background (very Dark Gray)
            c.rect(0, 0, letter[0], letter[1], fill=True)

            # Set font and font size for the heading
            c.setFont("Helvetica-Bold", 36)  # Font and size for the heading
            # Set text color
            c.setFillColorRGB(255 / 255, 155 / 255, 25 / 255)  # RGB color values for text (White)
            heading = hed
            c.drawCentredString(letter[0] / 2, letter[1] - 150, heading)

            # Set font size for the text
            c.setFont("Helvetica", 24)

            # Draw the second string (strng)
            c.drawCentredString(letter[0] / 2, letter[1] - 220, strng)  # assuming strng is defined elsewhere

            c.save()
            # Open the existing PDF and the new page as PDF objects
            existing_pdf = PyPDF2.PdfReader(open(existing_pdf_path, "rb"))
            new_page = PyPDF2.PdfReader(open("temp.pdf", "rb")).pages[0]

            # Create a PDF writer object to write the merged content
            pdf_writer = PyPDF2.PdfWriter()

            # Add existing pages to the writer
            for page_num in range(len(existing_pdf.pages)):
                page = existing_pdf.pages[page_num]
                pdf_writer.add_page(page)

            # Add the new page to the writer
            pdf_writer.add_page(new_page)

            # Write the merged content to the output PDF file
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)
        elif rep == 1:
            # Create a new canvas for the page
            c = canvas.Canvas("temp.pdf", pagesize=letter)
            # Set background color
            c.setFillColorRGB(0 / 255, 0 / 255, 102 / 255)  # RGB color values for background (Indigo)
            c.rect(0, 0, letter[0], letter[1], fill=True)

            # Set font and font size for the heading
            c.setFont("Helvetica-Bold", 36)  # Font and size for the heading
            # Set text color
            c.setFillColorRGB(255 / 255, 215 / 255, 0 / 255)  # RGB color values for text (Gold)
            heading = hed  # assuming hed is defined elsewhere
            c.drawCentredString(letter[0] / 2, letter[1] - 100, heading)

            # Set font size for the text
            c.setFont("Helvetica", 24)
            # Set text color
            c.setFillColorRGB(192 / 255, 192 / 255, 192 / 255)  # RGB color values for text (Light Gray)
            # Draw the second string (strng)
            lines = strng.splitlines()
            y_coordinate = letter[1] - 170
            for line in lines:
                c.drawCentredString(letter[0] / 2, y_coordinate, line)
                y_coordinate -= 24  # Adjust y-coordinate for the next line

            c.save()
            # Open the existing PDF and the new page as PDF objects
            existing_pdf = PyPDF2.PdfReader(open(existing_pdf_path, "rb"))
            new_page = PyPDF2.PdfReader(open("temp.pdf", "rb")).pages[0]

            # Create a PDF writer object to write the merged content
            pdf_writer = PyPDF2.PdfWriter()

            # Add existing pages to the writer
            for page_num in range(len(existing_pdf.pages)):
                page = existing_pdf.pages[page_num]
                pdf_writer.add_page(page)

            # Add the new page to the writer
            pdf_writer.add_page(new_page)

            # Write the merged content to the output PDF file
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

    print(f"Colorful page added to '{output_pdf_path}'.")