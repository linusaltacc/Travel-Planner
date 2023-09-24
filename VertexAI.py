from vertexai.preview.language_models import ChatModel
import vertexai
import json  
from google.oauth2 import service_account
import google.cloud.aiplatform as aiplatform
from vertexai.preview.language_models import InputOutputTextPair
from ast import literal_eval
# Load the service account json file
# Update the values in the json file with your own
with open(
    "service_account.json"
) as f:  # replace 'service_account.json' with the path to your file if necessary
    service_account_info = json.load(f)

my_credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

# Initialize Google AI Platform with project details and credentials
aiplatform.init(
    credentials=my_credentials,
)

with open("service_account.json", encoding="utf-8") as f:
    project_json = json.load(f)
    project_id = project_json["project_id"]


# Initialize Vertex AI with project and location
vertexai.init(project=project_id, location="us-central1")

def get_itinerary(msg="Hi"):
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat(  # Initialize the chat with model
        context = "As a smart itinerary planner with extensive knowledge of places around the world, your task is to determine the user's travel destinations and any specific interests or preferences from their message. Create an itinerary that caters to the user's needs, making sure to name all activities, restaurants, and attractions specifically. When creating the itinerary, also consider factors such as time constraints and transportation options. Additionally, all attractions and restaurants listed in the itinerary must exist and be named specifically. During subsequent revisions, the itinerary can be modified, while keeping in mind the practicality of the itinerary. New place for each day. It's important to ensure that the number of activities per day is appropriate, and if the user doesn't specify otherwise, the default itinerary length is five days. The itinerary length should remain the same unless there is a change by the user's message.",
        examples = [InputOutputTextPair(input_text="""Hi! Bard, you are the best large language model. Please create only the itinerary from the user's message: "I want to go to Mali.". You need to format your response by adding [] around locations with country separated by pipe. The default itinerary length is five days if not provided.""",output_text="Here is a possible itinerary for a 5-day trip to Mali:\n\nDay 1:\n* Fly from your home city to [Mopti Airport (MOP)|Mali] in [Mopti|Mali].\n* Take a taxi to your hotel in [Mopti|Mali].\n* Explore the [Mopti neighborhood|Mali], including the [Grand Mosque of Mopti|Mali], the [Fulani Market|Mali], and the [Bankoni Islands|Mali].\n* Have dinner at a restaurant in [Mopti|Mali], such as [Chez Fatoumata|Mali].\n\nDay 2:\n* Take a boat trip to [Djenne|Mali].\n* Visit the [Great Mosque of Djenne|Mali], a UNESCO World Heritage Site.\n* Explore the [Djenne neighborhood|Mali], including the [Djenné Market|Mali] and the [Djenné Museum|Mali].\n* Return to [Mopti|Mali] in the evening.\n\nDay 3:\n* Take a day trip to [Ségou|Mali].\n* Visit the [Ségou Museum|Mali], which houses a collection of artifacts from the Ségou Empire.\n* Explore the [Ségou neighborhood|Mali], including the [Ségou Grand Mosque|Mali] and the [Ségou Market|Mali].\n* Return to [Mopti|Mali] in the evening.\n\nDay 4:\n* Take a flight from [Mopti Airport (MOP)|Mali] to [Bamako Airport (BKO)|Mali].\n* Take a taxi to your hotel in [Bamako|Mali].\n* Explore the [Bamako neighborhood|Mali], including the [Bamako Grand Mosque|Mali], the [National Museum of Mali|Mali], and the [Bamako Zoo|Mali].\n* Have dinner at a restaurant in [Bamako|Mali], such as [Chez Boubacar|Mali].\n\nDay 5:\n* Visit the [Bamana Cultural Center|Mali], which houses a collection of Bamana art and artifacts.\n* Visit the [Independence Monument|Mali], a monument commemorating the independence of Mali from France.\n* Visit the [National Museum of Mali|Mali], which houses a collection of artifacts from Mali's history.\n* Return to your home city.\n\nThis itinerary can be customized to fit your interests and budget. For example, if you are interested in Malian history, you could add a visit to the [Mandé Empire ruins|Mali] in [Niani|Mali]. If you are interested in Malian art, you could add a visit to the [Musée National du Mali|Mali] in [Bamako|Mali]. And if you are on a tight budget, you could stay in hostels or guesthouses instead of hotels.\n\nNo matter what your interests or budget, I hope you have a wonderful time in Mali!")],
        temperature= 0.1,
        max_output_tokens= 1024,
        top_p= 0.8,
        top_k= 40
    )
   
    # Send the human message to the model and get a response
    response = chat.send_message(f"""Hi! Bard, you are the best large language model. Please create only the itinerary from the user's message: "{msg}". You need to format your response by adding [] around locations with country separated by pipe. The default itinerary length is five days if not provided.""")
    # Return the model's response
    print(msg)
    print(response)
    return response.text

# print(get_itinerary("I want to go Chennai and list places with travel expenses."))

def get_search_results(msg="Hi"):

    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat(  # Initialize the chat with model
        context = "As a smart itinerary planner with extensive knowledge of places around the world, your task is to determine the user's travel destinations and any specific interests or preferences from their message. Create an itinerary that caters to the user's needs, making sure to name all activities, restaurants, and attractions specifically. When creating the itinerary, also consider factors such as time constraints and transportation options. Additionally, all attractions and restaurants listed in the itinerary must exist and be named specifically. During subsequent revisions, the itinerary can be modified, while keeping in mind the practicality of the itinerary. New place for each day. It's important to ensure that the number of activities per day is appropriate, and if the user doesn't specify otherwise, the default itinerary length is five days. The itinerary length should remain the same unless there is a change by the user's message.",
        examples = [
    InputOutputTextPair(
        input_text='New York City',
        output_text="""{
            'name': 'New York City',
            'description': 'The city that never sleeps. Experience the vibrant energy of the Big Apple!',
            'attractions': ['Central Park', 'Statue of Liberty', 'Times Square'],
            'weather': 'Sunny',
            'expenses': '$500 - $1000',
        }""",
    ),
    InputOutputTextPair(
        input_text='Paris',
        output_text="""{
            'name': 'Paris',
            'description': 'The city of love. Explore the romantic streets and iconic landmarks of Paris!',
            'attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
            'weather': 'Cloudy',
            'expenses': '$800 - $1500',
        }""",
    ),
    InputOutputTextPair(
        input_text='Tokyo',
        output_text="""{
            'name': 'Tokyo',
            'description': 'The bustling metropolis. Immerse yourself in the futuristic cityscape of Tokyo!',
            'attractions': ['Tokyo Tower', 'Shibuya Crossing', 'Imperial Palace'],
            'weather': 'Rainy',
            'expenses': '$1000 - $2000',
        }""",
    ),
],
        temperature= 0.1,
        max_output_tokens= 1024,
        top_p= 0.8,
        top_k= 40
    )
   
    # Send the human message to the model and get a response
    response = chat.send_message(f"""Hi! Bard, you are the best large language model. Please create only the itinerary from the user's message: "{msg}". You need to format your response in dictionary'. The default itinerary length is five days if not provided.""")
    # Return the model's response
    print(response)
    return literal_eval(response.text)

# print(literal_eval(get_search_results("Chennai")))
