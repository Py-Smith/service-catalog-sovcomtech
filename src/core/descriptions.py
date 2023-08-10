class PagingDescription:
    page_size = 'Количество записей на странице'
    page_number = 'Номер страницы'


class FilmApiDescription:
    endpoint_film = 'Просмотр страницы фильма'
    endpoint_films = 'Список фильмов'
    sort = 'Тип сортировки'
    filter_genre = 'uuid жанра'
    endpoint_film_search = 'Поиск по фильмам'
    query = 'Запрос для поиска по наименованиям фильмов'


class GenreApiDescription:
    endpoint_genre = 'Информация о жанре'
    endpoint_genres = 'Список жанров'


class PersonApiDescription:
    endpoint_person_search = 'Информация о жанре'
    query = 'Запрос для поиска по фио персоны'
    endpoint_person = 'Список жанров'
    endpoint_person_films = 'uuid жанра'
