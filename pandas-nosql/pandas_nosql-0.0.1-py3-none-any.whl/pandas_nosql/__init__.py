from pymongo import MongoClient
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import redis
from cassandra.cluster import Cluster, BatchStatement
import pandas
from io import BytesIO
import pickle


def read_mongo(
        database: str,
        collection: str,
        normalize: bool = False,
        **mongo_client_kwargs):
    '''Read a MongoDB collection into a Pandas DataFrame'''
    with MongoClient(**mongo_client_kwargs) as client:
        db = client[database]
        collection = db[collection]
        if normalize:
            data = pandas.json_normalize(collection.find(), sep='_')
        else:
            data = pandas.DataFrame.from_records(collection.find())
    return data


pandas.read_mongo = read_mongo


def to_mongo(
        self,
        database: str,
        collection: str,
        modify_collection: bool = False,
        **mongo_client_kwargs):
    '''Insert DataFrame records into a MongoDB collection. Equivalent to insert_many'''
    with MongoClient(**mongo_client_kwargs) as client:
        db = client[database]
        if collection in db.list_collection_names() and not modify_collection:
            raise NameError(
                f'{collection!r} already exists in collection. Set modify_collection to True to modify.')
        collection = db[collection]
        collection.insert_many(self.to_dict(orient='records'))


pandas.core.frame.DataFrame.to_mongo = to_mongo


def read_elastic(
        hosts: str,
        index: str,
        username: str,
        password: str,
        fields: tuple,
        verify_certs: bool = False,
        normalize: bool = False,
        **kwargs):
    '''Read an Elasticsearch index into a Panda DataFrame'''
    assert isinstance(fields, tuple), 'fields must be a tuple'
    with Elasticsearch(hosts, basic_auth=(username, password), verify_certs=verify_certs, **kwargs) as es:
        data = es.search(index=index, body={'_source': fields})['hits']['hits']
    if normalize:
        dataframe = pandas.json_normalize(data)
        dataframe.columns = dataframe.columns.str.removeprefix('_source.')
        return dataframe.drop(columns='_score')
    return pandas.DataFrame.from_records(data).drop(columns='_score')


pandas.read_elastic = read_elastic


def to_elastic(
        self,
        hosts: str | list,
        username: str,
        password: str,
        index: str,
        verify_certs: bool = False,
        create_index: bool = False,
        stats_only: bool = True,
        **kwargs):
    '''Insert DataFrame records into an Elasticsearch index. Equivalent to bulk insert'''
    with Elasticsearch(hosts, basic_auth=(username, password), verify_certs=verify_certs, **kwargs) as es:
        if not es.indices.exists(index=index) and not create_index:
            raise IndexError(
                f'Elastic index {index!r} does not exist and {create_index=}')
        elif not es.indices.exists(index=index) and create_index:
            es.indices.create(index=index)
        docs = (
            {'_index': index, '_source': value}
            for value in self.to_dict(orient='index').values()
        )
        bulk(es, docs, stats_only=stats_only)


pandas.core.frame.DataFrame.to_elastic = to_elastic


def read_redis(host: str, port: int, redis_key: str, db: int=0):
    '''Read a pandas DataFrame which was saved to Redis using "pandas.to_redis"
    Any DataFrames read that was not saved using "pandas.to_redis" is not guaranteed
    to appear as expected.
    '''
    with redis.Redis(host=host, port=port, db=db) as r:
        return pandas.read_pickle(BytesIO(r.get(redis_key)))


pandas.read_redis = read_redis


def to_redis(self, host: str, port: int, redis_key: str, db: int=0, expire_seconds=None):
    '''Save DataFrame into Redis under the given redis_key.
    expire_seconds is optional. If None then redis_key will persist.
    '''
    with redis.Redis(host=host, port=port, db=db) as r:
        if expire_seconds is None:
            r.set(redis_key, pickle.dumps(self))
        else:
            r.set(redis_key, pickle.dumps(self))
            r.expire(redis_key, expire_seconds)


pandas.core.frame.DataFrame.to_redis = to_redis


def read_cassandra(contact_points: list, port: int, keyspace: str, table: str):
    '''Read an Apache Cassandra table into a Panda DataFrame'''
    with Cluster(contact_points=contact_points, port=port) as cluster:
        session = cluster.connect(keyspace=keyspace)
        rows = [row for row in session.execute(f'SELECT * FROM {table};')]
        return pandas.DataFrame.from_records(rows, columns=rows[0]._fields)


pandas.read_cassandra = read_cassandra


def to_cassandra(
        self,
        contact_points: list,
        port: int,
        keyspace: str,
        table: str):
    with Cluster(contact_points=contact_points, port=port) as cluster:
        cols = ','.join(self.columns)
        session = cluster.connect(keyspace=keyspace)
        qs = ('?,' * len(self.columns)).rstrip(',')
        insertions = session.prepare(
            f'INSERT INTO {table} ({cols}) VALUES ({qs})')
        batch = BatchStatement()
        for cols in self.itertuples(index=False):
            batch.add(insertions, cols)
        session.execute(batch)


pandas.core.frame.DataFrame.to_cassandra = to_cassandra
