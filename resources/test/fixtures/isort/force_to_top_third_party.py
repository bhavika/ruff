import os
from contextlib import contextmanager
from logging import getLogger
from typing import Optional
from typing import Union
from unittest.mock import patch

from local_module.constants import FOO_CONSTANT
from local_module.constants import BAR_CONSTANT
from local_module.constants import STAR_CONSTANT
from local_module.plugins.third_party_module.constants import CONSTANT_ENV
from local_module.plugins.third_party_module.exceptions import ThirdPartyModuleException

from third_party_module import API
from third_party_module import AnotherAPI
from third_party_module.exceptions import ThirdPartyRestException
