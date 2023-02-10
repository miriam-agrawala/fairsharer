from fair_sharer import fair_sharer

def test_fairsharer():
    trial_numbers = [1200, 1000, 800, 0]
    trial_iterations = 3
    fair_sharer(trial_numbers, trial_iterations) == [857.6, 1003.2, 912.0, 227.2]
