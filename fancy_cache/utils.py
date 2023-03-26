import hashlib
import logging
import time
import typing


LOGGER = logging.getLogger(__name__)


def md5(x) -> str:
    return hashlib.md5(x.encode("utf-8")).hexdigest()


def filter_remembered_urls(
    remembered_urls: typing.Dict[str, typing.Tuple[str, int]],
) -> typing.Dict[str, typing.Tuple[str, int]]:
    """
    Filter out any expired URLs from Fancy Cache's remembered urls.
    """
    now = int(time.time())
    # TODO: Remove the check for tuple in a future release as it will
    # no longer be needed once the new dictionary structure {url: (cache_key, expiration_time)}
    # has been implemented.
    remembered_urls = {
        key: value
        for key, value in remembered_urls.items()
        if isinstance(value, tuple) and value[1] > now
    }
    filtered_urls = [
        key
        for key, value in remembered_urls.items()
        if "/clubs/" in key and "/messages/" in key and isinstance(value, tuple) and value[1] < now
    ]
    LOGGER.info("fancy_cache.filter_remembered_urls: filtering these URLs: %s", filtered_urls)

    return remembered_urls
