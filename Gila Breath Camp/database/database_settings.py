import os
if "gila_testing_mode" in os.environ:
    DATABASE_NAME = "gila_testing.db"
else:
    DATABASE_NAME = "gila.db"
