import os
__access_key_id = os.getenv('AWS_ACCESS_KEY_ID_ENV_KEY')
print(__access_key_id)
__secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY_ENV_KEY')
print(__secret_access_key)
