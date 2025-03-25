import pytest
from energy import calculate_daily_energy_use, estimate_monthly_bill, detect_spike

def test_calculate_daily_energy_use():
    assert calculate_daily_energy_use([1, 2, 3]) == 6

def test_estimate_monthly_bill():
    assert estimate_monthly_bill(5, 0.3) == 45.0

def test_detect_spike_true():
    assert detect_spike([3, 3, 3, 10]) == True

def test_detect_spike_false():
    assert detect_spike([3, 3, 3, 4]) == False
