def test_parse_valid_csv():
    csv_content = "header1,header2\nvalue1,value2\nvalue3,value4"
    file_handle = io.StringIO(csv_content)
    
    expected_data = [
        ['header1', 'header2'],
        ['value1', 'value2'],
        ['value3', 'value4']
    ]
  
    actual_data = parse_csv_data(file_handle)
    
    assert actual_data == expected_data

