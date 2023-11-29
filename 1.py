import PyPDF2 
with open('все БИСО-03-22 ЯП КР папка.pdf', 'rb') as pdf_file: 
    pdf_reader = PyPDF2.PdfReader(pdf_file) 
    for i in range(0, len(pdf_reader.pages), 2): 
        pdf_writer = PyPDF2.PdfWriter() 
        pdf_writer.add_page(pdf_reader.pages[i]) 
        pdf_writer.add_page(pdf_reader.pages[i+1]) 
        #output_file_name = f'Python_Tutorial_{i}.pdf' 
        output_file_name = f'БИСО-03-22-КР-ЯП-{i}.pdf' 
        with open(output_file_name, 'wb') as output_file: 
            pdf_writer.write(output_file)