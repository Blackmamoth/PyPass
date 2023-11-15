from rich.console import Console


class ConsoleLogger:
    conosole = Console()

    @staticmethod
    def info(text):
        ConsoleLogger.conosole.print(
            f":bulb: {text}", style="bold green", justify="left"
        )

    @staticmethod
    def error(text):
        ConsoleLogger.conosole.print(f":x: {text}", style="bold red", justify="left")
