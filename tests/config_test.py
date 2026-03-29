from thesis_webscraper import config 

def test_config_value():
    assert config.SETTING_NAME == "expected_value", "Configuration setting does not match expected value"

