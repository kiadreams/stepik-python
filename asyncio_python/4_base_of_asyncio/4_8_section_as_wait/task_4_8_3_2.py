import asyncio

data = [
    {
        "Имя": "Sarah",
        "Фамилия": "Lewis",
        "Возраст": 54,
        "Навыки": 10,
        "Страна проживания": "Tuvalu",
        "Город проживания": "North Heathertown",
        "Уровень секретности": 1,
        "Псевдоним": "michelestanton",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "5857 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Turner, Craig and Ortiz",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Kevin",
        "Фамилия": "Watkins",
        "Возраст": 42,
        "Навыки": 6,
        "Страна проживания": "Bosnia and Herzegovina",
        "Город проживания": "Peterview",
        "Уровень секретности": 9,
        "Псевдоним": "gonzalezcarl",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "7446 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Bailey-Hughes",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Andrew",
        "Фамилия": "Allen",
        "Возраст": 22,
        "Навыки": 7,
        "Страна проживания": "American Samoa",
        "Город проживания": "Rebeccatown",
        "Уровень секретности": 2,
        "Псевдоним": "phorton",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "1652 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Davis and Sons",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Amanda",
        "Фамилия": "Smith",
        "Возраст": 60,
        "Навыки": 4,
        "Страна проживания": "Greenland",
        "Город проживания": "Elliottview",
        "Уровень секретности": 1,
        "Псевдоним": "ramirezmichael",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "6185 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Atkins, Estrada and Estes",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Samantha",
        "Фамилия": "Nguyen",
        "Возраст": 36,
        "Навыки": 5,
        "Страна проживания": "San Marino",
        "Город проживания": "West Christophermouth",
        "Уровень секретности": 9,
        "Псевдоним": "jimenezdaniel",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "2346 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Murray-Braun",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "David",
        "Фамилия": "Ingram",
        "Возраст": 39,
        "Навыки": 4,
        "Страна проживания": "Bahamas",
        "Город проживания": "North Austin",
        "Уровень секретности": 1,
        "Псевдоним": "jjackson",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "3363 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Spears and Sons",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Emma",
        "Фамилия": "Richardson",
        "Возраст": 59,
        "Навыки": 9,
        "Страна проживания": "French Guiana",
        "Город проживания": "North Nicolefurt",
        "Уровень секретности": 9,
        "Псевдоним": "velazquezkara",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "115 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Davenport-Fowler",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Brian",
        "Фамилия": "Aguilar",
        "Возраст": 47,
        "Навыки": 7,
        "Страна проживания": "Belgium",
        "Город проживания": "Herreraland",
        "Уровень секретности": 6,
        "Псевдоним": "cschaefer",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "2947 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Lee Inc",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Samantha",
        "Фамилия": "Chang",
        "Возраст": 41,
        "Навыки": 1,
        "Страна проживания": "Niger",
        "Город проживания": "Lake Juan",
        "Уровень секретности": 4,
        "Псевдоним": "mortontracy",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "6693 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Aguilar, Williams and Davis",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Brandon",
        "Фамилия": "Williams",
        "Возраст": 32,
        "Навыки": 10,
        "Страна проживания": "United States of America",
        "Город проживания": "Pattersonshire",
        "Уровень секретности": 2,
        "Псевдоним": "andrew89",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "2810 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Richardson-Jones",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Michael",
        "Фамилия": "Strickland",
        "Возраст": 52,
        "Навыки": 3,
        "Страна проживания": "Uganda",
        "Город проживания": "East Jordan",
        "Уровень секретности": 7,
        "Псевдоним": "christina71",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": None,
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Smith-Mayer",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Kyle",
        "Фамилия": "Barnett",
        "Возраст": 47,
        "Навыки": 3,
        "Страна проживания": "Taiwan",
        "Город проживания": "Kevinfort",
        "Уровень секретности": 1,
        "Псевдоним": "michaelburns",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "7745 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Parrish, Cox and Thomas",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Damon",
        "Фамилия": "Alvarado",
        "Возраст": 36,
        "Навыки": 10,
        "Страна проживания": "Egypt",
        "Город проживания": "Lamfort",
        "Уровень секретности": 5,
        "Псевдоним": "collinsmelissa",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "3894 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Banks Group",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Cindy",
        "Фамилия": "Sanchez",
        "Возраст": 50,
        "Навыки": 2,
        "Страна проживания": "Guinea-Bissau",
        "Город проживания": "Wademouth",
        "Уровень секретности": 9,
        "Псевдоним": "pennykeller",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "4045 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Rice Group",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Michelle",
        "Фамилия": "Hernandez",
        "Возраст": 44,
        "Навыки": 8,
        "Страна проживания": "Bahamas",
        "Город проживания": "Reedtown",
        "Уровень секретности": 3,
        "Псевдоним": "adriangentry",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "2744 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Cox, Smith and Richards",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Whitney",
        "Фамилия": "Ross",
        "Возраст": 30,
        "Навыки": 7,
        "Страна проживания": "Kazakhstan",
        "Город проживания": "Lovemouth",
        "Уровень секретности": 10,
        "Псевдоним": "lorismith",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "2687 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Williams, Butler and Rowland",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Deborah",
        "Фамилия": "Golden",
        "Возраст": 35,
        "Навыки": 3,
        "Страна проживания": "Belize",
        "Город проживания": "South Kathryn",
        "Уровень секретности": 2,
        "Псевдоним": "atkinstyler",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "698 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Pearson and Sons",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Nicholas",
        "Фамилия": "Whitaker",
        "Возраст": 44,
        "Навыки": 6,
        "Страна проживания": "United Kingdom",
        "Город проживания": "South Curtis",
        "Уровень секретности": 10,
        "Псевдоним": "rebeccaandrews",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "47 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Harrington-Wells",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Rebecca",
        "Фамилия": "Mercer",
        "Возраст": 59,
        "Навыки": 6,
        "Страна проживания": "Mayotte",
        "Город проживания": "Angelaborough",
        "Уровень секретности": 4,
        "Псевдоним": "jennifertaylor",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "141 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Stout Ltd",
        "Специализация": "Контрразведка"
    },
    {
        "Имя": "Mary",
        "Фамилия": "Mora",
        "Возраст": 27,
        "Навыки": 3,
        "Страна проживания": "Northern Mariana Islands",
        "Город проживания": "Wheelermouth",
        "Уровень секретности": 1,
        "Псевдоним": "ryanhernandez",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "4474 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Marquez-Mitchell",
        "Специализация": "Контрразведка"
    }
]


async def check_access(data_elem: dict[str, str | int | dict[str, str] | list[str]]) -> None:
    access_period = await asyncio.sleep(
        data_elem['Уровень секретности'],
        data_elem.get('Срок доступа')
    )
    if access_period is None:
        raise ValueError(
            f'Ошибка доступа: У участника {data_elem["Имя"]} {data_elem["Фамилия"]} срок доступа истек или не указан.'
        )
    print(
        f'Участник {data_elem["Имя"]} {data_elem["Фамилия"]} имеет действующий доступ. Продолжительность доступа: '
        f'{data_elem["Срок доступа"]}',
    )


async def main():
    tasks = [
        asyncio.create_task(check_access(person_data), name=f'{person_data['Имя']} {person_data['Фамилия']}')
        for person_data in data
    ]
    done, pending = await asyncio.wait(tasks, return_when='FIRST_EXCEPTION')
    if pending:
        exc_task = filter(lambda x: x.exception() is not None, done)
        print(next(exc_task).exception())
        for task in pending:
            task.cancel()
            print(f'Доступ участника {task.get_name()} отменен из-за критической ошибки.')


asyncio.run(main())
