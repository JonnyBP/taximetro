import pytest
import time
from main import calculate_fare, calculate_time, taximeter

def test_fare_basic():    # Check if the rate is correct.
    assert calculate_fare(10,10) == 0.7

def test_calculate_time_monkeypatch_stop(monkeypatch):    # Check if the time in ‘stopped’ is correct.
    # Set the stage
    start_time = 1000.0
    monkeypatch.setattr(time, 'time', lambda: 1010.0)   # Simulate that time.time() will return 1010.0, for a duration of 10s.
    
    #state, stopped_time, moving_time, start_time
    stoppedT,movedT = calculate_time(state="stopped",
        stopped_time=0.0,
        moving_time=20.0,
        start_time=start_time)
    
    # ASSERT: Verify the result.
    assert stoppedT == 10.0
    assert movedT == 20.0

def test_calculate_time_monkeypatch_move(monkeypatch):   # Check if the time in ‘moving’ is correct.
    # Set the stage
    start_time = 1000.0 
    monkeypatch.setattr(time, 'time', lambda: 1012.0)   # Simulate that time.time() will return 1012.0, for a duration of 12s.
    
    #state, stopped_time, moving_time, start_time
    stoppedT,movedT = calculate_time(state="moving",
        stopped_time=10.0,
        moving_time=20.0,
        start_time=start_time)
    
    # ASSERT: Verify the result.
    assert stoppedT == 10.0
    assert movedT == 20.0 + 12

def test_taximeter_simulation_monkeypatch(monkeypatch):    # Simulate a trip to ensure that the main loop runs without throwing any exceptions.

    # Simulate user input: start, move, stop, finish, exit -> 5 calls
    user_commands = ["start", "move", "stop", "finish", "exit"]
    command_iterator = iter(user_commands)
    monkeypatch.setattr('builtins.input', lambda _: next(command_iterator))

    # Simulate the calls to time.time() that it makes along the way.
    time_stamps = [1000, 1010, 1025, 1050, 1070, 1090]
    time_iterator = iter(time_stamps)
    monkeypatch.setattr('time.time', lambda: next(time_iterator))

    try:
        taximeter()
    except Exception as e:
        # ASSERT (implicit): If ANY exception is thrown, the test fails.
        pytest.fail(f"The taximeter() function caused an unexpected exception: {e}")