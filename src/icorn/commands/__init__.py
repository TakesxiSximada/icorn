import sys
import logging

import jumon


logger = logging.getLogger(__name__)


def main():
    rc = jumon.entry(__name__)
    logger.debug('Command exit: return code=%d', rc)
    sys.exit(rc)
