# health-check.py

## Build Instructions
- Step 1: Install Python v3.11.0 or newer. Make sure to check "Add Python 3.6 to PATH" checkbox.
- Step 2: Verify Python v3.11.0 or newer and Pip (should come installed and accessible from CLI if you checked the box mentioned in step 1) v22.3 or newer are both installed.
- Step 3: Clone health-check.py repository onto local machine. 'git clone https://github.com/mpeck451/health-check.git'
- Step 4: Install Non Standard Library python modules
  - Step 4a: Install PyYAML v6.0 or newer with Pip. 'pip install pyyaml'
  - Step 4b: Install Requests v2.30.0 or newer with Pip. 'pip install requests'
- Ready to run!

## How to Run
- Step 1: Run "health-check.py" script. YAML config file path required as input argument. ex: 'winpty python.exe "C:\Users\myUser\myFolder\health-check\sample-input-file.yaml"
- Step 2: Wait for script to make requests to endpoints every 15 seconds. First round of requests should initiate upon startup. Availability percentages will print to console.
- Step 3: Press "CTRL C" to end script.

## NOTES
- Python v3.11.0 or newer
- Pip v22.3 or newer
- Non Standard Python Library Modules:
  - Requests v2.30.0 or newer
  - PyYAML v6.0 or newer

MIT License

Copyright (c) 2023 Mason Lee Peck

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
