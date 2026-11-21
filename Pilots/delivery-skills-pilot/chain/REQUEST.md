# DEL-001 | Exclude archived pending orders from the count

The pilot product owner requests a count of pending orders that excludes archived pending orders. Keep old records without an archive flag active. Pending means the exact status `pending`; leave other statuses, empty inputs and the order data untouched. Scope is the existing Python counting helper and its tests, with no dependencies or new cash spend.
