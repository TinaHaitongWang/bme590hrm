from main_function import main_function
import numpy as np
import os


def test_json_output():
    main_function()
    expected = True
    for i in np.arange(31):
        current_file = 'test_data' + str(i + 1) + '.json'
        fullpath = os.path.join(os.getcwd(), "Metrics_test_data", current_file)
        if os.path.exists(fullpath):
            is_json_output = True
        else:
            is_json_output = False

    assert is_json_output == expected
