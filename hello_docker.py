#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:10:04 2017

@author: RudradeepGuha
"""

import click

@click.command()

def intro():
    """Prints 'Hello, docker' to the console"""
    click.echo("Hello, docker")
    
if __name__ == '__main__':
    intro()
