import environ

env = environ.Env()
env_file = environ.Path('.env')

environ.Env.read_env(env_file)

# DATABASES = {
#     'default': env.db()
# }