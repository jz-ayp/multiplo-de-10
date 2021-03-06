import pytest
import src.exercise

inp_1 = ['123']
out_1 = ['El número 123 no es múltiplo de 10']

inp_2 = ['24560']
out_2 = ['El número 24560 sí es múltiplo de 10']

inp_3 = ['102030']
out_3 = ['El número 102030 sí es múltiplo de 10']

# run the test function for each input/output pair
@pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2), (inp_3, out_3)])
def test_capture_stdout(capsys, test_input, expected):
    
    # Load the test input for the program execution:
    def mock_input(s):
        return test_input.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()

    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]

    # Test the actual program output against the anticipated program output:
    assert out == expected
