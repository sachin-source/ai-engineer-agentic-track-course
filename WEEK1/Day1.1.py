# First let's do an import. If you get an Import Error, double check that your Kernel is correct..

from dotenv import load_dotenv

# Next it's time to load the API keys into environment variables
# If this returns false, see the next cell!

load_dotenv(override=True)