from download.download_manager import DownloadManager
from utils.helper import PathManager
from utils.logger import logger


def main() -> None:
	path_manager = PathManager()
	download_manager = DownloadManager(path_manager)
	github_downloader = download_manager.create_github_downloader()
	database_path = github_downloader.download_database()
	logger.info("Datenbank geladen: %s", database_path)


if __name__ == "__main__":
	main()
