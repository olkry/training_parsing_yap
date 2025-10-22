# Импортируйте библиотеку BeautifulSoup.
from bs4 import BeautifulSoup

price_html = """
<table cellspacing="0" cellpadding="0" border="1">
  <tbody>
    <tr class="even_row">
      <th><p>№ п/п</p></th>
      <th class="armor"><p>Название</p></th>
      <th class="price"><p>Цена</p><p>рублей</p></th>
    </tr>
    <tr class="odd_row">
      <td><p>1.</p></td>
      <td class="armor"><p>Щит</p></td>
      <td class="price"><p>375</p></td>
    </tr>
    <tr class="even_row">
      <td><p>2.</p></td>
      <td class="armor"><p>Шлем</p></td>
      <td class="price"><p>297</p></td>
    </tr>
    <tr class="odd_row">
      <td><p>3.</p></td>
      <td class="armor"><p>Кольчуга</p></td>
      <td class="price"><p>565</p></td>
    </tr>
    <tr class="even_row">
      <td><p>4.</p></td>
      <td class="armor"><p>Булава</p></td>
      <td class="price"><p>1992</p></td>
    </tr>
    <!-- Сюда может добавиться неизвестное количество элементов экипировки.
      Их тоже нужно учитывать при расчёте средней цены. -->
  </tbody>
</table>
"""

# Создайте «суп».
soup = BeautifulSoup(price_html, features='lxml')

# Напишите здесь свой код.
prices = [int(price.text) for price in
          soup.find_all('td', attrs={'class': 'price'})]
result = sum(prices)/len(prices)

print('Средняя цена богатырских доспехов: ', result, 'рублей')
