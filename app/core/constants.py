RESPONSE_MODEL_EXCLUDE = (
    'user_id',
    'invested_amount',
    'fully_invested',
    'close_date'
)
DELETE_USER_405_DETAIL = 'Удаление пользователей запрещено!'
PROJECT_NOT_FOUND = 'Проект не найден!'
DETAIL_FOR_CHECK_DUPLICATE_NAME = 'Проект с таким именем уже существует!'
CLOSSED_PROJECT_CANT_EDIT = 'Закрытый проект нельзя редактировать!'
INVESTED_AMOUNT_IN_PROJECT_CANT_DELETE = 'В проект были внесены средства, не подлежит удалению!'
INCORRECT_FULL_AMOUNT = 'Нельзя установить требуемую cумму меньше уже вложенной'
APP_INFO = (
    'Фонд собирает пожертвования на различные целевые проекты: на медицинское '
    'обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в '
    'подвале, на корм оставшимся без попечения кошкам — на любые цели, '
    'связанные с поддержкой кошачьей популяции.'
)
APP_TITLE = 'Благотворительный фонд поддержки котиков QRKot.'
DATABASE_URL = 'sqlite+aiosqlite:///./fastapi.db'
SECRET = 'secret'
INVESTED_AMOUNT_DEFAULT = 0
MAX_LENGTH_CHARITY_PROJECT_NAME = 100