# gpodder-exporter

A simple command-line tool to export gPodder podcast titles and RSS URLs to a CSV file. This tool is helpful when you want to extract the list of subscribed podcasts and their RSS feeds from gPodder without having to manually parse the configuration files, which are not human-readable.

This program simply reads the gPodder database file and extracts the podcast titles and RSS URLs from it. It then saves the extracted data to a CSV file.

## Installation

You can install `gpodder-exporter` using pip:

`pip install gpodder-exporter`

## Usage

To use `gpodder-exporter`, simply run the following command:

`gpodder-export`

By default, the tool will look for the gPodder database file in the current working directory and save the output to a file named `podcast_titles_and_rss_urls.csv`.

If your database file is located in a different folder, you can provide the path using the `--data_folder` option:


`gpodder-export --data_folder /path/to/your/data_folder`


To specify a custom output path for the CSV file, use the `--output` option:

`gpodder-exporter --output /path/to/your/output.csv`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
