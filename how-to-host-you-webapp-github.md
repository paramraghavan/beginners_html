#  PWA Hosting on GitHub Pages

1. Other platforms like **Netlify**, **Vercel**, or **GitHub Pages** to host your PWA.
2. Ensure the `start_url` in your `manifest.json` matches your deployment URL.

---

## Steps to  host PWA on Github

Hosting a **Progressive Web Application (PWA)** on **GitHub Pages** is simple and free. Here’s a step-by-step guide:

---

### **Step 1: Prepare Your PWA**

1. Ensure your PWA has:
    - `index.html`: The main HTML file.
    - `manifest.json`: The web app manifest file.
    - `sw.js`: The service worker file for offline support.
    - Other assets like CSS, JavaScript, and images organized in folders.

2. Test your PWA locally using tools like **Live Server** in Visual Studio Code to ensure it works as expected.

---

### **Step 2: Create a GitHub Repository**

1. Log in to your GitHub account.
2. Create a new repository:
    - Click the **+** icon (top-right corner) and select **New repository**.
    - Name the repository (e.g., `my-pwa`).
    - Set it to **Public**.
    - Do not initialize with a README or `.gitignore` for now.

---

### **Step 3: Push Your PWA Code to GitHub**

1. **Initialize Git Locally**:
   Open your terminal or command prompt in your project folder and run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Connect to the GitHub Repository**:
   Replace `username` with your GitHub username and `my-pwa` with your repository name:
   ```bash
   git remote add origin https://github.com/username/my-pwa.git
   git branch -M main
   git push -u origin main
   ```

---

### **Step 4: Enable GitHub Pages**

1. Go to your repository on GitHub.
2. Click on the **Settings** tab.
3. Scroll down to the **Pages** section (on the left sidebar).
4. In the "Source" dropdown, select the **main branch** (or the branch where your code resides).
5. Click **Save**.
6. GitHub will provide a URL (e.g., `https://username.github.io/my-pwa/`) where your PWA is hosted.

---

### **Step 5: Update `manifest.json` and `sw.js` (Optional)**

If your PWA uses relative paths, it should work without changes. However, if you use absolute paths, update them to
reflect the GitHub Pages URL.

- **`manifest.json` Example**:
   ```json
   {
       "start_url": "/my-pwa/index.html",
       "icons": [
           {
               "src": "/my-pwa/images/icon-192x192.png",
               "sizes": "192x192",
               "type": "image/png"
           }
       ]
   }
   ```

- **`sw.js` Example**:
  Ensure the cached URLs are relative or include the `/my-pwa/` prefix.

---

### **Step 6: Test Your PWA**

1. Visit the GitHub Pages URL provided.
2. Test its functionality, including offline mode.
3. Use **Chrome DevTools > Lighthouse** to audit your PWA for compliance and performance.

---

### **Step 7: Make Updates**

1. To make changes:
    - Update your local code.
    - Commit the changes:
      ```bash
      git add .
      git commit -m "Updated PWA"
      git push
      ```
2. GitHub Pages will automatically deploy the updated code.

---

### **Tips for Better PWA Hosting on GitHub Pages**

1. **Custom Domain**: Use a custom domain by configuring DNS settings in the **Pages** section of GitHub.
2. **HTTPS**: GitHub Pages automatically provides HTTPS for secure hosting.
3. **404 Redirect**: Add a `.nojekyll` file if you face issues with asset loading.
