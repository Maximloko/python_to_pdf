from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

"""
Полезные ссылки
https://github.com/prajwollamichhane11/PDF-Handling-With-Python
https://docs.reportlab.com/reportlab/userguide/ch2_graphics/
https://stackoverflow.com/questions/27732213/how-to-add-bold-and-normal-text-in-one-line-using-drawstring-method-in-reportlab
"""
product_name = 'Название товара (первая строка)\n(вторая строка)'
product_article = '1234567890-1234567890-12345'
color = 'Черный'
size = '50'
consist = 'экокожа'
provider = 'ИП Сидоров В.Н.'
registerFont(TTFont('Arial', 'ARIAL.ttf'))
registerFont(TTFont('ArialBd', 'ARIALBd.ttf'))
registerFontFamily('Arial', normal='Arial', bold='ArialBd')

canvas = Canvas('new_file.pdf', pagesize=(60 * mm, 40 * mm))
canvas.setFont("ArialBd", 10)

textobject = canvas.beginText(1 * mm, 37 * mm, )
for line in product_name.splitlines(False):
    textobject.textLine(line.rstrip())
canvas.drawText(textobject)

canvas.setFont("Arial", 8)
canvas.drawString(1 * mm, 29 * mm, f'Артикул: {product_article}')
canvas.drawString(1 * mm, 26 * mm, f'Цвет: {color}')
canvas.drawString(1 * mm, 23 * mm, f'Размер: {size}')
canvas.drawString(1 * mm, 20 * mm, f'Состав: {consist}')
canvas.drawString(1 * mm, 17 * mm, f'Поставщик: {provider}')
canvas.drawImage('icon.png', 135, 48, width=30, height=30)
canvas.drawImage('barcode.png', 5, 2, width=158, height=43)
canvas.save()


