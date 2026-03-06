"""Punto de entrada principal de la aplicación."""

from src.config_loader import load_runtime_config
from src.acquisition.polling_manager import PollingManager
from src.historian.historian_service import HistorianService
from src.alarms.alarm_engine import AlarmEngine


def main() -> None:
    """Inicializa los servicios principales y arranca la aplicación."""
    config = load_runtime_config()

    historian = HistorianService(config=config)
    alarm_engine = AlarmEngine(config=config)
    polling_manager = PollingManager(
        config=config,
        historian=historian,
        alarm_engine=alarm_engine,
    )

    print("[INFO] Aplicación inicializada correctamente.")
    print(f"[INFO] Proyecto(s) cargado(s): {', '.join(config.projects)}")
    print("[INFO] Arranque de servicios de adquisición...")

    # En una implementación real, aquí se lanzarían bucles asíncronos,
    # hilos o servicios independientes.
    polling_manager.describe_startup()


if __name__ == "__main__":
    main()
