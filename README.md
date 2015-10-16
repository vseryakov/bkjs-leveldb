# LevelDB module for node and backendjs

# Usage

```javascript
  var ldb = require("bkjs-levelb");
  var db = new ldb.Database("/tmp/test.ldb", { create_if_missing: 1, compression: 1 }, function(err) {

     this.put("key1", "value1");
     this.put("key2", "value2");
     this.select("key", "key", { begins_with: 1 }, function(err, rows) {
       console.log(rows);
     });

  });
```

## Database class
- `new Database(file, options, callback)` - create new database object
  - options:
    - paranoid_checks - 1 for more runtime checks
    - create_if_missing - 1 to crete new DB
    - error_if_exists - 1 to only open existing DB
    - write_buffer_size -
    - max_open_files - number of file handles
    - block_size - default is 4096
    - compression - 1 to use Snappy compression
    - block_cache - pass LevelDB block cache pointer
    - filter_policy - bloom filter policy bits per key
- Properties:
  - open - 1 if the db is open
  - name - the database file name
- Methods:
  - close - close the database
  - drop - drop the database file
  - get(key, callback) - return value for the given key
  - put(key, value, flags, callback) - store a value for the given key
  - incr(key, num, flags, callback) - increment a value by a number
  - del(key, value, callback]) - delete a key
  - select(start, end, flags, callback]) - return list of matching records
    The flags are:
     - desc - 1 to return in descendent order
     - begins_with - 1 if match by beginning of the start key
     - count - number of records to return
  - batch(list, flags, callback) - put several records at once in a batch,
    list item can be a string to delete or an array with 2 items to put

- Options or flags
  - Read options
    - fill_cache - 1 or 0
    - verify_checksum - 1 or 0
  - Write options
    - sync - 1 or 0

# Author

Vlad Seryakov

