def test_preprocess_with_missing_values():
    """Test dengan data yang punya banyak missing values"""
    df = pd.DataFrame({
        'Age': [20, None, 30, None],
        'Fare': [None, 100, 200, 300],
        'Sex': ['male', 'female', None, 'male']
    })
    result = preprocess_data(df)
    assert result.isnull().sum().sum() == 0  # Tidak ada missing values
    assert len(result) == 4  # Tidak drop rows sembarangan
