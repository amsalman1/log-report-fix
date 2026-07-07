import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "Success criterion 1 failed: /app/report.json was not created"

    try:
        data = json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError("Success criterion 2 failed: /app/report.json must be valid JSON") from exc

    assert isinstance(data, dict), "Success criterion 2 failed: report must be a JSON object"
    return data


def test_success_criterion_1_report_created():
    """Success criterion 1: create the output file at /app/report.json."""
    assert REPORT_PATH.exists(), "missing /app/report.json"


def test_success_criterion_2_required_json_shape():
    """Success criterion 2: output is valid JSON with exactly total_requests, unique_ips, and top_path."""
    data = load_report()
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_success_criterion_3_total_requests():
    """Success criterion 3: total_requests equals the number of nonempty log entries."""
    data = load_report()
    assert data["total_requests"] == 6


def test_success_criterion_4_unique_ips():
    """Success criterion 4: unique_ips equals the number of distinct client IP addresses."""
    data = load_report()
    assert data["unique_ips"] == 3


def test_success_criterion_5_top_path():
    """Success criterion 5: top_path is the most frequently requested path."""
    data = load_report()
    assert data["top_path"] == "/index.html"
