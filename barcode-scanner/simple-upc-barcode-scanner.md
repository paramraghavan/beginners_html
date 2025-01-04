# Simple Barcode scanner

Using ZXing library for barcode scanner with html5 progressive web, mobile freindly explain with example

Let me explain the key components of this barcode scanner implementation:

1. Key Features:

- Mobile-friendly design
- Progressive Web App ready
- Handles device orientation changes
- Automatic back camera selection
- Visual feedback with scanning region
- Error handling and status messages
- Vibration feedback on successful scans

2. Important HTML Elements:

```html

<div id="reader">
    <div id="video-container">
        <video id="video" playsinline></video>
    </div>
</div>
```

- `playsinline`: Required for iOS to prevent fullscreen
- Video container provides proper sizing and positioning

3. Core Scanner Class Methods:

```javascript
class BarcodeScanner {
    async startScanning() {
        // Initialize camera and start scanning
    }
    
    handleSuccess(result) {
        // Process successful barcode detection
    }
    
    handleError(error) {
        // Handle errors gracefully
    }
}
```

4. Key ZXing Implementation:

```javascript
// Initialize reader
const codeReader = new ZXing.BrowserMultiFormatReader();

// Start scanning
await codeReader.decodeFromVideoDevice(
    deviceId,
    videoElement,
    (result, error) => {
        if (result) {
            // Handle successful scan
        }
    }
);
```

5. Mobile-Specific Features:

```javascript
// Prefer back camera
const backCamera = videoInputDevices.find(device => 
    device.label.toLowerCase().includes('back') ||
    device.label.toLowerCase().includes('rear')
);

// Handle orientation changes
window.addEventListener('orientationchange', () => {
    if (scanner.isScanning) {
        scanner.stopScanning();
        setTimeout(() => scanner.startScanning(), 100);
    }
});
```

6. Important CSS for Mobile:

```css
#video-container {
    width: 100%;
    height: 60vh;
    position: relative;
    overflow: hidden;
}

#video {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

To use this in your project:

1. Include ZXing library:

```html

<script src="https://unpkg.com/@zxing/library@latest"></script>
```

2. Copy the provided HTML, CSS, and JavaScript

3. Initialize the scanner:

```javascript
const scanner = new BarcodeScanner();
```

The scanner supports:

- Multiple barcode formats (QR, EAN, UPC, etc.)
- Real-time scanning
- Error handling
- Camera selection
- Mobile device orientation changes
- Visual feedback
- Haptic feedback (vibration)
