from datetime import date, datetime

from asyncpg import UniqueViolationError

from db_api.db_gino import db
from db_api.schemas.specialist import Specialist

async def create_db_specialist():
    spec1 = Specialist(id=1, new_queue=0, on_reception="0", num_window=1, start_talon="ОИС-", name_spec="Орехова И.С.", ip_address="192.168.0.105",
                       description="Подписание док-ов,\nсоздание списков на стипендии,\nобщие вопросы", bakalavr=1, specialist=0)
    await spec1.create()
    spec2 = Specialist(id=2, new_queue=0, on_reception="0", num_window=2, start_talon="ДАА-", name_spec="Данилова А.А.", ip_address="192.168.0.2",
                       description="Обеспечение движения контингента,\nподготовка справок о согласии на перевод,\nподготовка справок об обучении,\nпроставление оценок в БРС", bakalavr=1, specialist=1)
    await spec2.create()
    spec3 = Specialist(id=3, new_queue=0, on_reception="0", num_window=3, start_talon="КМС-", name_spec="Курочкина М.С.", ip_address="192.168.0.3",
                       description="Вопросы по экзаменам, поселение студентов,\nвыдача студика и пропуска,\nвопросы по учебе", bakalavr=1, specialist=0)
    await spec3.create()
    spec4 = Specialist(id=4, new_queue=0, on_reception="0", num_window=4, start_talon="ХЕА-", name_spec="Худякова Е.А.", ip_address="192.168.1.1.1",
                       description="Вопросы по экзаменам, вопросы по учебе", bakalavr=1, specialist=0)
    await spec4.create()
    spec5 = Specialist(id=5, new_queue=0, on_reception="0", num_window=5, start_talon="АИВ-", name_spec="Антропова И.В.", ip_address="192.168.0.4",
                       description="Выдача справок, работа с заболевшими Covid,\nработа с иностранными студентами, заочники", bakalavr=1, specialist=1)
    await spec5.create()
    spec6 = Specialist(id=6, new_queue=0, on_reception="0", num_window=6, start_talon="ВАВ-", name_spec="Волкова А.В.", ip_address="192.168.0.5",
                       description="Успеваемость на онлайн-курсах и майнорах,\nвыгрузка НТК", bakalavr=1, specialist=0)
    await spec6.create()
    spec7 = Specialist(id=7, new_queue=0, on_reception="0", num_window=7, start_talon="КНГ-", name_spec="Кийко Н.Г.", ip_address="192.168.0.6",
                       description="Формирование расписания и\nграфика пересдач", bakalavr=1, specialist=1)
    await spec7.create()
    spec8 = Specialist(id=8, new_queue=0, on_reception="0", num_window=8, start_talon="ТЛН-", name_spec="Тараненко Л.Н.", ip_address="192.168.0.7",
                       description="Формирование расписания ИОТ и\nграфика пересдач", bakalavr=1, specialist=0)
    await spec8.create()
    spec9 = Specialist(id=9, new_queue=0, on_reception="0", num_window=9, start_talon="КНА-", name_spec="Козырева Н.А.", ip_address="192.168.0.8",
                       description="Льготники, назначение стипендий,\nназначение мат. помощи", bakalavr=1, specialist=1)
    await spec9.create()
    spec10 = Specialist(id=10, new_queue=0, on_reception="0", num_window=10, start_talon="БГВ-", name_spec="Бутусова Г.В.", ip_address="192.168.0.9",
                        description="Подписание документов, стипендии,\nвыдача справок, мат. помощь", bakalavr=0, specialist=1)
    await spec10.create()


async def get_last_queue(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    last_queue = spec.last_queue
    if last_queue:
        return int(last_queue) + 1
    return 1


async def get_len_queue(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    if spec.queue:
        return len(spec.queue)
    return 0


async def add_to_queue(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    queue = spec.queue
    last_index = spec.last_queue
    if queue:
        queue.append(int(last_index) + 1)
        await spec.update(last_queue=last_index+1).apply()
    elif not last_index:
        queue = [1]
        await spec.update(last_queue=1).apply()
    else:
        queue = [int(last_index) + 1]
        await spec.update(last_queue=last_index+1).apply()
    # отправить запрос на клиент
    await spec.update(queue=queue).apply()


async def next_queue(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    queue = spec.queue
    start_talon = spec.start_talon
    if queue:
        start_talon += str(queue[0])
        queue.pop(0)
        await spec.update(queue=queue).apply()
        await on_reception_add(id, start_talon)
    else:
        start_talon = 0
        await on_reception_del(id)
    return start_talon


async def get_name_and_num_win(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    return spec.name_spec, spec.num_window


async def get_ip_address(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    return spec.ip_address


async def get_id_by_name(name: str):
    spec = await Specialist.query.where(Specialist.name_spec == name).gino.first()
    return int(spec.id)


async def get_start_talon(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    return spec.start_talon


async def read_new_queue(id:int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    if spec.new_queue == 1:
        await spec.update(new_queue=0).apply()
        return 1
    return 0


async def update_new_queue(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    await spec.update(new_queue=1).apply()


async def get_id_by_ip(ip: str):
    spec = await Specialist.query.where(Specialist.ip_address == ip).gino.first()
    return spec.id


async def on_reception_add(id: int, talon: str):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    await spec.update(on_reception=talon).apply()


async def on_reception_del(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    await spec.update(on_reception="0").apply()


async def on_reception_get(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    return spec.on_reception


async def get_description(id: int):
    spec = await Specialist.query.where(Specialist.id == id).gino.first()
    return spec.description


async def get_ids_bakalavr():
    all_specs = await Specialist.query.where(Specialist.bakalavr == 1).gino.all()
    arr = []
    for spec in all_specs:
        arr.append(spec.id)
    return sorted(arr)


async def get_ids_specialist():
    all_specs = await Specialist.query.where(Specialist.specialist == 1).gino.all()
    arr = []
    for spec in all_specs:
        arr.append(spec.id)
    return sorted(arr)


async def get_all_ids():
    all_specs = await Specialist.query.gino.all()
    arr = []
    for spec in all_specs:
        arr.append(spec.id)
    return sorted(arr)