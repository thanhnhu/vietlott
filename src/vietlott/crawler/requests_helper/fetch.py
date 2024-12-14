"""
fetch data utilities
"""

import re
from typing import Callable, Optional, Tuple

import requests
# from requests.exceptions import ProxyError, ReadTimeout, ConnectionError
# import urllib3
# from urllib3.exceptions import SSLError, InsecureRequestWarning, ConnectTimeoutError, NewConnectionError, ReadTimeoutError, MaxRetryError, TimeoutError, ConnectionError
# urllib3.disable_warnings(ConnectTimeoutError)
# urllib3.disable_warnings(NewConnectionError)

import pandas as pd
from io import StringIO

from vietlott.crawler.requests_helper.config import TIMEOUT

from loguru import logger

import threading


bad_proxies = []
lock = threading.Lock()

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
        # using proxy to avoid ban github ip
        proxies = get_proxies()
        # print(proxies)

        results = []
        for task in tasks:
            task_id, task_data = task["task_id"], task["task_data"]
            params = org_params.copy()
            body = org_body.copy()

            params.update(task_data["params"])
            body.update(task_data["body"])

            for index, row in proxies.iterrows():
                str_proxy = f"{row['IP Address']}:{row['Port']}"
                if str_proxy in bad_proxies: continue
                # print(f"proxy: {str_proxy}")

                proxy = { "http": str_proxy, "https": str_proxy }

                try:
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
                        bannedMess = "You are unable to access"
                        if bannedMess in res.text:
                            logger.error(
                                # f"req failed, args={task_data}, code={res.status_code}, headers={_headers}, params={params}, body={body}, res={res.text}, text={res.text[:200]}"
                                f"req failed, args={task_data}, code={res.status_code}, proxy={str_proxy}, res='Banned IP!!!'"
                            )
                        else:
                            logger.error(
                                # f"req failed, args={task_data}, code={res.status_code}, headers={_headers}, params={params}, body={body}, res={res.text}, text={res.text[:200]}"
                                f"req failed, args={task_data}, code={res.status_code}, proxy={str_proxy}, res={res.text}"
                            )
                        add_to_bad_list(str_proxy)
                        continue
                    try:
                        result = process_result_fn(params, body, res.json(), task_data)
                        results.append(result)
                        logger.debug(f"task {task_id}, proxy={str_proxy} done")
                        break # break the proxy loop
                    except Exception as error:
                        logger.error(
                            f"{type(error).__name__}, args={task_data}, text={res.text[:200]}, headers={headers}, cookies={cookies}, body={body}, params={params}"
                        )

                # handle exception on request
                except Exception as error:
                    # logger.error(f"{type(error).__name__}, task {task_id}, proxy={str_proxy}, error={error}")
                    logger.error(f"{type(error).__name__}, task {task_id}, proxy={str_proxy}")
                    add_to_bad_list(str_proxy)

        logger.debug(f"worker done, tasks={tasks_str}")
        return results

    return fetch


def get_proxies():
    resp = requests.get('https://free-proxy-list.net/')
    df = pd.read_html(StringIO(resp.text))[0]
    df = df[(df['Anonymity'] == 'elite proxy') & (df['Https'] == 'yes') & (df['Code'] == 'VN')]
    # filter if proxy is good
    # df = df[df.apply(lambda x: check_proxy(f"{x['IP Address']}:{x['Port']}"), axis=1)]
    return df


def check_proxy(proxy):
    checkApi = 'http://icanhazip.com'
    try:
        response = requests.get(checkApi, proxies={'https': '{proxy}'}, timeout=TIMEOUT)
        status = response.status_code
        return status == 200
    except Exception:
        return False

def add_to_bad_list(item):
    with lock:
        if item not in bad_proxies:
            bad_proxies.append(item)
