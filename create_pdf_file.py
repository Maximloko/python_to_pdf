from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
# https://github.com/prajwollamichhane11/PDF-Handling-With-Python
# https://docs.reportlab.com/reportlab/userguide/ch2_graphics/
# https://stackoverflow.com/questions/27732213/how-to-add-bold-and-normal-text-in-one-line-using-drawstring-method-in-reportlab

registerFont(TTFont('Arial', 'ARIAL.ttf'))
registerFont(TTFont('ArialBd', 'ARIALBd.ttf'))
registerFontFamily('Arial', normal='Arial', bold='ArialBd')

canvas = Canvas('new_file.pdf', pagesize=(60 * mm, 40 * mm))
canvas.setFont("ArialBd", 10)
my_text = 'Название товара (первая строка)\n(первая строка)'
textobject = canvas.beginText(1 * mm, 37 * mm,)
for line in my_text.splitlines(False):
    textobject.textLine(line.rstrip())
canvas.drawText(textobject)
# canvas.setFont("Arial", 8)
# canvas.drawString(1*mm, 30*mm, 'Название товара (первая строка)')
canvas.save()
