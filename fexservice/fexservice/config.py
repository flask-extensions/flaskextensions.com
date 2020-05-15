from dynaconf import LazySettings

from fexservice.validator import validators

settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF="FEXSERVICE",
    ENV_SWITCHER_FOR_DYNACONF="FEXSERVICE_ENV",
)

# Fire the validator settings
settings.validators.register(*validators)
settings.validators.validate()
