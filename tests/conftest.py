import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
import warnings
warnings.filterwarnings("ignore")
from catvsdog_model.processing.data_manager import load_test_dataset


@pytest.fixture
def sample_input_data():
    test_data = load_test_dataset()

    return test_data