from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from sqlalchemy.exc import DBAPIError
from manajemen_matakuliah.models import Matakuliah  
from manajemen_matakuliah.db import get_session


@view_config(route_name='get_matakuliah', renderer='json', request_method='GET')
def get_matakuliah(request):
    session = get_session(request)
    matakuliahs = session.query(Matakuliah).all()
    return [{
        'id': m.id,
        'kode': m.kode,
        'nama': m.nama,
        'sks': m.sks,
        'dosen': m.dosen,
    } for m in matakuliahs]


@view_config(route_name='get_matakuliah_by_id', renderer='json', request_method='GET')
def get_matakuliah_by_id(request):
    session = get_session(request)
    id = request.matchdict.get('id')
    matakuliah = session.query(Matakuliah).filter(Matakuliah.id == id).first()
    if not matakuliah:
        return HTTPNotFound()
    return {
        'id': matakuliah.id,
        'kode': matakuliah.kode,
        'nama': matakuliah.nama,
        'sks': matakuliah.sks,
        'dosen': matakuliah.dosen,
    }


@view_config(route_name='create_matakuliah', renderer='json', request_method='POST')
def create_matakuliah(request):
    session = get_session(request)
    data = request.json_body
    matakuliah = Matakuliah(
        kode=data.get('kode'),
        nama=data.get('nama'),
        sks=data.get('sks'),
        dosen=data.get('dosen'),
    )
    session.add(matakuliah)
    session.commit()
    return {'status': 'success', 'id': matakuliah.id}


@view_config(route_name='update_matakuliah', renderer='json', request_method='PUT')
def update_matakuliah(request):
    session = get_session(request)
    id = request.matchdict.get('id')
    matakuliah = session.query(Matakuliah).filter(Matakuliah.id == id).first()
    if not matakuliah:
        return HTTPNotFound()
    data = request.json_body
    matakuliah.kode = data.get('kode', matakuliah.kode)
    matakuliah.nama = data.get('nama', matakuliah.nama)
    matakuliah.sks = data.get('sks', matakuliah.sks)
    matakuliah.dosen = data.get('dosen', matakuliah.dosen)
    session.commit()
    return {'status': 'updated'}


@view_config(route_name='delete_matakuliah', renderer='json', request_method='DELETE')
def delete_matakuliah(request):
    session = get_session(request)
    id = request.matchdict.get('id')
    matakuliah = session.query(Matakuliah).filter(Matakuliah.id == id).first()
    if not matakuliah:
        return HTTPNotFound()
    session.delete(matakuliah)
    session.commit()
    return {'status': 'deleted'}


# Ini WAJIB ditambahin biar error tadi gak muncul
def includeme(config):
    config.scan(__name__)
