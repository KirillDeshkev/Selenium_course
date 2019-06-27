def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, "expected {}, got {}".format(expected_result, actual_result)


print(test_input_text(8, 11))
