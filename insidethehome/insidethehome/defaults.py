
MESSAGE = "Hello World"

# Fully read every request to ensure the nginx and uwsgi play nice
FORCE_READ_REQUESTS = True

# Default logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(hostname)s | %(asctime)s | %(levelname)s | %(name)s | %(message)s"
        }
    },
    "filters": {
        "add_hostname": {
            "()": "timber.filters.HostnameAddingFilter"
        }
    },
    "handlers": {
        "file_handler": {
            "class": "logging.handlers.WatchedFileHandler",
            "formatter": "simple",
            "filename": "/var/log/insidethehome/insidethehome.log",
            "filters": ["add_hostname"]
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["file_handler"]
    },
}
