from pathlib import Path
import requests

from utils.helper import PathManager


class GitHubDownloader:
	def __init__(self, path_manager: PathManager, database_url: str) -> None:
		self.path_manager = path_manager
		self.database_url = database_url

	def download_database(self) -> Path:
		"""Lädt AD_DC.db in den Ordner src/database herunter."""
		return self.download(self.database_url, "AD_DC.db")

	def download(self, url: str, filename: str) -> Path:
		"""Koordiniert Abruf, Zielpfad und Speichern einer Datei."""
		content = self._download_content(url)
		destination = self._create_destination(filename)
		self._save_content(destination, content)
		return destination

	def _download_content(self, url: str) -> bytes:
		"""Ruft den Dateiinhalt von GitHub ab."""
		response = requests.get(url, timeout=30)
		response.raise_for_status()
		return response.content

	def _create_destination(self, filename: str) -> Path:
		"""Erstellt den Ordner für eine Datei."""
		destination = self.path_manager.src("database", filename)
		destination.parent.mkdir(parents=True, exist_ok=True)
		return destination

	def _save_content(self, destination: Path, content: bytes) -> None:
		"""Speichert Binärdaten am Zielpfad."""
		destination.write_bytes(content)
