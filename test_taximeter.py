import pytest
import time
from main import calculate_fare, calculate_time

def test_fare_basico():    # Check if the rate is correct.
    assert calculate_fare(10,10) == 0.7

def test_calculate_time_mokeypatch_stop(monkeypatch):    # Check if the time in ‘stopped’ is correct.
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

def test_calculate_time_mokeypatch_move(monkeypatch):   # Check if the time in ‘moving’ is correct.
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