"""
S3 storages with predefined locations, to separate static files and user uploads.
"""
from storages.backends.s3boto import S3BotoStorage

# Static location with predefined location
S3BotoStorageStatic = lambda: S3BotoStorage(location='static')

# Media (user uploads) location with predefined location
S3BotoStorageMedia  = lambda: S3BotoStorage(location='media')
