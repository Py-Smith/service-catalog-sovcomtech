import logging
from functools import lru_cache
from uuid import UUID

from aioredis import Redis
from fastapi import Depends
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from db.postgres import get_session
from models.database.system import System, SystemCategory
# logger = logging.getLogger()

class SystemInfoService:

    def __init__(self, session: AsyncSession ):
        self.session = session


    async def get_all_systems(self) -> list:
        # TODO: Пример джоина с несколькими табицами

        # result = await self.session.execute(
        #     select(System.id.label('system_id'),
        #            System.name.label('system_name'),
        #            System.description.label('system_description'),
        #            SystemCategory.id.label
        #            )
        #     .select_from(System)
        #     .join(SystemCategory,
        #           System.category_id==SystemCategory.id)
        #     )
        result = await self.session.execute(
            select(System.id.label('system_id'),
                   System.name.label('system_name'),
                   System.description.label('system_description'),
                   System.category_id.label('category_id')
                   )
            .select_from(System)
            )

        return result.mappings().all()
    
    async def get_system_info(self, system_id: int) -> dict:
        result = await self.session.execute(
            select(System.id.label('system_id'),
                   System.name.label('system_name'),
                   System.description.label('system_description')
                   )
            .select_from(System)
            .where(System.id == system_id)
            )
        return result.mappings().first()
# class FilmService(ServiceMixin, RedisMixin):

#     _index_name = 'movies'

#     async def get_by_id(self, url: str, uuid: UUID) -> Film | None:
#         return await self.get_data(self._get_film_from_elastic, uuid=uuid)

#     async def _get_film_from_elastic(self, uuid: UUID) -> Film | None:
#         logger.info('get film by film_id:%s from es', uuid)
#         try:
#             doc = await self.elastic.get(index=self._index_name, id=str(uuid))
#         except NotFoundError:
#             logger.info('es data for film_id:%s not found', uuid)
#             return None
#         return Film(**doc['_source'])


# class FilmListService(ServiceMixin, RedisMixin):

#     _index_name = 'movies'
#     _size_return_es_data = 10000

#     async def get_all(self, url: str, sort: SortType, sort_direction: SortDirection, page_size: int, page_number: int,
#                       filter_genre: UUID = None, search_query: str = '') -> FilmList | None:
#         return await self.get_data(self._get_films_from_elastic, url=url, sort=sort, sort_direction=sort_direction,
#                                    page_size=page_size, page_number=page_number, filter_genre=filter_genre, search_query=search_query)

#     async def _get_films_from_elastic(self, url: str, sort: SortType, sort_direction: SortDirection,
#                                       page_size: int, page_number: int, filter_genre: UUID, search_query: str) -> FilmList | None:
#         logger.info('get films by %s from es', url)

#         sort_query = None
#         if sort and sort_direction:
#             sort_query = [{sort: {"order": sort_direction}}]

#         query = None
#         if filter_genre:
#             query = {
#                 'nested': {
#                     'path': 'genre',
#                     'query': {
#                         'match': {'genre.uuid': str(filter_genre)}
#                     }
#                 }
#             }
#         elif search_query:
#             query = {
#                 'query_string': {
#                     'fields': ['title'],
#                     'query': search_query
#                 }
#             }
#         elastic_query = {
#             'index': self._index_name,
#             'query': query,
#             'size': page_size,
#             'from_': (page_number - 1) * page_size,
#             'sort': sort_query
#         }
#         try:
#             films = await self.elastic.search(**elastic_query)
#             if not films['hits']['hits']:
#                 return None
#         except NotFoundError:
#             logger.info('es data for %s not found', url)
#             return None
#         if not films['hits']['hits']:
#             return None
#         elastic_query['from_'] = page_number * page_size
#         next_films = await self.elastic.search(**elastic_query)
#         next_page = False
#         if next_films['hits']['hits']:
#             next_page = True
#         return FilmList(films=[FilmShort(**item['_source']) for item in films['hits']['hits']], next_page=next_page)


# class FilmListByPersonService(ServiceMixin, RedisMixin):
#     _index_name = 'movies'
#     _size_return_es_data = 10000

#     async def get_by_person_id(self, url: str, person_uuid: UUID) -> FilmList | None:
#         return await self.get_data(self._get_films_from_elastic_by_person, url=url, person_uuid=person_uuid)

#     async def _get_films_from_elastic_by_person(self, url: str, person_uuid: UUID) -> list[FilmShort] | None:
#         logger.info('get films by %s from es', url)
#         sort_query = [{'imdb_rating': {'order': 'asc'}}]
#         query = {
#             'bool': {
#                 'should': [
#                     {'nested': {
#                         'path': 'actors',
#                         'query': {
#                             'match': {'actors.uuid': str(person_uuid)}
#                         }}},
#                     {'nested': {
#                         'path': 'writers',
#                         'query': {
#                             'match': {'writers.uuid': str(person_uuid)}
#                         }}},
#                     {'nested': {
#                         'path': 'directors',
#                         'query': {
#                             'match': {'directors.uuid': str(person_uuid)}
#                         }}},
#                 ]
#             }
#         }
#         try:
#             films = await self.elastic.search(
#                 index=self._index_name,
#                 query=query,
#                 size=self._size_return_es_data,
#                 sort=sort_query)
#         except NotFoundError:
#             logger.info('es data for %s not found', url)
#             return None
#         return [FilmShort(**item['_source']) for item in films['hits']['hits']]


# @lru_cache()
# def get_film_service(
#         redis: Redis = Depends(get_redis),
#         elastic: AsyncElasticsearch = Depends(get_elastic),
# ) -> FilmService:
#     return FilmService(redis, elastic)


# @lru_cache()
# def get_film_list_service(
#         redis: Redis = Depends(get_redis),
#         elastic: AsyncElasticsearch = Depends(get_elastic),
# ) -> FilmListService:
#     return FilmListService(redis, elastic)


@lru_cache()
def get_systems(
        session: AsyncSession = Depends(get_session),
) -> SystemInfoService:
    return SystemInfoService(session)
