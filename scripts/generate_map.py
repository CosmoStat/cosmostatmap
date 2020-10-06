#! /usr/bin/env python
# -*- coding: utf-8 -*-

from cosmostatmap import CosmoStatMap


def main():

    CosmoStatMap('./data/countries.yml').save()


if __name__ == "__main__":
    main()
