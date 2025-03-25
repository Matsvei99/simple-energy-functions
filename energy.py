def calculate_daily_energy_use(kwh_list):
    return sum(kwh_list)

def estimate_monthly_bill(daily_kwh, rate_per_kwh):
    return daily_kwh * rate_per_kwh * 30

def detect_spike(daily_data):
    avg = sum(daily_data) / len(daily_data)
    for day in daily_data:
        if day > avg * 1.5:
            return True
    return False
