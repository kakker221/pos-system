from app.core.config import config_manager

def test_configuration():
    try:
        # List available sections
        print("Available configuration sections:")
        sections = config_manager.get_all_sections()
        for section in sections:
            print(f"- {section}")
            
        # Test getting each section
        for section in sections:
            print(f"\nTesting {section} configuration:")
            config = config_manager.get_config_section(section)
            print(f'config: {config}')
            print(f"✓ Keys: {list(config.keys())}")
            
        # Test cache refresh
        print("\nTesting cache refresh:")
        config_manager.refresh_cache('database')
        print("✓ Cache refreshed successfully")
        
    except Exception as e:
        print(f"Error during testing: {str(e)}")

if __name__ == "__main__":
    test_configuration()
