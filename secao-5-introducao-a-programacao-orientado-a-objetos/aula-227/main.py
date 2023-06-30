from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, message):
        raise NotImplementedError()
    
    def error(self, message):
        return self._log(f"Error: {message}")
    
    def sucess(self, message):
        return self._log(f"Success: {message}")
    
class LogFileMixin(Log):
    def _log(self, message):
        with open(LOG_FILE, "a") as file:
            file.write(message + "\n")

class LogPrintMixin(Log):
    def _log(self, message):
        print(message)


if __name__ == "__main__":
    log = LogFileMixin()

    log.error("Ocorreu um erro!")
    log.sucess("Sucesso!")