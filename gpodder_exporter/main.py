import argparse
import sqlite3
import os
import csv
from pathlib import Path


def get_podcast_titles_and_rss_urls(data_folder="."):
    database_file = os.path.join(data_folder, 'Database')

    if not os.path.isfile(database_file):
        raise Exception("gPodder database file not found")

    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT title, url FROM podcast")

    titles_and_urls = cursor.fetchall()
    conn.close()
    return titles_and_urls


def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Podcast Title', 'RSS Feed URL'])
        csv_writer.writerows(data)


def main():
    parser = argparse.ArgumentParser(description="Export gPodder podcast titles and RSS URLs to a CSV file.")
    parser.add_argument('-d', '--data_folder', default=os.getcwd(),
                        help="Path to the folder containing the gPodder database file. Defaults to the current working directory.")
    parser.add_argument('-o', '--output', default="podcast_titles_and_rss_urls.csv",
                        help="Output CSV file path. Defaults to 'podcast_titles_and_rss_urls.csv' in the current working directory.")
    args = parser.parse_args()

    data_folder = Path(args.data_folder).resolve()
    output_path = Path(args.output).resolve()

    titles_and_urls = get_podcast_titles_and_rss_urls(data_folder)
    save_to_csv(titles_and_urls, output_path)
    print(f"Podcast titles and RSS URLs saved to '{output_path}'")


if __name__ == '__main__':
    main()
