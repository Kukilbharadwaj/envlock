# EnvLock

Encrypt and decrypt .env files safely for internal teams.

## Installation

```bash
pip install -e .
```

Or install directly:

```bash
pip install cryptography
```

## Usage

```bash
# Initialize envlock in your project
envlock init

# Encrypt a .env file
envlock encrypt

# Decrypt a .env.enc file
envlock decrypt

# Show version
envlock version
```

## Features

- 🔒 AES-256-GCM encryption
- 🔑 Password-based encryption with scrypt key derivation
- 📁 Automatic .gitignore configuration
- 🎯 Support for multiple environment files
- 🛡️ Secure file permissions (0o600)

## How it works

1. **Init**: Sets up .gitignore and creates first encrypted .env.enc file
2. **Encrypt**: Encrypts your .env files with a password
3. **Decrypt**: Decrypts .env.enc files back to .env

The encrypted files (.env.enc*) can be safely committed to version control.
Never commit unencrypted .env files!

## Security

- Uses AES-256-GCM authenticated encryption
- Password-based key derivation with scrypt
- Random salt and IV for each encryption
- Authentication tag to detect tampering
- Files created with restricted permissions (600)

## Requirements

- Python >= 3.8
- cryptography >= 41.0.0
