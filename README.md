This tool is designed to help data scientists hand label unlabeled datasets.

The tool currently only supports text data but will eventually support images and audio.

Usage:
python3 Main.py cfg.json

cfg.json:
{
    "data_type":"text",
    "data_path":"path_to_csv",
    "labels":["label1","label2"],
    "outfile":"out.csv"
}