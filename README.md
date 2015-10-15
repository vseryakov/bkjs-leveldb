# LevelDB module for node and backendjs

# Usage

## Database class
- `new Database(file, options, callback)` - create new database object
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

