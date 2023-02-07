from Example import Mathcalcualtion
def test_can_do_calcualtion():
    function_value=Mathcalcualtion()
    assert function_value.add(2) == 3
    assert function_value.subract(2) == 0