# Build mobile friendly PWA
- **HTML5 and JavaScript-based Progressive Web Applications (PWAs)** 
- Using **Visual Studio Code (VS Code)**

---

### **Step 1: Install VS Code**

1. **Download and Install VS Code**:
    - Go to the [official VS Code website](https://code.visualstudio.com/).
    - Download the version for your operating system and install it.

---

### **Step 2: Install Necessary Extensions**

1. **Open Extensions Panel**:
    - Click on the Extensions icon in the Activity Bar on the side (`Ctrl+Shift+X` or `Cmd+Shift+X` on Mac).
2. **Search for and Install These Extensions**:
    - **HTML Snippets**: Adds helpful snippets for HTML.
    - **Live Server**: Provides a local development server with live reload for testing.
    - **Prettier**: Ensures consistent formatting for HTML, CSS, and JavaScript.
    - **JavaScript (ES6) Code Snippets**: Adds useful JavaScript snippets.
    - **PWA Studio**: Helps with service worker and manifest management.
    - **Workbox**: Simplifies adding offline capabilities to your app.
    - **Debugger for Chrome**: Allows debugging of JavaScript directly in Chrome.

---

### **Step 3: Create a New Project**

1. **Open a New Workspace**:
    - Open VS Code and create a new folder for your project.
    - Go to `File > Open Folder` and select the folder.
2. **Set Up the File Structure**:
    - Create the following files and folders in the workspace:
      ```
      /project-folder
      ├── /css
      │   └── styles.css
      ├── /js
      │   └── app.js
      ├── /images
      ├── index.html
      ├── manifest.json
      └── sw.js
      ```

---

### **Step 4: Configure Basic HTML5**

1. **Edit `index.html`**:
   Add the boilerplate code:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>PWA Example</title>
       <link rel="stylesheet" href="css/styles.css">
       <link rel="manifest" href="manifest.json">
   </head>
   <body>
       <h1>Welcome to My PWA</h1>
       <script src="js/app.js"></script>
   </body>
   </html>
   ```

---

### **Step 5: Add PWA Essentials**

1. **Add a Manifest File (`manifest.json`)**:
   ```json
   {
       "name": "My PWA",
       "short_name": "PWA",
       "start_url": "/index.html",
       "display": "standalone",
       "background_color": "#ffffff",
       "theme_color": "#000000",
       "icons": [
           {
               "src": "images/icon-192x192.png",
               "sizes": "192x192",
               "type": "image/png"
           },
           {
               "src": "images/icon-512x512.png",
               "sizes": "512x512",
               "type": "image/png"
           }
       ]
   }
   ```

2. **Create a Service Worker (`sw.js`)**:
   Basic service worker for caching:
   ```javascript
   const CACHE_NAME = "pwa-cache-v1";
   const urlsToCache = ["/", "/index.html", "/css/styles.css", "/js/app.js"];

   self.addEventListener("install", event => {
       event.waitUntil(
           caches.open(CACHE_NAME).then(cache => {
               return cache.addAll(urlsToCache);
           })
       );
   });

   self.addEventListener("fetch", event => {
       event.respondWith(
           caches.match(event.request).then(response => {
               return response || fetch(event.request);
           })
       );
   });
   ```

3. **Register the Service Worker** in `app.js`:
   ```javascript
   if ('serviceWorker' in navigator) {
       navigator.serviceWorker.register('/sw.js')
           .then(() => console.log("Service Worker Registered"))
           .catch(err => console.error("Service Worker Registration Failed", err));
   }
   ```

---

### **Step 6: Run the Application**

1. **Start Live Server**:
    - Right-click on `index.html` and select **Open with Live Server**.
    - Your application will open in the browser.

2. **Test Responsiveness**:
    - Open Developer Tools (`Ctrl+Shift+I` or `Cmd+Opt+I` on Mac) and enable **Mobile View** to simulate different
      devices.

---

### **Step 7: Optimize for Mobile**

1. **Add CSS for Mobile Responsiveness**:
   In `css/styles.css`:
   ```css
   body {
       font-family: Arial, sans-serif;
       margin: 0;
       padding: 0;
   }

   h1 {
       text-align: center;
       color: #333;
   }

   @media (max-width: 600px) {
       h1 {
           font-size: 1.5em;
       }
   }
   ```

2. **Use Lighthouse to Audit Your App**:
    - Install the Lighthouse extension for Chrome.
    - Audit your app for PWA compliance and mobile-friendliness.

---

