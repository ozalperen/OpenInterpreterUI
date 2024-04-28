# Install

1. Create virtual environment

   ```bash
   conda create -n OpenInterpreterUI PYTHON=3.11
   ```

2. Activate the created environment

   ```bash
   conda activate OpenInterpreterUI
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. To run the OpenInterpreterUI, use the following command:
   ```bash
   streamlit run app.py --server.port 8501
   ```
