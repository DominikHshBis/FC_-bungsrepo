from download.github_download import GitHubDownloader

from utils.helper import PathManager, Helper


class DownloadManager:
	"""Factory für die benötigten Downloader."""

	def __init__(self, path_manager: PathManager) -> None:
		self.path_manager = path_manager
		self.config = Helper().load_service_config()
		self.github_downloader = self.create_github_downloader()

	def create_github_downloader(self) -> GitHubDownloader:
		"""Erstellt den GitHub-Downloader."""
		
		database_url = self.config["services"]["download_urls"]["mein_github"]["url"]
		return GitHubDownloader(self.path_manager, database_url)
