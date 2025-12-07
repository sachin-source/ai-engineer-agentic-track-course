# First let's do an import. If you get an Import Error, double check that your Kernel is correct..

from dotenv import load_dotenv

# Next it's time to load the API keys into environment variables
# If this returns false, see the next cell!

load_dotenv(override=True)

# Check the key - if you're not using OpenAI, check whichever key you're using! Ollama doesn't need a key.

import os
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
    
# And now - the all important import statement
# If you get an import error - head over to troubleshooting in the Setup folder
# Even for other LLM providers like Gemini, you still use this OpenAI import - see Guide 9 for why

from openai import OpenAI

# And now we'll create an instance of the OpenAI class
# If you're not sure what it means to create an instance of a class - head over to the guides folder (guide 6)!
# If you get a NameError - head over to the guides folder (guide 6)to learn about NameErrors - always instantly fixable
# If you're not using OpenAI, you just need to slightly modify this - precise instructions are in the AI APIs guide (guide 9)

openai = OpenAI()