from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

mainMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ ะฅะธัั ะฟัะพะดะฐะถ ๐", callback_data="๐")
        ],
        [
            InlineKeyboardButton(text="๐ฏ Lavash ๐ฏ", callback_data="๐ฏ"),
            InlineKeyboardButton(text="๐ญ Hot-dog ๐ญ", callback_data="๐ญ")
        ],
        [
            InlineKeyboardButton(text="๐ฎ Shaurma ๐ฎ", callback_data="๐ฎ"),
            InlineKeyboardButton(text="๐ Gamburger ๐", callback_data="๐")
        ],
        [
            InlineKeyboardButton(text="๐ฅ Assorti ๐ฅ", callback_data="๐ฅ"),
            InlineKeyboardButton(text="๐ Combo ๐", callback_data="๐")
        ],
        [
            InlineKeyboardButton(text="๐ฐ Desert ๐ฐ", callback_data="๐ฐ"),
            InlineKeyboardButton(text="๐ฅ Sous va salatlar ๐ฅ", callback_data="๐ฅ")
        ],
        [
            InlineKeyboardButton(text="๐น Sok va ichimliklar ๐น", callback_data="๐น"),
            InlineKeyboardButton(text="โ Choy va Kofelar โ", callback_data="โ")
        ]
    ]
)
menuXiti = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐๐ Tovuqli shaurma ๐๐", callback_data="1a"),
        ],
        [
            InlineKeyboardButton(text="๐ฅฉ Mol go'shtli danar ๐ฅฉ", callback_data="2a")
        ],
        [
            InlineKeyboardButton(text="๐๐๐ถ Achchiq tovuqli shaurma ๐๐๐ถ", callback_data="3a"),
        ],
        [
            InlineKeyboardButton(text="๐ฅฉ๐ฅ Mol go'shtli sab ๐ฅฉ๐ฅ", callback_data="4a")
        ],
        [
            InlineKeyboardButton(text="๐๐ฅ Tovuqli sab ๐๐ฅ", callback_data="5a"),
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuLav = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ฅฉ๐ฏ Mol go'shtli lavash ๐ฅฉ๐ฏ", callback_data="b1")
        ],
        [
            InlineKeyboardButton(text="๐๐ฏ Tovuqli lavash ๐๐ฏ", callback_data="b2")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ฅฉ๐ฏ Mini mol go'shtli lavash ๐ฝ๐ฅฉ๐ฏ", callback_data="b3")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐๐ฏ Mini tovuqli lavash ๐ฝ๐๐ฏ", callback_data="b4")
        ],
        [
            InlineKeyboardButton(text="๐ง๐ฅฉ๐ฏ Sirli mol go'shtli lavash ๐ง๐ฅฉ๐ฏ", callback_data="b5")
        ],
        [
            InlineKeyboardButton(text="๐ง๐๐ฏ Sir qo'shilgan tovuqli lavash ๐ง๐๐ฏ", callback_data="b6")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ง๐ฏ๐ฅฉ Mini sir qo'shilgan lavash ๐ฝ๐ง๐ฏ๐ฅฉ", callback_data="b7")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ง๐ฏ๐ Mini sir qo'shilgan lavash ๐ฝ๐ง๐ฏ๐", callback_data="b8")
        ],
        [
            InlineKeyboardButton(text="๐ฅฉ๐ถ๐ฏ Qalampirli lavash ๐ฅฉ๐ถ๐ฏ", callback_data="b9")
        ],
        [
            InlineKeyboardButton(text="๐๐ถ๐ฏ Qalampirli lavash ๐๐ถ๐ฏ", callback_data="ba")
        ],
        [
            InlineKeyboardButton(text="๐ฏ๐ฅ Fitter ๐ฏ๐ฅ", callback_data="bb")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
menuHot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ญ Hot-dog ๐ญ", callback_data="c1")
        ],
        [
            InlineKeyboardButton(text="๐ญ๐ญ Double Hot-dog ๐ญ๐ญ", callback_data="c2")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ญ Mini Hot-dog ๐ฝ๐ญ", callback_data="c3")
        ],
        [
            InlineKeyboardButton(text="๐ Kartoshka FRI ๐", callback_data="c4")
        ],
        [
            InlineKeyboardButton(text="๐๐ฅ Kartoshka po derevenski ๐ฅ๐", callback_data="c5")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ญ Kichik yoshdagilar uchun Hot-dog ๐ญ๐ฝ", callback_data="c6")
        ],
        [
            InlineKeyboardButton(text="๐๐ฅ Tovuqli Sab ๐ฅ๐", callback_data="c7")
        ],
        [
            InlineKeyboardButton(text="๐ฅฉ๐ฅ Mol go'shtli Sab ๐ฅ๐ฅฉ", callback_data="c8")
        ],
        [
            InlineKeyboardButton(text="๐ง๐๐ฅ Sir qo'shilgan Sab ๐ง๐๐ฅ", callback_data="c9")
        ],
        [
            InlineKeyboardButton(text="๐ง๐ฅฉ๐ฅ Sir qo'shilgan Sab ๐ง๐ฅฉ๐ฅ", callback_data="l2")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuShaur = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ฝ๐๐ฅฉ Mini mol go'shtli Shaurma ๐ฅฉ๐๐ฝ", callback_data="d1")
        ],
        [
            InlineKeyboardButton(text="๐๐ฅฉ Mol go'shtli Shaurma ๐ฅฉ๐", callback_data="d2")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐๐ Mini tovuqli Shaurma ๐๐๐ฝ", callback_data="d3")
        ],
        [
            InlineKeyboardButton(text="๐๐ Tovuqli Shaurma ๐๐", callback_data="d4")
        ],
        [
            InlineKeyboardButton(text="๐ถ๐๐ฅฉ Qalampirli Shaurma ๐ฅฉ๐๐ถ", callback_data="d5")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ถ๐๐ฅฉ Mini Qalampirli Shaurma ๐ฅฉ๐๐ถ๐ฝ", callback_data="d6")
        ],
        [
            InlineKeyboardButton(text="๐ถ๐๐ Qalampirli Shaurma ๐๐๐ถ", callback_data="d7")
        ],
        [
            InlineKeyboardButton(text="๐ฝ๐ถ๐๐ Mini Qalampirli Shaurma ๐๐๐ถ๐ฝ", callback_data="d8")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuGam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ Gamburger ๐", callback_data="e1")
        ],
        [
            InlineKeyboardButton(text="๐๐ Double Burger ๐๐", callback_data="e2")
        ],
        [
            InlineKeyboardButton(text="๐ง๐ Cheese burger ๐๐ง", callback_data="e3")
        ],
        [
            InlineKeyboardButton(text="๐ง๐๐ Double cheese burger ๐๐๐ง", callback_data="e4")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuAssorti = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ฅฉ Mol go'shtli danar ๐ฅฉ", callback_data="f1")
        ],
        [
            InlineKeyboardButton(text="๐ Tovuqli danar ๐", callback_data="f2")
        ],
        [
            InlineKeyboardButton(text="๐๐ Stripsi ๐๐", callback_data="f3")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuKombo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ญ๐ Kombo plyus ๐๐ญ", callback_data="g1")
        ],
        [
            InlineKeyboardButton(text="๐ญ๐ Detskoe Kombo ๐๐ญ", callback_data="g2")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuDesert = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐ฏ๐ฐ Medovik ๐ฐ๐ฏ", callback_data="h1")
        ],
        [
            InlineKeyboardButton(text="๐ง๐ฐ Cheese Cake ๐ฐ๐ง", callback_data="h2")
        ],
        [
            InlineKeyboardButton(text="๐ฉ๐ Donat yagodniy misks ๐๐ฉ", callback_data="h3")
        ],
        [
            InlineKeyboardButton(text="๐ฉ๐ญ Donat caramel ๐ญ๐ฉ", callback_data="h4")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuSous = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ketchup", callback_data="i1"),
            InlineKeyboardButton(text="Mayonez", callback_data="i2")
        ],
        [
            InlineKeyboardButton(text="Sir qo'shilgan sous", callback_data="i3"),
            InlineKeyboardButton(text="Chesnok qo'shilgan sous", callback_data="i4")
        ],
        [
            InlineKeyboardButton(text="Chili sous", callback_data="i5"),
            InlineKeyboardButton(text="Guruch", callback_data="i6")
        ],
        [
            InlineKeyboardButton(text="Salat", callback_data="i7"),
            InlineKeyboardButton(text="Non", callback_data="i8")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuSok = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sok Bliss. 1 litr", callback_data="j1")
        ],
        [
            InlineKeyboardButton(text="Pepsi 1.5 litr", callback_data="j2"),
            InlineKeyboardButton(text="Pepsi 0.5 litr", callback_data="j3")
        ],
        [
            InlineKeyboardButton(text="Gazsiz suv 0.5 litr", callback_data="j4"),
            InlineKeyboardButton(text="Pepsi razliv 0.4 litr", callback_data="j5")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

menuChoy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'k choy", callback_data="k1"),
            InlineKeyboardButton(text="Qora choy", callback_data="k2")
        ],
        [
            InlineKeyboardButton(text="Limonli ko'k choy", callback_data="k3"),
            InlineKeyboardButton(text="Limonli qora choy", callback_data="k4")
        ],
        [
            InlineKeyboardButton(text="Cappuccino", callback_data="k5"),
            InlineKeyboardButton(text="Americano", callback_data="k6")
        ],
        [
            InlineKeyboardButton(text="Latte", callback_data="k7"),
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

shaurmamenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="back")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

Lavashmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="ack")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

Hotdogmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l1")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)

Shaurmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l3")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Hamburgermenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l4")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Blyudamenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l5")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Combomenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l6")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Desertmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l7")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Sousmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l8")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Sokmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="l9")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
Choymenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="๐งบ Savatchaga qo'shish ๐งบ", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="๐ Ortga ๐", callback_data="m1")
        ],
        [
            InlineKeyboardButton(text="๐ฝ Menu ๐ฝ", callback_data="menu")
        ]
    ]
)
