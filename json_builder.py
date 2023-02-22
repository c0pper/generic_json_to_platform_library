import json
from tqdm import tqdm
from pathlib import Path
from datetime import datetime
from platform_utils_eai.functions import create_tax_library_zip, create_folder_structure, normalize_fucked_encoding, \
    create_annotated_file
from csv_builder import make_json
from typing import Callable
from custom_preprocess import custom_prep
import random

ROOT_PATH = "C:/Users/smarotta/Desktop/silvanus4.4 ann"


def main(json_path: Path, text_key: str, annotations_key: str = "", custom_text_preprocessing_function: Callable = None):
    with open(json_path, "r", encoding="UTF8") as j:
        ds = json.loads(j.read())
    folders = create_folder_structure(ROOT_PATH)

    tax = []

    texts = []
    #  shuffle list of json objects
    json_objects_list = list(ds.values())
    random.Random(420).shuffle(json_objects_list)
    for idx, obj in enumerate(tqdm(json_objects_list[:12000])):
        try:
            text = obj[text_key]
            if custom_text_preprocessing_function:
                text = custom_text_preprocessing_function(text)
            if annotations_key:
                annotations = obj[annotations_key]
            else:
                annotations = []
            texts.append(text)
            # print(idx)

            create_annotated_file(
                folders=folders,
                filename=json_path.stem + str(idx),
                text=text,
                annotations=annotations
            )
        except KeyError:
            raise KeyError("Verifica che il nome della chiave contente il testo sia corretto")

    create_tax_library_zip(folders=folders)


if __name__ == "__main__":
    CSV_PATH = Path("input/All_tweets_public.csv")
    ROOT_PATH = "C:/Users/smarotta/Desktop/silvanus4.4 ann"
    jsonFilePath = Path("output/All_tweets_public.json")
    make_json(CSV_PATH, jsonFilePath, "UserID")
    main(
        json_path=jsonFilePath,
        text_key="Text",
        custom_text_preprocessing_function=custom_prep
    )
