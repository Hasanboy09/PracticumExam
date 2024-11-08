REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'Practicum exam API',
    'DESCRIPTION': 'Exam API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}