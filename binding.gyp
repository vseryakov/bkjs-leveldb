{
    "target_defaults": {
      "defines": [
        "LEVELDB_PLATFORM_POSIX",
        "_REENTRANT",
        "_THREAD_SAFE",
        "_POSIX_PTHREAD_SEMANTICS",
        "UNSAFE_STAT_OK",
      ],
      "include_dirs": [
        ".",
        "bklib",
        "leveldb/include",
        "leveldb",
        "<(node_root_dir)/deps/openssl/openssl/include",
        "/opt/local/include",
        "<!(node -e \"require('nan')\")"
      ]
    },
    "targets": [
    {
      "target_name": "binding",
      "libraries": [
        "-L/opt/local/lib",
      ],
      "sources": [
        "binding.cpp",
        "leveldb/db/builder.cc",
        "leveldb/db/db_impl.cc",
        "leveldb/db/db_iter.cc",
        "leveldb/db/filename.cc",
        "leveldb/db/dbformat.cc",
        "leveldb/db/log_reader.cc",
        "leveldb/db/log_writer.cc",
        "leveldb/db/memtable.cc",
        "leveldb/db/repair.cc",
        "leveldb/db/table_cache.cc",
        "leveldb/db/version_edit.cc",
        "leveldb/db/version_set.cc",
        "leveldb/db/write_batch.cc",
        "leveldb/helpers/memenv/memenv.cc",
        "leveldb/table/block.cc",
        "leveldb/table/block_builder.cc",
        "leveldb/table/filter_block.cc",
        "leveldb/table/format.cc",
        "leveldb/table/iterator.cc",
        "leveldb/table/merger.cc",
        "leveldb/table/table.cc",
        "leveldb/table/table_builder.cc",
        "leveldb/table/two_level_iterator.cc",
        "leveldb/util/arena.cc",
        "leveldb/util/bloom.cc",
        "leveldb/util/cache.cc",
        "leveldb/util/coding.cc",
        "leveldb/util/comparator.cc",
        "leveldb/util/crc32c.cc",
        "leveldb/util/env.cc",
        "leveldb/util/env_posix.cc",
        "leveldb/util/filter_policy.cc",
        "leveldb/util/hash.cc",
        "leveldb/util/logging.cc",
        "leveldb/util/options.cc",
        "leveldb/util/status.cc",
        "leveldb/port/port_posix.cc"
      ],
      "conditions": [
        [ 'OS=="mac"', {
          "defines": [
            "OS_MACOSX",
          ],
          "xcode_settings": {
            "OTHER_CFLAGS": [
              "-g -fPIC",
            ],
          },
        }],
        [ 'OS=="linux"', {
          "defines": [
            "OS_LINUX",
          ],
          "cflags_cc+": [
            "-g -fPIC -rdynamic",
          ],
        }],
      ]
    }]
}
