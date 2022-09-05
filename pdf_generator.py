import pdfkit

#Define path to wkhtmltopdf(folder where you installed the lib)
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#Define the configuration to pdfkit
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

#Convert html file to pdf
#pdfkit.from_file(file_name, output_path='name_file.pdf', configuration=config)

#Convert url html to pdf
pdfkit.from_url('https://www.w3schools.com/html/default.asp', output_path='w3schools.pdf', configuration=config)


