"""This module contain class representing cli positional argument"""

from src.components.parser.arguments.arguments_abstract import ArgumentsAbstract
import argparse
import urllib.request as url


class Source(ArgumentsAbstract):
    """This class representing implementation of ArgumentsAbstract
     interface and init a positional Source parameter"""

    def add_argument(self) -> argparse:
        """
        This method is implementation of add_argument abstract method
        add Source parameter from console for load feed
        :return: argparse
        """
        self._parser.add_argument(
            'source', type=str, help='RSS URL'
        )

    def _validate_source(self, source: str) -> str:
        """
        This method validate incoming required source parameter url checker exception
        :param source: str
        :return: str
        """
        try:
            if url.urlopen(source).getcode() is not 200:
                raise argparse.ArgumentError

            return source

        except argparse.ArgumentError:
            raise argparse.ArgumentError('Server answer code is not 200')

