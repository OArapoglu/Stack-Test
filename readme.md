 # STACK_TEST TASK #
This task includes stack operations which are push, pop, peek, is_emtpy, get_size as well as tests in pytest.  
<br />
The fundamental modules and their definitions are as follows:
- exception.Exception: In includes NullElementException and EmptyStackException exceptions.
- node.Node: It represents a node having a data and a next property to show the next node.
- stack.Stack: It is an abstract of stack operations.
- stack_operation.Stack_Operation: It is the main file of this task and manages stack operations.
- tests.conftest.py: It includes the fixture of a stack in Pytest.
- tests.test_stack.py It includes the test scenarios for stack operations in Pytest.

### How to Run Program ###
Activate virtual environment.
<br/>
Below code for Windows.
```commandline
. env/scripts/activate
```
Run stack operations.
```commandline
python stack_operation.py
```

Run pytest
```commandline
python -m pytest
```

