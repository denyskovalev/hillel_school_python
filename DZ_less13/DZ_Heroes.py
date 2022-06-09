# ***1|2***
# Реалізувати клас Герой що має мати наступні атрибути: ім‘я, здоров‘я, ранг, сила і метод вдарити.
# Метод вдарити повинен наносити шкоду противнику в розмірі сили героя. Герой має мати наступні
# обмеження: здоров‘я від 0 до 100, ранг 1,2,3. Сила не більше 10% теперішнього здоров‘я героя.
# Не можна бити героїв здоров‘я яких менше 5.
#
# Реалізувати клас маг, який може відновлювати здоров'я інших героїв, також він має ранг як герой і
# може наносити удари. За відновлення здоров'я він бере гроші. ( Вам потрібно реалізувати цей функціонал ).
# Герой заробляє гроші за перемогу у бою з іншим героєм, також при перемозі він забирає всі гроші суперника.
# Скільки герой отримує грошей за перемогу і скільки коштує відновити здоров'я, на ваш розсуд)
#
# ***2|2***
# Розширити функціонал з минулої ДЗ:
#
# Добавити атрибут захист герою
# Створити можливість героям використовувати спорядження для збільшення захисту чи сили. Зробити обмеження
# на кількість спорядження одним героєм ( один герою не може носити 100500 мечів і 200к щитів ).
# Створити місце де герой може купити спорядження
# Створити арени, які можуть приймати поєдинок між героями.
# Створити можливість організовувати на арені турніри між героями з великим призовим фондом.
# Всі деталі реалізації на ваш розгляд.

from items_examp import general_sword, general_shield, officer_sword, officer_shield, warrior_sword, warrior_shield
from mad_arena import Arena
from players_examp import Hero, Mage
from shop import WeaponShop

# create shop

craft_shop = WeaponShop("Craft Shop")

# add to shop sets of weapons

craft_shop.add_item(general_sword)
craft_shop.add_item(general_shield)
craft_shop.add_item(officer_sword)
craft_shop.add_item(officer_shield)
craft_shop.add_item(warrior_sword)
craft_shop.add_item(warrior_shield)

# create heroes

naruto = Hero("Naruto")
sasuke = Hero("Sasuke")
tsunade = Mage("Tsunade")
dziraija = Hero("Dziraija")
orochimaru = Hero("Orochimaru")

# and change some characteristic heroes
dziraija.custom_characteristics("Dziraija", 100, 1, 7, 300, 10)
tsunade.custom_characteristics("Tsunade", 100, 1, 7, 300, 10)

# look at the shop after buy

print(craft_shop)

# add weapons to heroes

naruto.buy_item(craft_shop, warrior_sword)
naruto.buy_item(craft_shop, warrior_shield)
sasuke.buy_item(craft_shop, warrior_sword)
sasuke.buy_item(craft_shop, warrior_shield)
dziraija.buy_item(craft_shop, general_sword)
dziraija.buy_item(craft_shop, general_shield)

# eqip weapons

naruto.dress_item(warrior_sword)
naruto.dress_item(warrior_shield)
sasuke.dress_item(warrior_sword)
sasuke.dress_item(warrior_shield)

# create arena

madness_arena = Arena("Arena of Madness", 200)

# tournament example

madness_arena.tournament_automatic(naruto, sasuke)

# end more with 1 rank hero, setup weapons
dziraija.dress_item(general_sword)
dziraija.dress_item(general_shield)

madness_arena.tournament_automatic(dziraija, tsunade)
