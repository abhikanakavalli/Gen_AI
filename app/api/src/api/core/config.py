# from pydantic_settings import BaseSettings, SettingsConfigDict

# class Config(BaseSettings):
#     OPENAI_API_KEY: str

#     model_config = SettingsConfigDict(env_file=".env")

# config = Config()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    OPENAIKEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


config = Config()