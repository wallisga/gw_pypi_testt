def test_import():
    """Test that the package can be imported."""
    import gw_pypi_testt
    assert gw_pypi_testt.__version__
    
def test_version():
    """Test that version is set correctly."""
    import gw_pypi_testt
    assert gw_pypi_testt.__version__ == "0.1.0"