from dotenv import load_dotenv , dotenv_values
import os
load_dotenv()
print(os.getenv("NASDAQ_API_KEY"))
