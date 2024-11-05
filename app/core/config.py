from typing import Dict, Any, List
import json
import boto3
from botocore.exceptions import ClientError
from urllib.parse import quote_plus

class ConfigurationManager:
    def __init__(self):
        self.session = boto3.session.Session()
        self.client = self.session.client(
            service_name='secretsmanager',
            region_name='us-east-1' 
        )
        self.SECRET_PATHS_KEY = '/pos/dev/config/paths'
        self._secret_paths = None
        self._config_cache = {}

    def _get_secret_paths(self) -> Dict[str, str]:
        """
        Retrieve secret paths configuration from AWS Secrets Manager.
        This allows dynamic configuration of secret paths.
        """
        if self._secret_paths is None:
            try:
                paths = self.get_secret(self.SECRET_PATHS_KEY)
                self._secret_paths = paths
            except ClientError:
                self._secret_paths = {}
        return self._secret_paths

    def get_secret(self, secret_name: str) -> Dict[str, Any]:
        """Retrieve a single secret from AWS Secrets Manager"""
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
            if 'SecretString' in response:
                return json.loads(response['SecretString'])
        except ClientError as e:
            raise Exception(f"Failed to retrieve secret {secret_name}: {str(e)}")

    def get_config_section(self, section: str) -> Dict[str, Any]:
        """
        Get configuration for a specific section.
        Uses the paths defined in SECRET_PATHS_KEY.
        """
        paths = self._get_secret_paths()
        if section not in paths:
            raise KeyError(f"Configuration section '{section}' not found in paths configuration")
        
        if section not in self._config_cache:
            self._config_cache[section] = self.get_secret(paths[section])
        
        return self._config_cache[section]

    def refresh_cache(self, section: str = None):
        """
        Refresh the configuration cache.
        If section is provided, refresh only that section.
        """
        if section:
            self._config_cache.pop(section, None)
        else:
            self._config_cache.clear()
            self._secret_paths = None

    def get_all_sections(self) -> List[str]:
        """Get list of all available configuration sections"""
        return list(self._get_secret_paths().keys())

    def get_database_url(self) -> str:
        """Get database URL from config"""
        db_config = self.get_config_section('database')
        return f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

    def get_aws_config(self) -> Dict[str, str]:
        """Get AWS-specific configuration"""
        return self.get_config_section('aws')

    def get_auth_config(self) -> Dict[str, Any]:
        """Get authentication configuration"""
        return self.get_config_section('auth')

# Create a singleton instance
config_manager = ConfigurationManager()