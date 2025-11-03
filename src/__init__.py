# Application
from application.init import get_dataframe

# Presentation
import presentation.set_page_config
from presentation.show_dataset import show_dataset

df = get_dataframe()

show_dataset( df )