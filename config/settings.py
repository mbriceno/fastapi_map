from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Map My World"
    app_description: str = "Aplicacion de microservicios para el manejo de CRUD de ubicaciones y categorías" 
    db_user: str
    db_host: str
    db_name: str
    db_port: str
    db_user: str
    db_password: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
