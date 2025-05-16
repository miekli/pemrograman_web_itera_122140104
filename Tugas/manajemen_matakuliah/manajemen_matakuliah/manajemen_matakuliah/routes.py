def includeme(config):
    config.add_route('home', '/')
    config.add_route('get_matakuliah', '/matakuliah')
    config.add_route('get_matakuliah_by_id', '/matakuliah/{id}')
    config.add_route('create_matakuliah', '/matakuliah/tambah')
    config.add_route('update_matakuliah', '/matakuliah/edit/{id}')
    config.add_route('delete_matakuliah', '/matakuliah/hapus/{id}')
