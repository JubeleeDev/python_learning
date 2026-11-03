import json
import sys
import httpx
import logging

from pathlib import Path

logger = logging.getLogger(__name__)

def get_data(url: str, page_id: int) -> httpx.Response:
    return httpx.get(f"{url}/{page_id}", timeout=5) 

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level="INFO")

    print("HTTP CLI. Type any number do you want to request from page, X - exit")
    while True:

        page_id_str = input("Please, type an id of requested page: ")

        match page_id_str:
            case "X" | "x":
                logger.info("bye!")
                break
            case _:
                try:
                    page_id = int(page_id_str)
                except ValueError:
                    logger.error("wrong type of id argument, it must be an integer")
                    continue

                resource = "https://jsonplaceholder.typicode.com/todos"

                try:
                    res = get_data(resource, page_id)
                except httpx.TimeoutException:
                    logger.error("timeout error. please, try again later")
                    continue
                except httpx.RequestError:
                    logger.error("request error while processing resource %s", resource)
                    continue


                if res.status_code == 200:
                    path = Path(__file__).resolve().parent
                    file_path = path / "httpdata.json"

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(res.json(), f, ensure_ascii=False, indent=4)

                    logger.info("write to json file is successfully")

                else:
                    logger.warning("something went wrong, response code is %s", res.status_code)