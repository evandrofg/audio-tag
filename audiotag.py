#!/usr/bin/env python3

import sys
import argparse
import gi
gi.require_version('Tracker', '1.0')
from gi.repository import Tracker

class Query:
    def title(filename, title):
        querystr = "INSERT OR REPLACE { ?f nie:title '"
        querystr = querystr + title
        querystr = querystr + "' } WHERE { ?f nie:url <"
        querystr = querystr + filename
        querystr = querystr + "> } "
        return querystr


class Application:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("uri", type=str, help="full uri of the file to edit")
        parser.add_argument("title", type=str, help="new title for the track")

        args = parser.parse_args()

        querystr = Query.title(args.uri, args.title)
        conn = Tracker.SparqlConnection.get(None)
        print(querystr)
        curs = conn.update (querystr, 0, None)


def main():
    app = Application()

if __name__ == "__main__":
    sys.exit(main())
