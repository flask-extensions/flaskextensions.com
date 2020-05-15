from dynaconf import LazySettings

settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF="FEXAPI",
    ENV_SWITCHER_FOR_DYNACONF="FEXAPI_ENV",
)
