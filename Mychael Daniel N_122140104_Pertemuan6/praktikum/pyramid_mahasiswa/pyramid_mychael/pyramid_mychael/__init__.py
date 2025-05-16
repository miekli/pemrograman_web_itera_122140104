from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')

        # Tambahkan pyramid_tm agar request.tm tersedia
        config.include('pyramid_tm')

        config.scan()
    return config.make_wsgi_app()
