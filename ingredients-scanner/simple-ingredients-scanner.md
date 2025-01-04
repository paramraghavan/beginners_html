# Ingredients scanner using terrasect

How to use terrasect library to scan ingredients english text from packages, bottle, containers, etc ingrocery store
with html5 progressive web, mobile freindly explain with example

1. **Key Features**:
   - Real-time camera access
   - Camera switching (front/back)
   - Text recognition using Tesseract.js
   - Ingredient extraction logic
   - PWA support for offline usage
   - Mobile-responsive design
   - Loading indicators and status updates

2. **How to Use**:
   - Allow camera access when prompted
   - Point camera at ingredient list on product packaging
   - Click "Capture Image" button
   - Wait for processing (the app will show a loading indicator)
   - View extracted text and identified ingredients

3. **Technical Implementation**:
   - Uses HTML5 `getUserMedia` API for camera access
   - Canvas element for image capture
   - Tesseract.js for OCR (Optical Character Recognition)
   - Basic ingredient extraction algorithm looking for common markers
   - PWA manifest for installability
   - Mobile-first responsive design

4. **Tips for Best Results**:
   - Ensure good lighting
   - Hold the camera steady
   - Get close enough to the text for clear focus
   - Try to align text horizontally
   - Make sure the ingredient list is fully visible
