"""
fetch data utilities
"""

import re
from typing import Callable, Optional, Tuple

import requests
import pandas as pd
from io import StringIO

from vietlott.crawler.requests_helper.config import TIMEOUT

from loguru import logger


def get_vietlott_cookie() -> Tuple[str, dict]:
    res = requests.get("https://vietlott.vn/ajaxpro/")
    match = re.search(r'document.cookie="(.*?)"', res.text)
    if match is None:
        raise ValueError(f"cookie is None, text={res.text}")
    cookie = match.group(1)
    cookies = {cookie.split("=")[0]: cookie.split("=")[1]}
    return cookie, cookies


def fetch_wrapper(
    url: str,
    headers: Optional[dict],
    org_params: Optional[dict],
    org_body: dict,
    process_result_fn: Callable,
    cookies: dict,
):
    """
    return a fn to fetch data for a set of params and body
    """

    def fetch(tasks):
        """
        perform fetching on multiple requests
        replace: org_params, org_body
        :param tasks: list of dict(task_id, task_data{params, body})
        :return:
        """
        tasks_str = ",".join(str(t["task_id"]) for t in tasks)
        logger.debug(f"worker start, tasks_ids={tasks_str}")
        _headers = headers.copy()

        results = []
        for task in tasks:
            task_id, task_data = task["task_id"], task["task_data"]
            params = org_params.copy()
            body = org_body.copy()

            params.update(task_data["params"])
            body.update(task_data["body"])

            # using proxy to avoid ban github ip
            proxies = get_proxies()
            #print(proxies)
            random = proxies.sample(1)
            proxy = {
                #"http": f"{random['IP Address']}:{random['Port']}",
                "https": f"{random['IP Address'].iloc[0]}:{random['Port'].iloc[0]}"
            }
            #print(proxy)
            
            res = requests.post(
                url,
                json=body,
                params=params,
                headers=_headers,
                cookies=cookies,
                timeout=TIMEOUT,
                proxies=proxy
            )

            if not res.ok:
                logger.error(
                    #f"req failed, args={task_data}, code={res.status_code}, headers={_headers}, params={params}, body={body}, res={res.text}, text={res.text[:200]}"
                    f"req failed, args={task_data}, code={res.status_code}, proxy={proxy}, res={res.text}"
                )
                continue
            try:
                result = process_result_fn(params, body, res.json(), task_data)
                results.append(result)
                logger.debug(f"task {task_id} done")
            except requests.exceptions.JSONDecodeError as e:
                logger.error(
                    f"json decode error, args={task_data}, text={res.text[:200]}, headers={headers}, cookies={cookies}, body={body}, params={params}"
                )
                raise e
        logger.debug(f"worker done, tasks={tasks_str}")
        return results

    return fetch

def get_proxies():
    resp = requests.get('https://free-proxy-list.net/') 
    df = pd.read_html(StringIO(resp.text))[0]
    #df = df[(df['Anonymity'] == 'elite proxy') & (df['Https'] == 'yes') & (df['Code'] == 'VN')]
    df = df[(df['Https'] == 'yes') & (df['Code'] == 'VN')]
    return df
