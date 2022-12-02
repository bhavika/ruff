import os
from contextlib import contextmanager
from logging import getLogger
from typing import Optional
from typing import Union
from unittest.mock import patch

from merlin_pipelines.constants import MERLIN_PROJECT_NAME_ENV
from merlin_pipelines.constants import MERLIN_PROJECT_PATH_ENV
from merlin_pipelines.constants import SHOPIFY_TEAM_NAME_ENV
from merlin_pipelines.plugins.cometml.constants import COMET_GIT_DIRECTORY_ENV
from merlin_pipelines.plugins.cometml.exceptions import WrappedCometApiException

from comet_ml import API
from comet_ml import BaseExperiment
from comet_ml import ExistingExperiment
from comet_ml import Experiment
from comet_ml.exceptions import CometRestApiException
