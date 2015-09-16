import RPi.GPIO as GPIO
import time
from temboo.Library.Utilities.HTTP import Post
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("YOUR-TEMBOO-USERNAME", "myFirstApp", "YOUR-TEMBOO-TOKEN")

# Instantiate the Choreo
postChoreo = Post(session)

# Get an InputSet object for the Choreo
postInputs = postChoreo.new_input_set()

# Set the Choreo inputs
postInputs.set_RequestBody("{\n   \"sdid\": \"YOUR-SAMI-DEVICE-ID\",\n   \"type\": \"message\",\n   \"data\": {\n      \"text\": \"Yo\"\n   }\n}")
postInputs.set_RequestHeaders("{\n   \"Content-Type\": \"application/json\",\n   \"Authorization\": \"Bearer YOUR-SAMI-DEVICE-TOKEN\"\n}")
postInputs.set_Debug("true")
postInputs.set_URL("https://api.samsungsami.io/v1.1/messages")

# Set up the GPIO interface
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 14
button = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

# Say hi!
GPIO.output(led, 1)
time.sleep(2)
GPIO.output(led, 0)

# Doorbell
while True:
    if GPIO.input(button) == False:
        print("Button pressed")
        GPIO.output(led, 1)
        time.sleep(1)
        GPIO.output(led, 0)
        
        # Execute the Choreo
        postResults = postChoreo.execute_with_results(postInputs)

        # Print the Choreo outputs
        print("HTTPLog: " + postResults.get_HTTPLog())
        print("Response: " + postResults.get_Response())
        print("ResponseStatusCode: " + postResults.get_ResponseStatusCode())

GPIO.cleanup()
