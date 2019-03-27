#!/usr/bin/env python

import argparse

import rdflib


def convert(ttl_path, rdf_path):
    """Convert a .ttl ontology to .rdf syntax."""
    g = rdflib.Graph()
    g.parse(ttl_path, format='turtle')
    g.serialize(rdf_path, format='xml')


def main():
    """Convert a .ttl ontology to .rdf syntax."""
    parser = argparse.ArgumentParser()
    parser.add_argument('ttl_path')
    parser.add_argument('rdf_path')
    args = parser.parse_args()
    convert(args.ttl_path, args.rdf_path)


if __name__ == '__main__':
    main()
