import pytest
from project import calculate_shock_index, calculate_rts, evaluate_triage
vitals_data = {
    "name": "rihab toumi",
    "age": 27,
    "temperature": 37.0,
    "heart_rate": 100,
    "blood_pressure_sys": 120,
    "blood_pressure_dia": 90,
    "oxygen_saturation": 100.0,
    "glasgow_coma_scale": 15,
    "respiratory_rate": 22,
    "recorded_time": "2024-12-31 18:05:49"
}

def test_calculate_shock_index():
    """Test for the Shock Index calculation."""
    shock_index = calculate_shock_index(vitals_data)
    assert shock_index == 100 / 120, "Shock index is not calculated correctly"

def test_calculate_rts():
    """Test for the Revised Trauma Score (RTS) calculation."""
    rts = calculate_rts(vitals_data)
    expected_rts = (0.9368 * vitals_data["glasgow_coma_scale"] +
                    0.7326 * vitals_data["blood_pressure_sys"] +
                    0.2908 * vitals_data["respiratory_rate"])
    assert rts == expected_rts, f"RTS is not calculated correctly. Expected {expected_rts}, but got {rts}"

def test_evaluate_triage():
    """Test for triage evaluation."""
    feedback, triage_level = evaluate_triage(vitals_data)

    # Assert that certain feedback messages are present in the output
    assert "Shock Index: 0.83" in feedback[0], "Shock index feedback is incorrect"
    assert triage_level == "YELLOW - OBSERVATION", f"Triage level is incorrect. Expected 'YELLOW - OBSERVATION', but got {triage_level}"

if __name__ == "__main__":
    pytest.main()
