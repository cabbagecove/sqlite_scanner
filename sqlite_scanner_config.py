import os

# list all include directories
include_directories = [
    os.path.sep.join(x.split('/')) for x in ['extension/sqlite_scanner/src/include', 'extension/sqlite_scanner/src/include/storage']
]
# source files
source_files = [
    os.path.sep.join(x.split('/'))
    for x in [
        'extension/sqlite_scanner/src/storage/sqlite_catalog.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_delete.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_index_entry.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_index.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_insert.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_schema_entry.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_table_entry.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_transaction_manager.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_transaction.cpp',
        'extension/sqlite_scanner/src/storage/sqlite_update.cpp',

        'extension/sqlite_scanner/src/sqlite_db.cpp',
        'extension/sqlite_scanner/src/sqlite_extension.cpp',
        'extension/sqlite_scanner/src/sqlite_scanner.cpp',
        'extension/sqlite_scanner/src/sqlite_stmt.cpp',
        'extension/sqlite_scanner/src/sqlite_storage.cpp',
        'extension/sqlite_scanner/src/sqlite_utils.cpp',
    ]
]

