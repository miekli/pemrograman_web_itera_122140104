from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('.routes')    # sesuaikan path routes.py
    config.include('.views')     # kalau kamu juga mau load views lain yang tidak di routes
    config.scan()
    return config.make_wsgi_app()
