"""
Python Is Easy course @Pirple.com
Homework Assignment #10: Importing
Patrick Kalkman / patrick@simpletechture.nl

Details:

Pick any library that come with Python (https://docs.python.org/3/library/)
that we haven't covered in the course already.

Learn how to use the library extensively, then prepare a code sample that
showcases what you've learned. This can take any form you wish. You could
create an application with the library, or just show examples of how to use
its methods.


Extra Credit:

Share your knowledge with the community by writing a blog post instead of
just uploading a code sample! You don't need to mention this class at all,
just share what you've learned about that library. If you've been meaning to
start a coding blog, now you have a reason to do it! If you take this route,
just send us the link to the post instead of to your Github code,

"""

# I have looked into the standard Python logging library.
# Below a small sample that shows how to perform logging.
# In addition, I wrote a blog post about this using this library.
# See:
# https://medium.com/@pkalkman/python-logging-basics-458ad969e850?sk=8964aeeefdec9fb6ff05c5198545d94c

import logging

log = logging.getLogger("app")

sh = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
sh.setFormatter(formatter)
log.addHandler(sh)

log.addHandler(logging.FileHandler('logging.txt'))
log.setLevel(logging.DEBUG)

log.info("Starting application")
for row in range(10):
    log.info(f"Another log line {row}")
