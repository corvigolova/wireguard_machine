from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    WL_AUTO_UPDATE_URL: str
    AppID: str
    debug_mode: bool = False