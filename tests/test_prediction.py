import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# output from predict script not null
# output from predict script is str dataType
# the output is Y for example data


@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

# Test-1 ---> output is not nun
def test_single_pred(single_prediction):          
    assert single_prediction is not None

# Test-2 ---> dataType is string
def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('Prediction')[0],str)

# Test-3 ---> check that the output is Y
def test_single_pred_validate(single_prediction):
    assert single_prediction.get('Prediction')[0] == 'Y'