# manajemen_matakuliah/db.py

from .models import DBSession

def get_session(request):
    return DBSession
