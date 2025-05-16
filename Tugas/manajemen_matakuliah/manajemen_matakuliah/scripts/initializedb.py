from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from manajemen_matakuliah.models import Base
import transaction

def main(argv=None):
    """Script to initialize the database."""
    from pyramid.paster import get_appsettings
    import sys

    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print("Usage: initialize_db <config_uri>")
        sys.exit(1)

    config_uri = argv[1]
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')

    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

if __name__ == '__main__':
    main()
