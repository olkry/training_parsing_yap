import re

from bs4 import BeautifulSoup

some_html = """
<article>
  Произвольный текст перемежается ссылками на разные картинки и документы.
  <a href="http://url.com/some_pic.jpg"><img src="..."></a>
  <a href="http://url.com/another_img.jpeg">Ссылка на картинку</a>
  <a href="http://url.com/not_an_image.docx">Документ Word</a>
  <a href="http://url.com/funny_pic.gif">Гифка</a>
  <a href="http://url.com/media1.png"><img src="..."></a>
  <a href="http://url.com/png_sheet.xlsx">Электронная таблица</a>
  <a href="http://url.com/it_s_a_trap.jpg.zip">Архив</a>
  <a href="http://url.com/pdf_with_gif.pdf">Документ PDF</a>
  <a href="http://url.com/something_strange.agif">Неизвестный объект</a>
</article>
"""

soup = BeautifulSoup(some_html, 'lxml')
pictures = soup.find_all('a', {'href': re.compile(r'.+\.(jpe?g|gif|png)$')})
print(pictures)