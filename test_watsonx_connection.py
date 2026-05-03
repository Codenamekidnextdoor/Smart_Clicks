#!/usr/bin/env python3
"""
Test script to diagnose watsonx API connection issues.
This will help identify why responses are empty.
"""

import os
import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Setup detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_credentials():
    """Test if credentials are available"""
    print("\n" + "="*70)
    print("STEP 1: Checking Credentials")
    print("="*70)
    
    api_key = os.getenv('WATSONX_API_KEY')
    project_id = os.getenv('WATSONX_PROJECT_ID')
    endpoint = os.getenv('WATSONX_ENDPOINT', 'https://us-south.ml.cloud.ibm.com')
    
    print(f"API Key: {'✓ Set' if api_key else '✗ Not set'}")
    print(f"Project ID: {'✓ Set' if project_id else '✗ Not set'}")
    print(f"Endpoint: {endpoint}")
    
    if api_key:
        print(f"API Key (first 10 chars): {api_key[:10]}...")
    if project_id:
        print(f"Project ID (first 10 chars): {project_id[:10]}...")
    
    return api_key, project_id, endpoint


def test_sdk_import():
    """Test if IBM SDK is installed"""
    print("\n" + "="*70)
    print("STEP 2: Testing IBM SDK Import")
    print("="*70)
    
    try:
        from ibm_watsonx_ai.foundation_models import ModelInference
        from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
        print("✓ IBM watsonx SDK is installed")
        return True
    except ImportError as e:
        print(f"✗ IBM watsonx SDK not installed: {e}")
        print("\nTo install, run:")
        print("  pip install ibm-watsonx-ai")
        return False


def test_database_credentials():
    """Test credentials from database"""
    print("\n" + "="*70)
    print("STEP 3: Checking Database Credentials")
    print("="*70)
    
    try:
        from database.db_manager import DatabaseManager
        db = DatabaseManager()
        
        api_key = db.get_setting('watsonx_api_key')
        project_id = db.get_setting('watsonx_project_id')
        endpoint = db.get_setting('watsonx_endpoint')
        
        print(f"DB API Key: {'✓ Set' if api_key else '✗ Not set'}")
        print(f"DB Project ID: {'✓ Set' if project_id else '✗ Not set'}")
        print(f"DB Endpoint: {endpoint or '✗ Not set'}")
        
        if api_key:
            print(f"DB API Key (first 10 chars): {api_key[:10]}...")
        if project_id:
            print(f"DB Project ID (first 10 chars): {project_id[:10]}...")
        
        return api_key, project_id, endpoint
    except Exception as e:
        print(f"✗ Error accessing database: {e}")
        return None, None, None


def test_watsonx_client():
    """Test watsonx client initialization"""
    print("\n" + "="*70)
    print("STEP 4: Testing WatsonxClient Initialization")
    print("="*70)
    
    try:
        from ai_integration.bob_client import WatsonxClient
        
        # Get credentials from database
        from database.db_manager import DatabaseManager
        db = DatabaseManager()
        
        api_key = db.get_setting('watsonx_api_key')
        project_id = db.get_setting('watsonx_project_id')
        endpoint = db.get_setting('watsonx_endpoint')
        
        if not api_key or not project_id:
            print("✗ Missing credentials in database")
            return None
        
        print("Initializing WatsonxClient...")
        client = WatsonxClient(
            api_key=api_key,
            project_id=project_id,
            endpoint=endpoint
        )
        print("✓ WatsonxClient initialized successfully")
        return client
        
    except Exception as e:
        print(f"✗ Failed to initialize WatsonxClient: {e}")
        logger.exception("Full traceback:")
        return None


def test_simple_generation(client):
    """Test simple text generation"""
    print("\n" + "="*70)
    print("STEP 5: Testing Simple Text Generation")
    print("="*70)
    
    if not client:
        print("✗ No client available")
        return
    
    try:
        prompt = "Say 'Hello, World!' and nothing else."
        print(f"Prompt: {prompt}")
        print("\nGenerating response...")
        
        response = client.generate_text(prompt)
        
        print(f"\nResponse type: {type(response)}")
        print(f"Response length: {len(response) if response else 0}")
        print(f"Response: {repr(response)}")
        
        if not response or not response.strip():
            print("\n✗ ISSUE FOUND: Response is empty!")
            print("This is the root cause of your null output problem.")
        else:
            print("\n✓ Response received successfully")
            
    except Exception as e:
        print(f"\n✗ Generation failed: {e}")
        logger.exception("Full traceback:")


def test_chat_method(client):
    """Test chat method"""
    print("\n" + "="*70)
    print("STEP 6: Testing Chat Method")
    print("="*70)
    
    if not client:
        print("✗ No client available")
        return
    
    try:
        message = "What is 2+2?"
        print(f"Message: {message}")
        print("\nGenerating chat response...")
        
        response = client.chat(message)
        
        print(f"\nResponse type: {type(response)}")
        print(f"Response length: {len(response) if response else 0}")
        print(f"Response: {repr(response)}")
        
        if not response or not response.strip():
            print("\n✗ ISSUE FOUND: Chat response is empty!")
        else:
            print("\n✓ Chat response received successfully")
            
    except Exception as e:
        print(f"\n✗ Chat failed: {e}")
        logger.exception("Full traceback:")


def test_mock_client():
    """Test mock client as fallback"""
    print("\n" + "="*70)
    print("STEP 7: Testing Mock Client (Fallback)")
    print("="*70)
    
    try:
        from ai_integration.bob_client import MockWatsonxClient
        
        print("Initializing MockWatsonxClient...")
        client = MockWatsonxClient()
        print("✓ MockWatsonxClient initialized")
        
        print("\nTesting mock generation...")
        response = client.generate_text("Test prompt")
        print(f"Mock response: {response}")
        
        if response:
            print("✓ Mock client works correctly")
        else:
            print("✗ Even mock client returns empty!")
            
    except Exception as e:
        print(f"✗ Mock client failed: {e}")
        logger.exception("Full traceback:")


def main():
    """Run all diagnostic tests"""
    print("\n" + "="*70)
    print("WATSONX CONNECTION DIAGNOSTIC TOOL")
    print("="*70)
    print("\nThis tool will help diagnose why your API returns empty responses.\n")
    
    # Test 1: Credentials
    env_api_key, env_project_id, env_endpoint = test_credentials()
    
    # Test 2: SDK
    sdk_available = test_sdk_import()
    
    if not sdk_available:
        print("\n" + "="*70)
        print("DIAGNOSIS: IBM SDK not installed")
        print("="*70)
        print("\nThe system is likely using MockWatsonxClient.")
        print("Install the SDK with: pip install ibm-watsonx-ai")
        return
    
    # Test 3: Database credentials
    db_api_key, db_project_id, db_endpoint = test_database_credentials()
    
    # Test 4: Initialize client
    client = test_watsonx_client()
    
    # Test 5: Simple generation
    test_simple_generation(client)
    
    # Test 6: Chat method
    test_chat_method(client)
    
    # Test 7: Mock client
    test_mock_client()
    
    # Summary
    print("\n" + "="*70)
    print("DIAGNOSTIC SUMMARY")
    print("="*70)
    
    if not sdk_available:
        print("\n⚠ IBM SDK not installed - using mock responses")
    elif not db_api_key or not db_project_id:
        print("\n⚠ Credentials not configured in database")
    elif not client:
        print("\n✗ Failed to initialize watsonx client")
    else:
        print("\n✓ All tests completed - check results above")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDiagnostic interrupted by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        logger.exception("Full traceback:")

# Made with Bob
