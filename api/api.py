import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/home')
def home():
    return """
    <h2>Some Header</h2>

    <script type="text/jsx" src="/scripts/ReactComponent1.js">
    </script>
    
    <div id="one">
    <!-- This element's contents will be replaced with ReactComponent1. -   ->
    </div>
    
    <script type="text/jsx" src="/scripts/ReactComponent2.js">
    </script>
    
    <div id="two">
    <!-- This element's contents will be replaced with ReactComponent2. -->
    </div>
    """
