def toilet_distance(steps, step_height):
    step_distance = step_height / 100  # convert cm to m
    down_distance = steps * step_distance * 2  # go down and back up
    weekly_distance = down_distance * 5 * 7  # 5 toilet breaks per day, 7 days per week
    return f"For {steps} steps of {step_height} cm, the keeper travels {weekly_distance:.2f} m per week."
print(toilet_distance(100, 20))