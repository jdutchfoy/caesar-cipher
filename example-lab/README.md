# README.md

## Caesar Cipher

The Caesar Cipher is a simple encryption technique that shifts each letter in a plaintext message by a certain number of positions down the alphabet.

## Features

- Encryption: Encrypt a plain text phrase with a given shift.
- Decryption: Restore an encrypted text back to its original form with the correct shift.
- Cracking: Decode an encrypted message without knowing the shift used.
- Unit Tests: Includes comprehensive unit tests for encryption, decryption, and cracking.

## Usage

To use the Caesar Cipher functions, follow these steps:

1. Import the `encrypt`, `decrypt`, and `crack` functions from the `example_lab.example_script` module:

   ```python
   from example_lab.example_script import encrypt, decrypt, crack
   ```

2. Encryption:

   ```python
   encrypted_text = encrypt(plain_text, shift)
   ```

3. Decryption:

   ```python
   decrypted_text = decrypt(encrypted_text, shift)
   ```

4. Cracking:

   ```python
   cracked_text = crack(encrypted_text)
   ```

## Testing

The project includes unit tests to verify the correctness of the Caesar Cipher functions. To run the tests, you need to have `pytest` installed. Run the following command in the project's root directory:

```bash
pytest
```

For the actual code implementation, please refer to the [example_script.py](example_lab/example_script.py) file.

For the unit tests, please refer to the [test_caesar_cipher.py](tests/test_caesar_cipher.py) file.

## Dependencies

The project has the following dependencies:

- Python 3.x

## Contributing

Contributions to the Caesar Cipher project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

