import json
from tqdm import tqdm
from pathlib import Path
from datetime import datetime
from platform_utils_eai.functions import create_libraries_zip, create_folder_structure, normalize_fucked_encoding, \
    create_annotated_file


ROOT_PATH = "C:/Users/smarotta/Desktop/silvanus4.4 ann"


def main(json_path: Path, text_key: str, annotations_key: str = ""):
    with open(json_path, "r", encoding="UTF8") as j:
        ds = json.loads(j.read())
    time = datetime.now().strftime('%d_%m_%y_%H_%M')
    folders = create_folder_structure(ROOT_PATH)

    tax = []

    texts = []
    for idx, obj in enumerate(tqdm(ds.values())):
    # for idx, obj in enumerate(tqdm(ds)):
    #     print(idx, obj)
        # if obj.get("relevant"):
        #     print(obj["relevant"])
        text = obj[text_key]
        if annotations_key:
            annotations = obj[annotations_key]
        else:
            annotations = []
        # print(json_path.stem + str(idx), text)
        texts.append(text)

        create_annotated_file(
            folders=folders,
            filename=json_path.stem + str(idx),
            text=text,
            annotations=annotations
        )

    create_libraries_zip(folders=folders)


if __name__ == "__main__":
    JSON_PATH = Path("beAWARE_Italian.json")
    main(
        json_path=JSON_PATH,
        text_key="text"
    )
