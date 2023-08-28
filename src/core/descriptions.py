class PagingDescription:
    limit: str = 'Количество записей на странице'
    page: str = 'Номер страницы'
    count: str = 'Кол-во страниц которое вернулось в ответе'


class SystemApiDescription:
    all_system_api = 'Получение информации по всем доступным системам'
    system_by_api = 'Получение информации по ID системы'
    system_service_api = 'Получение информации по сервисам, которые доступны для данной системы'


class SystemServiceDescription:
    main_teams_api: str = 'Получение информаии об основных командах, которые участвуют в предоставлении услуги'
    competence_teams_api: str = 'Получение информаии о командах компетенций'


class CategoryDescription:
    all_category_api: str = 'Информация о всех категориях систем/оборудования по которым предоставляется услуга'
    category_by_id_api: str = 'Получение информации о категории по ее ID'
    system_in_category_by_id_api: str = 'Получение списка систем/оборудования которые входят в категорию'
