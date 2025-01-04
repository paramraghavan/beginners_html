# How to run your website over HTTPS for development/testing

The `python -m http.server` module does not natively support HTTPS, as it is designed to run a basic HTTP server.
However, you can set up an HTTPS server for your website using Python with the help of the `http.server` module combined
with the `ssl` module.

### **Steps to Run a Simple HTTPS Server**

1. **Generate a Self-Signed SSL Certificate**
   To enable HTTPS, you need an SSL certificate. You can create a self-signed certificate using `openssl`.

   ```bash
   openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
   ```

    - `key.pem`: This is your private key.
    - `cert.pem`: This is your self-signed certificate.

   Save both files in the same directory as your HTML file.

---

2. **Create an HTTPS Server Script**
   Use the `http.server` and `ssl` modules in Python to run an HTTPS server.

   Create a Python file (e.g., `https_server.py`) with the following content:

   ```python
   import http.server
   import ssl

   # Define the handler to serve files
   handler = http.server.SimpleHTTPRequestHandler

   # Set up the server
   httpd = http.server.HTTPServer(('localhost', 4443), handler)

   # Wrap the server with SSL
   httpd.socket = ssl.wrap_socket(
       httpd.socket,
       keyfile="key.pem",  # Path to your private key
       certfile="cert.pem",  # Path to your certificate
       server_side=True
   )

   print("Serving on https://localhost:4443")
   httpd.serve_forever()
   ```

---

3. **Run the Script**
   Execute the script from the terminal:

   ```bash
   python https_server.py
   ```

---

4. **Access Your Website**
   Open your browser and go to:

   ```
   https://localhost:4443
   ```

    - You might see a browser warning about the self-signed certificate. Since it’s for local development, you can
      safely proceed.

---

### **Important Notes**

- **Self-Signed Certificates**: These are only suitable for local development. For production, use a trusted certificate
  authority (e.g., Let's Encrypt).
- **Firewall Rules**: Ensure port `4443` (or the one you specify) is not blocked.
- **Python Version**: This script requires Python 3.7 or newer.

This setup allows you to serve your website over HTTPS locally with Python.