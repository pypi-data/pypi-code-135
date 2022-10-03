import argparse
import sqlite3


parser = argparse.ArgumentParser('add_author_institute')
parser.add_argument('author', type=str)
parser.add_argument('institute', type=str)
args = parser.parse_args()


c = sqlite3.connect('authors_institutes.db')

c.executescript("INSERT OR IGNORE INTO author_institutes "
                "(author_name, institute_address) "
                f"VALUES('{args.author}', '{args.institute}');")
c.commit()

c.close()