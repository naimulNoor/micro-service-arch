import boto3
from io import BytesIO

# Set your AWS credentials and region
aws_access_key_id = 'AKIAX3X6M7S6IQPDTIYF'
aws_secret_access_key = 'GUHRFPiPp5iTum+WSAdnq/Ks/aOqwIRtRMFCWG4w'
aws_region = 'us-east-1'  # Specify your AWS region

# Initialize a Boto3 Polly client with credentials and region
client = boto3.client('polly', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Text to be converted to speech
text = "Hello, this is a test of Amazon Polly text-to-speech service."

# Request speech synthesis
response = client.synthesize_speech(
    OutputFormat='mp3',  # Format of the output audio (other options include 'ogg_vorbis', 'pcm')
    Text=text,           # The text you want to convert
    VoiceId='Joanna'     # Voice to use (you can choose from various voices)
)

# Get the audio stream
audio_stream = response['AudioStream'].read()

# Save the audio to a file or do further processing
with open('output.mp3', 'wb') as f:
    f.write(audio_stream)

print("Audio file saved as 'output.mp3'")