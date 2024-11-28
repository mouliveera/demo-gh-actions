# demo-gh-actions

### Step 1: Set Up Your Repository
1. **Clone Your Repo**:
   ```bash
   git clone https://github.com/your-username/demo-gh-actions.git
   cd demo-gh-actions
   ```

2. **Create a Flask Application**:
   Inside the `demo-gh-actions` directory, create a file named `app.py` with the following code:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hellow_world():
       return '<h1 style="color:hellow">Hellow World!</h1>'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=8080)
   ```

3. **Add `requirements.txt`**:
   Create a file named `requirements.txt` in the same directory and add:
   ```plaintext
   flask
   ```

4. **Commit and Push**:
   ```bash
   git add app.py requirements.txt
   git commit -m "Add Flask Hellow World app"
   git push origin main
   ```

---

### Step 2: Create GitHub Actions Workflow
1. **Create Workflow Directory**:
   Inside your local repo, create a directory for GitHub Actions workflows:
   ```bash
   mkdir -p .github/workflows
   ```

2. **Create Workflow File**:
   Create a new file `.github/workflows/run-flask.yml` and paste the following content:

   ```yaml
   name: Run Flask App

   on:
     push:
       branches:
         - main
     workflow_dispatch:

   jobs:
     run-flask:
       runs-on: ubuntu-latest

       steps:
         # Step 1: Checkout the code
         - name: Checkout code
           uses: actions/checkout@v3

         # Step 2: Set up Python environment
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.9'  # Python version

         # Step 3: Install dependencies
         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt

         # Step 4: Run Flask app
         - name: Run Flask App
           run: |
             python app.py
   ```

3. **Commit and Push Workflow File**:
   ```bash
   git add .github/workflows/run-flask.yml
   git commit -m "Add GitHub Actions workflow for Flask app"
   git push origin main
   ```

---

### Step 3: Trigger GitHub Actions
1. **Go to Your Repository on GitHub**.
2. Click on the **"Actions"** tab in your repo.
3. You should see a workflow named "Run Flask App". It will automatically start running on a push to the `main` branch.
4. If it doesn't auto-trigger, click **"Run Workflow"** to start it manually.

---

### Step 4: View Logs
1. Click on the running workflow in the **"Actions"** tab.
2. Navigate through the steps to check if the Flask app starts successfully.

---

### Key Notes
- The Flask app will run in the GitHub Actions environment, but you cannot directly access it from your browser since it runs in a virtual machine.
- To test locally, run:
  ```bash
  python app.py
  ```
  Then open `http://127.0.0.1:8080` in your browser to see "Hellow World!"

