"""This module contain class representing cli optional argument"""

from src.components.parser.arguments import ArgumentsAbstract


class Colorize(ArgumentsAbstract):

    def add_argument(self):
        self._parser.add_argument(
            '--colorize', default=False, action='store_true', help='Colorize console output'
        )
