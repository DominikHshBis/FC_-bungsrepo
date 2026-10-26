
from pathlib import Path
from typing import Any




class PathManager:
	"""Erzeugt projektweite, absolute Pfade unabhängig vom Arbeitsverzeichnis."""

	def __init__(self) -> None:
		self.project_root = Path(__file__).resolve().parents[2]

	def absolute(self, *parts: str | Path) -> Path:
		"""Gibt einen absoluten Pfad relativ zum Projekt oder direkt zurück."""
		path = Path(*parts).expanduser()
		if not path.is_absolute():
			path = self.project_root / path
		return path.resolve()

	def src(self, *parts: str | Path) -> Path:
		"""Gibt einen absoluten Pfad innerhalb des src-Ordners zurück."""
		return self.absolute("src", *parts)
    
class Helper():
    
    def read_yaml(self, file_path: str | Path, path_manager: PathManager) -> Any:
        import yaml
        """Liest eine YAML-Datei ein."""
        absolute_path = path_manager.absolute(file_path)
        with absolute_path.open("r", encoding="utf-8") as yaml_file:
            return yaml.safe_load(yaml_file)

    def read_json(self,file_path: str | Path, path_manager: PathManager) -> Any:
        import json
        """Liest eine JSON-Datei ein."""
        absolute_path = path_manager.absolute(file_path)
        with absolute_path.open("r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def load_service_config(self) -> Any:
	
        """Liest die service.yaml aus dem utils-Ordner ein."""
        path_manager = PathManager()
        service_file = path_manager.src("utils", "service.yaml")
        return self.read_yaml(service_file, path_manager)
